import os, sys
# We'll render HTML templates and access data sent by POST
# using the request object from flask. Redirect and url_for
# will be used to redirect the user once the upload is done
# and send_from_directory will help us to send/show on the
# browser the file that the user just uploaded
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from werkzeug import secure_filename

# Initialize the Flask application
app = Flask(__name__)

@app.route('/')
def api_hello1():
    return render_template( 'Main.html')

@app.route('/moreinformation')
def api_hello2():
    return render_template( 'Usage.html')

@app.route('/addServices')
def api_hello3():
    return render_template( 'Cart.html')


#hostName = '10.154.205.158'
if __name__ == '__main__':
    app.run(
        host='localhost',
        #hostName,
        port=int("80"),
        debug=True
    )
