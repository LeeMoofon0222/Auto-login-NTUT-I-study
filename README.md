# Auto-login-NTUT-i-study
<h2>Purpose</h2>
The purpose of this project is to expedite access to the NTUT iStudy platform and save more time. <br><br>
Processing and recognizing verification codes are the focal points of this project because making the program identify the verification code poses a challenge. After all, verification codes are designed to distinguish between robots and humans. Therefore, this has become the biggest challenge of this project.
<h2>Process</h2>
First, a web crawler is used to access the webpage, which is the entrance portal of NCTU. It automatically fills in your account and password and takes a screenshot of the verification code on the website and saves it. Then, the image is processed to remove noise, recognized, and finally outputs the text of the verification code. <br><br>
When the verification code is entered incorrectly, the program will automatically repeat the process of entering the account, password, and verification code recognition until it is correct.
<h2>Execution Video</h2>
https://youtu.be/THIRfXeIIFs
<h2>Packages</h2>
selenium.webdriver<br>
helium<br>
pytesseract<br>
cv2<br>
numpy<br>
<h2>Intro</h2>
<img src="https://github.com/LeeMoofon0222/Auto-login-NTUT-i-study/blob/main/ReadMe_Picture/Pic1.png?raw=true">
<img src="https://github.com/LeeMoofon0222/Auto-login-NTUT-i-study/blob/main/ReadMe_Picture/Pic2.png?raw=true">
<img src="https://github.com/LeeMoofon0222/Auto-login-NTUT-i-study/blob/main/ReadMe_Picture/Pic3.png?raw=true">
<img src="https://github.com/LeeMoofon0222/Auto-login-NTUT-i-study/blob/main/ReadMe_Picture/Pic4.png?raw=true">
<img src="https://github.com/LeeMoofon0222/Auto-login-NTUT-i-study/blob/main/ReadMe_Picture/Pic5.png?raw=true">
<img src="https://github.com/LeeMoofon0222/Auto-login-NTUT-i-study/blob/main/ReadMe_Picture/Pic6.png?raw=true">
<img src="https://github.com/LeeMoofon0222/Auto-login-NTUT-i-study/blob/main/ReadMe_Picture/Pic7.png?raw=true">
<img src="https://github.com/LeeMoofon0222/Auto-login-NTUT-i-study/blob/main/ReadMe_Picture/Pic8.png?raw=true">
<img src="https://github.com/LeeMoofon0222/Auto-login-NTUT-i-study/blob/main/ReadMe_Picture/Pic9.png?raw=true">
