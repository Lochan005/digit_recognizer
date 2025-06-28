# digit_recognizer
Handwritten Digit Recognizer Web App

This is a beginner-level result with advance level libraries and a  web application that allows users to draw a digit (0–9) on a canvas and instantly see what digit the AI model predicts.
It combines the power of machine learning (CNN + MNIST) with an interactive Flask-based web interface.

Why I built this

I wanted to explore how a real-world machine learning model can be integrated into an actual web application. Most tutorials stop at model training — but here, I took it further by:

Training a Convolutional Neural Network (CNN) on the MNIST dataset

Creating a clean and interactive frontend where you can draw digits

Deploying the trained model through a Flask API that gives real-time predictions

Dockerizing the entire project for easy deployment anywhere



Features

Draw digits directly in your browser (HTML5 Canvas)

Trained using TensorFlow on MNIST dataset

Real-time predictions from a CNN model

Lightweight Flask backend

Fully containerized with Docker
