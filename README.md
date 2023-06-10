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
We use image augmentation by applying various transformations to the original images, to creates additional training samples with different variations. Image augmentation is useful to expanding the training data with diverse variations and to reduce overfitting.
- [Cow Preprocessing](https://github.com/Ternaku-id/ternaku-bangkit-machine-learning/blob/main/cow_preprocessing.ipynb)
- [Goat Preprocessing](https://github.com/Ternaku-id/ternaku-bangkit-machine-learning/blob/main/goat_preprocessing.ipynb)
## 5. Create models and training data
For model architecture, resize the image into 180x180 and we use transfer learning using MobilenetV2.
The Architecture of MobileNetV2:
- [Cow Model](https://github.com/Ternaku-id/ternaku-bangkit-machine-learning/blob/main/cow_model.ipynb)
- [Goat Model](https://github.com/Ternaku-id/ternaku-bangkit-machine-learning/blob/main/goat_model.ipynb)
![MobileNetV2](https://www.thepythoncode.com/media/articles/use-transfer-learning-for-image-flower-classification-keras-python/mobilenet-mo_hGSqcA7.png)
## 6. Evaluate the model
Cow distribution dataset
- ![cow distribution dataset](https://github.com/Ternaku-id/ternaku-bangkit-machine-learning/blob/main/graph/cow_distribution_dataset.png)
Cow model accuracy and loss
- ![cow accuracy and loss](https://github.com/Ternaku-id/ternaku-bangkit-machine-learning/blob/main/graph/cow_accuracy_and_loss.png)
Goat model accuracy and loss
- ![goat distribution dataset](https://github.com/Ternaku-id/ternaku-bangkit-machine-learning/blob/main/graph/goat_distribution_dataset.png)
Goat model accuracy and loss
- ![goat accuracy and loss](https://github.com/Ternaku-id/ternaku-bangkit-machine-learning/blob/main/graph/goat_accuracy_and_loss.png)
<!-- ## 7. Test the model
We then test our model and here is the result:
[Testing](https://github.com/Ternaku-id/ternaku-bangkit-machine-learning/blob/main/testing.ipynb) -->
<!-- nomor 7 jangan dibuka karena itu bukan pake model di apl wkwk -->
