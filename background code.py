from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import Message ,Text
import tkinter.ttk as ttk
import tkinter.font as font
import time


window = tk.Tk()
window.title("Blind,Deaf,Dum")


bg = PhotoImage(file = 'D:\\Swathi\\Working code\\object detection,text reading,color detection\\Object Detection\\bg.png')
label = ttk.Label(window, image = bg)
PhotoImage(file = 'D:\\Swathi\\Working code\\object detection,text reading,color detection\\Object Detection\\bg.png')

lbl = tk.Label(window, text="********* VIRTUAL EYE ********",width=27  ,height=2  ,fg="white"  ,bg="blue" ,font=('Arial', 20, ' bold ') ) 
lbl.place(x=400, y=100)



def object_detection():
    # import the necessary packages
    import numpy as np
    import argparse
    import imutils
    import time
    import cv2
    import os
    from twilio.rest import Client

    # Find these values at https://twilio.com/user/account
    account_sid = "ACab8cdf5516d4926859b6bc0779e1ac4c"
    auth_token = "383b20d729df7459f9197516c48f5a6e"

    client = Client(account_sid, auth_token)


    ap = argparse.ArgumentParser()

    ap.add_argument("-c", "--confidence", type=float, default=0.5,
            help="minimum probability to filter weak detections")
    ap.add_argument("-t", "--threshold", type=float, default=0.3,
            help="threshold when applyong non-maxima suppression")
    args = vars(ap.parse_args())

    # load the COCO class labels our YOLO model was trained on
    labelsPath = os.path.sep.join(["object-coco\coco.names"])
    LABELS = open(labelsPath).read().strip().split("\n")

    # initialize a list of colors to represent each possible class label
    np.random.seed(42)
    COLORS = np.random.randint(0, 255, size=(len(LABELS), 3),
            dtype="uint8")

    # derive the paths to the YOLO weights and model configuration
    #weightsPath = os.path.sep.join([args["yolo"], "yolov3.weights"])
    #configPath = os.path.sep.join([args["yolo"], "yolov3.cfg"])


    print("Loading ...................")
    net = cv2.dnn.readNetFromDarknet('object-coco\yolov3.cfg', 'object-coco\yolov3.weights')
    ln = net.getLayerNames()
    ln = [ln[i[0] - 1] for i in net.getUnconnectedOutLayers()]

    vs = cv2.VideoCapture(0)
    writer = None
    (W, H) = (None, None)

    try:
            prop = cv2.cv.CV_CAP_PROP_FRAME_COUNT if imutils.is_cv2() \
                    else cv2.CAP_PROP_FRAME_COUNT
            total = int(vs.get(prop))
            print("[INFO] {} total frames in video".format(total))

    # an error occurred while trying to determine the total
    # number of frames in the video file
    except:
            print("[INFO] could not determine # of frames in video")
            print("[INFO] no approx. completion time can be provided")
            total = -1




    while True:

            (grabbed, frame) = vs.read()

            # if the frame was not grabbed, then we have reached the end
            # of the stream
            if not grabbed:
                    break

            # if the frame dimensions are empty, grab them
            if W is None or H is None:
                    (H, W) = frame.shape[:2]

            # construct a blob from the input frame and then perform a forward
            # pass of the YOLO object detector, giving us our bounding boxes
            # and associated probabilities
            blob = cv2.dnn.blobFromImage(frame, 1 / 255.0, (416, 416),
                    swapRB=True, crop=False)
            net.setInput(blob)
            start = time.time()
            layerOutputs = net.forward(ln)
            end = time.time()

            # initialize our lists of detected bounding boxes, confidences,
            # and class IDs, respectively
            boxes = []
            confidences = []
            classIDs = []

            # loop over each of the layer outputs
            for output in layerOutputs:
                    # loop over each of the detections
                    for detection in output:
                            # extract the class ID and confidence (i.e., probability)
                            # of the current object detection
                            scores = detection[5:]
                            classID = np.argmax(scores)
                            confidence = scores[classID]

                            # filter out weak predictions by ensuring the detected
                            # probability is greater than the minimum probability
                            if confidence > args["confidence"]:
                                    # scale the bounding box coordinates back relative to
                                    # the size of the image, keeping in mind that YOLO
                                    # actually returns the center (x, y)-coordinates of
                                    # the bounding box followed by the boxes' width and
                                    # height
                                    box = detection[0:4] * np.array([W, H, W, H])
                                    (centerX, centerY, width, height) = box.astype("int")

                                    # use the center (x, y)-coordinates to derive the top
                                    # and and left corner of the bounding box
                                    x = int(centerX - (width / 2))
                                    y = int(centerY - (height / 2))

                                    # update our list of bounding box coordinates,
                                    # confidences, and class IDs
                                    boxes.append([x, y, int(width), int(height)])
                                    confidences.append(float(confidence))
                                    classIDs.append(classID)

            # apply non-maxima suppression to suppress weak, overlapping
            # bounding boxes
            idxs = cv2.dnn.NMSBoxes(boxes, confidences, args["confidence"],
                    args["threshold"])

            # ensure at least one detection exists
            if len(idxs) > 0:
                    # loop over the indexes we are keeping
                    for i in idxs.flatten():
                            # extract the bounding box coordinates
                            (x, y) = (boxes[i][0], boxes[i][1])
                            (w, h) = (boxes[i][2], boxes[i][3])

                            # draw a bounding box rectangle and label on the frame
                            color = [int(c) for c in COLORS[classIDs[i]]]
                            cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
                            text = "{}: {:.4f}".format(LABELS[classIDs[i]],
                                    confidences[i])
    ##                        print(text)
                            text1="{}".format(LABELS[classIDs[i]])
    ##                        print(text1)
                            if (text1 == 'cell phone'):
                                    print("cellphone")
                                    client.api.account.messages.create(
                                            to="+91-9739817305",
                                            from_="+1 15182899852" ,  #+1 210-762-4855"
                                            body=" cell phone Detected" )
                            
                            if (text1 == 'book'):
                                    print("book")
                                    client.api.account.messages.create(
                                            to="+91-9739817305",
                                            from_="+1 15182899852" ,  #+1 210-762-4855"
                                            body=" Book Detected" )


                            if (text1 == 'bottle'):
                                    print("bottle")
                                    client.api.account.messages.create(
                                            to="+91-9739817305",
                                            from_="+1 15182899852" ,  #+1 210-762-4855"
                                            body=" bottle Detected" )

                            if (text1 == 'person'):
                                    print("person")
                                    client.api.account.messages.create(
                                            to="+91-9739817305",
                                            from_="+1 15182899852" ,  #+1 210-762-4855"
                                            body=" Person Detected" )

                            if (text1 == 'dog'):
                                    print("dog")
                                    client.api.account.messages.create(
                                            to="+91-9739817305",
                                            from_="+1 15182899852" ,  #+1 210-762-4855"
                                            body=" Person Detected" )

                            
                            if (text1 == 'horse'):
                                    print("horse")
                                    client.api.account.messages.create(
                                            to="+91-9739817305",
                                            from_="+1 15182899852" ,  #+1 210-762-4855"
                                            body=" Person Detected" )
                                    
                                    
                            cv2.putText(frame, text, (x, y - 5),
                                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
                            

            cv2.imshow('name',frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                    Object.close()
                    break


    # release the file pointers
    print("[INFO] cleaning up...")
    #writer.release()
    vs.release()

def Text():
    #!/usr/bin/env python
    import numpy as np
    import sys
    ##import cv2
    import os
    from playsound import playsound

    from gtts import gTTS
    import os

    print ("Enter the Text :")
    #str=input()
    str=input()
    print (str)
    #while True:
        
    #mtext = 'welcome to india welcome to india welcome to india '
    lag = 'en'
    myobj = gTTS(text=str, lang=lag, slow =False)
    myobj.save("aa.mp3")
    playsound("aa.mp3")
    os.system("mpg321 hi.mp3")

def Speech():
    #!/usr/bin/env python
    import numpy as np
    import sys
    import cv2
    import os
    import pytesseract
    from gtts import gTTS
    from PIL import Image
    import time
    from playsound import playsound

    from PIL import Image
    cap = cv2.VideoCapture(0)
    sample=0;
    error=0
    print('Opening CAM')
    time.sleep(2)
    while(cap.isOpened()):
        #while(True):
        ret, img = cap.read()
        #print(ret)
        if ret:
            gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            cv2.imshow('frame',img)
            cv2.imwrite('frame.png',img)
            # cv2.waitKey(1)
            sample=sample+1
            if (sample == 50):
                sample =0
                error=1
                print('Camera break')
                    
                cap.release()
        if error ==0:
            print('Camera is interrupted\nPlease execute the script again')
    ##                cv2.destroyAllWindows()
        if error ==1:
            print('image is caputured')
            im = Image.open("frame.png")
            text = pytesseract.image_to_string(im,lang = 'eng')
            #temp = text.encode('utf-8')
            #type(text)
            ##############espeak#####################
            lag = 'en'
            myobj = gTTS(text=text,lang=lag, slow =False)
            myobj.save("test.mp3")
            playsound("test.mp3")
            os.system("mpg321 test.mp3")
            ###########################################
            print(text)
                        
    cap.release()
    cv2.destroyAllWindows()

    
trainImg = tk.Button(window, text="Object_Detection", command=object_detection  ,fg="Black"  ,bg="White"  ,width=15  ,height=2, activebackground = "blue" ,font=('times', 15, ' bold '))
trainImg.place(x=450, y=200)

trackImg = tk.Button(window, text="Text_Voice ", command=Text  ,fg="Black"  ,bg="White"  ,width=15  ,height=2, activebackground = "blue" ,font=('times', 15, ' bold '))
trackImg.place(x=650, y=200)

trackImg = tk.Button(window, text="Images_Voice", command=Speech  ,fg="Black"  ,bg="White"  ,width=15  ,height=2, activebackground = "blue" ,font=('times', 15, ' bold '))
trackImg.place(x=450, y=300)


quitWindow = tk.Button(window, text="Quit", command=window.destroy  ,fg="Black"  ,bg="White"  ,width=15  ,height=2, activebackground = "blue" ,font=('times', 15, ' bold '))
quitWindow.place(x=650, y=300)
##print(quitWindow)


label.pack()
window.mainloop()
