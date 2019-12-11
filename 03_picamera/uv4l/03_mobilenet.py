import time

import numpy as np
import cv2

import tensorflow as tf
import tensorflow_hub as hub

if __name__ == "__main__":

    tf.enable_eager_execution()

    # Load the mobilenet model
    module = hub.Module(
        'https://tfhub.dev/google/imagenet/mobilenet_v2_140_224/classification/3')
    height, width = hub.get_expected_image_size(module)

    # Test model on random input data
    input_shape = (1, height, width, 3)

    image = np.array(np.random.random_sample(input_shape), dtype=np.float32)
    logits = module(image)

    stream_url = 'http://raspberrypi.local:8080/stream/video.mjpeg'
    cap = cv2.VideoCapture()
    cap.open(stream_url)

    while True:
        ret, frame = cap.read()
        if ret:

            start_time = time.time()

            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            delay = time.time() - start_time

            cv2.putText(
                img=frame,
                text=f'{delay:.02}s',
                org=(5, 25),
                fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                fontScale=1,
                color=(0, 255, 0),
                lineType=cv2.LINE_AA,
            )

            frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
            cv2.imshow('frame', frame)

            k = cv2.waitKey(1) & 0xff

            if k == ord('q'):
                break

    cap.release()
    cv2.destroyAllWindows()
