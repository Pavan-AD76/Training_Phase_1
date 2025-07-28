use customer;
select * from shopping_data;
SELECT ROUND(SUM(price) / COUNT(DISTINCT invoice_no),2) AS Average_Order_Value FROM shopping_data;
