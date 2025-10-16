import cv2


capo = cv2.VideoCapture('cam.mp4')

if (capo.isOpened()== False):
    print("Error opening video file")


while(capo.isOpened()):
    

    ret, frame = capo.read()
    if ret == True:
   
        cv2.imshow('Frame', frame)
        
  
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    else:
        break

capo.release()

cv2.destroyAllWindows()



