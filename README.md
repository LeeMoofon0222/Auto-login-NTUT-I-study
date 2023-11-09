# Auto-login-NTUT-i-study
<h2>目的</h2>
做這個專題的目的是為了更快速的進入北科i學員，節省更多時間。<br><br>
驗證碼處理與識別這是這個專題的重心，因為要讓程式識別出來驗證碼有難度。畢竟驗證碼本來就是在識別機器人與人類。因此，這也成了此專題最大的挑戰。
<h2>流程</h2>
首先先用網頁爬蟲進入網頁，就是北科大入口網站，自動填入你的帳號還有密碼，並截圖網站上的驗證碼把它存起來。然後將圖片進行去噪處理，識別、最後輸出驗證碼的文字。<br><br>
當驗證碼輸入錯的時候，程式就會自動重複輸入一次帳號、密碼還有驗證碼識別。直到對為止。<br><br>
打完驗證碼之後再使用helium套件自動按按鈕，最後進入北科i學員，實現自動登入的功能。
<h2>執行影片</h2>
https://youtu.be/THIRfXeIIFs
<h2>使用套件:</h2>
selenium.webdriver<br>
helium<br>
pytesseract<br>
cv2<br>
numpy<br>
<h2>介紹</h2>
<img src="https://github.com/LeeMoofon0222/Auto-login-NTUT-i-study/blob/main/ReadMe_Picture/Pic1.png?raw=true">
<img src="https://github.com/LeeMoofon0222/Auto-login-NTUT-i-study/blob/main/ReadMe_Picture/Pic2.png?raw=true">
<img src="https://github.com/LeeMoofon0222/Auto-login-NTUT-i-study/blob/main/ReadMe_Picture/Pic3.png?raw=true">
<img src="https://github.com/LeeMoofon0222/Auto-login-NTUT-i-study/blob/main/ReadMe_Picture/Pic4.png?raw=true">
<img src="https://github.com/LeeMoofon0222/Auto-login-NTUT-i-study/blob/main/ReadMe_Picture/Pic5.png?raw=true">
<img src="https://github.com/LeeMoofon0222/Auto-login-NTUT-i-study/blob/main/ReadMe_Picture/Pic6.png?raw=true">
<img src="https://github.com/LeeMoofon0222/Auto-login-NTUT-i-study/blob/main/ReadMe_Picture/Pic7.png?raw=true">
<img src="https://github.com/LeeMoofon0222/Auto-login-NTUT-i-study/blob/main/ReadMe_Picture/Pic8.png?raw=true">
<img src="https://github.com/LeeMoofon0222/Auto-login-NTUT-i-study/blob/main/ReadMe_Picture/Pic9.png?raw=true">
