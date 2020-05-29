import numpy as np
import cv2
import sys
import time
video_path = '/Users/admin/Downloads/2018-10-25/VID_20181016_143349.mp4'
cv2.ocl.setUseOpenCL(False)
version = cv2.__version__.split('.')[0]
print (version)
ax1 = 20
ay = 0
ay2 = 800
bx1 = 827
by = 0
by2 = 800
i = 1 
start_time = time.time()
cap = cv2.VideoCapture(video_path)
fgbg = cv2.createBackgroundSubtractorMOG2()
while (cap.isOpened):
    ret,frame = cap.read()	
    if ret==True:
        fgmask = fgbg.apply(frame)
        cv2.line(frame,(ax1,ay),(ax1,ay2),(255,0,0),2)
        print("1")
        cv2.line(frame,(bx1,by),(bx1,by2),(255,0,0),2)
        print("2")
        contours,hierarchy = cv2.findContours(fgmask.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        print("3")
        for c in contours:
            print("inside the first for")
            if cv2.contourArea(c) < 1000:
                continue
                print("inside if 1")
            (x, y, w, h) = cv2.boundingRect(c)
            print ("X:",x)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0),2)
            cv2.circle (frame,(int((x+x+w)/2),int ((y+y+h)/2)),1,(0,255,0),-1)
            print("before the first or")
            while(ax1== int((x+x+w)/2)):
                print("inside the while")
                start_time = time.time()
                break
                
            while int (bx1)>= int ((x+x+w)/2):
                print ("inside the second loop")
                print ("X:",x)
                print ("bX1",bx1)
                if int(ax1)<= int((x+x+w)/2)&int(ax1+10) >= int((x+x+w)/2):
                    cv2.line(frame,(bx1,by),(bx1,by2),(0,255,0),2)
                    Speed = Speed_Cal(time.time() - start_time)
                    print("Car Number "+str(i)+" Speed: "+str(Speed))
                    i = i + 1
                    cv2.putText(img, "Speed: "+str(Speed)+"KM/H", (x,y-15), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0),3)
                    break
                    
            else :
                cv2.putText(frame, "Calcuting", (100,200), cv2.FONT_HERSHEY_SIMPLEX, 1,(0,255,0),3)
                break                
        #cv2.imshow('video', frame)
        cv2.imshow('foreground and background',fgmask)
        cv2.imshow('rgb',frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
cap.release()
cv2.destroyAllWindows()

def Speed_Cal(time):
    try:
        Speed = (9.144*3600)/(time*1000)
        return Speed
    except ZeroDivisionError:
        print (5)