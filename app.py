from flask import Flask, request, jsonify, render_template
import cv2
import numpy as np
from tensorflow.keras.models import load_model

app = Flask(__name__)

# Load the model once when the server starts
print("Loading model...")
model = load_model('my_animal_classifier.keras')
print("Model loaded successfully!")

class_names = ['Airplane', 'Automobile', 'Bird', 'Cat', 'Deer', 
 'Dog', 'Frog', 'Horse', 'Ship', 'Truck']

@app.route('/')
def home():
    # Serve the HTML UI
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'})
    
    file = request.files['file']
    
    # 1. Convert the uploaded web file into an OpenCV image array
    file_bytes = np.frombuffer(file.read(), np.uint8)
    image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
    
    if image is None:
        return jsonify({'error': 'Invalid image format'})

    # 2. Process exactly like your training data
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image_resized = cv2.resize(image, (32, 32))
    img_ready = np.expand_dims(image_resized, axis=0) / 255.0
    
    # 3. Make the prediction
    predictions = model.predict(img_ready)[0]
    
    # Get the top prediction
    predicted_index = np.argmax(predictions)
    confidence = float(np.max(predictions) * 100)
    label = class_names[predicted_index]
    
    # Return the result as JSON to the frontend
    return jsonify({
        'label': label,
        'confidence': round(confidence, 2)
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)