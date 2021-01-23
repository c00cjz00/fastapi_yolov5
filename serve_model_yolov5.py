import time
import subprocess

from io import BytesIO
import numpy as np
from PIL import Image

# 執行指令
def cmd(command):
    subp = subprocess.Popen(command,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,encoding="utf-8")
    subp.wait(30)
    if subp.poll() == 0:
        print(subp.communicate()[0])
    else:
        print("失败")

# 函式: 讀取讀片
# 範例 file=@cat02.png;type=image/png
def read_imagefile(file) -> Image.Image:
    # 內存讀取二進制數據, 轉為圖片
    image = Image.open(BytesIO(file))
    return image

# 函式: 預測圖片
def predict(mycmd):  
    result = cmd(mycmd)
    return result 

'''
# 直接執行
prediction = predict(filename)
print(prediction)
'''
