import pandas as pd
from pandas import DataFrame as df
import matplotlib.pyplot as plt
from collections import Counter
movies_df=pd.read_csv('movies.csv')
print(movies_df)
len(movies_df.index)
print(movies_df.shape)
print(movies_df.loc[0][0])
print(movies_df.loc[1][2])
print(movies_df.loc[2][2])
movies_df.set_index('movieId')
movies_df['generes_arr']=movies_df['genres'].str.split('|')
print(movies_df.head())
animation_df=movies_df[movies_df.generes_arr.map(lambda x:'Animation'in x)]
print(len(animation_df.index))
romance_df=movies_df[movies_df.generes_arr.map(lambda y:'Romance' in y)]
print(len(romance_df.index))
movies_lambda=lambda x:set(['Romance','Comedy']).issubset(x)
masala_movies=movies_df[movies_df.generes_arr.map(movies_lambda)]
print(len(masala_movies.index))
print(masala_movies)
counter_lambda=lambda x:len(x)
movies_df['genre_count']=movies_df.generes_arr.apply(counter_lambda)
print(movies_df.head())
plt.hist(movies_df.genre_count)
plt.title("Generes Histogram")
plt.xlabel("# of generes")
plt.ylabel("# of movies")
plt.axis([0,9,0,15000])
plt.show()
flattened_genres=[item for sublist in movies_df.generes_arr for item in sublist]
genre_dict=dict(Counter(flattened_genres))
print(genre_dict)
plt.pie(genre_dict.values(),labels=genre_dict.keys())
plt.show()
x=list(range(len(genre_dict)))
plt.xticks(x,genre_dict.keys(),rotation=80)
plt.bar(x,genre_dict.values())
plt.grid()
plt.plot()
plt.show()




