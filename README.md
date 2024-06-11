# Visualizing Activism: Analyzing Image Types on Reddit Engagement
![All Clusters](https://github.com/lariosmel13/poli17proj/blob/54e0c8a6e852dbf6e07c2a5ee7de77bdd5ff0aa8/clusters/clusters.png)
## Introduction
In the era of digital communication, social media platforms have become more than socialization hubs, evolving into powerful domains for political activism. Images play a significant role in capturing attention and stimulating user enagement. Understanding how different types of images influence user interaction can provide valuable insights for researchers, content creators and platform developers. This project aims to delve into image based engagement on Reddit through image clustering and regression analysis. I hope to shed light on visual factors that drive engagement.

## Methods
Image Clustering
* [ResNet50 model](https://pytorch.org/vision/main/models/generated/torchvision.models.resnet50.html)

Linear Regression
* [Gradient Boosting](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingRegressor.html)

## Hypothesis
1. After observing different college subreddits, some possible category clusters will be: memes, active protests, images featuring cops, school communications, screenshots from other social media.
2. For the linear regression, it is hypothesized that images featuring cops will reflect the most positive enagement. This hypothesis stems from the national media coverage and public discourse triggered by the intervention of law enforcement at encampents.

The Mobilizing Power of Visual Media Across Stages of Social-Mediated Protests by Yingdan Lu and Yilang Peng found that crowd-based photos predicted the most engagement when observing the Black Lives Matter, Stop Asian Hate and Women's March protests on Twitter. It is likely that the same will be found when studying Reddit posts, however it will be interesting to see what other types of images produce the most engagement.

## Collecting Data
### Packages
* import praw
* import pandas as pd
* from PIL import Image
* import requests
### [Reddit API Documentation](https://www.reddit.com/dev/api/)
* keywords = ['palestine','protest','israel','encampent']
* subreddits = ['ucla', 'UCSD', 'UCSB', 'UCSC', 'UCI', 'UCDavis', 'ucmerced', 'ucr', 'berkeley','columbia','Harvard','yale','princeton','georgetown','nyu','UIUC','aggies','ucf','Purdue','ASU','rit','uofm','rutgers','VirginiaTech','csuf','CSULB','CSULA','humboldtstate','Drexel','EmersonCollege','Emory','IndianaUniversity','mit','riceuniversity','stanford','PennStateUniversity','Berklee','bostoncollege','BostonU','Bowdoin','BrownU','Caltech','calarts','CalPoly','chapmanuniversity','Cornell','gwu','gatech','LSU','LMU','washu','VirginiaTech','Vanderbilt','UoP','udub','USC','usfca','UPenn','seattleu','scrippscollege','scad','SJSU','Pepperdine','pace','OregonStateUniv','jhu','harveymudd','Fordham','CUNY','claremontcolleges','Grinnell','Gonzaga','cmu','CalPolyPomona','CSUS','AmericanU','amherstcollege','baylor']
* Formed df with Subreddit, Image URL, Upvotes, Date
* Retrieved images from links manually and added them to Google Drive, then uploaded them to Colab

## Image Cluster Preprocessing
### Packages
* import numpy as np
* import os
* import cv2
* from keras.applications import ResNet50
* from keras.applications.resnet50 import preprocess_input
* from sklearn.cluster import KMeans
* from sklearn.decomposition import PCA
* import matplotlib.pyplot as plt
### Preprocessing
* Images:
  * resize:(224,224)
  * convert from BGR to RGB
  *  used preprocess_input to preprocess images according to ResNet50 model
  *  extracted features using model
  *  normalized features

## Linear Regression Preprocessing
* manually added image cluster category to each post in df
* made new df with only image cluster category and Upvotes
* applied min-max normalization since there were different amounts of each category
* one-hot-encoding

## Experiments
### Image Clusters
* Tried k=3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20
* Ended up choosing k=4, clusters made the most sense at k=4
* Hard to determine theme from other clusters
### Found Most Upvotes
* Used Normalized data set:
 * Added upvotes by image type
 * Used .idxmax to find which one had the most upvotes
  * Misc: 5.668547
  * Protest: 11.971039
  * School: 3.825000
  * Screenshots: 4.557554
### Linear Regression
* Tried: Random Forest, Linear Regression, Ridge Regression
* Ended up using Gradient Boosting Regression, because it performed the best.
## Evalution
### Linear Regression
* Coefficients:
 * Intercept: 0.23190770384441436
 * ID_Misc : 0.03411019786445862
 * ID_Protest : 0.029837666143125045
 * ID_School : 0.021450598118525465
 * ID_Screenshots : 0.014661104828747051
 * Intercept: Presents baseline predicted number of Reddit Upvotes. If a Reddit post contained none of the types of images, the model predicts a baseline number of upvotes of approximately 0.232
 * ID_Misc: Model expects an increase in number of upvotes by approximately 0.034 units for Miscellaneous Posts
 * ID_Protest: An Active Protest image expects and increase in predicted number of upvotes by 0.030 units.
 * ID_School: School Communications images expect an increase in predicted number of upvotes by 0.021 units.
 * ID_Screenshots: Screenshots type imafe predicts an increase in number of upvotes by 0.015 units.

Main image categories found in posts were Miscellaneous (memes, maps, protest posters), Active Protests, School Communications and Screenshots. In this particular study the most succesful images were Active Protest images, however a regression analysis was done to predict potential enagement. The intercept provides the expected number of upvotes for a post without any specific type of images, while the coefficients quantify the additional impact of including specific type of images on the predicted number of upvotes. 
  


## Discussion

### Challenges and Limitations
* The Reddit API only allowed accesss to recent post data
* Only one protest was observed
* The dataset is small
### Future Work
* Retry project with access to more posts/older posts
* Observe more protests

