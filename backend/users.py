from connection import db, client
import psycopg2
#  ========== USERS ==========


def get_users():
    try:
        db.execute("SELECT * FROM users")
        return db.fetchall()  # Returns a list of dictionaries
    except psycopg2.Error as e:
        print(e)


def create_user(username, email, password, profile_pic):
    try:
        db.execute(""" 
                INSERT INTO users 
                (username, email, password,profile_pic)
                VALUES (%s, %s, %s, %s) RETURNING *
                """,
                   (username, email, password, profile_pic))
        client.commit()
        return db.fetchall()
    except psycopg2.Error as e:
        print(e)


def get_user_by_username(username):
    try:
        db.execute("SELECT * FROM users WHERE username = %s", (username,))
        return db.fetchone()  # Returns a dictionary
    except psycopg2.Error as e:
        print(e)


def get_user_by_id(user_id):
    try:
        db.execute("SELECT * FROM users WHERE id = %s", (user_id,))
        return db.fetchone()  # Returns a dictionary
    except psycopg2.Error as e:
        print(e)


def update_user_by_id(user_id, username, email, password, profile_pic):
    try:
        db.execute(""" UPDATE users SET username = %s, email = %s, password = %s, profile_pic = %s WHERE id = %s""",
                   (username, email, password, profile_pic, user_id))
        client.commit()
    except psycopg2.Error as e:
        print(e)


def delete_user_by_id(user_id):
    try:
        db.execute("DELETE FROM users WHERE id = %s", (user_id,))
        client.commit()
    except psycopg2.Error as e:
        print(e)
