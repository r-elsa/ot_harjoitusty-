import random
import time
from mimesis import Person, Text, Datetime
from mimesis.locales import Locale
from db_connection import get_db_connection



def drop_tables(connection):
    """ print(date_time) """

    cursor = connection.cursor()

    cursor.execute('''
            drop table if exists user;
    ''')

    cursor.execute('''
            drop table if exists tweet;
    ''')

    cursor.execute('''
            drop table if exists like;
    ''')

    cursor.execute('''
            drop table if exists comment;
        ''')

    cursor.execute('''
            drop table if exists follow;
        ''')

    connection.commit()


def create_tables(connection):
    cursor = connection.cursor()

    cursor.execute('''
        create table user (
            user_id text,
            name text,
            username text,
            password text,
            profile_picture text,
            admin boolean
        );
    ''')

    cursor.execute('''
        create table tweet (
            tweet_id text,
            user_id text,
            send_time time,
            message text,
            picture_url text
        );
    ''')

    cursor.execute('''
        create table like (
            like_id text,
            user_id text,
            tweet_id text,
            send_time time
        );
    ''')

    cursor.execute('''
        create table comment (
            comment_id text,
            user_id text,
            tweet_id text,
            send_time time,
            message text
        );
    ''')

    connection.commit()


def insert_testdata(connection):
    person = Person(Locale.EN)
    text = Text(Locale.EN)

    cursor = connection.cursor()

    # 1. 15 users

    # hardcoded testuser
    cursor.execute(
        "insert into user (user_id, name, username, password,"
        "profile_picture, admin)  values (?, ?, ?, ?, ?, ?)",
        ('user1', 'Chelsea Yu', 'chelseayu', 'chelseayu_8746', 'url', False)
    )

    for i in range(2, 15):

        cursor.execute(
            "insert into user (user_id, name, username, password,"
            "profile_picture, admin)  values (?, ?, ?, ?, ?, ?)",
            (f'user{i}', person.full_name(), person.username(mask=None, drange=(1000, 2100)),
             person.password(length=8, hashed=False), 'url', False)
        )

    # 30 tweets
    for i in range(1, 30):

        cursor.execute(
            "insert into tweet (tweet_id, user_id, send_time,"
            "message, picture_url) values (?, ?, ?, ?, ?)",
            (f'tweet{i}', f"user{random.randint(0,15)}", time.time(),
             random.choice((text.sentence(), text.quote())), 'url')
        )

    # 200 likes
    for i in range(1, 200):
        cursor.execute(
            "insert into like (like_id, user_id, tweet_id, send_time) values (?, ?, ?, ?)",
            (f'like{i}', f"user{random.randint(0,15)}",
             f"tweet{random.randint(0,30)}", time.time())
        )

    # 100 comments
    for i in range(1, 100):
        cursor.execute(
            "insert into comment (comment_id, user_id, tweet_id,"
            "send_time, message) values (?, ?, ?, ?, ?)",
            (f"comment{i}", f"user{random.randint(0,15)}",
             f"tweet{random.randint(0,30)}",
             time.time(), text.sentence())
        )
    connection.commit()


def initialize_database():
    connection = get_db_connection()

    drop_tables(connection)
    create_tables(connection)
    # comment out this line if you want an empty database
    insert_testdata(connection)


if __name__ == "__main__":
    initialize_database()
