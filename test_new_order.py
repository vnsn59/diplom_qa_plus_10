import sender_requests
import pytest


# Позитивная проверка
def positive_assert(track):
    response_to_order = sender_requests.get_order_track(track)
    assert response_to_order.status_code == 200


# Тест из задания.
# Проверка, что по треку заказа можно получить данные о заказе
def test_get_success_response_for_track_order():
    positive_assert(sender_requests.track_number_parsing())