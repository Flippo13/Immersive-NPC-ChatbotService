from flask import Flask, jsonify, request
from flask_cors import CORS
import requests
import sys
import os


app = Flask(__name__)
CORS(app)
urls = {}


@app.route('/chat')
def main():
    