# QR-code-based-Attendance-System-Mobile-Application-using-Kivy-and-OpenCV-in-Python

A complete attendance system package containing a QR code generator app and a QR code scanner, that can be used in any educational or commercial institution to track and maintain a student/employee attendance record. 

## TABLE OF CONTENTS

- [1. LIBRARIES USED](#1-libraries-used)
  * [1.1 FOR QR CODE GENERATOR - MOBILE APPLICATION](#11-for-qr-code-generator---mobile-application)
  * [1.2 FOR QR CODE SCANNER](#12-for-qr-code-scanner)
- [2. INTERFACE OF THE MOBILE APPLICATION](#2-interface-of-the-mobile-application)
  * [2.1 SCREEN 1 - HOME](#21-screen-1---home)
  * [2.2 SCREEN 2- QR CODE GENERATION SCREEN](#22-screen-2--qr-code-generation-screen)
- [3. BUILD PROCEDURE](#3-build-procedure)
  * [3.1 QR CODE GENERATOR - MOBILE APPLICATION](#31-qr-code-generator---mobile-application)
  * [3.2 QR CODE SCANNER](#32-qr-code-scanner)


## 1. LIBRARIES USED

### 1.1 FOR QR CODE GENERATOR - MOBILE APPLICATION

1. Kivy

2. KivyMD

3. qrcode

4. plyer

5. pyjnius

6. android.permissions (This package will only work in android, so use it only while converting the python file to Apk)

### 1.2 FOR QR CODE SCANNER

1. OpenCV

2. pyzbar

3. Xlwt

4. datetime

## 2. INTERFACE OF THE MOBILE APPLICATION

### 2.1 SCREEN 1 - HOME
<img src="https://user-images.githubusercontent.com/58739134/180676388-01228cc5-9f92-4187-9c4a-66d0b44e1c14.jpg" width=300 >

### 2.2 SCREEN 2- QR CODE GENERATION SCREEN
<img src="https://user-images.githubusercontent.com/58739134/180679026-4e645cf3-16aa-421b-bfa9-6e97f2ef2ed9.jpg" width=300 >

## 3. BUILD PROCEDURE

### 3.1 QR CODE GENERATOR - MOBILE APPLICATION

1. The QR-Code Generator is developed using the Kivy Framework in Python.

2. [QR_code_generator_App.py](https://github.com/Dalersingh-rs/QR-code-based-Attendance-System-Mobile-Application-using-Kivy-and-OpenCV-in-Python/blob/main/QR_code_generator_App.py) is coded in a way that it can be executed on a desktop for testing and modification purposes.

3. Before converting it into an APK, uncomment few lines in [QR_code_generator_App.py](https://github.com/Dalersingh-rs/QR-code-based-Attendance-System-Mobile-Application-using-Kivy-and-OpenCV-in-Python/blob/main/QR_code_generator_App.py) as mentioned in comments. Here, we add Pyjnius and android.permissions module to access java classes and permissions in android respectively.

4. Google Collab is used to convert the python file into APK file format. It is used because Kivy requires Linux environment to function properly while converting to APK. Google Collab helps us in creating the Linux environment virtually.

5. In Google Collab, create new workbook and upload the [QR_code_generator_App.py](https://github.com/Dalersingh-rs/QR-code-based-Attendance-System-Mobile-Application-using-Kivy-and-OpenCV-in-Python/blob/main/QR_code_generator_App.py), [layout.kv](https://github.com/Dalersingh-rs/QR-code-based-Attendance-System-Mobile-Application-using-Kivy-and-OpenCV-in-Python/blob/main/layout.kv), [qr_code.png](https://github.com/Dalersingh-rs/QR-code-based-Attendance-System-Mobile-Application-using-Kivy-and-OpenCV-in-Python/blob/main/qr_code.png), [buildozer.spec](https://github.com/Dalersingh-rs/QR-code-based-Attendance-System-Mobile-Application-using-Kivy-and-OpenCV-in-Python/blob/main/buildozer.spec) files in current working directory.

6. Execute the commands given in the [Google_Collab_Commands.txt](https://github.com/Dalersingh-rs/QR-code-based-Attendance-System-Mobile-Application-using-Kivy-and-OpenCV-in-Python/blob/main/Google_Collab_Commands.txt) file to convert it to an APK file.

### 3.2 QR CODE SCANNER 

1. The QR Code Scanner uses OpenCV to access the camera and read the QR code.

2. Pyzbar is used to decode the QR code and provide information about the individual.

3. When the generated QR-Code is scanned, Xlwt package is used to write the inidivual's data to an excel file created under the name of current date/time using the datetime package.

#### THANK YOU :)
