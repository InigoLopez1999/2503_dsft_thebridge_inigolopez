import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import mean_squared_error, mean_absolute_percentage_error
from sklearn.linear_model import Lasso
import pickle
import os
from flask import Flask, jsonify, request, abort

app = Flask(__name__)
app.config["DEBUG"] = True

print(__file__)

print(os.path.dirname(__file__))
os.chdir(os.path.dirname(__file__))

# End Point "/"
@app.route('/', methods=['GET'])
def home():
    return "<h1>My API</h1><p>Esta es una API para predicción de ventas en función de la inversión en marketing.</p>"

@app.route('/v1/predict', methods=['GET'])
def predict():
    # Cargar el modelo
    # Obtener los parámetros del request
    # Hacer la predicción y devolverla
    model = pickle.load(open('ad_model.pkl','rb'))
    tv = request.args.get('tv', None)
    radio = request.args.get('radio', None)
    newspaper = request.args.get('newspaper', None)

    print(tv,radio,newspaper)
    print(type(tv))

    if tv is None or radio is None or newspaper is None:
        return "Args empty, the data are not enough to predict"
    else:
        prediction = model.predict([[float(tv),float(radio),float(newspaper)]])
    
    return jsonify({'predictions': prediction[0]})

app.run()