DROP DATABASE IF EXISTS t1;
CREATE DATABASE t1;
USE t1;

CREATE TABLE books (
    book_id BIGINT UNSIGNED,
    title varchar(255),
    author varchar(255),
    genre varchar(255),
    publisher varchar(255),
    year SMALLINT,
    price DECIMAL(28, 2),
    currency ENUM('USD', 'EUR'),
    PRIMARY KEY (book_id)
);
