import pandas as pd
import ast

movies = pd.DataFrame(pd.read_csv("movies_metadata.csv"))

"""
Handling dates. 
- Mixed formatting in the release date column, eliminating rows with dates that contain a '-' so that it can
be converted to datetime easier. All dates in this format are before 1900 anyway.
- for relevancy purposes and also to cut down the dataset, any movies prior to 2000 will also be removed.
"""

movies = movies[~movies['release_date'].str.contains('-')]
movies['release_date'] = pd.to_datetime(movies['release_date'], format='%m/%d/%Y', errors="coerce")
movies = movies[movies['release_date'] > pd.to_datetime('2000-01-01')]

#removing rows w/ null values (except for belongs_to_collection)
movies = movies.dropna(subset=['release_date', 'title', 'vote_average'])

#getting just the name of the series from the belongs_to_collection column (prev a dictionary containing additional info)
inSeries = movies.dropna(subset=['belongs_to_collection'])
inSeries['belongs_to_collection'] = inSeries['belongs_to_collection'].apply(ast.literal_eval)
inSeries['belongs_to_collection'] = inSeries['belongs_to_collection'].str['name']

noSeries = movies[movies['belongs_to_collection'].isna()]

#getting equal parts inSeries and noSeries
movies_clean = pd.concat([inSeries.sample(100, random_state=1), noSeries.sample(100, random_state=1)])
movies_clean.columns = ['series', 'release_date', 'title', 'rating']
#clean
movies_clean['series'] = movies_clean['series'].str.replace("'", "", regex=False)
movies_clean['series'] = movies_clean['series'].str.replace('"', "", regex=False)
movies_clean['title'] = movies_clean['title'].str.replace("'", "", regex=False)
#put into files
movies_clean.to_csv("moves_data.csv", index = False)
movies_clean.to_json("movies_data.json", orient='records', date_format="iso")