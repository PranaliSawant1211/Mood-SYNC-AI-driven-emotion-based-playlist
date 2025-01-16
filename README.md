# MOOD SYNC: AI driven emotion based playlist

The **MOOD SYNC** is an **AI-driven platform** designed to generate music based on the user's emotional state and mood. By leveraging cutting-edge deep learning algorithms, this project provides a personalized music experience by analyzing facial expressions and categorizing them into different emotional classes.

## 🚀 Project Overview

- **AI-Powered Emotion Detection**: Utilizes Convolutional Neural Networks (CNN) to analyze facial expressions and classify them into seven emotions.
- **AI-Driven Music Generation**: Implements a Long Short-Term Memory (LSTM) model to dynamically generate music in MIDI (Music Instrument Digital Interface) format based on detected emotions.
- **Customized Playlists**: Automatically generates playlists tailored to the user’s mood, ensuring an engaging and personalized music experience.
- **Facial Expression Analysis**: Uses AI-based techniques for tone mapping, emotion recognition, and playlist creation.

## 🎯 Key Features

- **Emotion Analysis with AI**: Captures images using the webcam, processes them with deep learning models, and classifies emotions (e.g., happy, sad, neutral).
- **AI-Based Playlist Creation**: Generates personalized playlists for seven different emotions, including happy, sad, neutral, and more.
- **Dynamic Music Generation**: Employs LSTM for generating music files based on emotional categories, ensuring a unique and adaptive music experience.
- **Automation**: Automates song selection and periodic playlist updates based on real-time emotion detection.
- **Dataset**: Uses the **FER2013** open-source dataset, specifically designed for emotion recognition tasks.

## 🛠️ Technologies Used

- **Deep Learning**: Convolutional Neural Networks (CNN), Long Short-Term Memory (LSTM)
- **Programming Language**: Python
- **Libraries**: TensorFlow, Keras, OpenCV, NumPy, pandas
- **File Formats**: MIDI for music generation
- **Tools**: Haar Cascade Classifier for face detection


## 💡 Getting Started

### Prerequisites

- Python 3.x installed
- Required libraries: TensorFlow, Keras, OpenCV, NumPy, pandas

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/Mood-Based-Music-Player.git
   cd Mood-Based-Music-Player

2. Install Dependencies
    pip install -r requirements.txt

3. Run the application:
    python app1.py

4. Access the platform:
     Open your browser and navigate to http://127.0.0.1:5000.

📌 Dataset
The project uses the FER2013 dataset, an open-source dataset containing grayscale images of faces labeled with seven emotions:

-> Angry

-> Disgust

-> Fear

-> Happy

-> Sad

-> Surprise
-> Neutral

The dataset was created for an ongoing project by Pierre-Luc Carrier and Aaron Courville and shared publicly for a Kaggle competition.

    
