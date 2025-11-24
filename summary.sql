select * from books;
select  year,
        count(*) as book_count,
        concat('$', round(avg(if(strcmp(currency, "USD"), price * 1.2, price)), 2)) as average
from books
group by year
order by year;
