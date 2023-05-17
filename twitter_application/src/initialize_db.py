from db_connection import get_db_connection


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


def initialize_database():
    connection = get_db_connection()

    drop_tables(connection)
    create_tables(connection)


if __name__ == "__main__":
    initialize_database()
