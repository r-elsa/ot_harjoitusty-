from db_connection import get_db_connection
import time

from mimesis import Person, Text, Datetime, Internet
from mimesis.locales import Locale
from mimesis import Internet
""" from mimesis.utils import download_image """
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

    ## 1. users
    cursor.execute(
            "insert into user  (id, name, username, password, profile_picture, admin)  values (?, ?, ?, ?, ?, ?)",
            ('user1', 'Chelsea Yu', 'chelseayu_2020', 'chelseayu', 'url', False )
        )
    
    cursor.execute(
            "insert into user  (id, name, username, password, profile_picture, admin)  values (?, ?, ?, ?, ?, ?)",
            ('user2', person.full_name(), person.username(mask=None, drange=(1000, 2100)), person.password(length=8, hashed=False), 'url', False )
        )
    
    cursor.execute(
            "insert into user  (id, name, username, password, profile_picture, admin)  values (?, ?, ?, ?, ?, ?)",
            ('user3', person.full_name(), person.username(mask=None, drange=(1000, 2100)), person.password(length=8, hashed=False), 'url', False )
        )
    
    cursor.execute(
            "insert into user  (id, name, username, password, profile_picture, admin)  values (?, ?, ?, ?, ?, ?)",
            ('user4', person.full_name(), person.username(mask=None, drange=(1000, 2100)), person.password(length=8, hashed=False), 'url', False )
        )
    
    cursor.execute(
            "insert into user  (id, name, username, password, profile_picture, admin)  values (?, ?, ?, ?, ?, ?)",
            ('user5', person.full_name(), person.username(mask=None, drange=(1000, 2100)), person.password(length=8, hashed=False), 'url', False )
        )
    
    cursor.execute(
            "insert into user  (id, name, username, password, profile_picture, admin)  values (?, ?, ?, ?, ?, ?)",
            ('user6', person.full_name(), person.username(mask=None, drange=(1000, 2100)), person.password(length=8, hashed=False), 'url', False )
        )
    
    cursor.execute(
            "insert into user  (id, name, username, password, profile_picture, admin)  values (?, ?, ?, ?, ?, ?)",
            ('user7', person.full_name(), person.username(mask=None, drange=(1000, 2100)), person.password(length=8, hashed=False), 'url', False )
        )
    

    
    """  date = Datetime(start=2023, end=2023, timezone=None) """

   
    ##  tweets (both hardcoded and taken from library mimesis )
    cursor.execute(
            "insert into tweet (id, user_id, send_time, message, picture_url) values (?, ?, ?, ?, ?)",
            ('tweet1', 'user1', time.time(), 'We all enjoy thinking about the past because we miss memories.', 'url')
        )
    
    cursor.execute(
            "insert into tweet (id, user_id, send_time, message, picture_url) values (?, ?, ?, ?, ?)",
            ('tweet2', 'user2', time.time(), ' Imagine ads before dreams every night.', 'url')
        )
    
    cursor.execute(
            "insert into tweet (id, user_id, send_time, message, picture_url) values (?, ?, ?, ?, ?)",
            ('tweet3', 'user3', time.time(), 'I wish it was already possible for AI to create music right for my mood.', 'url')
        )
    
    cursor.execute(
            "insert into tweet (id, user_id, send_time, message, picture_url) values (?, ?, ?, ?, ?)",
            ('tweet4', 'user4', time.time(), 'what do you like?', 'url')
        )
    cursor.execute(
            "insert into tweet (id, user_id, send_time, message, picture_url) values (?, ?, ?, ?, ?)",
            ('tweet5', 'user5', time.time(), 'I just refuse to take a single bite of my food until I find something good to watch.', 'url')
        )
    
    cursor.execute(
            "insert into tweet (id, user_id, send_time, message, picture_url) values (?, ?, ?, ?, ?)",
            ('tweet6', 'user1', time.time(),  text.sentence(), 'url')
        )

    cursor.execute(
            "insert into tweet (id, user_id, send_time, message, picture_url) values (?, ?, ?, ?, ?)",
            ('tweet7', 'user2', time.time(),  text.sentence(), 'url')
        )
    
    cursor.execute(
            "insert into tweet (id, user_id, send_time, message, picture_url) values (?, ?, ?, ?, ?)",
            ('tweet8', 'user2', time.time(),  text.quote(), 'url')
        )
    
    cursor.execute(
            "insert into tweet (id, user_id, send_time, message, picture_url) values (?, ?, ?, ?, ?)",
            ('tweet9', 'user3', time.time(),  text.sentence(), 'url')
        )
    
    cursor.execute(
            "insert into tweet (id, user_id, send_time, message, picture_url) values (?, ?, ?, ?, ?)",
            ('tweet10', 'user4', time.time(),  text.sentence(), 'url')
        )
    
    cursor.execute(
            "insert into tweet (id, user_id, send_time, message, picture_url) values (?, ?, ?, ?, ?)",
            ('tweet11', 'user5', time.time(),  text.quote(), 'url')
        )
    cursor.execute(
            "insert into tweet (id, user_id, send_time, message, picture_url) values (?, ?, ?, ?, ?)",
            ('tweet12', 'user6', time.time(),  text.quote(), 'url')
        )
    

    
    ## likes

    cursor.execute(
            "insert into like (id, user_id, tweet_id, send_time) values (?, ?, ?, ?)",
            ('like1', 'user1', 'tweet1', time.time())
        )
    
    cursor.execute(
            "insert into like (id, user_id, tweet_id, send_time) values (?, ?, ?, ?)",
            ('like2', 'user1', 'tweet2', time.time())
        )
    
    cursor.execute(
            "insert into like (id, user_id, tweet_id, send_time) values (?, ?, ?, ?)",
            ('like3', 'user1', 'tweet3', time.time())
        )
    
    cursor.execute(
            "insert into like (id, user_id, tweet_id, send_time) values (?, ?, ?, ?)",
            ('like4', 'user2', 'tweet1', time.time())
        )

    cursor.execute(
            "insert into like (id, user_id, tweet_id, send_time) values (?, ?, ?, ?)",
            ('like5', 'user2', 'tweet5', time.time())
        )
    
    cursor.execute(
            "insert into like (id, user_id, tweet_id, send_time) values (?, ?, ?, ?)",
            ('like6', 'user3', 'tweet4', time.time())
        )
    
    cursor.execute(
            "insert into like (id, user_id, tweet_id, send_time) values (?, ?, ?, ?)",
            ('like7', 'user3', 'tweet3', time.time())
        )
    
    cursor.execute(
            "insert into like (id, user_id, tweet_id, send_time) values (?, ?, ?, ?)",
            ('like8', 'user4', 'tweet1', time.time())
        )
    
    cursor.execute(
            "insert into like (id, user_id, tweet_id, send_time) values (?, ?, ?, ?)",
            ('like9', 'user5', 'tweet3', time.time())
        )
    
    cursor.execute(
            "insert into like (id, user_id, tweet_id, send_time) values (?, ?, ?, ?)",
            ('like10', 'user6', 'tweet2', time.time())
        )
    
    ###
    cursor.execute(
            "insert into like (id, user_id, tweet_id, send_time) values (?, ?, ?, ?)",
            ('like11', 'user6', 'tweet2', time.time())
        )
    
    cursor.execute(
            "insert into like (id, user_id, tweet_id, send_time) values (?, ?, ?, ?)",
            ('like12', 'user6', 'tweet2', time.time())
        )
    cursor.execute(
            "insert into like (id, user_id, tweet_id, send_time) values (?, ?, ?, ?)",
            ('like13', 'user6', 'tweet2', time.time())
        )
    cursor.execute(
            "insert into like (id, user_id, tweet_id, send_time) values (?, ?, ?, ?)",
            ('like14', 'user6', 'tweet2', time.time())
        )
    cursor.execute(
            "insert into like (id, user_id, tweet_id, send_time) values (?, ?, ?, ?)",
            ('like15', 'user6', 'tweet2', time.time())
        )
    cursor.execute(
            "insert into like (id, user_id, tweet_id, send_time) values (?, ?, ?, ?)",
            ('like16', 'user6', 'tweet2', time.time())
        )
    
    cursor.execute(
            "insert into like (id, user_id, tweet_id, send_time) values (?, ?, ?, ?)",
            ('like17', 'user6', 'tweet2', time.time())
        )
    cursor.execute(
            "insert into like (id, user_id, tweet_id, send_time) values (?, ?, ?, ?)",
            ('like18', 'user6', 'tweet2', time.time())
        )
    cursor.execute(
            "insert into like (id, user_id, tweet_id, send_time) values (?, ?, ?, ?)",
            ('like19', 'user6', 'tweet2', time.time())
        )
    cursor.execute(
            "insert into like (id, user_id, tweet_id, send_time) values (?, ?, ?, ?)",
            ('like20', 'user6', 'tweet2', time.time())
        )



    for i in range(1,50):
    
        cursor.execute(
            "insert into comment (id, user_id, tweet_id, send_time, message) values (?, ?, ?, ?, ?)",
            (f"comment{i}",f"user{random.randint(0,7)}", f"tweet{random.randint(0,12)}", time.time(),text.sentence())
        ) 
 
    connection.commit()


def initialize_database():
    connection = get_db_connection()

    drop_tables(connection)
    create_tables(connection)
    insert_testdata(connection)
   

if __name__ == "__main__":
    initialize_database()
