from connection import db, client
#  ========== JOB POST ==========


def create_job_post(user_id, title, description, location, salary, job_type, company_name, company_logo, company_url, company_email):
    db.execute(""" 
               INSERT INTO job_post (user_id, title, description, location, salary, job_type, company_name, company_logo, company_url, company_email)
               VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
               """,
               (user_id, title, description, location, salary, job_type, company_name, company_logo, company_url, company_email))
    client.commit()


def get_job_post():
    db.execute("SELECT * FROM job_post")
    return db.fetchall()  # Returns a dictionary


def get_job_post_by_id(job_post_id):
    db.execute("SELECT * FROM job_post WHERE id = %s", (job_post_id,))
    return db.fetchone()  # Returns a dictionary


def get_job_post_by_user_id(user_id):
    db.execute("SELECT * FROM job_post WHERE user_id = %s", (user_id,))
    return db.fetchall()  # Returns a dictionary


def update_job_post(title, description, location, salary, job_type, company_name, company_logo, company_url, company_email, job_post_id):
    db.execute("""
               UPDATE job_post SET title = %s, 
               description = %s, location = %s,
               salary = %s, job_type = %s,
               company_name = %s, company_logo = %s,
               company_url = %s,
               company_email = %s
               WHERE id = %s""",
               (title, description, location, salary, job_type, company_name, company_logo, company_url, company_email, job_post_id))
    client.commit()


def delete_job_post(job_post_id):
    db.execute("DELETE FROM job_post WHERE id = %s", (job_post_id,))
    client.commit()


def get_job_post_by_location(location):
    db.execute("SELECT * FROM job_post WHERE location = %s", (location,))
    return db.fetchall()  # Returns a dictionary


def get_job_post_by_job_type(job_type):
    db.execute("SELECT * FROM job_post WHERE job_type = %s", (job_type,))
    return db.fetchall()  # Returns a dictionary


def get_job_post_by_salary(salary):
    db.execute("SELECT * FROM job_post WHERE salary = %s", (salary,))
    return db.fetchall()  # Returns a dictionary


def get_job_post_by_company_name(company_name):
    db.execute("SELECT * FROM job_post WHERE company_name = %s", (company_name,))
    return db.fetchall()  # Returns a dictionary


def get_job_post_by_title(title):
    db.execute("SELECT * FROM job_post WHERE title = %s", (title,))
    return db.fetchall()  # Returns a dictionary


def get_job_post_by_company_email(company_email):
    db.execute("SELECT * FROM job_post WHERE company_email = %s",
               (company_email,))
    return db.fetchall()  # Returns a dictionary
