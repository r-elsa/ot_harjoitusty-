from db_connection import get_db_connection
import time

def drop_tables(connection):
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
    cursor = connection.cursor()

    ## users
    cursor.execute(
            "insert into user  (id, name, username, password, profile_picture, admin)  values (?, ?, ?, ?, ?, ?)",
            ('user1', 'Chelsea Yu', 'chelseayu', 'chelseayu', 'url', False )
        )
    
    cursor.execute(
            "insert into user  (id, name, username, password, profile_picture, admin)  values (?, ?, ?, ?, ?, ?)",
            ('user2', 'Laura Mccarthy', 'lauramccarthy', 'lauramccarthy', 'url', False )
        )
    
    cursor.execute(
            "insert into user  (id, name, username, password, profile_picture, admin)  values (?, ?, ?, ?, ?, ?)",
            ('user3', 'Dale Stokes', 'dalestokes', 'dalestokes', 'url', False )
        )
    
    cursor.execute(
            "insert into user  (id, name, username, password, profile_picture, admin)  values (?, ?, ?, ?, ?, ?)",
            ('user4', 'Kirk Medina', 'kirkmedina', 'kirkmedina', 'url', False )
        )
    
    cursor.execute(
            "insert into user  (id, name, username, password, profile_picture, admin)  values (?, ?, ?, ?, ?, ?)",
            ('user5', 'Vincent Perry', 'vincentperry', 'vincentperry', 'url', False )
        )
    
    cursor.execute(
            "insert into user  (id, name, username, password, profile_picture, admin)  values (?, ?, ?, ?, ?, ?)",
            ('user6', 'Brett Vargas', 'brettvargas', 'brettvargas', 'url', False )
        )
   
    ## 5 tweets
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
            ('tweet3', 'user2', time.time(), 'I wish it was already possible for AI to create music right for my mood.', 'url')
        )
    
    cursor.execute(
            "insert into tweet (id, user_id, send_time, message, picture_url) values (?, ?, ?, ?, ?)",
            ('tweet4', 'user3', time.time(), 'what do you like?', 'url')
        )
    cursor.execute(
            "insert into tweet (id, user_id, send_time, message, picture_url) values (?, ?, ?, ?, ?)",
            ('tweet5', 'user3', time.time(), 'I just refuse to take a single bite of my food until I find something good to watch.', 'url')
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

 
    connection.commit()


def initialize_database():
    connection = get_db_connection()

    drop_tables(connection)
    create_tables(connection)
    insert_testdata(connection)
   

if __name__ == "__main__":
    initialize_database()
