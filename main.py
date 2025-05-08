import cv2
import time
import glob
from emailing import send_email
video = cv2.VideoCapture(0)
time.sleep(1) # sleep will avoid black frames , 1 is seconds to wait until 1 seocnd.
first_frame = None
status_list = []
count = 1
while True:
    status = 0 # when loop starts status is 0 when loop run , when there is image it is set to 1 in the bottom of the code

    check, frame = video.read()

    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2GRAY) # converting all image sto gray scale
    gray_frame_gau = cv2.GaussianBlur(gray_frame, (21,21), 0) # blurring the image for a better process using Gaussianblur, 21, 21 is amount of blurness, 0 is standardd deviation



    if first_frame is None:
        first_frame = gray_frame_gau # if first frame is none we will go thr video and give gausiian frame as the first frame.
        continue  # skip detection on the very first frame

    delta_frame = cv2.absdiff(first_frame, gray_frame_gau)
    cv2.imshow("my video", delta_frame)

    thresh_frame = cv2.threshold(delta_frame, 60, 255, cv2.THRESH_BINARY)[1] # 30 is threshold value 30,for second item of the list we will use [1]
    dil_frame = cv2.dilate(thresh_frame, None, iterations=2)
    cv2.imshow("my video", dil_frame)  #threshold is used to get white color for object and rest frame to be black

    contours, check = cv2.findContours(dil_frame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) # it will detect the contours , the white parts in the frame
    for contour in contours:
        area = cv2.contourArea(contour)
        if area < 25000 or area > 280000:
            continue
        x,y,w,h = cv2.boundingRect(contour)
        rectangle = cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3) # last 3 numbers are colour of the rectange , creating the rectangle in the frame
        if rectangle.any():
            status = 1
            cv2.imwrite(f"images/{count}.png", frame)  # storing the frames in the images folder
            count = count + 1
            all_images = glob.glob("images/*.png")
            index = int(len(all_images) / 2)
            image_with_object = all_images[index]


    status_list.append(status)
    status_list = status_list[-2:]
    if len(status_list) >= 2 and status_list[-2] == 1 and status_list[-1] == 0:
        send_email(image_with_object)

    print(status_list)



    cv2.imshow("Video", frame)


    key = cv2.waitKey(1)
    if key == ord("q"):    # when you press q it will stop the webcam
        break

video.release()