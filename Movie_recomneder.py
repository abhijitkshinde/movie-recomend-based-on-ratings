import pandas as pd

df_user_rating = pd.read_csv('user.data',sep="\t",header=None)
df_user_rating.columns = ['user_id','item_id','rating','timestamp']


df_movie_name = pd.read_csv('Movie_Id_Titles')


df_movie_name = df_movie_name.rename(columns={'title':'movie_title'})


df = pd.merge(df_user_rating,df_movie_name,on='item_id')


rating_and_no_of_rating = pd.DataFrame(df.groupby('movie_title')['rating'].mean().sort_values(ascending=False))

rating_and_no_of_rating['no_of_ratings'] = df.groupby('movie_title')['rating'].count()

rating_and_no_of_rating = rating_and_no_of_rating.sort_values('no_of_ratings')


pt = df.pivot_table(index='user_id',columns='movie_title',values='rating')

test_movie = input('Enter movie name : ')
movie_vector = pt[test_movie].dropna()
similar_movies = pt.corrwith(movie_vector)

corr_df = pd.DataFrame(similar_movies,columns=['Correlation'])
corr_df = corr_df.join(rating_and_no_of_rating['no_of_ratings']).dropna()
corr_df = corr_df[corr_df['no_of_ratings']>100].sort_values('Correlation',ascending=False)
print(corr_df.head(10))




