import numpy as np
import cv2
from collections import deque

def canva():
    def setValues(x):
       print("")

    cv2.namedWindow("Color detectors")
    cv2.createTrackbar("Upper Hue", "Color detectors", 142, 180,setValues)
    cv2.createTrackbar("Upper Saturation", "Color detectors", 255, 255,setValues)
    cv2.createTrackbar("Upper Value", "Color detectors", 255, 255,setValues)
    cv2.createTrackbar("Lower Hue", "Color detectors", 53, 180,setValues)
    cv2.createTrackbar("Lower Saturation", "Color detectors", 109, 255,setValues)
    cv2.createTrackbar("Lower Value", "Color detectors", 85, 255,setValues)

    bpoints = [deque(maxlen=1024)]
    gpoints = [deque(maxlen=1024)]

    blue_index = 0
    green_index = 0

    kernel = np.ones((5,5),np.uint8)

    colors = [(0, 255, 255), (255, 255, 255)]
    colorIndex = 0

    paintWindow = np.zeros((600,700,3)) + 255
    paintWindow = cv2.rectangle(paintWindow, (525,100), (620,164), (0,0,0), 2)
    paintWindow = cv2.rectangle(paintWindow, (525,220), (620,284), colors[0], -1)
    paintWindow = cv2.rectangle(paintWindow, (525,350), (620,414), colors[1], -1)

    cv2.putText(paintWindow, "CLEAR", (535, 130), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2, cv2.LINE_AA)
    cv2.putText(paintWindow, "YELLOW", (535, 260), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2, cv2.LINE_AA)
    cv2.putText(paintWindow, "WHITE", (535, 390), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2, cv2.LINE_AA)

    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        frame = cv2.flip(frame, 1)
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)


        u_hue = cv2.getTrackbarPos("Upper Hue", "Color detectors")
        u_saturation = cv2.getTrackbarPos("Upper Saturation", "Color detectors")
        u_value = cv2.getTrackbarPos("Upper Value", "Color detectors")
        l_hue = cv2.getTrackbarPos("Lower Hue", "Color detectors")
        l_saturation = cv2.getTrackbarPos("Lower Saturation", "Color detectors")
        l_value = cv2.getTrackbarPos("Lower Value", "Color detectors")
        Upper_hsv = np.array([u_hue,u_saturation,u_value])
        Lower_hsv = np.array([l_hue,l_saturation,l_value])

        frame = cv2.rectangle(frame, (525,100), (620,164), (122,122,122), -1)
        frame = cv2.rectangle(frame, (525,220), (620,284), colors[0], -1)
        frame = cv2.rectangle(frame, (525,350), (620,414), colors[1], -1)
        cv2.putText(frame, "CLEAR", (535, 130), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2, cv2.LINE_AA)
        cv2.putText(frame, "YELLOW", (535, 260), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2, cv2.LINE_AA)
        cv2.putText(frame, "WHITE", (535, 390), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2, cv2.LINE_AA)

        Mask = cv2.inRange(hsv, Lower_hsv, Upper_hsv)
        Mask = cv2.erode(Mask, kernel, iterations=1)
        Mask = cv2.morphologyEx(Mask, cv2.MORPH_OPEN, kernel)
        Mask = cv2.dilate(Mask, kernel, iterations=1)

        cnts,_ = cv2.findContours(Mask.copy(), cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE)
        center = None

        if len(cnts) > 0:
            cnt = sorted(cnts, key = cv2.contourArea, reverse = True)[0]
            ((x, y), radius) = cv2.minEnclosingCircle(cnt)
            cv2.circle(frame, (int(x), int(y)), int(radius), (0, 0, 255), 2)
            M = cv2.moments(cnt)
            center = (int(M['m10'] / M['m00']), int(M['m01'] / M['m00']))

            if 525 <= center[0] <= 620:
                if 100 <= center[1] <= 164:
                    bpoints = [deque(maxlen=512)]
                    gpoints = [deque(maxlen=512)]

                    blue_index = 0
                    green_index = 0

                    paintWindow[67:,:,:] = 255
                elif 220 <= center[1] <= 284:
                        colorIndex = 0
                elif 220 <= center[1] <= 414:
                        colorIndex = 1
            else :
                if colorIndex == 0:
                    bpoints[blue_index].appendleft(center)
                elif colorIndex == 1:
                    gpoints[green_index].appendleft(center)
        else:
            bpoints.append(deque(maxlen=512))
            blue_index += 1
            gpoints.append(deque(maxlen=512))
            green_index += 1

        points = [bpoints, gpoints]
        for i in range(len(points)):
            for j in range(len(points[i])):
                for k in range(1, len(points[i][j])):
                    if points[i][j][k - 1] is None or points[i][j][k] is None:
                        continue
                    cv2.line(frame, points[i][j][k - 1], points[i][j][k], colors[i], 2)
                    cv2.line(paintWindow, points[i][j][k - 1], points[i][j][k], colors[i], 2)

        cv2.imshow("Tracking", frame)
        cv2.imshow("mask",Mask)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()