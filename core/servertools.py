# -*- coding: utf-8 -*-
# --------------------------------------------------------------------------------
# Server management
# --------------------------------------------------------------------------------

import datetime
import os
import re
import time
import urlparse
import filetools

from core import httptools, jsontools
from core.item import Item
from platformcode import config, logger, platformtools

dict_servers_parameters = {}


def find_video_items(item=None, data=None):
    """
    Función genérica para buscar vídeos en una página, devolviendo un itemlist con los items listos para usar.
     - Si se pasa un Item como argumento, a los items resultantes mantienen los parametros del item pasado
     - Si no se pasa un Item, se crea uno nuevo, pero no contendra ningun parametro mas que los propios del servidor.

    @param item: Item al cual se quieren buscar vídeos, este debe contener la url válida
    @type item: Item
    @param data: Cadena con el contendio de la página ya descargado (si no se pasa item)
    @type data: str

    @return: devuelve el itemlist con los resultados
    @rtype: list
    """
    logger.info()
    itemlist = []

    if data is None and item is None:
        return itemlist

    # Descarga la página
    if data is None:
        data = httptools.downloadpage(item.url).data

    # Crea un item si no hay item
    if item is None:
        item = Item()

    # Busca los enlaces a los videos
    for label, url, server in findvideos(data):
        title = "Enlace encontrado en %s" % label
        itemlist.append(Item(channel=item.channel, action='play', title=title, url=url, server=server))

    return itemlist



# Para un servidor y una url, devuelve la url normalizada según patrones del json
def normalize_url(serverid, url):
    new_url = url # si no se encuentra patrón devolver url tal cual

    server_parameters = get_server_parameters(serverid)
    # Recorre los patrones
    for pattern in server_parameters.get("find_videos", {}).get("patterns", []):
        # ~ logger.info(pattern["pattern"])

        # Recorre los resultados
        found = False
        for match in re.compile(pattern["pattern"], re.DOTALL).finditer(url):
            new_url = pattern["url"]
            for x in range(len(match.groups())):
                new_url = new_url.replace("\\%s" % (x + 1), match.groups()[x])

            if new_url not in server_parameters["find_videos"].get("ignore_urls", []):
                found = True
            else:
                new_url = url
            break
        
        if found: break

    # ~ logger.info("Server: %s, Url: %s => %s" % (serverid, url, new_url))
    return new_url


def get_servers_itemlist(itemlist):
    """
    Obtiene el servidor para cada uno de los items, en funcion de su url.
     - Asigna el servidor y la url modificada.
     - Si no se encuentra servidor para una url, se asigna "directo"
    """
    # Recorre los servidores
    for serverid in get_servers_list().keys():
        server_parameters = get_server_parameters(serverid)

        # Recorre los patrones
        for pattern in server_parameters.get("find_videos", {}).get("patterns", []):
            # ~ logger.info(pattern["pattern"])

            # Recorre los resultados
            for match in re.compile(pattern["pattern"], re.DOTALL).finditer("\n".join([item.url.split('|')[0] for item in itemlist if not item.server])):
                url = pattern["url"]
                for x in range(len(match.groups())):
                    url = url.replace("\\%s" % (x + 1), match.groups()[x])

                for item in itemlist:
                    if match.group() in item.url:
                        # ~ logger.info('Found pattern ' + pattern["pattern"])
                        item.server = serverid
                        if '|' in item.url:
                            item.url = url + '|' + item.url.split('|')[1]
                        else:
                            item.url = url

    for item in itemlist:
        if not item.server and item.url: # Si no se ha encontrado server
            item.server = "desconocido" #"directo"

    return itemlist


def findvideos(data, skip=False, disabled_servers=False):
    """
    Recorre la lista de servidores disponibles y ejecuta la funcion findvideosbyserver para cada uno de ellos
    :param data: Texto donde buscar los enlaces
    :param skip: Indica un limite para dejar de recorrer la lista de servidores. Puede ser un booleano en cuyo caso
    seria False para recorrer toda la lista (valor por defecto) o True para detenerse tras el primer servidor que
    retorne algun enlace. Tambien puede ser un entero mayor de 1, que representaria el numero maximo de enlaces a buscar.
    :return:
    """
    logger.info()
    devuelve = []
    skip = int(skip)
    servers_list = get_servers_list().keys()

    # Ejecuta el findvideos en cada servidor activo
    for serverid in servers_list:
        if not disabled_servers and not is_server_enabled(serverid):
            continue

        devuelve.extend(findvideosbyserver(data, serverid, disabled_servers=disabled_servers))
        if skip and len(devuelve) >= skip:
            devuelve = devuelve[:skip]
            break

    return devuelve


