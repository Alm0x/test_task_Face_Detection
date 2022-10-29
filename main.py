import cv2
import sys
from os import path, mkdir


def face_capture(filename):
    # Creating a directories
    if not path.exists('output_videos'):
        mkdir('output_videos')
    if not path.exists('output_txts'):
        mkdir('output_txts')

    # Getting simple file name
    index = path.basename(filename).index('.')
    simple_filename = path.basename(filename)[:index]

    # Initializing the cascade
    cascade_path = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
    face_cascade = cv2.CascadeClassifier(cascade_path)

    # Initializing the video input
    video_path = filename
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print('Sorry, can\'t open your video')
    else:
        # Getting sizes
        frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fps = int(cap.get(cv2.CAP_PROP_FPS))

        # Initializing the video writer
        video_cod = cv2.VideoWriter_fourcc(*'mp4v')
        output_path = 'output_videos/' + simple_filename + '.mp4'
        video_output = cv2.VideoWriter(
            output_path,
            video_cod,
            fps,
            (frame_width, frame_height)
        )

        # Initializing the txt output
        output_txt_path = 'output_txts/' + simple_filename + '.txt'
        txt_output = open(output_txt_path, 'w')

        counter = 0
        seconds_counter = 0
        minutes_counter = 0
        # Video processing
        while cap.isOpened():
            ret, frame = cap.read()
            if ret:
                # Finding faces
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                faces = face_cascade.detectMultiScale(
                    gray,
                    scaleFactor=1.35,
                    minNeighbors=10,
                )
                # Making boxes
                for (x, y, w, h) in faces:
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

                # Writing to txt_output
                counter += 1
                if counter == fps and len(faces) > 0:
                    seconds_counter += 1
                    counter = 0
                    if seconds_counter == 60:
                        minutes_counter += 1
                        seconds_counter = 0
                    txt_output.write\
                        (
                            'At ' +
                            str(minutes_counter) + ' minutes and ' +
                            str(seconds_counter) + ' seconds coords are:\n'
                        )
                    for (x, y, w, h) in faces:
                        txt_output.write\
                            (
                                'Top-Left: (' +
                                str(x) + ', ' + str(y) +
                                ') and Bottom-Right:(' +
                                str(x + w) + ', ' + str(y + h) +
                                ')\n'
                            )

                # Write the frame in output file
                video_output.write(frame)
            else:
                break
        txt_output.close()
        cap.release()
        video_output.release()
        print('The video was successfully created')


def main():
    n = len(sys.argv)
    if n == 1:
        print('Please select a video file')
    elif n == 2:
        face_capture(sys.argv[1])
    else:
        print('Wrong number of arguments')


if __name__ == '__main__':
    main()
