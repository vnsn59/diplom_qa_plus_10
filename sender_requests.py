import configuration as config
import data
import requests


# Запрос на создание заказа
def post_new_order(create_order):
    return requests.post(config.URL_SERVICE + config.CREATE_ORDER,
                         json=create_order,
                         headers=data.headers)


# Парсинг ответа о создании заказаБ чтобы достать трек
def track_number_parsing(order=data.create_order):
    return post_new_order(order).json()["track"]


# Запрос на получение заказа по треку
def get_order_track(track=track_number_parsing()):
    return requests.get(config.URL_SERVICE + config.GET_ORDER_TRACK,
                        params={"t": track})
