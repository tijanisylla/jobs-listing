import psycopg2
import psycopg2.extras
from dotenv import load_dotenv
import os
# import jwt


#  ========== DATABASE CONNECTION ==========
load_dotenv()
database_url = os.getenv("DATABASE_URL")

client = psycopg2.connect(database_url)
db = client.cursor(cursor_factory=psycopg2.extras.DictCursor)


def create_table_user():
    try:
        db.execute("""
                   CREATE TABLE IF NOT EXISTS users (
                   id SERIAL PRIMARY KEY,
                   username VARCHAR(255) NOT NULL,
                   email VARCHAR(255) NOT NULL,
                   password VARCHAR(255) NOT NULL,
                   profile_pic VARCHAR(255) NULL
                   );
                 """

                   )
        client.commit()
        print("Users table created!")
    except Exception as e:
        print(e)


def create_jobs_table():
    try:
        db.execute(""" 
               
                CREATE TABLE IF NOT EXISTS job_post (
                id SERIAL PRIMARY KEY,
                title VARCHAR(255) NOT NULL,
                description VARCHAR(255) NOT NULL,
                location VARCHAR(255) NOT NULL,
                salary VARCHAR(255) NOT NULL,
                job_type VARCHAR(255) NOT NULL,
                company_name VARCHAR(255) NOT NULL,
                company_logo VARCHAR(255) NOT NULL,
                company_url VARCHAR(255) NOT NULL,
                company_email VARCHAR(255) NOT NULL,
                user_id INTEGER NOT NULL,
                FOREIGN KEY (user_id) REFERENCES users (id)
                );
               """)
        client.commit()
        print("Jobs table created!")
    except Exception as e:
        print(e)


# ========== CHECK IF DATABASE EXISTS  ==========
def check_db():
    if database_url:
        return True
    else:
        return False


print("Checking if database exists...", check_db())
if check_db() == True:
    print("Database exists!")
    create_table_user()
    create_jobs_table()
else:
    print("Database does not exist!")

print("Database connection successful!", check_db())
