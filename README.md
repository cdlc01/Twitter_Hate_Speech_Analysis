# Twitter Hate Speech Analysis in 2021

## Author: Christopher de la Cruz

## Overview

## Business Problem

According to both the FBI (Federeal Bureau of Investigations) and the Geneva International Center for Justice, both hate crimes and hate speech have been on a significant rise over the past few years. Hate speech is particularly difficult to police and control because unlike most hate crimes, it happens on the internet and can be masked in anonmity much easier. For the purpose of clear communication on this project, we will define hate speech by the definition of the United Nations (UN) which defines it as "any kind of communication in speech, writing or behaviour, that attacks or uses pejorative or discriminatory language with reference to a person or a group on the basis of who they are, in other words, based on their religion, ethnicity, nationality, race, colour, descent, gender or other identity factor." Therefore, telling someone "Fuck you" is offensive but it is not hate speech unless they were told that due to an identification factor. This project seeks to classify specific terms that can highlight hate speech and identify trends and patterns happening in today's world.

## Data

My data of labeled hate tweets and not hate tweets were built from five different datasets of labeled tweets:

- Twitter Hate Speech dataset on Kaggle (https://www.kaggle.com/vkrahul/twitter-hate-speech)
- Twitter Hate Speech and Offensive Language dataset on Kaggle (https://www.kaggle.com/mrmorj/hate-speech-and-offensive-language-dataset?select=labeled_data.csv)
- Hate Speech dataset on Kaggle (https://www.kaggle.com/pandeyakshive97/hate-speech-dataset)
- Hate Speech (English) dataset on Kaggle (https://www.kaggle.com/ibtesama/hatespeech?select=english.tsv)
- COVID Hate Tweet dataset from Georgia Tech & CLAWS (http://claws.cc.gatech.edu/covid#dataset-download)

## Methods

In the search for the optimal classification dataset, I tested about INSERT NUMBER HERE different models including Multinomial Bayes, Logistic Regression, Decision Tree, Random Forest, ADA Boosting, Gradient Boosting, XGBoost, and a Deep Learning Neural Network. For pre-processing, I tested two different regex statements (one pulled only words from the tweets and the other pulled words, hashtags and mentions) and different class balances with SMOTE. For vectorization, I tested both TF-IDF (Term Frequency - Inverse Document Frequency) and Count Vectorizer. Pipelines and Grid Searches were used in order to find optimal models. 

## Result 1

Looking at a word frequency chart, we can see the the most targeted identity classes (not the most used words) in our tweet collection are (not in this order):

- Race: Asian
- Race: Black
- Race: White
- Gender: Women
- Sexual Orientation: Gay

## Visual 1

![Hate_Tweets_Word_Freq](https://user-images.githubusercontent.com/77891283/121957777-de803300-cd30-11eb-9618-3ecf67ce5891.png)

## Result 2

The violin plots suggest that hate tweets are longer on average then not hate tweets but we need to be 100% sure. A two sample T-Test with a chosen alpha level of 0.05 returned a p-values of less then 0.05 therefore the two groups are statistally significantly different. Furthermore, the histogram data on the two groups approximate the hate tweets to be about 24 characters longer on average then not hate tweets

## Visual 2

![Hate_speech_violinplots](https://user-images.githubusercontent.com/77891283/121961059-eb9f2100-cd34-11eb-8e3d-2e6de654c190.png)
![Hate_speech_Histograms](https://user-images.githubusercontent.com/77891283/121961070-ef32a800-cd34-11eb-97d2-4c62d565ca10.png)

## Result 3

## Visual 3

## Conclusions

For More Information
Please review my full analysis in my Jupyter Notebook or my presentation: INSERT Jupyter Notebook AND PDF Presentation

For any additional questions, please contact Christopher de la Cruz at cdelacruz2013@gmail.com

Repository Structure  
```js
├── README.md                                         <- The top-level README for reviewers of this project                                                         
├── Nan.pdf                                           <- PDF version of project presentation                                                                       
├── EDA.ipynb                                         <- Narrative documentation of analysis in Jupyter notebook      
├── Modeling                                          <- Folder of individual model notebooks                                                                       
  ├── data                                            <- Both sourced externally and generated from code                                                        
  ├── ADA Boosting Classifier.ipynb                   <- Narrative documentation of ADA Boosting analysis Classifier in Jupyter notebook                               ├── Decision Tree Classifier.ipynb                  <- Narrative documentation of Decision Tree Classifier analysis in Jupyter notebook                             ├── First Simple Model.ipynb                        <- Narrative documentation of Dummy Classifier analysis in Jupyter notebook                                     ├── Gradient Boosting Classifier.ipynb              <- Narrative documentation of Gradient Boosting Classifier analysis in Jupyter notebook                         ├── Logistic_Regression_Classifier.ipynb            <- Narrative documentation of Logistic Regression Classifier analysis in Jupyter notebook                       ├── Multinomial_Bayes.ipynb                         <- Narrative documentation of Multinomial Bayes Classifier analysis in Jupyter notebook
  ├── Random Forest Classifier.ipynb                  <- Narrative documentation of Random Forest Classifier analysis in Jupyter notebook                             ├── Support Vector Classifier.ipynb                 <- Narrative documentation of Support Vector Classifier analysis in Jupyter notebook
  └── XGBoost Classifier.ipynb                        <- Narrative documentation of XGBoost Classifier analysis in Jupyter notebook                                 
└── images                                            <- Both sourced externally and generated from code  
```
