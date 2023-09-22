Автоматизация теста к API
Шаги автотеста:
1.Выполнить запрос на создание заказа.
2.Сохранить номер трека заказа.
3.Выполнить запрос на получения заказа по треку заказа.
4.Проверить, что код ответа равен 200.
Для запуска тестов должны быть установлены пакеты pytest и requests
Запуск всех тестов выполянется командой pytest.

SQl ЗАПРОСЫ 

SELECT
    "Couriers"."login",
COUNT(*)
FROM
    "Orders"
LEFT JOIN "Couriers" ON "Orders"."courierId" = "Couriers"."id"
WHERE
    "Orders"."inDelivery" = True
GROUP BY "Couriers"."login";


2/SELECT
    "Orders"."track",
CASE
    WHEN "Orders"."finished" = True THEN 2
    WHEN "Orders"."cancelled" = True THEN -1
    WHEN "Orders"."inDelivery" = True THEN 1
    ELSE 0
END as expectedStatus
FROM
    "Orders";