import sender_stand_requests
import data

def assert_status_code_success(response):
    assert response.status_code == 200

#Создание заказа и получение трека заказа
def create_new_order_get_track():
    order_body = data.body_order.copy()
    response = sender_stand_requests.post_new_order(order_body)
    return response.json()["track"]

#Проверка на получение заказа по треку со статусом 200 ответ
#Ольга Петрова 08-а когорта "Инженер по тестированию плюс"Дипломная работа
def test_order():
    track = create_new_order_get_track()
    response = sender_stand_requests.get_order(track)
    assert_status_code_success(response)
