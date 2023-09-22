import configuration
import requests
import data

#Создание нового заказа (получение трека в ответе)
def post_new_order(body_order):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=body_order,
                         headers=data.headers)

#Получение заказа по треку
def get_order(track):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_PATH,
                         params={"t":track},
                         headers=data.headers)

