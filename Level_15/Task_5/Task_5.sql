use customer;
select * from shopping_data;
SELECT customer_id, COUNT(customer_id) FROM shopping_data where invoice_date between '01-02-2025' and '01-05-2025' GROUP BY customer_id HAVING COUNT(customer_id) > 1