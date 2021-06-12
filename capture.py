import cv2

count = 0
# Opens the Video file from same folder
cap= cv2.VideoCapture('traffic video.MP4')
i=0
while(cap.isOpened() and i<5):
    ret, frame = cap.read()
    if ret == False:
        break
    cv2.imwrite('image'+str(i)+'.jpg',frame)
    count += 30 # 30 fps means one second
    cap.set(1, count)
    i+=1
    

cap.release()
cv2.destroyAllWindows()
