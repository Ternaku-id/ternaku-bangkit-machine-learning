# Ternaku-Bangkit-Machine-Learning
# This contains what Machine Learning's team do
the job of Machine learning Team is to learn and make machine learning model of pink eye and healthy eye of goat and cow. We make 2 model for this App, 1 is for cow that contain 2 class, pinkeye and healthy. and 1 is for goat that also contain 2 class, pinkeye and healthy.

## 1. Search information source related to the project
we have to read journal or other resource to gain more knowledge about the disease.
### Information Resource
We get information from various source such as:
- [Mengenal Penyakit Pink Eye (Mata Merah) Pada Ternak Kambing & Domba](https://disnakeswan.lebakkab.go.id/mengenal-penyakit-pink-eye-mata-merah-pada-ternak-kambing-domba/)
- [Pink Eye Cases in Goats at The Sawangan Farm](https://e-journal.unair.ac.id/JAVEST/article/download/25060/14106)
- [Penyakit Pinkeye Pada Sapi](https://bbibsingosari.ditjenpkh.pertanian.go.id/penyakit-pinkeye-pada-sapi/#:~:text=Pinkeye%20diakibatkan%20oleh%20bakteri%20Moraxella,bakteri%20ini%20mudah%20menyerang%20mata.)
- [PENGOBATAN DAN PENCEGAHAN PENYAKIT PINK EYE PADA TERNAK](http://cybex.pertanian.go.id/mobile/artikel/95335/PENGOBATAN-DAN-PENCEGAHAN-PENYAKIT-PINK-EYE-PADA-TERNAK/)

## 2. Search dataset for different type of eyes
We collect images of pink eye and healthy eye from cow eye and goat eye
### Dataset Resource
We get dataset from various source such as:
- [Penyakit Mata Sapi Computer Vision Project](https://universe.roboflow.com/fachri/penyakit-mata-sapi)
- [Google Images](https://images.google.com/)

## 3. Preparation Data
after collecting the datasets, we do preparation data by cleaning the images we found not suitable for our model.
#### Link to dataset
- [DATASET ML](https://drive.google.com/drive/folders/1_FB1UIOc-UrCFNujgb_W0W27A0NcOlNz?usp=sharing)
## 4. Preprocessing Data
We use image augmentation to expanding the training data with diverse variations and to reduce overfitting. And we resize the image into 640x640 because the image we found is not in a same size.
## 5. Create models and training data
For model architecture, we use transfer learning using MobilenetV2.
The Architecture:
[MobileNetV2](https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.thepythoncode.com%2Farticle%2Fuse-transfer-learning-for-image-flower-classification-keras-python&psig=AOvVaw3rpH8r-GM5fMSPW53yzHif&ust=1686382280469000&source=images&cd=vfe&ved=0CBEQjRxqFwoTCMDihdjVtf8CFQAAAAAdAAAAABAE)
## 6. evaluate the model that has been obtained and re-create the model
