from flask import Flask , request
import logging
import sys

from routes.desktop import bp as bp_desktop
#logging.basicConfig(datefmt='%Y-%m-%d %H:%M:%S', format='[%(asctime)s][%(levelname)s] %(message)s', level=logging.DEBUG, stream=sys.stdout)
logging.basicConfig(datefmt='%Y-%m-%d %H:%M:%S', format='[%(levelname)s] %(message)s', level=logging.DEBUG, stream=sys.stdout)


app = Flask(__name__)
app.register_blueprint(bp_desktop)


if __name__ == "__main__":
    logging.info("creating app from __main__")
    #create_app().run(host = "0.0.0.0", debug=True)
    #create_app().run()
    app.run(debug=True)



'''


app = Flask(__name__)

from routes.desktop import bp as bp_desktop
app.register_blueprint(bp_desktop)

@app.route('/ping', methods = ['GET', 'POST'])
def ping():

    if request.method == 'GET':
        logging.info(f'data sent: {request.args.to_dict(flat=False)}')
        return f'data sent: {request.args.to_dict(flat=False)}'
    if request.method == 'POST':
        #logging.info(f'keys form: {request.form.keys()}, values: {request.form.values()}')
        logging.info(f'keys data: {request.data}, values: {request.data}')
        return f'data sent: {request.data}'

    return 'pong'
'''













