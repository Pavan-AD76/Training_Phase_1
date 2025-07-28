use customer;
SELECT gender,max(price) as max_price,min(price) as min_price,avg(price) as avg_price,ROUND(sum(price),2) as sum_price ,count(price) as total
from shopping_data
where gender in ('Male','Female')
group by gender;