def findvideosbyserver(data, serverid, disabled_servers=False):
    devuelve = []

    serverid = get_server_id(serverid)
    if not disabled_servers and not is_server_enabled(serverid):
        return devuelve

    server_parameters = get_server_parameters(serverid)
    if "find_videos" in server_parameters:
        # Recorre los patrones
        for pattern in server_parameters["find_videos"].get("patterns", []):
            msg = "%s\npattern: %s" % (serverid, pattern["pattern"])
            # Recorre los resultados
            for match in re.compile(pattern["pattern"], re.DOTALL).finditer(data):
                url = pattern["url"]
                # Crea la url con los datos
                for x in range(len(match.groups())):
                    url = url.replace("\\%s" % (x + 1), match.groups()[x])

                value = server_parameters["name"], url, serverid
                if value not in devuelve and url not in server_parameters["find_videos"].get("ignore_urls", []):
                    devuelve.append(value)

                msg += "\nurl encontrada: %s" % url
                logger.info(msg)

    return devuelve


# Por defecto no se tienen en cuenta los servidores desactivados y se devuelve 'directo' si no se encuentra.
# Con disabled_servers=True se detectan tb los desactivados y se devuelve None si no se encuentra.
def get_server_from_url(url, disabled_servers=False):
    encontrado = findvideos(url, skip=True, disabled_servers=disabled_servers)
    if len(encontrado) > 0:
        return encontrado[0][2]
    else:
        if not disabled_servers:
            return 'directo' # No devuelve desconocido pq puede que sea un "conocido" que esté desactivado
        else:
            return None



# Para un servidor y una url, devuelve video_urls ([]), puede (True/False), motivo_no_puede
def resolve_video_urls_for_playing(server, url, url_referer=''):
    logger.info("Server: %s, Url: %s" % (server, url))
    video_urls = []

    server = get_server_id(server) # por si hay servers con múltiples ids

    # Si el vídeo es "directo" o "local", no hay que buscar más
    if server == "directo" or server == "local":
        video_urls.append(["%s [%s]" % (urlparse.urlparse(url)[2][-4:], server), url])

    else:
        # Parámetros json del server
        server_parameters = get_server_parameters(server) if server else {}
        server_name = server_parameters['name'] if 'name' in server_parameters else server.capitalize()

        if 'active' not in server_parameters:
            errmsg = 'No existe conector para el servidor %s' % server_name
            logger.error(errmsg)
            return [], False, errmsg

        if server_parameters['active'] == False:
            errmsg = 'El conector para el servidor %s está desactivado' % server_name
            if 'notes' in server_parameters: errmsg += '. ' + server_parameters['notes']
            logger.debug(errmsg)
            return [], False, errmsg

        # Importa el server
        try:
            server_module = __import__('servers.%s' % server, None, None, ["servers.%s" % server])
        except:
            errmsg = 'No se ha podido importar el servidor %s' % server_name
            logger.error(errmsg)
            import traceback
            logger.error(traceback.format_exc())
            return [], False, errmsg

        # Llama a get_video_url() del server
        try:
            response = server_module.get_video_url(page_url=url, url_referer=url_referer)
            if isinstance(response, basestring):
                return [], False, '[%s] %s' % (server_name, response)
            elif len(response) > 0:
                video_urls.extend(response)
        except:
            errmsg = 'Se ha producido un error en el servidor %s' % server_name
            logger.error(errmsg)
            import traceback
            logger.error(traceback.format_exc())
            return [], False, errmsg

        if len(video_urls) == 0:
            return [], False, 'No se encuentra el vídeo en %s' % server_name

    return video_urls, True, ''


# Para servers con varios ids, busca si es uno de los ids alternativos y devuelve el id principal
def get_server_id(serverid):
    # A mano para evitar recorrer todos los servidores !? (buscar "more_ids" en los json de servidores)
    return corregir_servidor(serverid)

    serverid = serverid.lower()

    # Obtenemos el listado de servers
    server_list = get_servers_list().keys()

    # Si el nombre está en la lista
    if serverid in server_list:
        return serverid

    # Recorre todos los servers buscando el nombre alternativo
    for server in server_list:
        params = get_server_parameters(server)
        if 'more_ids' not in params:
            continue
        if serverid in params['more_ids']:
            return server

    return '' # Si no se encuentra nada se devuelve una cadena vacia


