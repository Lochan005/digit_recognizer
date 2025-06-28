from flask import Flask, render_template, request, jsonify
import tensorflow as tf
import numpy as np
import re
import base64
from PIL import Image
from io import BytesIO

app = Flask(__name__)
model = tf.keras.models.load_model("model/digit_model.h5")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    img_data = re.sub('^data:image/.+;base64,', '', data['image'])
    img_bytes = base64.b64decode(img_data)
    img = Image.open(BytesIO(img_bytes)).convert("L").resize((28, 28))
    img_array = np.array(img)
    img_array = 1 - img_array / 255.0
    img_array = img_array.reshape(1, 28, 28, 1)
    print("Shape:", img_array.shape)
    print("Pixel values - max:", img_array.max(), "min:", img_array.min())
    prediction = model.predict(img_array)
    predicted_digit = int(np.argmax(prediction))
    return jsonify({"prediction": predicted_digit})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
