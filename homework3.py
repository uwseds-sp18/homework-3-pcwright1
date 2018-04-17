import pandas as pd
import sqlite3
import numpy as np
import os.path


# Function 1
def create_dataframe(url):

    if os.path.isfile(url):
    	conn = sqlite3.connect(url)
    	df = pd.read_sql_query(
    	    """select video_id, category_id, 'us' as language from USvideos \
    	    union \
    	    select video_id, category_id, 'GB' as language from GBvideos \
    	    union \
    	    select video_id, category_id, 'FR' as language from FRvideos \
    	    union \
    	    select video_id, category_id, 'DE' as language from DEvideos \
    	    union \
    	    select video_id, category_id, 'CA' as language from CAvideos;""", conn)
    	print ('Succeeded:', str(url))
    	return df
    else:
    	raise ValueError(str("Invalid URL: " + str(url)))
    	#raise ValueError("Invalid URL: ")


# Helpful functions for question 2
def test_length(df):
    return len(df)>=10
def test_column_names(df):
    return set(df.columns) == {'video_id', 'category_id', 'language'}
def test_index(df):
    return len(df) == len(df.loc[:,['video_id','language']].drop_duplicates())

# Function 2:
def test_create_dataframe(df):
    return test_length(df) & test_column_names(df) & test_index(df)

if __name__ == "__main__":
  create_dataframe('class.db')
  create_dataframe('fake_url.db')