def is_server_enabled(server):
    """
    Función comprobar si un servidor está segun la configuración establecida
    @param server: Nombre del servidor
    @type server: str

    @return: resultado de la comprobación
    @rtype: bool
    """
    server_parameters = get_server_parameters(server)
    # ~ logger.debug(server_parameters)
    if 'active' not in server_parameters or server_parameters['active'] == False:
        return False
    return config.get_setting('status', server=server, default=0) >= 0

def is_server_available(server):
    """
    Función comprobar si existe el json de un servidor
    @param server: Nombre del servidor
    @type server: str

    @return: resultado de la comprobación
    @rtype: bool
    """
    path = os.path.join(config.get_runtime_path(), 'servers', server + '.json')
    return os.path.isfile(path)


def get_server_parameters(server):
    """
    Obtiene los datos del servidor
    @param server: Nombre del servidor
    @type server: str

    @return: datos del servidor
    @rtype: dict
    """
    global dict_servers_parameters
    if server not in dict_servers_parameters:
        try:
            if server == 'desconocido': 
                dict_server = {'active': False, 'id': 'desconocido', 'name': 'Desconocido'}
                dict_servers_parameters[server] = dict_server
                return dict_server

            path = os.path.join(config.get_runtime_path(), 'servers', server + '.json')
            if not os.path.isfile(path):
                logger.info('No se encuentra el json del servidor: %s' % server)
                return {}

            data = filetools.read(path)
            dict_server = jsontools.load(data)

            # valores por defecto si no existen:
            dict_server['active'] = dict_server.get('active', False)
            if 'find_videos' in dict_server:
                dict_server['find_videos']['patterns'] = dict_server['find_videos'].get('patterns', list())
                dict_server['find_videos']['ignore_urls'] = dict_server['find_videos'].get('ignore_urls', list())

            dict_servers_parameters[server] = dict_server

        except:
            mensaje = "Error al cargar el json del servidor: %s\n" % server
            import traceback
            logger.error(mensaje + traceback.format_exc())
            return {}

    return dict_servers_parameters[server]




def get_server_setting(name, server, default=None):
    config.get_setting('server_' + server + '_' + name, default=default)
    return value

def set_server_setting(name, value, server):
    config.set_setting('server_' + server + '_' + name, value)
    return value


def get_servers_list():
    """
    Obtiene un diccionario con todos los servidores disponibles

    @return: Diccionario cuyas claves son los nombre de los servidores (nombre del json)
    y como valor un diccionario con los parametros del servidor.
    @rtype: dict
    """
    server_list = {}
    for server in os.listdir(os.path.join(config.get_runtime_path(), 'servers')):
        if server.endswith('.json'):
            serverid = server.replace('.json', '')
            server_parameters = get_server_parameters(serverid)
            if server_parameters['id'] != serverid:
                logger.error('El id: %s no coincide con el fichero del server %s' % (server_parameters['id'], serverid))
                continue
            # ~ if server_parameters['active'] == True:
                # ~ server_list[serverid] = server_parameters
            server_list[serverid] = server_parameters # devolver aunque no esté activo para poder detectar sus patrones.

    return server_list


# Normalizar nombre del servidor (para los canales que no lo obtienen de los patrones, y para evitar bucle more_ids en get_server_id())
def corregir_servidor(servidor):
    servidor = servidor.strip().lower()
    if servidor in ['waaw', 'waaw1', 'waav', 'netu', 'hqq', 'megavideo', 'megaplay']: return 'netutv'
    elif servidor in ['povwideo', 'powvldeo', 'powv1deo', 'povw1deo']: return 'powvideo'
    elif servidor in ['steamplay', 'streamp1ay']: return 'streamplay'
    elif servidor in ['jplayer', 'feurl']: return 'fembed'
    elif servidor in ['google', 'google drive']: return 'gvideo'
    elif servidor == 'vidto': return 'vidtodo'
    elif servidor == 'vev': return 'vevio'
    elif servidor == 'v-s': return 'vsmobi'
    elif servidor == 'dood': return 'doodstream'
    elif servidor == 'archive': return 'archiveorg'
    elif servidor in ['my', 'my.mail', 'my.mail.ru']: return 'mailru'
    elif servidor in ['ok', 'ok.ru', 'ok server']: return 'okru'
    elif servidor == 'youtu': return 'youtube'
    elif servidor == 'mp4up': return 'mp4upload'
    elif servidor == 'yourup': return 'yourupload'
    elif servidor == 'verys': return 'verystream'
    elif servidor == 'flix': return 'flix555'
    elif servidor == 'biter': return 'byter'
    elif servidor == 'thevideo': return 'thevideome'
    elif servidor == 'onefichier': return '1fichier'
    elif servidor in ['uploaded', 'ul', 'ul.to']: return 'uploadedto'
    # ~ elif servidor == 'uptobox': return 'uptostream'
    else: return servidor


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Reordenación/Filtrado de enlaces
# --------------------------------

