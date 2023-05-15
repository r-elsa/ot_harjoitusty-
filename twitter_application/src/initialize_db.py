from db_connection import get_database_connection


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
            id int primary key,
            name text,
            username text,
            password text,           
            profile_picture text,
            admin boolean
        );        
    ''')

    
    cursor.execute('''    
        create table tweet (
            id int primary key,
            user_id int,
            send_time time,
            message text,
            picture_url text
        );  
    ''')

    
    cursor.execute(''' 
        create table like (
            id int primary key,
            user_id int,
            tweet_id int,
            send_time time
        );      
    ''')

    
    cursor.execute('''
        create table comment (
            id int primary key,
            user_id int,
            tweet_id int,
            send_time time,
            message text    
        );       
    ''')

    
    cursor.execute('''
        create table follow (
        id int primary key,
        follower int,
        following int,
        send_time time
        );
       
    ''')

    connection.commit()


def initialize_database():
    connection = get_database_connection()

    drop_tables(connection)
    create_tables(connection)


if __name__ == "__main__":
    initialize_database()
