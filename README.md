# Animal Image Classifier Web Application

A lightweight, full-stack web application that uses a deep learning Convolutional Neural Network (CNN) trained on Kaggle to classify uploaded images into distinct animal categories. The project features a responsive, clean frontend interface paired with a Python Flask backend for real-time model inference.

## 🚀 Features
* **Cloud-to-Local Inference:** Run a heavy-duty model trained in the cloud locally on your CPU instantly.
* **Drag-and-Drop / File Upload:** Clean user interface to upload images from your local device.
* **Instant Preview:** Real-time client-side rendering of the uploaded image before analysis.
* **Asynchronous Processing:** Uses the JavaScript Fetch API to communicate with the Flask server backend without reloading the page.
* **Robust Safety Checks:** Server-side validation handles invalid file formats smoothly without crashing.

## 📂 Project Structure
```text
my_classifier_app/
│
├── app.py                       # Flask server and prediction pipeline
├── my_animal_classifier.keras   # Trained Keras model binary (Excluded from Git)
├── .gitignore                   # Safe deployment rules
├── README.md                    # Project documentation
└── templates/
    └── index.html               # Frontend UI layout and interaction logic
🛠️ Tech Stack
Frontend: HTML5, CSS3, JavaScript (Vanilla ES6+)

Backend: Python, Flask

Machine Learning: TensorFlow/Keras, OpenCV, NumPy

🔧 Setup & Installation
1. Clone the Repository
Bash
git clone [https://github.com/YourUsername/YourRepositoryName.git](https://github.com/YourUsername/YourRepositoryName.git)
cd my_classifier_app
2. Set Up a Virtual Environment
It is highly recommended to isolate your dependencies using a virtual environment:

Bash
# Create environment
python -m venv venv

# Activate environment (Windows)
venv\Scripts\activate

# Activate environment (Mac/Linux)
source venv/bin/bin/activate
3. Install Dependencies
Install the required packages using pip:

Bash
pip install flask tensorflow opencv-python numpy
4. Place Your Model File
Ensure you download your trained model binary (my_animal_classifier.keras) from your Kaggle notebook output and paste it directly into the root directory (my_classifier_app/).

Note: This file is automatically ignored by Git via .gitignore to prevent repository bloating.

🏃 How to Run the Application
Make sure your virtual environment is active.

Launch the Flask development server:

Bash
python app.py
Open your web browser and navigate to:

Plaintext
[http://127.0.0.1:5000](http://127.0.0.1:5000)
Upload an image (supported classes: Cat, Dog, Bird, Frog, Horse, etc.) and click Analyze Image to view the classification result and model confidence score.