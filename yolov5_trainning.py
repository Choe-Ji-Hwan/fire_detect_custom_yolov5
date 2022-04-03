# -*- coding: utf-8 -*-
"""yolov5_trainning.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1U0aXpEDjOql5H8m5oXGSMiJ6znMEqcTf

# **사전 설치**
"""

from google.colab import drive
drive.mount('/content/drive')

!git clone https://github.com/ultralytics/yolov5

# Commented out IPython magic to ensure Python compatibility.
# %cd yolov5
# %pip install -qr requirements.txt

"""# **데이터셋 가져오기**


"""

!curl -L "https://app.roboflow.com/ds/GAUG758dC1?key=nuDFxqHLzM" > roboflow.zip;

!unzip roboflow.zip; rm roboflow.zip

"""# **이미지 한번에 긁어모으기 위한 glob 모듈 사용**"""

from glob import glob
tra_img_list = glob('/content/drive/MyDrive/Colab_Notebooks/dataset/train/images/*.jpg') # train 이미지 경로
val_img_list = glob('/content/drive/MyDrive/Colab_Notebooks/dataset/test/images/*.jpg') # 테스트 이미지 경로
for img in tra_img_list:
  print(img)


with open('/content/drive/MyDrive/Colab_Notebooks/dataset/train.txt', 'w') as f:
  f.write('\n'.join(tra_img_list) + '\n')

with open('/content/drive/MyDrive/Colab_Notebooks/dataset/test.txt', 'w') as f:
  f.write('\n'.join(val_img_list) + '\n')

"""# **튜토리얼 학습**"""

!python train.py --img 416 --batch 16 --epochs 50 --data /content/yolov5/data/data.yaml --weights yolov5s.pt --name result_fire --cfg ./models/yolov5s.yaml

"""# **그림을 위한 설치**"""

!pip install wandb

"""결과는 yolov5/runs/train/exp/results.csv에 결과 저장
이미지는 yolov5/runs/train/exp/results.png에 결과 저장
"""

from utils.plots import plot_results
plot_results('runs/train/exp/results.png')  # plot 'results.csv' as 'results.png'

"""# **학습 결과를 다운로드하고 싶다면, 내용 모두 압축하여 저장**"""

!zip -r train_result.zip runs/train/exp

"""# **검증하기는 생략, 바로 적용해보기**
테스트 결과는 ```/runs/detect/exp``` 경로에 저장
"""

!python detect.py --source 'https://www.youtube.com/watch?v=mI9oyFMUlfg'  # YouTube

!zip -r test_result.zip runs/detect/exp

!git add .
!git commit -m "tutorial"
!git push origin master

