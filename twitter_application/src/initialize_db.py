from db_connection import get_db_connection
import time

from mimesis import Person, Text, Datetime, Internet
from mimesis.locales import Locale
import random 


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
            id text primary key,
            name text,
            username text,
            password text,           
            profile_picture text,
            admin boolean
        );        
    ''')

    cursor.execute('''    
        create table tweet (
            id text primary key,
            user_id text,
            send_time time,
            message text,
            picture_url text
        );  
    ''')

    cursor.execute(''' 
        create table like (
            id text primary key,
            user_id text,
            tweet_id text,
            send_time time
        );      
    ''')

    cursor.execute('''
        create table comment (
            id text primary key,
            user_id text,
            tweet_id text,
            send_time time,
            message text    
        );       
    ''')

    cursor.execute('''

        create table follow (
        id string primary key,
        follower string,
        following string,
        send_time time
        );
       
    ''')

    connection.commit()


def insert_testdata(connection):
    person = Person(Locale.EN)
    text = Text(Locale.EN)

    """ net = Internet() """
    """ img_url = net.stock_image(category='food', width=1920, height=1080)
    download_image(url=img_url, save_path='/some/path/') """
    
  
    cursor = connection.cursor()

    ## 1. 15 users

    # hardcoded testuser
    cursor.execute(
            "insert into user (id, name, username, password, profile_picture, admin)  values (?, ?, ?, ?, ?, ?)",
            ('user1', 'Chelsea Yu', 'me', 'me', 'url', False )
        )
    
    
    for i in range(2,15):
    
        cursor.execute(
                "insert into user (id, name, username, password, profile_picture, admin)  values (?, ?, ?, ?, ?, ?)",
                (f'user{i}', person.full_name(), person.username(mask=None, drange=(1000, 2100)), person.password(length=8, hashed=False), 'url', False )
            )
   
    # 30 tweets 
    for i in range(1,30):
    
        cursor.execute(
                "insert into tweet (id, user_id, send_time, message, picture_url) values (?, ?, ?, ?, ?)",
                (f'tweet{i}', f"user{random.randint(0,15)}", time.time(), random.choice((text.sentence(),text.quote())), 'url')
            )
    
   
    ## 200 likes
    for i in range(1,200):
        cursor.execute(
            "insert into like (id, user_id, tweet_id, send_time) values (?, ?, ?, ?)",
            (f'like{i}', f"user{random.randint(0,15)}", f"tweet{random.randint(0,30)}", time.time())
        )
    
    
    # 100 comments
    for i in range(1,100):
        cursor.execute(
            "insert into comment (id, user_id, tweet_id, send_time, message) values (?, ?, ?, ?, ?)",
            (f"comment{i}",f"user{random.randint(0,15)}", f"tweet{random.randint(0,30)}", time.time(),text.sentence())
        ) 
 
    connection.commit()


def initialize_database():
    connection = get_db_connection()

    drop_tables(connection)
    create_tables(connection)
    insert_testdata(connection) # comment out this line if you want an empty database
   

if __name__ == "__main__":
    initialize_database()
