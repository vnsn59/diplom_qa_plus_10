# Задание1
	
SELECT 
    cr.login,
    COUNT(ord."courierId") AS "Количество заказов в доставке"
FROM
    "Couriers" AS cr
INNER JOIN
    "Orders" AS ord ON cr.id = ord."courierId"
WHERE 
    ord."inDelivery" = true
GROUP BY cr.login;

# Задание2
SELECT
    track,
    CASE
        WHEN finished = true THEN 2
        WHEN cancelled = true THEN -1
        WHEN "inDelivery" = true THEN 1
        ELSE 0
    END
FROM
    "Orders";
