#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests


# In[2]:


import pandas as pd


# In[7]:


import praw
import pandas as pd
from PIL import Image
from io import BytesIO
import requests

def get_image_posts(keywords, limit=None, max_posts=500000):
    
    reddit = praw.Reddit(
        client_id='Pgl8vZVzWgNonBLHHzSwzw',
        client_secret='UVZMYLXI56NoZgt41t0T4ufHk3RYHQ',
        user_agent='Poli179proj/1.0(https://github.com/lariosmel13/poli17proj.git)'
    )

    
    posts = []
    for submission in reddit.subreddit("all").search(query=' OR '.join(keywords), sort='relevance', syntax='cloudsearch', time_filter='all', limit=None):
        if len(posts) >= max_posts:
            break
        if not submission.is_self and any(keyword in submission.title.lower() for keyword in keywords):
            posts.append({
                'Subreddit': submission.subreddit.display_name,
                'Title': submission.title,
                'Image URL': submission.url,
                'Upvotes': submission.score,
                'Date': submission.created_utc
            })
    return posts

def create_dataframe(posts):
    df = pd.DataFrame(posts)
    return df

def display_images(posts):
    for post in posts:
        image_url = post['Image URL']
        response = requests.get(image_url)
        img = Image.open(BytesIO(response.content))
        img.show()

keywords = ['college protest','ucla protest','ucsd protest','encampment','systemic racism','protest','palestine','israeli-palestine','gaza','free palestine','israel','zionist','rafah','israel war','divest']  # Keywords to filter posts

posts = get_image_posts(keywords, limit=None, max_posts=500000)
df = create_dataframe(posts)

selected_columns=['Subreddit', 'Image URL','Upvotes','Date']
selected_df=df[selected_columns]
print(selected_df)  


# In[9]:


selected_df.to_csv('reddit_posts.csv',index=False)


# In[ ]:





# In[ ]:




