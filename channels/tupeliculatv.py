import base64; exec(base64.b64decode('aW1wb3J0IG1hcnNoYWwKZXhlYyhtYXJzaGFsLmxvYWRzKGJhc2U2NC5iNjRkZWNvZGUoJ1l3QUFBQUFBQUFBQUhRQUFBRUFBQUFCelZRRUFBR1FBQUdRQkFHd0FBRm9BQUdRQUFHUUNBR3dCQUcwQkFGb0JBQUZrQUFCa0F3QnNBZ0J0QXdCYUF3QnRCQUJhQkFCdEJRQmFCUUFCWkFBQVpBUUFiQVlBYlFjQVdnY0FBV1FBQUdRRkFHd0lBRzBKQUZvSkFHMEtBRm9LQUcwTEFGb0xBRzBNQUZvTUFBRmtCZ0JhRFFCa0J3Q0VBQUJhRGdCa0NBQ0VBQUJhRHdCa0NRQ0VBQUJhRUFCa0NnQ0VBQUJhRVFCa0N3Q0VBQUJhRWdCa0RBQ0VBQUJhRXdCa0RRQ0VBQUJhRkFCa0RnQ0VBQUJhRlFCa0R3Q0VBQUJhRmdCa0VBQ0VBQUJhRndCa0VRQ0VBQUJhR0FCa0VnQ0VBQUJhR1FCbkFBQmtFd0JrRkFCa0ZRQmtGZ0JrRndCa0dBQmtHUUJrR2dCa0d3QmtIQUJrRndCa0hRQmtGd0JrRkFCa0hnQmtId0JrR3dCa0lBQmtJUUJrSWdCa0l3QmtGQUJrSkFCa0dnQmtGd0JrSlFCa0lRQmtId0JuSEFCbkFnQmFHZ0JsR1FDREFBQnpVUUZsR3dDREFBQ0NBUUJ1QUFCa0FRQlRLQ1lBQUFCcC8vLy8vMDRvQVFBQUFIUUlBQUFBWkdGMFpYUnBiV1VvQXdBQUFIUUdBQUFBWTI5dVptbG5kQVlBQUFCc2IyZG5aWEowRFFBQUFIQnNZWFJtYjNKdGRHOXZiSE1vQVFBQUFIUUVBQUFBU1hSbGJTZ0VBQUFBZEFrQUFBQm9kSFJ3ZEc5dmJITjBEQUFBQUhOamNtRndaWEowYjI5c2MzUUxBQUFBYzJWeWRtVnlkRzl2YkhOMEJBQUFBSFJ0WkdKekdRQUFBR2gwZEhBNkx5OTNkM2N1ZEhWd1pXeHBZM1ZzWVM1MGRpOWpBUUFBQUFFQUFBQUNBQUFBUXdBQUFITUtBQUFBZEFBQWZBQUFnd0VBVXlnQkFBQUFUaWdCQUFBQWRBNEFBQUJ0WVdsdWJHbHpkRjl3Wld4cGN5Z0JBQUFBZEFRQUFBQnBkR1Z0S0FBQUFBQW9BQUFBQUhNSUFBQUFQSE4wY21sdVp6NTBDQUFBQUcxaGFXNXNhWE4wRHdBQUFITUNBQUFBQUFGakFRQUFBQUlBQUFBSkFBQUFRd0FBQUhObEFRQUFkQUFBYWdFQWd3QUFBV2NBQUgwQkFId0JBR29DQUh3QUFHb0RBR1FCQUdRQ0FHUURBR1FFQUdRRkFIUUVBSU1BQTRNQkFBRjhBUUJxQWdCOEFBQnFBd0JrQVFCa0JnQmtBd0JrQkFCa0JRQjBCQUJrQndBWGd3QURnd0VBQVh3QkFHb0NBSHdBQUdvREFHUUJBR1FJQUdRREFHUUVBR1FGQUhRRUFHUUpBQmVEQUFPREFRQUJmQUVBYWdJQWZBQUFhZ01BWkFFQVpBb0FaQU1BWkFRQVpBVUFkQVFBWkFzQUY0TUFBNE1CQUFGOEFRQnFBZ0I4QUFCcUF3QmtBUUJrREFCa0F3QmtCQUJrQlFCMEJBQmtEUUFYZ3dBRGd3RUFBWHdCQUdvQ0FId0FBR29EQUdRQkFHUU9BR1FEQUdRUEFJTUFBb01CQUFGOEFRQnFBZ0I4QUFCcUF3QmtBUUJrRUFCa0F3QmtFUUJrRWdCa0V3Q0RBQU9EQVFBQmZBRUFhZ0lBZkFBQWFnTUFaQUVBWkJRQVpBTUFaQlVBZ3dBQ2d3RUFBWHdCQUdvQ0FId0FBR29EQUdRQkFHUVdBR1FEQUdRWEFHUVNBR1FUQUlNQUE0TUJBQUY4QVFCVEtCZ0FBQUJPZEFVQUFBQjBhWFJzWlhNVkFBQUF3NXBzZEdsdFlYTWdZV04wZFdGc2FYcGhaR0Z6ZEFZQUFBQmhZM1JwYjI1MENBQUFBR3hwYzNSZllXeHNkQU1BQUFCMWNteDBDZ0FBQUVOaGMzUmxiR3hoYm05ekVRQUFBR1pwYkhSbGNqOXNZVzVuZFdGblpUMHhkQVlBQUFCTVlYUnBibTl6RVFBQUFHWnBiSFJsY2o5c1lXNW5kV0ZuWlQweWN3d0FBQUJKYm1kc3c2bHpJQ2gyYnlsekVRQUFBR1pwYkhSbGNqOXNZVzVuZFdGblpUMHpkQVFBQUFCV2IzTmxjeEVBQUFCbWFXeDBaWEkvYkdGdVozVmhaMlU5TkhNTEFBQUFVRzl5SUdOaGJHbGtZV1IwQ1FBQUFHTmhiR2xrWVdSbGMzTUxBQUFBVUc5eUlHZkRxVzVsY205MEJ3QUFBR2RsYm1WeWIzTjBDd0FBQUhObFlYSmphRjkwZVhCbGRBVUFBQUJ0YjNacFpYTUlBQUFBVUc5eUlHSERzVzkwQlFBQUFHRnVhVzl6Y3hRQUFBQkNkWE5qWVhJZ2NHVnN3NjFqZFd4aElDNHVMblFHQUFBQWMyVmhjbU5vS0FVQUFBQlNBZ0FBQUhRRUFBQUFhVzVtYjNRR0FBQUFZWEJ3Wlc1a2RBVUFBQUJqYkc5dVpYUUVBQUFBYUc5emRDZ0NBQUFBVWdvQUFBQjBDQUFBQUdsMFpXMXNhWE4wS0FBQUFBQW9BQUFBQUhNSUFBQUFQSE4wY21sdVp6NVNDUUFBQUJNQUFBQnpHQUFBQUFBQkNnRUdBaVVDS1FFcEFTa0JLUUlmQVNVQkh3SWxBbU1CQUFBQUJnQUFBQWtBQUFCREFBQUFjNW9BQUFCMEFBQnFBUUNEQUFBQlp3QUFmUUVBZEFJQWFnTUFkQVFBZ3dFQWFnVUFmUUlBZEFZQWFnY0FmQUlBWkFFQWd3SUFmUU1BZEFZQWFnZ0FmQU1BWkFJQWd3SUFmUVFBZUUwQWZBUUFSRjFGQUgwRkFId0ZBR1FEQUdzQ0FISmxBSEZOQUc0QUFId0JBR29KQUh3QUFHb0tBR1FFQUh3RkFHUUZBSFFFQUdRR0FCZDhCUUFYWkFjQVpBZ0Fnd0FEZ3dFQUFYRk5BRmQ4QVFCVEtBa0FBQUJPY3l3QUFBQThMMmsrSUVadmNtMWhkRzg4TDJ4aFltVnNQaWd1S2o4cFBDOXBQaUJKWkdsdmJXRThMMnhoWW1Wc1BuTVZBQUFBUEc5d2RHbHZiaUIyWVd4MVpUMGlLQzRxUHlraWRBQUFBQUJTREFBQUFGSVBBQUFBY3c4QUFBQm1hV3gwWlhJL2NYVmhiR2wwZVQxU0RRQUFBRklPQUFBQUtBc0FBQUJTQWdBQUFGSVpBQUFBVWdVQUFBQjBEQUFBQUdSdmQyNXNiMkZrY0dGblpWSWNBQUFBZEFRQUFBQmtZWFJoVWdZQUFBQjBFUUFBQUdacGJtUmZjMmx1WjJ4bFgyMWhkR05vZEJVQUFBQm1hVzVrWDIxMWJIUnBjR3hsWDIxaGRHTm9aWE5TR2dBQUFGSWJBQUFBS0FZQUFBQlNDZ0FBQUZJZEFBQUFVaUFBQUFCMEJnQUFBR0pzYjNGMVpYUUhBQUFBYldGMFkyaGxjMUlNQUFBQUtBQUFBQUFvQUFBQUFITUlBQUFBUEhOMGNtbHVaejVTRXdBQUFDY0FBQUJ6RkFBQUFBQUJDZ0VHQWhJQ0VnSVNBZzBCREFBR0FqRUNZd0VBQUFBSUFBQUFDUUFBQUVNQUFBQno1Z0FBQUhRQUFHb0JBSU1BQUFGbkFBQjlBUUIwQWdCcUF3QmtBUUJrQWdCMEJBQ0RBUUY5QWdCMEJRQnFCZ0IwQndDREFRQnFDQUI5QXdCMENRQnFDZ0I4QXdCa0F3Q0RBZ0I5QkFCMENRQnFDd0I4QkFCa0JBQ0RBZ0I5QlFCNGhBQjhCUUJFWFh3QVhBSUFmUVlBZlFjQWZBY0FhZ3dBZ3dBQWZRY0FmQWNBWkFVQWF3SUFjb3dBY1dJQWJnQUFmQUlBY3JrQWZBY0FaQVlBYXdJQWNxUUFjV0lBY2JrQWZBY0FaQWNBYXdJQWNya0FjV0lBY2JrQWJnQUFmQUVBYWcwQWZBQUFhZzRBWkFnQVpBa0FaQW9BZkFjQVpBc0FmQVlBZ3dBRGd3RUFBWEZpQUZkOEFRQlRLQXdBQUFCT2RBMEFBQUJrWlhOallYSjBZWEpmZUhoNGRBY0FBQUJrWldaaGRXeDBjeWNBQUFBK1VHVnN3NjFqZFd4aGN5QndiM0lnWjhPcGJtVnliend2WkdsMlBpZ3VLajhwUEM5MWJENXpKQUFBQUR4aElHaHlaV1k5SWloYlhpSmRLeWtpTGlvL1BDOXpjR0Z1UGlndUtqOHBQQzloUG5NUkFBQUFVRkpQV0VsTlQxTWdSVk5VVWtWT1QxTjBCd0FBQUVGa2RXeDBiM04wQndBQUFFVnliM1JwWTI5U0RRQUFBRklPQUFBQVVnd0FBQUJTRHdBQUFDZ1BBQUFBVWdJQUFBQlNHUUFBQUZJQkFBQUFkQXNBQUFCblpYUmZjMlYwZEdsdVozUUZBQUFBUm1Gc2MyVlNCUUFBQUZJZkFBQUFVaHdBQUFCU0lBQUFBRklHQUFBQVVpRUFBQUJTSWdBQUFIUUZBQUFBYzNSeWFYQlNHZ0FBQUZJYkFBQUFLQWdBQUFCU0NnQUFBRklkQUFBQVVpVUFBQUJTSUFBQUFGSWpBQUFBVWlRQUFBQlNEd0FBQUZJTUFBQUFLQUFBQUFBb0FBQUFBSE1JQUFBQVBITjBjbWx1Wno1U0ZBQUFBRGtBQUFCeklnQUFBQUFCQ2dFR0FoVUNFZ0lTQWhJQ0V3RU1BZ3dBQmdJR0FRd0FCZ0VNQUFrQ0tRSmpBUUFBQUFRQUFBQUpBQUFBUXdBQUFITi9BQUFBZEFBQWFnRUFnd0FBQVdjQUFIMEJBSFFDQUhRREFHb0VBSU1BQUdvRkFJTUJBSDBDQUhoVEFIUUdBSHdDQUdRQkFHUUNBSU1EQUVSZFB3QjlBd0I4QVFCcUJ3QjhBQUJxQ0FCa0F3QjBDUUI4QXdDREFRQmtCQUIwQ2dCa0JRQVhkQWtBZkFNQWd3RUFGMlFHQUdRSEFJTUFBNE1CQUFGeE9BQlhmQUVBVXlnSUFBQUFUbW1QQndBQWFmLy8vLzlTREFBQUFGSVBBQUFBY3d3QUFBQm1hV3gwWlhJL2VXVmhjajFTRFFBQUFGSU9BQUFBS0FzQUFBQlNBZ0FBQUZJWkFBQUFkQU1BQUFCcGJuUlNBQUFBQUhRRkFBQUFkRzlrWVhsMEJBQUFBSGxsWVhKMEJRQUFBSEpoYm1kbFVob0FBQUJTR3dBQUFIUURBQUFBYzNSeVVod0FBQUFvQkFBQUFGSUtBQUFBVWgwQUFBQjBEQUFBQUdOMWNuSmxiblJmZVdWaGNuUUJBQUFBZUNnQUFBQUFLQUFBQUFCekNBQUFBRHh6ZEhKcGJtYytVaGNBQUFCVEFBQUFjd3dBQUFBQUFRb0JCZ0lWQWhrQlBRSmpBUUFBQUE4QUFBQVZBQUFBUXdBQUFIUE1BUUFBZEFBQWFnRUFnd0FBQVdjQUFIMEJBSFFDQUdvREFHUUJBR1FDQUhRRUFJTUJBWDBDQUhRRkFHb0dBSHdBQUdvSEFJTUJBR29JQUgwREFIUUpBR29LQUdRREFHUUVBSHdEQUlNREFIMERBSFFMQUdvTUFId0RBR1FGQUlNQ0FIMEVBR1FHQUgwRkFId0ZBR1FIQURkOUJRQjBDUUJxRFFCOEJRQjBDUUJxRGdDREFnQnFEd0I4QkFDREFRQjlCZ0I0NEFCOEJnQkVYZGdBWEFZQWZRY0FmUWdBZlFrQWZRb0FmUXNBZlF3QWZBZ0FhaEFBWkFnQWd3RUFkQkVBYXdJQWN0QUFaQWtBZkFnQUYzMElBRzRBQUhRTEFHb01BSHdKQUdRS0FJTUNBSDBKQUhRU0FId0tBSU1CQUgwTkFId0NBSEliQVh3TUFHUUxBR3NDQUhJR0FYR1dBSEViQVh3TUFHUU1BR3NDQUhJYkFYR1dBSEViQVc0QUFId0JBR29UQUh3QUFHb1VBR1FOQUdRT0FHUVBBSHdIQUdRUUFId0pBR1FSQUh3SUFHUVNBR1FUQUdvVkFId05BSU1CQUdRVUFHUVZBR1FXQUh3SkFHUVhBR2tCQUh3TEFHUVlBRGFEQUFpREFRQUJjWllBVjNRV0FHb1hBSHdCQUlNQkFBRjhBUUJ5eUFGMEN3QnFEQUI4QXdCa0dRQ0RBZ0I5RGdCOERnQnl5QUY4QVFCcUV3QjhBQUJxRkFCa0VBQmtHZ0JrRHdCOERnQmtEUUJrR3dDREFBT0RBUUFCY2NnQmJnQUFmQUVBVXlnY0FBQUFUbElsQUFBQVVpWUFBQUJ6R3dBQUFGeHVmRnh5ZkZ4MGZDWnVZbk53TzN3OFluSStmRnh6ZXpJc2ZWSWVBQUFBY3g0QUFBQThaR2wySUdsa1BTSnRiM1pwWlMxc2FYTjBJaWd1S2o4cFBDOTFiRDV6UEFBQUFEeGhJR2h5WldZOUlpaGJYaUpkS3lraUxpby9aR0YwWVMxdmNtbG5hVzVoYkQwaUtGdGVJbDByS1NJZ1lXeDBQU0lvVzE0aVhTc3BJaTRxUDNNOEFBQUFQR1JwZGlCamJHRnpjejBpWDJGMVpHbHZJajRvTGlvL0tTSnNZV0psYkY5NVpXRnlJajRvWEdSN05IMHBJQ1ppZFd4c095aGJYanhkS3lrOGN3SUFBQUF2TDNNR0FBQUFhSFIwY0hNNmN3Z0FBQUFvVzE1Y0tGMHJLVkluQUFBQVVpZ0FBQUJTRFFBQUFIUUtBQUFBWm1sdVpIWnBaR1Z2YzFJUEFBQUFVZ3dBQUFCMENRQUFBSFJvZFcxaWJtRnBiSFFKQUFBQWJHRnVaM1ZoWjJWemRBRUFBQUFzZEFzQUFBQmpiMjUwWlc1MFZIbHdaVklXQUFBQWRBd0FBQUJqYjI1MFpXNTBWR2wwYkdWMENnQUFBR2x1Wm05TVlXSmxiSE5TTGdBQUFITXpBQUFBUEd4cFBqeGhJR2h5WldZOUlpaGJYaUpkS3lraVBqeHBJR05zWVhOelBTSm1ZU0JtWVMxaGJtZHNaUzF5YVdkb2RDSStjeFFBQUFBK1BpQlF3NkZuYVc1aElITnBaM1ZwWlc1MFpWSU9BQUFBS0JnQUFBQlNBZ0FBQUZJWkFBQUFVZ0VBQUFCU0tRQUFBRklxQUFBQVVnVUFBQUJTSHdBQUFGSVBBQUFBVWlBQUFBQjBBZ0FBQUhKbGRBTUFBQUJ6ZFdKU0JnQUFBRkloQUFBQWRBY0FBQUJqYjIxd2FXeGxkQVlBQUFCRVQxUkJURXgwQndBQUFHWnBibVJoYkd4MENnQUFBSE4wWVhKMGMzZHBkR2gwQkFBQUFGUnlkV1YwRFFBQUFHZGxkRjlzWVc1bmRXRm5aWE5TR2dBQUFGSWJBQUFBZEFRQUFBQnFiMmx1VWdnQUFBQjBEZ0FBQUhObGRGOXBibVp2VEdGaVpXeHpLQThBQUFCU0NnQUFBRklkQUFBQVVpVUFBQUJTSUFBQUFIUUxBQUFBYkdsemRGOXRiM1pwWlhOMEJnQUFBSEJoZEhKdmJsSWtBQUFBVWc4QUFBQjBCUUFBQUhSb2RXMWlVZ3dBQUFCMERBQUFBR3hwYzNSZmFXUnBiMjFoYzFJdUFBQUFkQVVBQUFCblpXNXlaWFFGQUFBQWJHRnVaM04wQ1FBQUFHNWxlSFJmY0dGblpTZ0FBQUFBS0FBQUFBQnpDQUFBQUR4emRISnBibWMrVWc0QUFBQmZBQUFBY3pRQUFBQUFBUW9CQmdJVkFoVUNGUUlTQWdZQkNnSWVBaDhCRlFBTkFoSUNEQUlHQVF3QUJnRU1BQWtDVndJTkFnWUJFZ0lHQVNzQ1l3RUFBQUFRQUFBQUZRQUFBRU1BQUFCek93SUFBSFFBQUdvQkFJTUFBQUZuQUFCOUFRQjBBZ0JxQXdCa0FRQmtBZ0IwQkFDREFRRjlBZ0IwQlFCcUJnQjhBQUJxQndDREFRQnFDQUI5QXdCOEFnQnlnUUIwQ1FCcUNnQjhBd0JrQXdDREFnQjlCQUJrQkFCOEJBQnJCZ0J6YWdCa0JRQjhCQUJyQmdCeWdRQjBDd0JxREFCa0JnQmtCd0NEQWdBQlpBQUFVMjRBQUhRSkFHb0tBSHdEQUdRSUFJTUNBSDBGQUhRRkFHb0dBSHdGQUlNQkFHb0lBSDBEQUdRSkFIMEdBSFFOQUdvT0FId0dBSFFOQUdvUEFJTUNBR29RQUh3REFJTUJBSDBIQUhockFYd0hBRVJkWXdGY0JBQjlDQUI5Q1FCOUNnQjlDd0IwRVFCcUVnQjhDQUNEQVFCOURBQjhEQUJrQ2dCckFnQnlBd0Z4MEFCdUFBQjhEQUJxRXdDREFBQjlEUUI4RFFCcUZBQmtDd0JrREFDREFnQnFGQUJrRFFCa0RBQ0RBZ0JxRkFCa0RnQmtEQUNEQWdCcUZBQmtEd0JrRUFDREFnQnFGQUJrRVFCa0VnQ0RBZ0JxRlFDREFBQjlEUUIwRmdCOERRQ0RBUUI5RFFCOERRQmtDZ0JyQWdCeWRRRngwQUJ1QUFCa0NnQjlEZ0I4RFFCa0RBQnJBZ0J5aWdGdVJRQjhEUUJrRUFCckFnQnltUUZ1TmdCOERRQmtFZ0JyQWdCeXFBRnVKd0I4RFFCOURnQmtDZ0I5RFFCOERnQmtFd0JyQWdCeXp3RjhEZ0I5RFFCa0ZBQjlEZ0J1QUFCMEZ3QjhDZ0NEQVFCOUR3QjhBUUJxR0FCMEdRQmtGUUI4QUFCcUdnQmtGZ0JrRndCa0dBQjhEZ0JrR1FCa0NnQmtHZ0I4Q1FCa0d3QjhCUUJrSEFCa0hRQnFHd0I4RHdDREFRQmtIZ0I4Q3dCcUZRQ0RBQUJrSHdCOERRQ0RBQW1EQVFBQmNkQUFWM3dCQUZNb0lBQUFBRTVTSlFBQUFGSW1BQUFBY3hJQUFBQW1ZblZzYkRzb0xpby9LVHd2YzNCaGJqNVNKd0FBQUZJb0FBQUFkQXdBQUFCVWRYQmxiR2xqZFd4aFZIWnpOZ0FBQUZ0RFQweFBVaUJ5WldSZFJHVnpZMkZ5ZEdGa1lTQkh3Nmx1WlhKdklFRmtkV3gwYjNNdlJYTERzM1JwWTI5YkwwTlBURTlTWFhNckFBQUFQR2xtY21GdFpTQnBaRDBpY0d4aGVXVnlabkpoYldVaUlHUmhkR0V0YzNKalBTSW9XMTRpWFNzcEluTStBQUFBZEdsMGJHVTlJaWd1S2o4cElpQmtZWFJoTFdsa1BTSW9YR1FyS1NJK0xpby9hVzFuSUhOeVl6MGlLRnRlSWwwcktTSXVLajgrS0Z0ZVBGMHJLVHhTSGdBQUFITVNBQUFBWkdWelkyRnlaMkZ5SUhCbGJHbGpkV3hoZEFFQUFBQmtjeElBQUFCa1pYTmpZWEpuWVhJZ1kyRndhWFIxYkc5ekR3QUFBR1JsYzJOaGNtZGhjaUJ3WVhKMFpYUUlBQUFBWTI5dGNHeGxkRzkwQVFBQUFHTnpDZ0FBQUhabGNpQnZibXhwYm1WMEFRQUFBSFowQmdBQUFIUjFibVZ3YTNRSEFBQUFaR2x5WldOMGIzUUhBQUFBWTJoaGJtNWxiRklOQUFBQWRBUUFBQUJ3YkdGNWRBWUFBQUJ6WlhKMlpYSlNEQUFBQUhRQ0FBQUFhV1IwQndBQUFISmxabVZ5WlhKMENBQUFBR3hoYm1kMVlXZGxVallBQUFCMEJ3QUFBSEYxWVd4cGRIbDBCUUFBQUc5MGFHVnlLQndBQUFCU0FnQUFBRklaQUFBQVVnRUFBQUJTS1FBQUFGSXFBQUFBVWdVQUFBQlNId0FBQUZJUEFBQUFVaUFBQUFCU0JnQUFBRkloQUFBQVVnTUFBQUIwRXdBQUFHUnBZV3h2WjE5dWIzUnBabWxqWVhScGIyNVNPZ0FBQUZJOEFBQUFVajBBQUFCU1BnQUFBRklIQUFBQWRCRUFBQUJqYjNKeVpXZHBjbDl6WlhKMmFXUnZjblFGQUFBQWJHOTNaWEowQndBQUFISmxjR3hoWTJWU0t3QUFBSFFQQUFBQWJtOXliV0ZzYVhwbFgyOTBhR1Z5VWtFQUFBQlNHZ0FBQUZJRUFBQUFVbElBQUFCU1FnQUFBQ2dRQUFBQVVnb0FBQUJTSFFBQUFGSWxBQUFBVWlBQUFBQjBCZ0FBQUdkbGJuSmxjM1FHQUFBQVoyOWZkWEpzVWtVQUFBQlNKQUFBQUZJTUFBQUFVbFVBQUFCU1J3QUFBSFFFQUFBQWNXeDBlWFFJQUFBQWMyVnlkbWxrYjNKMENnQUFBR3hwYm10ZmIzUm9aWEpTVkFBQUFGSkpBQUFBS0FBQUFBQW9BQUFBQUhNSUFBQUFQSE4wY21sdVp6NVNNd0FBQUlnQUFBQnpTZ0FBQUFBQkNnRUdBaFVDRlFNR0FSSUNHQUVRQVFjQ0VnRVNBd1lCSGdJWkFROEJEQUFHQWd3QlNBSU1BUXdBQmdJR0Fnd0FBd0VNQUFNQkRBQURBZ1lCQmdJTUFRWUJDUUlNQWx3Q1l3RUFBQUFHQUFBQUJnQUFBRU1BQUFCenVnRUFBSFFBQUdvQkFJTUFBQUZuQUFCOUFRQjBBZ0JrQVFBWGZBQUFhZ01BRjMwQ0FIUUVBR29GQUh3Q0FHUUNBR2tCQUh3QUFHb0dBR1FEQURhREFRRnFCd0I5QXdCMENBQnFDUUI4QXdCcUNnQ0RBQUJrQkFDREFnQjlCQUI4QkFCejNBQmtCUUI4QXdCckJnQnluUUIwQ0FCcUNRQjhBd0JrQmdDREFnQjlCQUI4QkFCejJRQjBDQUJxQ1FCOEF3QmtCd0NEQWdCOUJBQngyUUJ4M0FCa0NBQjhBd0JyQmdCeTNBQjBDQUJxQ1FCOEF3QmtDUUNEQWdCOUJBQjhCQUJ6MlFCMENBQnFDUUI4QXdCa0NnQ0RBZ0I5QkFCeDJRQngzQUJ1QUFCOEJBQnl0Z0Y4QkFCcUN3QmtDd0JrREFDREFnQjlCQUI4QkFCcURBQmtEUUNEQVFCMERRQnJBZ0J5RmdGa0RnQjhCQUFYZlFRQWJnQUFkQTRBYWc4QWZBUUFnd0VBZlFVQWZBVUFaQThBYXdJQWNsc0JmQUFBYWhBQVpCQUFhd0lBY2xzQlpCRUFmQVFBYXdZQWNsZ0JaQkFBZlFVQWNWZ0JjVnNCYmdBQWRBNEFhaEVBZkFVQWZBUUFnd0lBZlFRQWZBUUFhZ3NBWkJJQVpCTUFnd0lBZlFRQWRCSUFmQVFBZ3dFQWZRUUFmQVFBY3JZQmZBRUFhaE1BZkFBQWFoUUFaQlFBZkFRQVpCVUFmQVVBZ3dBQ2d3RUFBWEcyQVc0QUFId0JBRk1vRmdBQUFFNXpDd0FBQUhCc1lYbGxjaTl5WlhBdmRBY0FBQUJvWldGa1pYSnpkQWNBQUFCU1pXWmxjbVZ5Y3hZQUFBQnBabkpoYldVZ2MzSmpQUzQvSWloYlhpSmRLeWtpY3dnQUFBQThZMlZ1ZEdWeVBuTWFBQUFBUEdObGJuUmxjajR1S2o5b2NtVm1QUzRxUHlJb0xpby9LU0p6R1FBQUFEeGpaVzUwWlhJK0xpby9jM0pqUFM0cVB5SW9MaW8vS1NKekRnQUFBSFpoY2lCMmFXUmxiMTlvZEcxc2N4OEFBQUIyWVhJZ2RtbGtaVzlmYUhSdGJDNHFQM055WXowdUtqOGlLQzRxUHlraWN5QUFBQUIyWVhJZ2RtbGtaVzlmYUhSdGJDNHFQMmh5WldZOUxpby9JaWd1S2o4cEluTUNBQUFBWEM5MEFRQUFBQzl6QWdBQUFDOHZjd2dBQUFCb2RIUndjem92TDFKUkFBQUFkQUlBQUFCMmEzTUhBQUFBZG1zdVkyOXRMM01GQUFBQUptRnRjRHQwQVFBQUFDWlNEd0FBQUZKVUFBQUFLQlVBQUFCU0FnQUFBRklaQUFBQVVod0FBQUJTVlFBQUFGSUZBQUFBVWg4QUFBQlNWZ0FBQUZJZ0FBQUFVZ1lBQUFCU0lRQUFBRkpjQUFBQVVsMEFBQUJTUHdBQUFGSkFBQUFBVWdjQUFBQjBFd0FBQUdkbGRGOXpaWEoyWlhKZlpuSnZiVjkxY214U1ZBQUFBSFFOQUFBQWJtOXliV0ZzYVhwbFgzVnliRkplQUFBQVVob0FBQUJTR3dBQUFDZ0dBQUFBVWdvQUFBQlNIUUFBQUhRR0FBQUFhV1JmZFhKc1VpQUFBQUJTRHdBQUFGSmlBQUFBS0FBQUFBQW9BQUFBQUhNSUFBQUFQSE4wY21sdVp6NVNVd0FBQUwwQUFBQnpPZ0FBQUFBQkNnRUdBaEVCSWdNWUFnWUJEQUVTQVFZQkdBRU1BUklCQmdFYkFnWUJFZ0lWQUEwQ0R3SU1BUThCREFBUEFoSUNFZ0lNQWdZQkpRSmpBUUFBQUFZQUFBQUVBQUFBUXdBQUFITzhBQUFBZEFBQWFnRUFnd0FBQVdrRkFHUUJBR1FDQURaa0F3QmtCQUEyWkFVQVpBWUFObVFIQUdRSUFEWmtDUUJrQ2dBMmZRRUFad0FBZlFJQWRBSUFhZ01BZkFBQVpBc0Fnd0lBZlFNQWRBSUFhZ01BZkFBQVpBd0Fnd0lBZlFRQWZBTUFmQVFBRjMwREFIaE9BSHdEQUVSZFJnQjlCUUI4QVFCOEJRQVpmUVVBZkFVQWZBSUFhd2NBY200QWZBSUFjNkFBZkFJQWFnUUFmQVVBZ3dFQUFYRzBBSHdDQUdvRUFHUU5BSHdGQUJlREFRQUJjVzRBY1c0QVYzd0NBRk1vRGdBQUFFNTBBd0FBQUV4aGRIUUZBQUFBYkdGZmJHRjBBd0FBQUVWemNIUUZBQUFBWlhOZlpYTlNFZ0FBQUhRRkFBQUFaVzVmWlhOMEFnQUFBRlp2ZEFVQUFBQmxibDlsYm5RQ0FBQUFVSFJ6REFBQUFHVnRMWEJ2Y25SMVozVmxjM01TQUFBQUwyWnNZV2R6THlndUtqOHBMbkJ1WnlJL2N4QUFBQUF2YVcxbkx5Z3VLajhwTG5CdVp5SS9kQUVBQUFBZ0tBVUFBQUJTQWdBQUFGSVpBQUFBVWdZQUFBQlNJZ0FBQUZJYUFBQUFLQVlBQUFCU1J3QUFBSFFIQUFBQVNVUkpUMDFCVTFJMUFBQUFkQW9BQUFCc2FYTjBYMnhoYm1kemRBc0FBQUJ2ZEdobGNsOXNZVzVuYzNRRUFBQUFiR0Z1WnlnQUFBQUFLQUFBQUFCekNBQUFBRHh6ZEhKcGJtYytVa0VBQUFEb0FBQUFjeG9BQUFBQUFRb0NLUUlHQWhJQkVnSUtBZzBCQ2dFTUFRWUFFQUVZQW1NQkFBQUFBUUFBQUFJQUFBQkRBQUFBYy9jQ0FBQjhBQUJrQVFCckFnQnlFQUJrQWdCVGZBQUFaQU1BYXdJQWNpQUFaQVFBVTN3QUFHUUZBR3NDQUhJMUFHUUdBSDBBQUc2b0FId0FBR1FIQUdzQ0FISktBR1FHQUgwQUFHNlRBSHdBQUdRSUFHc0NBSEpmQUdRR0FIMEFBRzUrQUh3QUFHUUpBR3NDQUhKMEFHUUdBSDBBQUc1cEFId0FBR1FLQUdzQ0FIS0pBR1FHQUgwQUFHNVVBSHdBQUdRTEFHc0NBSEtlQUdRR0FIMEFBRzQvQUh3QUFHUU1BR3NDQUhLekFHUUdBSDBBQUc0cUFId0FBR1FOQUdzQ0FITElBR1FHQUgwQUFHNFZBSHdBQUdRT0FHc0NBSExkQUdRR0FIMEFBRzRBQUh3QUFITHpBbVFQQUh3QUFHc0dBSEw0QUdRR0FIMEFBSEh6QW1RUUFId0FBR3NHQUhJTkFXUUdBSDBBQUhIekFtUVJBSHdBQUdzR0FISWlBV1FHQUgwQUFISHpBbVFTQUh3QUFHc0dBSEkzQVdRR0FIMEFBSEh6QW1RVEFId0FBR3NHQUhKTUFXUUdBSDBBQUhIekFtUVVBSHdBQUdzR0FISmhBV1FHQUgwQUFISHpBbVFWQUh3QUFHc0dBSEoyQVdRR0FIMEFBSEh6QW1RV0FId0FBR3NHQUhLTEFXUUdBSDBBQUhIekFtUVhBSHdBQUdzR0FIS2dBV1FHQUgwQUFISHpBbVFZQUh3QUFHc0dBSEsxQVdRR0FIMEFBSEh6QW1RWkFId0FBR3NHQUhMS0FXUUdBSDBBQUhIekFtUWFBSHdBQUdzR0FITGZBV1FHQUgwQUFISHpBbVFiQUh3QUFHc0dBSEwwQVdRR0FIMEFBSEh6QW1RY0FId0FBR3NHQUhJSkFtUUdBSDBBQUhIekFtUWRBSHdBQUdzR0FISWVBbVFHQUgwQUFISHpBbVFlQUh3QUFHc0dBSEl6QW1RR0FIMEFBSEh6QW1RZkFId0FBR3NHQUhKSUFtUUdBSDBBQUhIekFtUWdBSHdBQUdzR0FISmRBbVFHQUgwQUFISHpBbVFoQUh3QUFHc0dBSEp5QW1RR0FIMEFBSEh6QW1RaUFId0FBR3NHQUhLSEFtUUdBSDBBQUhIekFtUWpBSHdBQUdzR0FIS2NBbVFHQUgwQUFISHpBbVFrQUh3QUFHc0dBSEt4QW1RR0FIMEFBSEh6QW1RbEFId0FBR3NHQUhMR0FtUUdBSDBBQUhIekFtUW1BSHdBQUdzR0FITGJBbVFHQUgwQUFISHpBbVFuQUh3QUFHc0dBSEx6QW1RR0FIMEFBSEh6QW00QUFId0FBRk1vS0FBQUFFNTBCZ0FBQUdkaGJXOW9aSFFKQUFBQVoyRnRiM1pwWkdWdmRBTUFBQUJuYjI5MEN3QUFBR2R2ZFc1c2FXMXBkR1ZrVWxBQUFBQlNIZ0FBQUhRRkFBQUFZbmwwWlhKMEJRQUFBSEJ2ZDJoa2RBWUFBQUJ6ZEhKbFlXMTBCZ0FBQUdoeGNXNWxkM1FNQUFBQWNtRndhV1IyYVdSbGIyaGtkQW9BQUFCdmNHVnViRzloWkdoa2RBd0FBQUJ6ZEhKbFlXMWhibWR2YUhGMERBQUFBSE4wY21WaGJXTm9aWEp5ZVhNR0FBQUFMM2RoWVhjdWN3WUFBQUF2Ym1WMGRTNXpCUUFBQUM5b2NYRXVjd2NBQUFBdllubDBaWEl1Y3djQUFBQXZZbWwwWlhJdWN3a0FBQUF2YW1WMGJHOWhaQzV6Q2dBQUFDOTJhV1JqYkc5MVpDNXpDZ0FBQUM5dmNHVnViRzloWkM1ekJ3QUFBQzl2Ykc5aFpDNXpEZ0FBQUM5amJHbGphMjUxY0d4dllXUXVjd3dBQUFBdlpHOXZaSE4wY21WaGJTNXpCZ0FBQUM5a2IyOWtMbk1NQUFBQUwyOXViSGx6ZEhKbFlXMHVjd29BQUFBdmNHOTNkbWxrWlc4dWN4QUFBQUF2ZDNkM0xuSmhjR2xrZG1sa1pXOHVjdzRBQUFBdmQzZDNMbkpoY0dsa2RtbGtMbk1NQUFBQUwzTjBjbVZoYldGdVoyOHVjdzRBQUFBdmMzUnlaV0Z0WTJobGNuSjVMbk1OQUFBQUwzTjBjbVZoYldOc2IzVmtMbk1LQUFBQUwzTjBjbVZoYldsNExuTU1BQUFBTDNOMGNtVmhiWEJzWVhrdWN3Z0FBQUF2ZEdobGRtbGtMbk1LQUFBQUwzUm9aWFpwWkdWdkxuTVBBQUFBTDNkM2R5NTFjR3h2WVdSdGNEUXVjd3dBQUFBdmRtVnllWE4wY21WaGJTNG9BQUFBQUNnQkFBQUFVbFFBQUFBb0FBQUFBQ2dBQUFBQWN3Z0FBQUE4YzNSeWFXNW5QbEplQUFBQS9RQUFBSE9VQUFBQUFBRU1BQVFCREFBRUFnd0FDUUVNQUFrQkRBQUpBUXdBQ1FFTUFBa0JEQUFKQVF3QUNRRU1BQWtCREFBSkFnWUJEQUFKQVF3QUNRRU1BQWtCREFBSkFRd0FDUUVNQUFrQkRBQUpBUXdBQ1FFTUFBa0JEQUFKQVF3QUNRRU1BQWtCREFBSkFRd0FDUUVNQUFrQkRBQUpBUXdBQ1FFTUFBa0JEQUFKQVF3QUNRRU1BQWtCREFBSkFRd0FDUUVNQUFrQkRBQU1BbU1DQUFBQUJBQUFBQVFBQUFCREFBQUFjMzhBQUFCMEFBQnFBUUJrQVFCOEFRQVdnd0VBQVhrckFIUUNBR1FDQUJkOEFRQnFBd0JrQXdCa0JBQ0RBZ0FYZkFBQVh3UUFkQVVBZkFBQWd3RUFVMWR1UEFBQkFRRmtCUUJrQUFCc0JnQjlBZ0I0SlFCOEFnQnFCd0NEQUFCRVhSY0FmUU1BZEFBQWFnZ0FaQVlBZkFNQUZvTUJBQUZ4V3dCWFp3QUFVMWhrQUFCVEtBY0FBQUJPY3drQUFBQjBaWGgwYnpvZ0pYTnpDUUFBQUhObFlYSmphRDl4UFZKMEFBQUFkQUVBQUFBcmFmLy8vLzl6QWdBQUFDVnpLQWtBQUFCU0FnQUFBRklaQUFBQVVod0FBQUJTWFFBQUFGSVBBQUFBVWc0QUFBQjBBd0FBQUhONWMzUUlBQUFBWlhoalgybHVabTkwQlFBQUFHVnljbTl5S0FRQUFBQlNDZ0FBQUhRRkFBQUFkR1Y0ZEc5U2hnQUFBSFFFQUFBQWJHbHVaU2dBQUFBQUtBQUFBQUJ6Q0FBQUFEeHpkSEpwYm1jK1VoZ0FBQUFwQVFBQWN4SUFBQUFBQVJFQ0F3RWRBUTRCQXdFTUFSTUJGUUZqQUFBQUFBUUFBQUFJQUFBQVF3QUFBSE5yQUFBQVpBRUFaQUFBYkFBQWZRQUFmQUFBYWdFQVpBSUFnd0VBZlFFQWVFa0FkQUlBUkYxQkFIMENBSHdCQUhRREFHb0VBR1FEQUdvRkFHY0FBSHdDQUVSZEVnQjlBd0IwQmdCOEF3Q0RBUUJlQWdCeFBnQ0RBUUNEQVFCckFnQnlJZ0IwQndCVGNTSUFWM1FJQUZNb0JBQUFBRTVwLy8vLy8zTVVBQUFBUTI5dWRHRnBibVZ5TGxCc2RXZHBiazVoYldWU0hnQUFBQ2dKQUFBQWRBUUFBQUI0WW0xamRBd0FBQUJuWlhSSmJtWnZUR0ZpWld4MEFnQUFBR3d4ZEFZQUFBQmlZWE5sTmpSMENRQUFBR0kyTkdSbFkyOWtaVkpDQUFBQWRBTUFBQUJqYUhKU1FBQUFBRklxQUFBQUtBUUFBQUJTaXdBQUFIUUJBQUFBWVZJeUFBQUFkQUVBQUFCNUtBQUFBQUFvQUFBQUFITUlBQUFBUEhOMGNtbHVaejUwQmdBQUFHd3hNV3d4TVRVQkFBQnpEQUFBQUFBQ0RBRVBBUTBCTndBSUFXbGpBQUFBYVVjQUFBQnBlQUFBQUdreEFBQUFhVm9BQUFCcE1nQUFBR2xzQUFBQWFYVUFBQUJwVEFBQUFHbHVBQUFBYVhBQUFBQnBWZ0FBQUdsMkFBQUFhVzBBQUFCcFNnQUFBR2xvQUFBQWFXSUFBQUJwUmdBQUFHbElBQUFBS0J3QUFBQlNPZ0FBQUZJQUFBQUFkQXdBQUFCd2JHRjBabTl5YldOdlpHVlNBUUFBQUZJQ0FBQUFVZ01BQUFCMENRQUFBR052Y21VdWFYUmxiVklFQUFBQWRBUUFBQUJqYjNKbFVnVUFBQUJTQmdBQUFGSUhBQUFBVWdnQUFBQlNIQUFBQUZJTEFBQUFVZ2tBQUFCU0V3QUFBRklVQUFBQVVoY0FBQUJTRGdBQUFGSXpBQUFBVWxNQUFBQlNRUUFBQUZKZUFBQUFVaGdBQUFCU2t3QUFBRktOQUFBQWRCRUFBQUJYWldKRmNuSnZja1Y0WTJWd2RHbHZiaWdBQUFBQUtBQUFBQUFvQUFBQUFITUlBQUFBUEhOMGNtbHVaejUwQ0FBQUFEeHRiMlIxYkdVK0F3QUFBSE1vQUFBQURBSVFBaHdCRUFFaUF3WURDUVFKRkFrU0NSb0pEQWtwQ1RVSkt3a1ZDU3dKREFrSVlBRUpBQT09JykpKQ=='))