import joblib
#model_pretrained = joblib.load('LoanOrNot-LR-20230508.pkl')
import numpy as np
 
from flask import Flask, request, render_template
import json as js
app = Flask(__name__)
app.static_folder = 'static'

@app.route("/")
def formPage():
    return render_template('index.html')

@app.route("/submit", methods=['POST'])
def submit():
    return "i"
# @app.route('/judge_age',methods=['post','get'])
# def judge_age():
#     age=js.loads(request.data)
#     if int(age)<=16 and age!="":
#         return "請年紀輸入大於16000"
#     elif int(age)>16:
#         return ""
if __name__ == "__main__":
    app.run()