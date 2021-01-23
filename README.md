### 安裝
```
sudo apt-get update
sudo apt-get install libgl1-mesa-dev
sudo apt-get install gcc g++
conda create -n detectron2 pip
conda activate 
pip install torch==1.7.1+cpu torchvision==0.8.2+cpu torchaudio===0.7.2 -f https://download.pytorch.org/whl/torch_stable.html

pip install fastapi
pip install uvicorn[standard]
pip install aiofiles python-multipart
pip install opencv-python
pip install tqdm
pip install Jinja2
git clone https://github.com/facebookresearch/detectron2.git
python -m pip install -e detectron2
```
### 執行
```
python form.py
```
或
```
uvicorn form:app  --host 0.0.0.0 --port 9999
```
### 瀏覽
```
http://$IP:9999
```

Editor: Allen Chuang
<<<<<<< HEAD

=======
>>>>>>> 323a21115e6c0290d0853324eaf1c9825e2f394e
