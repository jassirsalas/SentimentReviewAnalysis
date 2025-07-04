from flask import Flask, request, jsonify
import joblib
import re
import os

app = Flask(__name__)

MODEL_PATH = './trained_model.pkl'


# load modedel
try:
    model = joblib.load(MODEL_PATH)
    print("model loaded")
except FileNotFoundError:
    print(f"Error: check model path")
    exit()

def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    return text

@app.route('/predict', methods=['POST'])
def predict():
    if not request.is_json:
        return jsonify({"error": "json request needed"}), 400

    data = request.get_json()
    comentario = data.get('comentario')

    if not comentario:
        return jsonify({"error": "field 'comentario' not found in json"}), 400

    clean_comment = preprocess_text(comentario)

    prediction = model.predict([clean_comment])[0]

    return jsonify({"sentimiento_predicho": prediction})

if __name__ == '__main__':
    if not os.path.exists(MODEL_PATH):
        print("check model path. run 'python main.py' first")
        exit()

    app.run(host='0.0.0.0', port=5000)