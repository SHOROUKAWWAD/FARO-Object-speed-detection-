import numpy as np
import cv2
import sys
import time 

def process_Video(video_path):

    cv2.ocl.setUseOpenCL(False)

    version = cv2.__version__.split('.')[0]
    print (version)

    #read video file
    cap = cv2.VideoCapture(video_path)
    out = cv2.VideoWriter('output.avi', -1, 20.0, (640,480))

    fgbg = cv2.createBackgroundSubtractorMOG2()


    while (cap.isOpened):

      #if ret is true than no error with cap.isOpened
        ret, frame = cap.read()
   
        if ret==True:

            #apply background substraction
            fgmask = fgbg.apply(frame)
					
		    #check opencv version
		 
            (contours, hierarchy) = cv2.findContours(fgmask.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
            x2 = 0
            y2 = 0
            speed_X = 0
            speed_Y = 0
            #looping for contours
            for c in contours:
                if cv2.contourArea(c) < 180000:
                    continue
                start_time = time.clock()	
                #get bounding box for the vehicle
                (x, y, w, h) = cv2.boundingRect(c)
                print ("X:",x)
                #for instant calculation of the velicity
                time_diff = time.clock()- start_time
                if (time_diff !=0):
                    speed_X = ((x-x2)*3600)/(time_diff*1000)
                    x2 = x
                    speed_Y = ((x-y2)*3600)/(time_diff*1000)
                    y2 = y
                #draw bounding box
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                if (speed_X<0 and x != 0 and speed_Y ==0):
                    cv2.putText(frame, "Speed:(east) "+str(abs(speed_X))+"KM/H", (x,y-15), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0),3)
                elif(speed_X>0 and x != 0 and speed_Y ==0):
                    cv2.putText(frame, "Speed:(west) "+str(abs(speed_X))+"KM/H", (x,y-15), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0),3)
                elif (speed_Y >0 and speed_X ==0):
                    cv2.putText(frame, "Speed:(north) "+str(abs(speed_Y))+"KM/H", (x,y-15), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0),3)
                elif (speed_Y>0 and speed_X==0):
                    cv2.putText(frame, "Speed:(south) "+str(abs(speed_Y))+"KM/H", (x,y-15), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0),3)
                else:
                    cv2.putText(frame, "Speed:(X) "+str((speed_X))+"KM/H"+ "Speed:(Y) "+str((speed_Y))+"KM/H", (x,y-15), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0),3)
            out.write(frame)
            cv2.imshow('foreground and background',fgmask)
            cv2.imshow('rgb',frame)
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
    out.release()
    cap.release()
    cv2.destroyAllWindows()
