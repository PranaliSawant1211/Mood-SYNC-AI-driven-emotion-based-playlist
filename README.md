# Mood-Based-Music-Player-Final-year-project-
Mood based music player is designed to generate music based on the user's emotional state and mood. The deep learning algorithm used in this project is a Convolutional Neural Network (CNN) which categorizes facial expressions into seven sentiments. This dataset consists of 35.887 grayscale, 48x48 sized face images with various emotions - 7 emotions, all labeled.

We have implemented a Music Generation Model using Long short-term memory (LSTM) algorithm where the one hot encoded vector will be translated and result in MIDI (Music Instrument Digital Interface) file format.

The main aim of this project is to help the user automatically play songs based on their emotions. It captures images using the webcam, tone mapping of the image, and facial expression extraction, and then classifies the type of emotion using a classifier to generate the playlist according to the emotion.

This project also takes human facial images containing some expression as input and recognizes and classifies them into appropriate expression classes such as happy, sad, and neutral. A playlist is created according to seven different types of emotion. This provides users with more customized and organized playlists and a better platform for all music listeners.

Our goal is to ensure automation of song selection and periodic updating of playlists, providing user-preferred music with emotion awareness. The project utilizes the Fer2013 open-source dataset created for an ongoing project by Pierre-Luc Carrier and Aaron Courville, which is shared publicly for a Kaggle competition, shortly before ICML 2013.
