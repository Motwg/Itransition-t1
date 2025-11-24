select * from books;

select  year as publication,
        count(*) as book_count,
        concat('$', round(avg(if(strcmp(currency, "USD"), price * 1.2, price)), 2)) as average_price
from books
group by year
order by year;
