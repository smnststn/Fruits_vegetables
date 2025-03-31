from flask import Flask, request, jsonify
import tensorflow as tf
from PIL import Image
import numpy as np
import json

app = Flask(__name__)

# Load Model
model = tf.keras.models.load_model('C:/Users/smnst/Fruits_vegetables/our_model.keras', compile=False)

# Load class labels from JSON
with open("class_labels.json", "r") as json_file:
    class_labels_dict = json.load(json_file)

# Convert keys to integers (JSON saves them as strings)
class_labels_dict = {int(k): v for k, v in class_labels_dict.items()}

def preprocess_image(image):
    image = image.resize((224, 224))  # Adjust to model input size
    image = np.array(image) / 255.0
    image = np.expand_dims(image, axis=0)
    return image

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files and 'url' not in request.form:
        return jsonify({"error": "No file or URL provided"}), 400

    # Process file or URL input
    if 'file' in request.files:
        file = request.files['file']
        # Process image file here
    elif 'url' in request.form:
        url = request.form['url']
        # Process image from URL here

    # Return a prediction (modify according to your model)
    prediction = "apple"  # example of the predicted class

    return jsonify({"prediction": prediction})
