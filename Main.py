from selenium.webdriver import FirefoxOptions
import helium
import pytesseract
import cv2
import numpy as np

# 帳號與密碼
account="Your account"
password="Your password"
# 網址 
schoolweb = "https://nportal.ntut.edu.tw/index.do?thetime=1633838254210"

# 設定火狐瀏覽器
options = FirefoxOptions()
#設定視窗大小
options.add_argument("--width=1600")
options.add_argument("--height=800")
driver = helium.start_firefox(schoolweb, options=options)

# 等到出現「請輸入驗證碼」出現時，再跑以下程式
helium.wait_until(helium.Text("請輸入驗證碼").exists)

# 找到所有可以填入文字的區塊
textfields = helium.find_all(helium.TextField())

# 驗證碼處理

# 截圖驗證碼
driver.save_screenshot("temp.png")
img = cv2.imread("temp.png")
x=1080
y=290
w=168
h=50
captcha=img[y:y+h, x:x+w]


#驗證碼識別

def yanjon(captcha):
    #cv2.medianBlur(captcha,3)
    captcha = cv2.GaussianBlur(captcha, (5, 5), 0)
    #低值低值濾波
    #cv2.blur(captcha, (9, 9))
    # 轉成灰階
    graycaptcha = cv2.cvtColor(captcha, cv2.COLOR_BGR2GRAY)
    # 二值化
    ret,whitecaptcha=cv2.threshold(graycaptcha, 145, 255, cv2.THRESH_BINARY_INV)
    #kernel = np.ones((3,3), np.uint8)
    #侵蝕與膨脹
    #erode = cv2.erode(whitecaptcha, kernel, iterations=1)
    #whitecaptcha = cv2.dilate(erode, kernel, iterations=1)
    # 轉成白底黑字
    height, width = whitecaptcha.shape
    blackcaptcha = whitecaptcha.copy()
    for i in range(height):
      for j in range(width):
        blackcaptcha[i, j] = (255 - whitecaptcha[i, j])
    img1 = np.array(blackcaptcha)
    return img1
  
pytesseract.pytesseract.tesseract_cmd =r'C:/Program Files/Tesseract-OCR/tesseract.exe'#for debug
#轉換字元
final_captcha=(pytesseract.image_to_string(yanjon(captcha)))
final_captcha = final_captcha.replace(' ', '')
final_captcha = final_captcha.replace('/', 'I')
final_captcha = final_captcha.replace('.', '')
final_captcha = final_captcha.replace(',', '')
final_captcha = final_captcha.replace('|', 'I')
final_captcha = final_captcha.replace('@', 'G')
final_captcha = final_captcha.replace(')', 'j')
final_captcha = final_captcha.replace(';', 'I')
final_captcha = final_captcha.replace('\\', 'I')
final_captcha = final_captcha.replace('*', 'P')
final_captcha = final_captcha.replace('1', 'I')
final_captcha = final_captcha.replace('2', 'Z')
final_captcha = final_captcha.replace('6', 'G')
final_captcha = final_captcha.replace('7', 'T')
final_captcha = final_captcha.replace('-', '')
final_captcha = final_captcha.replace('&', '')
final_captcha = final_captcha.replace('!', 'I')
final_captcha = final_captcha.replace('￥', 'Y')
final_captcha = final_captcha.replace('0', 'O')
final_captcha = final_captcha.replace('\'', '')
final_captcha = final_captcha.replace('?', 'S')
final_captcha = final_captcha.replace('〝', '')
final_captcha = final_captcha.replace('〞', '')
final_captcha = final_captcha.replace('}', 'J')
final_captcha = final_captcha.replace('‘', '')
final_captcha = final_captcha.replace('￡', 'E')
final_captcha = final_captcha.replace('€', 'E')
final_captcha = final_captcha.replace('￠', 'C')
final_captcha = final_captcha.replace('t', 'L')
final_captcha = final_captcha.replace(':', '')
final_captcha = final_captcha.replace('"', '')
final_captcha = final_captcha.replace('}', 'J')
final_captcha = final_captcha.replace('_', '')
final_captcha = final_captcha.replace('e', 'C')
final_captcha = final_captcha.replace(']', 'J')
final_captcha = final_captcha.replace('%', 'X')
final_captcha = final_captcha.replace('i', 'I')


