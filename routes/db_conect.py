import mysql.connector
import logging
from mysql.connector import (connection)
from flask_mysqldb import MySQL

def get_connection():
  try:
    cnx = mysql.connector.connect(user='Bowling2gether',password='Vy3A33B4!yAi@J3',host='Bowling2gether.mysql.pythonanywhere-services.com',database='Bowling2gether$Bowling')
    logging.debug('connection established')
    return cnx
  except mysql.connector.Error as err:
    logging.exception('error during db connection' , msg=err)
