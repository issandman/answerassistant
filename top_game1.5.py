import win32gui, win32ui, win32con, win32api
from PIL import Image
import pytesseract
import webbrowser
import requests
import re

def window_capture(filename):		#screen capturn
   hwnd = 0
   hwndDC = win32gui.GetWindowDC(hwnd)
   mfcDC = win32ui.CreateDCFromHandle(hwndDC)
   saveDC = mfcDC.CreateCompatibleDC()
   saveBitMap = win32ui.CreateBitmap()
   saveBitMap1 = win32ui.CreateBitmap()
   MoniterDev = win32api.EnumDisplayMonitors(None,None)
   #w = MoniterDev[0][2][2]
   #h = MoniterDev[0][2][3]
   w = 430
   h = 130
   w1 = 300
   h1 = 260
   saveBitMap.CreateCompatibleBitmap(mfcDC,w,h)
   saveBitMap1.CreateCompatibleBitmap(mfcDC,w1,h1)
   saveDC.SelectObject(saveBitMap)
   saveDC.BitBlt((0,0),(w,h),mfcDC,(45,215),win32con.SRCCOPY)
   saveBitMap.SaveBitmapFile(saveDC,filename)
   
   saveDC.SelectObject(saveBitMap1)
   saveDC.BitBlt((0,0),(w1,h1),mfcDC,(78,372),win32con.SRCCOPY)
   saveBitMap1.SaveBitmapFile(saveDC,'haha1.jpg')
   
def highlight(text11, text12, text13, html0_str):		#matching highlight
	sym = '《'
	sym1 = '》'
	for i in range(len(text11)):
		if (text11[i] == sym) or (text11[i] == sym1):
			continue
		html0_str = re.sub(text11[i], '<span id="result" style="background:blue;color:red;">' + text11[i] + '</span>', html0_str, 0)
	for i in range(len(text12)):
		if (text12[i] == sym) or (text12[i] == sym1):
			continue
		html0_str = re.sub(text12[i], '<span id="result" style="background:red;color:black;">' + text12[i] + '</span>', html0_str, 0)
	for i in range(len(text13)):
		if (text13[i] == sym) or (text13[i] == sym1):
			continue
		html0_str = re.sub(text13[i], '<span id="result" style="background:green;color:yellow;">' + text13[i] + '</span>', html0_str, 0)
   

window_capture('haha.jpg')
text = pytesseract.image_to_string(Image.open('haha.jpg'),lang='chi_sim').split()
text1 = pytesseract.image_to_string(Image.open('haha1.jpg'),lang='chi_sim').split('\n\n')		#options
print(text)
print(text1)

del(text[0])		#exception: deleter order number
list =''.join(text)
url = 'http://www.baidu.com/s?wd=%s' % list
try:
	text11 = text1[0].split()
	text12 = text1[1].split()
	text13 = text1[2].split()
except:
	webbrowser.open(url)


html0 = requests.get(url)
html0.encoding='utf-8'
html0_str = str(html0.text)
highlight(text11, text12, text13, html0_str)


fh=open('C:/Users/han/Desktop/test.html','w',encoding='utf-8')
fh.write(html0_str)
fh.close()
url = 'file:///C:/Users/han/Desktop/test.html'
webbrowser.open(url)


# driver = webdriver.Chrome(r'C:\Python34\chromedriver.exe')
# driver.get("http://www.baidu.com")