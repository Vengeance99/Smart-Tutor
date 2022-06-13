import cv2
import numpy as np

def puzzle():
    cap = cv2.VideoCapture(0)

    font = cv2.FONT_HERSHEY_COMPLEX
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

    x1 = 750
    x2 = 930
    y1 = 100
    y2 = 300

    Result_Count1 = 0
    Result_Count2 = 0
    Result_Count3 = 0
    Result_Count4 = 0

    Pattern_Matrix = np.zeros((9, 9), np.uint8)

    Pattern_1 = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 255, 0, 0, 0, 0, 0, 255, 0],
                          [0, 255, 0, 0, 0, 0, 0, 255, 0],
                          [0, 255, 255, 0, 0, 0, 255, 255, 0],
                          [0, 255, 255, 0, 0, 0, 255, 255, 0],
                          [0, 255, 255, 255, 0, 255, 255, 255, 0],
                          [0, 255, 255, 255, 0, 255, 255, 255, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0],
                          ], dtype=np.uint8)

    Pattern_2 = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 255, 255, 255, 255, 255, 255, 255, 0],
                          [0, 255, 255, 255, 255, 255, 255, 255, 0],
                          [0, 255, 255, 255, 255, 255, 255, 255, 0],
                          [0, 255, 255, 255, 255, 255, 255, 255, 0],
                          [0, 255, 255, 255, 0, 255, 255, 255, 0],
                          [0, 255, 255, 255, 0, 255, 255, 255, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0],
                          ], dtype=np.uint8)

    Pattern_3 = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 255, 255, 255, 0, 255, 255, 255, 0],
                          [0, 255, 255, 255, 0, 255, 255, 255, 0],
                          [0, 255, 255, 0, 0, 0, 255, 255, 0],
                          [0, 255, 255, 0, 0, 0, 255, 255, 0],
                          [0, 255, 0, 0, 0, 0, 0, 255, 0],
                          [0, 255, 0, 0, 0, 0, 0, 255, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0],

                          [0, 0, 0, 0, 0, 0, 0, 0, 0],
                          ], dtype=np.uint8)

    Pattern_4 = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 255, 0, 0, 0, 0, 0, 255, 0],
                          [0, 255, 0, 0, 0, 0, 0, 255, 0],
                          [0, 255, 255, 255, 0, 255, 255, 255, 0],
                          [0, 255, 255, 255, 0, 255, 255, 255, 0],
                          [0, 0, 0, 255, 255, 255, 0, 0, 0],
                          [0, 0, 0, 255, 255, 255, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0],
                          ], dtype=np.uint8)

    while 1:
        ret, frame = cap.read()
        frame = cv2.flip(frame, +1)

        if not ret:
            break
        if cv2.waitKey(1) == ord('s'):
            break

        frame2 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        #cv2.imshow('Gray Image', frame2)

        ret, thresh1 = cv2.threshold(frame2, 150, 255, cv2.THRESH_BINARY)
        #cv2.imshow('Binary Image', thresh1)

        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 3)

        width = int((x2 - x1) / 9)
        height = int((y2 - y1) / 9)
        W1 = x1
        H1 = y1
        W2 = x1 + width
        H2 = y1 + height

        for i in range(0, 9):
            for j in range(0, 9):
                Sum = np.sum(thresh1[H1: H2, W1:W2])
                if Sum > 56100:
                    Pattern_Matrix[i, j] = 255
                else:
                    Pattern_Matrix[i, j] = 0
                W1 = W2
                W2 = W2 + width

                Sum = 0
            W1 = x1
            W2 = x1 + width
            H1 = H2
            H2 = H2 + height

        for a in range(0, 9):
            for b in range(0, 9):
                if Pattern_Matrix[a, b] == Pattern_1[a, b]:
                    Result_Count1 = Result_Count1 + 1
                if Pattern_Matrix[a, b] == Pattern_2[a, b]:
                    Result_Count2 = Result_Count2 + 1
                if Pattern_Matrix[a, b] == Pattern_3[a, b]:
                    Result_Count3 = Result_Count3 + 1
                if Pattern_Matrix[a, b] == Pattern_4[a, b]:
                    Result_Count4 = Result_Count4 + 1


        Match_Percentage1 = (Result_Count1 / 81) * 100
        Match_Percentage2 = (Result_Count2 / 81) * 100
        Match_Percentage3 = (Result_Count3 / 81) * 100
        Match_Percentage4 = (Result_Count4 / 81) * 100

        Result_Count1 = 0
        Result_Count2 = 0
        Result_Count3 = 0
        Result_Count4 = 0

        if Match_Percentage1 > 90:
            S = "Pattern 1  " + str(round(Match_Percentage1, 1)) + '% Match'
            cv2.putText(frame, S, (5, 50), font, 2, (0, 255, 0), 2, cv2.LINE_AA)
        elif Match_Percentage2 > 90:
            S = "Pattern 2  " + str(round(Match_Percentage2, 1)) + '% Match'
            cv2.putText(frame, S, (5, 50), font, 2, (0, 255, 0), 2, cv2.LINE_AA)
        elif Match_Percentage3 > 90:
            S = "Pattern 3  " + str(round(Match_Percentage3, 1)) + '% Match'
            cv2.putText(frame, S, (5, 50), font, 2, (0, 255, 0), 2, cv2.LINE_AA)
        elif Match_Percentage4 > 90:
            S = "Pattern 4  " + str(round(Match_Percentage4, 1)) + '% Match'
            cv2.putText(frame, S, (5, 50), font, 2, (0, 255, 0), 2, cv2.LINE_AA)
        else:
            cv2.putText(frame, "No Match Found", (5, 50), font, 2, (0, 0, 255), 2, cv2.LINE_AA)

        cv2.imshow('Original Image', frame)
        #cv2.imshow('Pattern Template', thresh1[y1:y2, x1:x2])