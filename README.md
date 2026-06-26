# MLE-Project-Text-Classification
[https://user-images.githubusercontent.com/74038190/216122041-518ac897-8d92-4c6b-9b3f-ca01dcaf38ee.png]
😊 Hey Everybody!! 

In this project we'll...
- Build 2 text classification pipelines using the Amazon Product Reviews dataset and scikit-learn. 
- Develop an API (using the Flask and Requests libraries) that other Python developers can use to access our pipelines.

## Topics Covered
- Dataset preparation
- Building text classification pipelines using Scikit-learn
- Hyperparameter tuning
- Deploying the pipelines via Flask
- Developing our own API so other developers can use our pipelines using Python 

## Major Frameworks used
- Pandas
- Scikit-learn
- Flask

## Project Structure
**notebooks**\
The notebooks for cleaning the Amazon Product Reviews dataset and builiding the text classification pipelines.
- *data_prep.ipynb* (Data preparation)
- *mlp_pipeline.ipynb* (Train & Hyperparameter-tune the ```MLPClassifier``` pipeline)
- *nbayes_pipeline.ipynb* (Train & Hyperparameter-tune the ```MultinomialNB``` pipeline)

  - **pipelines**\
    The saved text classificaion pipelines. You can download them and use them in your own projects if you'd like. Just make sure you have the same version of scikit-learn ("scikit-learn>=1.9.0").
    - *mlp_pipeline.joblib*
    - *nbayes_pipeline.joblib*

  - **data**\
    The Amazon Product Reviews dataset from Kaggle and our cleaned version are stored in this folder. I left the original Kaggle *readme.txt* as well.
    - *readme.txt*
    - *train.csv*
    - *test.csv*
    - *full_cleaned_dataset.csv*

**flask_api**\
The flask server and python API. The pipelines are in this folder to eliminate filepath issues. 
- *mlp_pipeline.joblib*
- *nbayes_pipeline.joblib*
- *server.py*
- *text_classifier_api.py*

## Citations
Link to dataset: [https://www.kaggle.com/datasets/kritanjalijain/amazon-reviews]
