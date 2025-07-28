WITH CustomerSpend AS (SELECT customer_id, SUM(Price) AS total_spent FROM shopping_data GROUP BY customer_id)
SELECT customer_id,total_spent,spend_rank FROM (
    SELECT customer_id,total_spent,RANK() OVER (ORDER BY total_spent DESC) AS spend_rank FROM CustomerSpend) AS RankedCustomers
WHERE spend_rank <= 5;
