from flask import Flask, render_template, jsonify, request
import joblib
import numpy as np
from tensorflow.keras.models import load_model

app = Flask(__name__)

# Cargar el modelo y scaler
model = load_model('modelo_prediccion_oro.keras')  # Asegúrate de que el archivo esté en la misma carpeta
scaler = joblib.load('scaler.pkl')  # Asegúrate de que el archivo scaler.pkl esté en la misma carpeta

# Ruta para la página principal
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para predecir el precio del oro
@app.route('/predecir')
def predecir():
    horizon = int(request.args.get('horizon', 5))  # El valor del horizonte, por defecto 5 días

    # Lógica para generar la predicción
    # Aquí debes pasar las características necesarias para la predicción
    # Esto puede cambiar dependiendo de cómo estés gestionando los datos de entrada
    X_test = np.random.randn(1, 90, 9)  # Solo un ejemplo, sustituye con la entrada real

    # Normaliza las entradas
    X_test_scaled = scaler.transform(X_test.reshape(-1, 9)).reshape(1, 90, 9)

    # Predicción
    prediccion = model.predict(X_test_scaled)
    prediccion = prediccion.flatten().tolist()  # Convertir la predicción a una lista para devolverla

    return jsonify({'prediccion': prediccion})

# Ejecutar el servidor
if __name__ == '__main__':
    app.run(debug=True)
