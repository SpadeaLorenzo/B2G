import sys
import logging
logging.basicConfig(datefmt='%Y-%m-%d %H:%M:%S', format='[%(levelname)s] %(message)s', level=logging.DEBUG, stream=sys.stdout)
logging.info('\n'.join(sys.path))
logging.info(f'current path: {__file__}')

from db_connect import get_connection
from datetime import  datetime , date

import json
from flask import Blueprint , request , render_template


bp = Blueprint('desktop', __name__)

# Function that defines if the code of the match exixst in the database.
def match_exists(match_code):
    try:
        cnx = get_connection()
        cur = cnx.cursor(dictionary=True)
        query = ("Select code FROM matches")
        cur.execute(query)
        for row in cur:
            if(row == row[match_code]):
                return True
            cur.close()
            cnx.close()
    except Exception as e:
        logging.exception(e)
    return False


#This function inserts the data of a new match inside the db.
@bp.route("/desktop/newmatch" , methods=['POST'])
def get_insert_new_match():
    if request.method == 'POST':
        content_type = request.headers.get('Content-Type')
        if(content_type == 'application/json'):
            json = request.json
            c = json["code"]
            p = json["players"]
            w = json["winner"]
            t = json["turns"]
            i = json["is_done"]
            new_match(c,p,w,t,i)
        else:
            print("invalid content type")
    else:
        print("invalid method request");
    return "200"



def new_match(c,p,w,t,i):
    try:
        cnx = get_connection()
        cursor = cnx.cursor()
        now = datetime.now()
        statement = """INSERT INTO matches(code, players, data_match, winner, turns,is_done ) VALUES (%s,%s,%s,%s,%s,%s)"""
        val = (c,p,now,w,t,i)
        cursor.execute(statement, val)
        cursor.close()
        cnx.commit()
        cnx.close()
    except Exception as e:
        logging.exception(e)
        return False


#Retursn al the matches stored in the db
@bp.route("/macthes")
def get_matches():
    try:
        cnx = get_connection()
        cur = cnx.cursor(dictionary=True)
        query = ("Select * FROM matches")
        cur.execute(query)
        for row in cur:
            print(row)
        cur.close()
        cnx.close()
    except Exception as e:
        logging.exception(e)
    return False

@bp.errorhandler(404)
def page_not_found(e):
	"""Gestisce gli errori 404 delle pagine non trovate."""
	logging.exception(f'Error 404: {e}')
	return render_template("error.html", message = "La pagina non è stata trovata.", details = str(e))

@bp.route("/desktop/ping2" , methods = ['GET', 'POST'])
def ping():

    if request.method == 'GET':
        logging.info(f'data sent: {request.args.to_dict(flat=False)}')
        return f'data sent: {request.args.to_dict(flat=False)}'
    if request.method == 'POST':
        #logging.info(f'keys form: {request.form.keys()}, values: {request.form.values()}')
        logging.info(f'keys data: {request.data}, values: {request.data}')
        return f'data sent: {request.data}'

    return 'pong'
#route for switching rounds
#route for


