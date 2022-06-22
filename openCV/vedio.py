import cv2
from cv2 import COLOR_BGR2GRAY

cap = cv2.VideoCapture(0)

while(True):
    rel,frame = cap.read()
    gray = cv2.cvtColor(frame,COLOR_BGR2GRAY) 
    cv2.show("videos",gray)
    k = cv2.waitKey(0)
    if k == ord('q'):
        break
cv2.release()
cv2.destroyAllWindows()