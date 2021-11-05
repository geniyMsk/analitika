import psycopg2
import datetime
import random
# from config import DB_USER, DB_PASS, DB_HOST, DB_PORT, DB_NAME
from psycopg2.extras import NamedTupleCursor

import config
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

try:
    connection = psycopg2.connect(user=config.DB_USER,
                                  password=config.DB_PASS,
                                  host=config.DB_HOST,
                                  port=config.DB_PORT)
    connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = connection.cursor()
    cursor.execute(f"""CREATE DATABASE db_bot_analitika""")
    print(f'База данных db_bot_analitika создана')
    cursor.close()
    connection.close()
except:
    pass


def create_tables():
    connection = psycopg2.connect(user=config.DB_USER,
                                  password=config.DB_PASS,
                                  host=config.DB_HOST,
                                  port=config.DB_PORT,
                                  database=config.DB_NAME)
    connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = connection.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS users 
            (chat_id INTEGER UNIQUE, username TEXT, reg_dt DATE, last_message DATE)""")
    # cursor.execute("""CREATE TABLE IF NOT EXISTS stat
    #            (reg_all INTEGER, reg_today INTEGER, last_message INTEGER, last_message_today""")
    cursor.close()
    connection.close()


def add_user(chat_id, username):
    connect = psycopg2.connect(user=config.DB_USER,
                               password=config.DB_PASS,
                               host=config.DB_HOST,
                               port=config.DB_PORT,
                               database=config.DB_NAME)
    connect.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = connect.cursor()
    cursor.execute(f"""INSERT INTO users (chat_id, username, reg_dt) VALUES
                                         ({chat_id}, '{username}', '{datetime.date.today()}')""")
    connect.commit()
    connect.close()


def get_all_chat_id():
    connect = psycopg2.connect(user=config.DB_USER,
                               password=config.DB_PASS,
                               host=config.DB_HOST,
                               port=config.DB_PORT,
                               database=config.DB_NAME)
    connect.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = connect.cursor()
    cursor.execute("""SELECT chat_id FROM users""")
    chat_ids = cursor.fetchall()
    connect.commit()
    connect.close()
    return chat_ids


def set_date_last_message(chat_id):
    connect = psycopg2.connect(user=config.DB_USER,
                               password=config.DB_PASS,
                               host=config.DB_HOST,
                               port=config.DB_PORT,
                               database=config.DB_NAME)
    connect.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = connect.cursor()
    cursor.execute(f"""UPDATE users SET last_message = '{datetime.date.today()}' WHERE chat_id = {chat_id}""")
    connect.commit()
    connect.close()


def count_all_reg():
    connect = psycopg2.connect(user=config.DB_USER,
                               password=config.DB_PASS,
                               host=config.DB_HOST,
                               port=config.DB_PORT,
                               database=config.DB_NAME)
    connect.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = connect.cursor()
    cursor.execute(f"""SELECT count(*) FROM users""")
    all_reg = cursor.fetchone()[0]
    connect.commit()
    connect.close()
    return all_reg


def count_all_reg_today():
    connect = psycopg2.connect(user=config.DB_USER,
                               password=config.DB_PASS,
                               host=config.DB_HOST,
                               port=config.DB_PORT,
                               database=config.DB_NAME)
    connect.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = connect.cursor()
    cursor.execute(f"""SELECT count(*) FROM users WHERE reg_dt = '{datetime.date.today()}'""")
    all_reg_today = cursor.fetchone()[0]
    connect.commit()
    connect.close()
    return all_reg_today


def count_last_message():
    connect = psycopg2.connect(user=config.DB_USER,
                               password=config.DB_PASS,
                               host=config.DB_HOST,
                               port=config.DB_PORT,
                               database=config.DB_NAME)
    connect.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = connect.cursor()
    cursor.execute(f"""SELECT count(*) FROM users WHERE last_message IS NOT NULL""")
    last = cursor.fetchone()[0]
    connect.commit()
    connect.close()
    return last


def count_last_message_today():
    connect = psycopg2.connect(user=config.DB_USER,
                               password=config.DB_PASS,
                               host=config.DB_HOST,
                               port=config.DB_PORT,
                               database=config.DB_NAME)
    connect.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = connect.cursor()
    cursor.execute(f"""SELECT count(*) FROM users WHERE last_message = '{datetime.date.today()}'""")
    last_today = cursor.fetchone()[0]
    connect.commit()
    connect.close()
    return last_today
