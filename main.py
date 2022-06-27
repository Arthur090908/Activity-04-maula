import cv2
filePath = 'simon.jpg'
imgFlag = int(1)
img = cv2.imread(filePath,imgFlag)
cv2.imshow("Baby simon",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
