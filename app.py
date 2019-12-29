from flask import Flask
from flask import request
from flask import render_template
#import requests
import numpy as np
from sklearn.externals import joblib
app=Flask(__name__)
model=joblib.load('model.pkl')
@app.route('/')
def home():
    return "HELLO"
@app.route('/predict',methods=['GET','POST'])
def predict():
  out=""
  if(request.method=='POST'):
    x1=float(request.form["x1"])
    x2=float(request.form["x2"])
    x3=float(request.form["x3"])
    x4=float(request.form["x4"])
    data=[[x1,x2,x3,x4]]
    out=model.predict(data)
  return render_template('home.html',out=out)
if __name__ == '__main__':
   app.run(debug = True,port=3000)