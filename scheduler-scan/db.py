import mysql.connector
import os
import uuid
from datetime import datetime, timedelta

user = os.environ.get('DB_USER')
password = os.environ.get('DB_PASSWORD')
host = os.environ.get('DB_HOST')
database = os.environ.get('DB_DATABASE')

def get_domains():
    try:
        # print('[*] connecting to db')
        cnx = mysql.connector.connect(user=user, password=password, host=host, database=database)
    except Exception as ex:
        print(ex)
        exit(1)

    cursor = cnx.cursor()
    stmt = "SELECT * FROM wp_posts WHERE post_type = 'domain'"
    cursor.execute(stmt)
    domains = [parse_cpt(domain) for domain in cursor.fetchall()]
    cursor.close()
    cnx.close()

    return domains

def get_user_role(id):
    try:
        # print('[*] connecting to db')
        cnx = mysql.connector.connect(user=user, password=password, host=host, database=database)
    except Exception as ex:
        print(ex)
        exit(1)

    cursor = cnx.cursor()
    stmt = "select * from wp_usermeta where meta_key = 'wp_capabilities'"
    cursor.execute(stmt)
    users = [user for user in cursor.fetchall()]
    usermeta = [user for user in users if user[1] == id].pop()

    cursor.close()
    cnx.close()

    return parse_usermeta(usermeta)['meta_value']

def set_scan_status(status, id):
    try:
        # print('[*] connecting to db')
        cnx = mysql.connector.connect(user=user, password=password, host=host, database=database)
    except Exception as ex:
        print(ex)
        exit(1)

    cursor = cnx.cursor()
    stmt = f"UPDATE wp_posts SET post_content_filtered = '{status}' WHERE id = '{id}'"
    cursor.execute(stmt)
    cnx.commit()
    cursor.close()
    cnx.close()


def parse_cpt(cpt_raw):
    return {
        'id': cpt_raw[0],
        'post_author': cpt_raw[1],
        'post_date': cpt_raw[2],
        'post_date_gmt': cpt_raw[3],
        'post_content': cpt_raw[4],
        'post_title': cpt_raw[5],
        'post_excerpt': cpt_raw[6],
        'post_status': cpt_raw[7],
        'comment_status': cpt_raw[8],
        'ping_status': cpt_raw[9],
        'post_password': cpt_raw[10],
        'post_name': cpt_raw[11],
        'to_ping': cpt_raw[12],
        'pinged': cpt_raw[13],
        'post_modified': cpt_raw[14],
        'post_modified_gmt': cpt_raw[15],
        'post_content_filtered': cpt_raw[16],
        'post_parent': cpt_raw[17],
        'guid': cpt_raw[18],
        'menu_order': cpt_raw[19],
        'post_type': cpt_raw[20],
        'post_mime_type': cpt_raw[21],
        'comment_count': cpt_raw[22],

    }

def parse_usermeta(raw):
    return {
        'umeta_id': raw[0],
        'user_id': raw[1],
        'meta_key': raw[2],
        'meta_value': raw[3],
    }