import logging
import sys
from tkinter import EXCEPTION
from flask import Flask

from housing.exception import HousingException

app=Flask(__name__)

@app.route("/",methods=['Get','Post'])

def index():
    try:
        raise Exception('we are testing exception')
    except Exception as ex:
        housingEx=HousingException(ex,sys)
        logging.info(housingEx.error_message)
        logging.info("log for raising excepiton")

    return "Flask running"

if __name__=="__main__":
    app.run(debug=True)
