import cv2
import pyzbar.pyzbar as pyzbar
import time
from datetime import datetime
import xlwt

def enterdata(student_name):
    if student_name in names:
        pass
    else:
        names.append(student_name)  #appending the student name to the NAMES list
        fob.write(student_name + '\n')  # writing the student name to the file FOB which will store the
                                        # names of students who are present

def writeexcel(names, reg_format_date):

    wb = xlwt.Workbook()
    sheet1 = wb.add_sheet('Sheet 1')
    style = xlwt.easyxf('font: bold 1')

    sheet1.write(0,0,"Index",style)
    sheet1.write(0,1,"Student Name",style)
    sheet1.write(0,2,"Present/Absent",style)

    for i,name in enumerate(names,start=1):
        sheet1.write(i, 0, i)
        sheet1.write(i, 1,name)
        sheet1.write(i, 2,"Present")

    wb.save('Attendance List ' + reg_format_date + '.xls')

def checkdata(data):
    try:
        student_name=data.decode("utf-8")  # to convert the byte string to normal string
        if student_name in names:
            print(f'{student_name} is already present')
            # to display text in the window, we use the below line
            cv2.putText(frame, f'{student_name} is already present', (50, 50), font, 2, (255, 0, 0), 3)

        else:
            print(f"Student{len(names)+1}: {student_name} - Present")
            enterdata(student_name) # function call to add student name in the list NAMES
            cv2.putText(frame, student_name, (50, 50), font, 2,(255, 0, 0), 3) # to display text in the window

    except TypeError:
        print('Invalid ID !!!')
        return


""" used to capture video // argument 0 means first camera, 1 means second camera,
we can also enter the location of a video file to capture its video"""
cap = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_PLAIN

current_date_time=datetime.now().strftime("%d-%m-%Y_%I.%M_%p")
fob = open(current_date_time + '.txt', 'w+')
names = []
print('Reading QR code.....')

while True:

    # it reads the video frame by frame, returns a tuple with 2 args,
    # 1st is Return value indicating if a frame was read correctly (True) or not (False).
    # 2nd is the frame which is readed
    _, frame = cap.read()

    # used to flip a 2D-Array.  parameters are source,flipcode
    # 0 means flipping around the x-axis and positive value (for example, 1) means flipping around y-axis.
    # Negative value (for example, -1) means flipping around both axes.
    frame = cv2.flip(frame, 1)

    decodedObjects = pyzbar.decode(frame) #decodes the QRcode and returns a list which contains tuples.
                                          #the data field in the returned list has a byte string of the decoded qrcode

    for obj in decodedObjects: #used to access the tuple which is present inside the list
        checkdata(obj.data)    #function call
        time.sleep(1)

    cv2.imshow("Frame", frame)

    #To stop the execution and close the camera and window
    if cv2.waitKey(1) == 13:
        cv2.destroyAllWindows()
        break

fob.close()  #closing the file
writeexcel(names, current_date_time)
