#creating database
import cv2, sys, numpy, os
haar_file = 'haarcascade_frontalface_default.xml'
datasets = 'datasets'  #All the faces data will be present this folder
import face_recognition
import shutil
import boto3
from sklearn.metrics import precision_score, recall_score, f1_score
    

def addUserFace(name):
    sub_data = name
    path = os.path.join(datasets, sub_data)
    if not os.path.isdir(path):
        os.mkdir(path)
    (width, height) = (130, 100)    # defining the size of image
    face_cascade = cv2.CascadeClassifier(haar_file)
    webcam = cv2.VideoCapture(0) #'0' is use for my webcam, if you've any other camera attached use '1' like this

    
    count = 1
    (_, im) = webcam.read()
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 4)
    cv2.imwrite('%s/%s.jpg' % (path,count), im)
    webcam.release()

def VerifyUser(name):
    global face_encoding,known
    sub_data = name 
    print(name)   
    path = os.path.join(datasets, sub_data)
    database = path+"/1.jpg"
    image=cv2.imread(database)
    image=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
    boxes=face_recognition.face_locations(image,model="hog")
    known = face_recognition.face_encodings(image,boxes)[0]
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = small_frame[:, :, ::-1]
    

    try:
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encoding = face_recognition.face_encodings(rgb_small_frame, face_locations)
        matches = face_recognition.compare_faces(known, face_encoding)
        
        if(matches[0]==True):
            print(matches[0])
            print("Face recognised")
            return 1
        else:
            print("Face Not Recognised")
            return("Face Not Recognised")
    except:
        return "Face Not Found"
    

def DeleteFaces():
    shutil.rmtree(datasets)
    os.mkdir("datasets")
