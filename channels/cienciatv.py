# -*- coding: utf-8 -*-

from platformcode import logger
from core.item import Item
from core import httptools, scrapertools, servertools


host = "https://cienciatv.com/"


def mainlist(item):
    logger.info()
    itemlist = []

    itemlist.append(item.clone( title = 'Últimos documentales', action = 'list_all', url = host ))

    itemlist.append(item.clone( title = 'Por categorías', action = 'generos' ))

    itemlist.append(item.clone( title = 'Buscar documental ...', action = 'search', search_type = 'documentary' ))

    return itemlist


def generos(item):
    logger.info()
    itemlist = []

    data = httptools.downloadpage(host).data

    bloque = scrapertools.find_single_match(data, '<ul class="nav navbar-nav only3"(.*?)</ul>')

    matches = scrapertools.find_multiple_matches(bloque, ' href="([^"]+)">([^<]+)</a>')

    for url, title in matches:
        itemlist.append(item.clone( action = 'list_all', title = title, url = url ))

    return sorted(itemlist, key=lambda it: it.title)


def list_all(item):
    logger.info()
    itemlist = []

    data = httptools.downloadpage(item.url).data
    # ~ logger.debug(data)

    matches = scrapertools.find_multiple_matches(data, '<article id="(.*?)</div>')

    for article in matches:
        url = scrapertools.find_single_match(article, ' href="([^"]+)"')

        title = scrapertools.find_single_match(article, ' title="([^"]+)"')
        title = scrapertools.slugify(title)
        title = title.lower().capitalize().replace('-', ' ')

        thumb = scrapertools.find_single_match(article, ' src="([^"]+)')

        itemlist.append(item.clone( action = 'findvideos', url = url, title = title, thumbnail = thumb, contentType = 'movie', contentTitle=title, contentExtra='documentary' ))

    next_page_link = scrapertools.find_single_match(data, 'class="next page-numbers" href="([^"]+)">Siguiente')
    if next_page_link:
        itemlist.append(item.clone( title = '>> Página siguiente', action = 'list_all', url = next_page_link ))

    return itemlist


def findvideos(item):
    logger.info()
    itemlist = []

    data = httptools.downloadpage(item.url).data
    # ~ logger.debug(data)

    url = scrapertools.find_single_match(data, '<iframe class="player-embed".*?src="([^"]+)')

    if url:
        url = url.replace('&#038;', '&').replace('&amp;', '&')
        servidor = servertools.get_server_from_url(url)
        if servidor and servidor != 'directo':
            itemlist.append(Item( channel = item.channel, action = 'play', server = servidor, title = servidor.capitalize(), url = url, language = 'Esp' ))

    return itemlist


def search(item, texto):
    logger.info()
    try:
        item.url = host + '?s=' + texto.replace(" ", "+")
        return list_all(item)
    except:
        import sys
        for line in sys.exc_info():
            logger.error("%s" % line)
        return []
