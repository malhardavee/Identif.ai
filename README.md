# Identif.ai 🤖

A simple, real-time face recognition system built with Python, OpenCV, and a custom k-Nearest Neighbors (KNN) algorithm. This project can collect face data from a webcam and then recognize those faces in a live video feed.

## Features

* **Face Data Collection**: Easily capture and store face data for new users.
* **Real-Time Recognition**: Identifies known faces from a live webcam stream.
* **Lightweight**: Uses NumPy and a straightforward KNN model, making it fast and easy to understand.

## Requirements

* Python 3
* OpenCV (`opencv-python`)
* NumPy

You will also need the `haarcascade_frontalface_alt.xml` file in the same directory as the Python scripts.

## Installation

1.  Clone this repository to your local machine:
    ```bash
    git clone [https://github.com/YOUR_USERNAME/Identif.ai.git](https://github.com/YOUR_USERNAME/Identif.ai.git)
    cd Identif.ai
    ```

2.  Install the required Python libraries:
    ```bash
    pip install opencv-python numpy
    ```

## How to Use

This project has two parts: collecting face data and then running the recognition.

### 1. Collect Face Data

Before you can recognize a face, you must add it to the dataset.

1.  First, create a directory to store the data files:
    ```bash
    mkdir face_dataset
    ```
    (Your scripts are set to save and load from this folder.)

2.  Run the data collection script:
    ```bash
    python face_data.py
    ```

3.  The script will ask you to `Enter the name of person : `. Type the person's name and press Enter.

4.  A webcam window will open. Position the person's face in the frame. The script will capture and save samples of the face.

5.  Once you are done, press **`q`** to quit the data collection. This will save a new `.npy` file with that person's name in the `face_dataset` folder.

6.  Repeat this process for each new person you want the system to learn.

### 2. Run Face Recognition

After you have collected data for at least one person, you can run the recognition script.

1.  Run the main recognition script:
    ```bash
    python face_recognition.py
    ```

2.  A webcam window will open. The script will load all the `.npy` data from the `face_dataset` folder, train its KNN model, and begin scanning.

3.  When it recognizes a face, it will draw a green rectangle and label it with the correct name.

4.  Press **`q`** to quit the program.

## File Descriptions

* **`face_data.py`**: Script to capture, process, and save face data from a webcam into a `.npy` file.
* **`face_recognition.py`**: The main script. It loads all saved data, trains the KNN model, and performs real-time recognition.
* **`face_detection.py`**: A simple utility script for testing real-time *detection* (it finds faces but does not identify them).
* **`videoread.py`**: A basic helper script to test if your webcam is correctly configured and working with OpenCV.
* **`haarcascade_frontalface_alt.xml`**: The pre-trained OpenCV model file used for detecting the location of faces in an image.
* **`/face_dataset/`** (Directory): The default folder where all the collected face data (`.npy` files) are stored.
