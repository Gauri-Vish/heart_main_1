from flask import Flask,render_template,request, jsonify
import requests
import pickle


app=Flask(__name__)
model = pickle.load(open('bagging.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/',methods=['GET','POST'])
def predict():
 
    if request.method=='POST':
        
        age = request.form["age"]
        sex=request.form['sex']
        chest_pain=request.form['chest_pain']
        trestbps = request.form['trestbps']
        chol = request.form['chol']
        fbs = request.form['fbs']
        restecg=request.form['restecg']
        thalach = request.form['thalach']
        exang = request.form['exang']
        oldpeak=request.form['oldpeak']
        slope = request.form['slope']
        ca = request.form['ca']
        thal = request.form['thal']
        
        prediction = str(model.predict([[age,sex,chest_pain,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]])[0])
        
        if prediction=='0':
            return render_template('index.html',prediction_text='NO disease')
        else:
            return render_template('index.html',prediction_text='yes disease')
     
       
if __name__ == '__main__':
    app.run(debug=True)