import cvlib
import cv2

file = input("Enter the path of an image file: ")
idx_dot = file.rfind('.')
new_file = file[:idx_dot] + '_mosaic' + file[idx_dot:]

print(new_file)

img = cv2.imread(file)

faces, confidence = cvlib.detect_face(img)

for face in faces:
    (startX, startY) = face[0], face[1]
    (endX, endY) = face[2], face[3]

    face_region = img[startY:endY, startX:endX]
    M, N, D = face_region.shape

    face_region = cv2.resize(
        face_region, None, fx=0.05, fy=0.05, interpolation=cv2.INTER_AREA)
    face_region = cv2.resize(
        face_region, (N, M), interpolation=cv2.INTER_AREA)
    img[startY:endY, startX:endX] = face_region

    # cv2.rectangle(img, (startX, startY), (endX, endY), (0, 255 ,0), 2)

cv2.imshow("Face Mosaic", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite(new_file, img)
