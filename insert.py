import json
from pathlib import Path
from typing import Any

import mysql.connector

CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': 'safe',
    'db': 't1',
}


def parse(
    book: dict[str, Any],
) -> tuple[
    int,
    str | None,
    str | None,
    str | None,
    str | None,
    int | None,
    str | None,
    str | None,
]:
    def price_currency(price: Any) -> tuple[str, str] | tuple[None, None]:
        if isinstance(price, str) and len(price) > 1:
            if price[0] == '$':
                return price[1:], 'USD'
            if price[0] == '€':
                return price[1:], 'EUR'
        return None, None

    return (
        book['id'],
        # I assume other fields might be missing
        book.get('title'),
        book.get('author'),
        book.get('genre'),
        book.get('publisher'),
        book.get('year'),
        *price_currency(book.get('price', ' ')),
    )


if __name__ == '__main__':
    with Path('out.json').open('r') as f:
        data: list[Any] = json.load(f, object_hook=parse)
        db = mysql.connector.connect(
            host=CONFIG['host'],
            user=CONFIG['user'],
            password=CONFIG['password'],
            database=CONFIG['db'],
        )
        cursor = db.cursor()
        sql = """INSERT INTO books (book_id, title, author, genre, publisher, year, price, currency)
                 VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""

        _ = cursor.executemany(sql, data)
        _ = db.commit()
