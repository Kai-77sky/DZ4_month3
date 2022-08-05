import sqlite3
from config import bot


def sql_create():
    global connection, cursor
    connection = sqlite3.connect("db.sqlite3")
    cursor = connection.cursor()
    if connection:
        print("database connected successfully")
    connection.execute(
        """
        CREATE TABLE IF NOT EXISTS menu 
        (photo TEXT, name TEXT PRIMARY KEY, description TEXT,price INTEGER)
        """
    )


async def sql_insert(state):
    async with state.proxy() as data:
        cursor.execute("""
        INSERT INTO tvshow VALUES (?, ?, ?,?)
        """, tuple(data.values()))
        connection.commit()


async def sql_select(message):
    for result in cursor.execute("""SELECT * FROM menu""").fetchall():
        await bot.send_photo(message.chat.id,
                             result[0],
                             caption=f'Title {result[1]}\n'
                                     f'Description: {result[2]}')





async def sql_casual_select():
    return cursor.execute("""SELECT * FROM menu""").fetchall()




async def sql_delete(data):
    cursor.execute("""
    DELETE FROM menu WHERE title == ?
    """, (data,))
    connection.commit()
