import cv2

show = cv2.imread("img/lenna.png",1)
img = cv2.rectangle(show,(0,0),(255,255),(255,0,0),-1)
cv2.imshow("image",img)
k = cv2.waitKey(0)
if k == ord('q'):
    cv2.destroyAllWindows()
# elif k == ord('s'):
#     cv2.imwrite("img/lena_copy.jpeg",show)
#     cv2.destroyAllWindows()