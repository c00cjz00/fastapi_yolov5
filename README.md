### 安裝
```
sudo apt-get update
sudo apt-get install libgl1-mesa-dev
sudo apt-get install gcc g++
conda create -n yolov5 pip
conda activate 
git clone https://github.com/c00cjz00/fastapi_yolov5
cd fastapi_yolov5
pip install -r requirements.txt

pip install fastapi
pip install uvicorn[standard]
pip install aiofiles python-multipart
pip install opencv-python
pip install tqdm
pip install Jinja2
```
### 執行
```
python form_yolov5.py
```
或
```
uvicorn form_yolov5:app  --host 0.0.0.0 --port 9876
```
### 瀏覽
```
http://$IP:9876
```

Editor: Allen Chuang
<<<<<<< HEAD

=======
>>>>>>> 323a21115e6c0290d0853324eaf1c9825e2f394e
