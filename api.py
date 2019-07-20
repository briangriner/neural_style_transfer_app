from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS
from pandas import DataFrame
import os
import io
import pandas as pd
import numpy as np
from pandas import DataFrame
import json
import requests
import urllib3
import re
from matplotlib import pylab
from sklearn import linear_model
import math
# API stuff
app = Flask(__name__)
CORS(app)  # <-- CORS is necessary for React.js's Axion to be able to use the methods in the api!
api = Api(app)

notes = {}


class Test(Resource):
    def put(self):
        # Parsing. View docs(https://flask-restful.readthedocs.io/en/latest/) if this isn't what you need.
        # parser.add_argument('list', action='append') lets flask know that list an argument that can hold 2+ pieces of data in this data :
        # put('http://localhost:5000/', data={"list" : ["When was Barack Obama's birthday?", "What is 10 plus 5 equal to?"]}).json()
        # With that, you have one piece of metadata associated with 2 or more peice of data(aka a list) that can be indexed
        # args is the main class here, and since list is the subclass(an arg of class args) of args, we can mention it freely
        # and access it like this : args.list. We can index by doing args.list[index]

        parser = reqparse.RequestParser()
        parser.add_argument('paths',action='append')
        args = parser.parse_args()
        paths=list(args.paths)
        print("PATHS",paths)
        function_to_call = "python neural_style_transfer_BG.py"+ " " + paths[0]+" " +paths[1]+" " + paths[2]+" --iter 1"
        os.system(function_to_call)
        z = {'output': "SUCCESS"}  # Formatting this is important. If you don't format it right,
        return z


api.add_resource(Test, '/')

if __name__ == '__main__':
    app.run(port=5001, debug=True)