#當偵測不到時，直接降驗證碼設成ABCD
if final_captcha=='':
   final_captcha=('ABCD')
#填入號、密碼與驗證碼
helium.write(account, into=textfields[0])
helium.write(password, into=textfields[1])
helium.write(final_captcha, into=textfields[2])
#按下登入鍵
python_button = driver.find_elements_by_xpath("/html/body/form/div/div[3]/div/div[5]/input")[0]
python_button.click() 

#定義[登入]函式
def enter():
    helium.wait_until(helium.Text("請輸入驗證碼").exists)
    textfields = helium.find_all(helium.TextField())
    driver.save_screenshot("temp.png")
    img = cv2.imread("temp.png")
    x=1080
    y=290
    w=168
    h=50
    captcha=img[y:y+h, x:x+w]
    final_captcha=(pytesseract.image_to_string(yanjon(captcha)))
    final_captcha = final_captcha.replace(' ', '')
    final_captcha = final_captcha.replace('/', 'I')
    final_captcha = final_captcha.replace('.', '')
    final_captcha = final_captcha.replace(',', '')
    final_captcha = final_captcha.replace('|', 'I')
    final_captcha = final_captcha.replace('@', 'G')
    final_captcha = final_captcha.replace(')', 'j')
    final_captcha = final_captcha.replace(';', 'I')
    final_captcha = final_captcha.replace('\\', 'I')
    final_captcha = final_captcha.replace('*', 'P')
    final_captcha = final_captcha.replace('1', 'I')
    final_captcha = final_captcha.replace('2', 'Z')
    final_captcha = final_captcha.replace('6', 'G')
    final_captcha = final_captcha.replace('8', 'B')
    final_captcha = final_captcha.replace('7', 'T')
    final_captcha = final_captcha.replace('-', '')
    final_captcha = final_captcha.replace('&', '')
    final_captcha = final_captcha.replace('!', 'I')
    final_captcha = final_captcha.replace('￥', 'Y')
    final_captcha = final_captcha.replace('0', 'O')
    final_captcha = final_captcha.replace('\'', '')
    final_captcha = final_captcha.replace(':', '')
    final_captcha = final_captcha.replace('t', 'L')
    final_captcha = final_captcha.replace('"', '')
    final_captcha = final_captcha.replace('}', 'J')
    final_captcha = final_captcha.replace('‘', 'J')
    final_captcha = final_captcha.replace('’', 'J')
    final_captcha = final_captcha.replace('_', '')
    final_captcha = final_captcha.replace('?', 'S')
    final_captcha = final_captcha.replace('〝', '')
    final_captcha = final_captcha.replace('￡', 'E')
    final_captcha = final_captcha.replace('€', 'E')
    final_captcha = final_captcha.replace('￠', 'C')
    final_captcha = final_captcha.replace('e', 'C')
    final_captcha = final_captcha.replace('%', 'X')
    final_captcha = final_captcha.replace(']', 'J')
    final_captcha = final_captcha.replace('a', 'O')
    if final_captcha=='':
        final_captcha=('ABCD')
    helium.write(account, into=textfields[2])
    helium.write(password, into=textfields[1])
    helium.write(final_captcha, into=textfields[0])
    python_button = driver.find_elements_by_xpath("/html/body/form/div/div[3]/div/div[5]/input")[0]#登入按鈕
    python_button.click() 

while True:
    #當驗證碼打對時，按按鈕至北科i學員
    if helium.Text("教務系統").exists():  
        helium.wait_until(helium.Text("教務系統").exists)
        python_button = driver.find_elements_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div[2]/div/div/div[2]/ul/li[2]/a")[0]#教務系統按鈕
        python_button.click()
        python_button = driver.find_elements_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div[2]/div/div/div[2]/ul/li[2]/div/ul/li[4]/span/a")[0]#北科i學員按鈕
        python_button.click()
        break
    #當驗證碼打錯時，重新執行登入動作
    if helium.Text("登入失敗！").exists():
        python_button = driver.find_elements_by_xpath("/html/body/center/h3[2]/input")[0]#重新登入按鈕
        python_button.click()
        enter()

               
input()
helium.kill_browser()     
  


 


