import json
from pathlib import Path
from typing import Any

import mysql.connector


def parse(
    book: dict[str, Any],
) -> tuple[
    int | None,
    str | None,
    str | None,
    str | None,
    str | None,
    int | None,
    str | None,
    str | None,
]:
    def price_currency(price: str | Any) -> tuple[str, str] | tuple[None, None]:
        if price[0] == '$':
            return price[1:], 'USD'
        if price[0] == '€':
            return price[1:], 'EUR'
        return None, None

    return (
        book.get('id'),
        book.get('title'),
        book.get('author'),
        book.get('genre'),
        book.get('publisher'),
        book.get('year'),
        *price_currency(book.get('price', ' ')),
    )


if __name__ == '__main__':
    with Path('out.json').open('r') as f:
        data: list[Any] = json.load(
            f,
            object_hook=parse,
        )
        db = mysql.connector.connect(host='localhost', user='root', password='safe', database='t1')
        cursor = db.cursor()
        sql = """INSERT INTO books (book_id, title, author, genre, publisher, year, price, currency)
                 VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""

        _ = cursor.executemany(sql, data)
        _ = db.commit()
