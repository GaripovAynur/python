#!/bin/python3

import psycopg2
import sys
from loguru import logger

logger.add("diff_modules.log", format="{message}", level="INFO")

host_connect_server = sys.argv[1]
database_connect = sys.argv[2]
user_connect = sys.argv[3]
table = sys.argv[4]
host_connect_test_countur = sys.argv[5]
password_connect = sys.argv[6]

def connect_db(
        host = None,
        user = None,
        password = None,
        database = None
    ):

    connection = psycopg2.connect(
        host = host,
        user = user,
        password = password,
        database = database
    )
 
    with connection.cursor() as cursor:
        cursor.execute(
            f" SELECT id, name, description, enabled from {table} ORDER BY id;"
        )

        list_result = cursor.fetchall()
    return list_result


prod_resulte = set(connect_db(host=host_connect_server, user=user_connect, password=password_connect, database=database_connect))
test_resulte = set(connect_db(host=host_connect_test_countur, user=user_connect, password=password_connect, database=database_connect))
difference_modules = list(prod_resulte.difference(test_resulte))
if difference_modules:
    for index_difference_modules in range(len(difference_modules)):
        if difference_modules[index_difference_modules][3] == "True":
            logger.info(f"""Выключить модуль на тестовом контуре, ID: {difference_modules[index_difference_modules][0]}, NAME: {difference_modules[index_difference_modules][1]}, DESCRIPTION:  {difference_modules[index_difference_modules][2]}""")
        else:
            logger.info(f"""Включить модуль на тестовом контуре, ID: {difference_modules[index_difference_modules][0]}, NAME: {difference_modules[index_difference_modules][1]}, DESCRIPTION:  {difference_modules[index_difference_modules][2]}""")

else:
     logger.info("Нет разницы, все модули совподают")
