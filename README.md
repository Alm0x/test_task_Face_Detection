# test_task_Face_Detection
This repository contains solution for Test task 1 of these "Detection of face substitution by the photo on video of the proctoring system"

# How to start the application:
### 1. Download `openCV` by running the following command:
`pip install opencv-python` (or `pip3 install opencv-python` in case you have python3 installed)
### 2. Run the following command to start the application:
`python main.py <filename>` (or `python3 main.py <filename>` in case you have python3 installed)

`filename` here is path to the video you want to handle, for example you can use provided test videos: 
`python main.py videos/one_person.mp4`

### 3. Results:
You can find edited video in `output_videos` directory and text file 
with information about faces found in the video in `output_txts` directory