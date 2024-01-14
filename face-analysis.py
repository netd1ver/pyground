from deepface import DeepFace
import cv2
import numpy as np

img = input("Enter the path of an image file: ")

face_analysis = DeepFace.analyze(img_path=img)
# print(face_analysis)

cv_img = cv2.imread(img, cv2.IMREAD_COLOR)

region = face_analysis[0]['region']
pt1 = region['x'], region['y']
pt2 = region['x'] + region['w'], region['y'] + region['h']
face = cv_img[pt1[1]:pt2[1], pt1[0]:pt2[0]]

cv_img = cv_img.astype('int32')
cv_img = np.clip(cv_img - 100, 0, 255)
cv_img = cv_img.astype('uint8')

cv_img[pt1[1]:pt2[1], pt1[0]:pt2[0]] = face

cv2.rectangle(cv_img, pt1=pt1, pt2=pt2, color=(241, 242, 64), thickness=1)

gender = face_analysis[0]['dominant_gender']
age = str(face_analysis[0]['age'])
race = face_analysis[0]['dominant_race']
emotion = face_analysis[0]['dominant_emotion']
race_per = str(round(face_analysis[0]['race'][race], 1))
emotion_per = str(round(face_analysis[0]['emotion'][emotion], 1))

cv2.putText(
    cv_img, 
    'Gender: ' + gender, (pt1[0]+10, pt2[1]+20), 
    cv2.FONT_HERSHEY_SIMPLEX, 
    0.4, 
    (241, 242, 64), 
    1, 
    cv2.LINE_AA)
cv2.putText(
    cv_img, 
    'Age: ' + age, (pt1[0]+10, pt2[1]+40), 
    cv2.FONT_HERSHEY_SIMPLEX, 
    0.4, (241, 242, 64), 1, cv2.LINE_AA)
cv2.putText(
    cv_img, 
    'Race: ' + race + ' ' + race_per + '%', 
    (pt1[0]+10, pt2[1]+60), 
    cv2.FONT_HERSHEY_SIMPLEX, 
    0.4, (241, 242, 64), 1, cv2.LINE_AA)
cv2.putText(
    cv_img, 
    'Emotion: ' + emotion + ' ' + emotion_per + '%', 
    (pt1[0]+10, pt2[1]+80), 
    cv2.FONT_HERSHEY_SIMPLEX, 
    0.4, 
    (241, 242, 64), 1, cv2.LINE_AA)

cv2.imshow("who r u", cv_img)
cv2.waitKey(0)
