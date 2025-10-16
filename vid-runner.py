import cv2
import os

with open("code.py", "r") as f:
        exec(f.read())

# Create a VideoCapture object and read from input file
capo = cv2.VideoCapture('cam.avi')

# Check if camera opened successfully
if (capo.isOpened()== False):
    print("Error opening video file")

# Read until video is completed
while(capo.isOpened()):
    
# Capture frame-by-frame
    ret, frame = capo.read()
    if ret == True:
    # Display the resulting frame
        cv2.imshow('Frame', frame)
        
    # Press Q on keyboard to exit
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

# Break the loop
    else:
        break

# When everything done, release
# the video capture object
capo.release()

# Closes all the frames
cv2.destroyAllWindows()