def filter_and_sort_by_quality(itemlist):
    servers_sort_quality = config.get_setting('servers_sort_quality', default=0) # 0: orden web, 1: calidad desc, 2: calidad asc

    # Ordenar por preferencia de calidades
    # ------------------------------------
    logger.info('Preferencias de orden para calidades: %s' % servers_sort_quality)
    
    if servers_sort_quality == 1:
        return sorted(itemlist, key=lambda it: it.quality_num, reverse=True)
    elif servers_sort_quality == 2:
        return sorted(itemlist, key=lambda it: it.quality_num)
    else:
        return itemlist


def filter_and_sort_by_server(itemlist):
    # not it.server para casos en que no está definido y se resuelve en el play del canal

    # Quitar enlaces de servidores descartados por el usuario
    # -------------------------------------------------------
    servers_discarded = config.get_setting('servers_discarded', default='')
    if servers_discarded != '':
        servers_discarded_list = servers_discarded.lower().replace(' ', '').split(',')
        logger.info('Servidores descartados por el usuario: %s' % ', '.join(servers_discarded_list))
        # ~ itemlist = filter(lambda it: not it.server or it.server.lower() not in servers_discarded_list, itemlist)
        itemlist = filter(lambda it: (not it.server and 'indeterminado' not in servers_discarded_list) or (it.server and it.server.lower() not in servers_discarded_list), itemlist)

    # Ordenar enlaces de servidores preferidos del usuario
    # ----------------------------------------------------
    servers_preferred = config.get_setting('servers_preferred', default='')
    servers_unfavored = config.get_setting('servers_unfavored', default='')
    if servers_preferred != '' or servers_unfavored != '':
        servers_preferred_list = servers_preferred.lower().replace(' ', '').split(',')
        servers_unfavored_list = servers_unfavored.lower().replace(' ', '').split(',')
        if servers_preferred != '': logger.info('Servidores preferentes para el usuario: %s' % ', '.join(servers_preferred_list))
        if servers_unfavored != '': logger.info('Servidores última opción para el usuario: %s' % ', '.join(servers_unfavored_list))

        def numera_server(servidor):
            if not servidor: servidor = 'indeterminado'
            if servidor in servers_preferred_list:
                return servers_preferred_list.index(servidor)
            elif servidor in servers_unfavored_list:
                return 999 - servers_unfavored_list.index(servidor)
            else: 
                return 99

        itemlist = sorted(itemlist, key=lambda it: numera_server(it.server.lower()))

    # Quitar enlaces de servidores inactivos
    # --------------------------------------
    return filter(lambda it: not it.server or is_server_enabled(get_server_id(it.server)), itemlist)


def get_lang(lang):
    if not lang: return '?'
    if lang in ['Esp','Lat']: return lang
    return 'VO'

def filter_and_sort_by_language(itemlist):
    # prefs = {'Esp': pref_esp, 'Lat': pref_lat, 'VO': pref_vos} dónde pref_xxx "0:Descartar|1:Primero|2:Segundo|3:Tercero"

    # Quitar enlaces de idiomas descartados y ordenar por preferencia de idioma
    # -------------------------------------------------------------------------
    prefs = config.get_lang_preferences()
    logger.info('Preferencias de idioma para servidores: %s' % str(prefs))
    prefs['?'] = 4 # Cuando no hay idioma mostrar al final

    itemlist = filter(lambda it: prefs[get_lang(it.language)] != 0, itemlist)

    return sorted(itemlist, key=lambda it: prefs[get_lang(it.language)])
