use customer;
select * from shopping_data;
SELECT customer_id,COUNT(DISTINCT invoice_no) AS total_orders,MAX(price) AS Total_spent FROM shopping_data 
GROUP BY customer_id 
HAVING COUNT(DISTINCT invoice_no) >= 5 
ORDER BY total_spent DESC LIMIT 1;