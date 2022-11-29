# Auto-login-NTUT-i-study
首先先用selenium網頁爬蟲進入網頁，就是北科大入口網站，然後使用helium自動填入你的帳號還有密碼，並且截圖網站上的驗證碼並把它存起來。然後將圖片進行去噪處理，識別、輸出驗證碼的文字。但是當驗證碼輸入錯的時候，那程式就會自動重複輸入一次帳號、密碼還有驗證碼識別。直到對為止。打完驗證碼之後利用helium自動按按鈕，最後進入北科i學員，實現自動登入的功能。
使用套件:
selenium.webdriver
helium
pytesseract
cv2
numpy
