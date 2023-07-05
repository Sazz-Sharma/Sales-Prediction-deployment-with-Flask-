from flask import Flask, render_template,request
import numpy as np
import pickle
model = pickle.load(open('model.pkl','rb'))


app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predictSomething():
    tv = int(request.form['TVsales'])
    radio = int(request.form['RadioSales'])
    social = int(request.form['socialSales'])
    inf = int(request.form['influencer'])
    value = model.predict([[tv, radio, social, inf]])[0]
    return render_template('index.html', prediction_text = f"Predicted Sales = ${value:.4f} million", tvPrev=tv,radioPrev=radio, socialPrev= social)
    


if __name__=='__main__':
    app.run(debug=True)