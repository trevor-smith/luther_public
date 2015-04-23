import pandas as pd
import numpy as np
import pickle
import itertools
from pandas.tools.plotting import scatter_matrix
import matplotlib.pyplot as plt
%pylab inline

from __future__ import print_function
import statsmodels.api as sm
import matplotlib.pyplot as plt
from statsmodels.sandbox.regression.predstd import wls_prediction_std

data_all = pd.read_csv('df_foreign_clean.csv')

data_egypt = data_all.reindex(columns=['Egypt','title', 'dtg', 'country', 'key', 'gdp', 'production budget', 'year', 'genre', 'rating_r', 'rating_g', 'rating_pg13', 'rating_pg', 'rating_unrated', 'favorability', 'genre_Foreign', 'genre_Drama', 'genre_Comedy', 'genre_Horror', 'genre_Animation', 'genre_Thriller', 'genre_Romantic Comedy', 'genre_Action', 'genre_Action / Adventure', 'genre_Documentary', 'genre_Comedy / Drama', 'genre_Romance', 'genre_Action Comedy', 'genre_Drama / Thriller', 'genre_Period Drama', 'genre_Sci-Fi Action', 'genre_Family Comedy', 'genre_Family Adventure', 'genre_Action Thriller', 'genre_Fantasy', 'genre_Crime Drama', 'genre_Action Horror', 'genre_Music Drama', 'genre_Other'])
data_france = data_all.reindex(columns=['France','title', 'dtg', 'country', 'key', 'gdp', 'production budget', 'year', 'genre', 'rating_r', 'rating_g', 'rating_pg13', 'rating_pg', 'rating_unrated', 'favorability', 'genre_Foreign', 'genre_Drama', 'genre_Comedy', 'genre_Horror', 'genre_Animation', 'genre_Thriller', 'genre_Romantic Comedy', 'genre_Action', 'genre_Action / Adventure', 'genre_Documentary', 'genre_Comedy / Drama', 'genre_Romance', 'genre_Action Comedy', 'genre_Drama / Thriller', 'genre_Period Drama', 'genre_Sci-Fi Action', 'genre_Family Comedy', 'genre_Family Adventure', 'genre_Action Thriller', 'genre_Fantasy', 'genre_Crime Drama', 'genre_Action Horror', 'genre_Music Drama', 'genre_Other'])
data_germany = data_all.reindex(columns=['Germany','title', 'dtg', 'country', 'key', 'gdp', 'production budget', 'year', 'genre', 'rating_r', 'rating_g', 'rating_pg13', 'rating_pg', 'rating_unrated', 'favorability', 'genre_Foreign', 'genre_Drama', 'genre_Comedy', 'genre_Horror', 'genre_Animation', 'genre_Thriller', 'genre_Romantic Comedy', 'genre_Action', 'genre_Action / Adventure', 'genre_Documentary', 'genre_Comedy / Drama', 'genre_Romance', 'genre_Action Comedy', 'genre_Drama / Thriller', 'genre_Period Drama', 'genre_Sci-Fi Action', 'genre_Family Comedy', 'genre_Family Adventure', 'genre_Action Thriller', 'genre_Fantasy', 'genre_Crime Drama', 'genre_Action Horror', 'genre_Music Drama', 'genre_Other'])
data_japan = data_all.reindex(columns=['Japan','title', 'dtg', 'country', 'key', 'gdp', 'production budget', 'year', 'genre', 'rating_r', 'rating_g', 'rating_pg13', 'rating_pg', 'rating_unrated', 'favorability', 'genre_Foreign', 'genre_Drama', 'genre_Comedy', 'genre_Horror', 'genre_Animation', 'genre_Thriller', 'genre_Romantic Comedy', 'genre_Action', 'genre_Action / Adventure', 'genre_Documentary', 'genre_Comedy / Drama', 'genre_Romance', 'genre_Action Comedy', 'genre_Drama / Thriller', 'genre_Period Drama', 'genre_Sci-Fi Action', 'genre_Family Comedy', 'genre_Family Adventure', 'genre_Action Thriller', 'genre_Fantasy', 'genre_Crime Drama', 'genre_Action Horror', 'genre_Music Drama', 'genre_Other'])
data_jordan = data_all.reindex(columns=['Jordan','title', 'dtg', 'country', 'key', 'gdp', 'production budget', 'year', 'genre', 'rating_r', 'rating_g', 'rating_pg13', 'rating_pg', 'rating_unrated', 'favorability', 'genre_Foreign', 'genre_Drama', 'genre_Comedy', 'genre_Horror', 'genre_Animation', 'genre_Thriller', 'genre_Romantic Comedy', 'genre_Action', 'genre_Action / Adventure', 'genre_Documentary', 'genre_Comedy / Drama', 'genre_Romance', 'genre_Action Comedy', 'genre_Drama / Thriller', 'genre_Period Drama', 'genre_Sci-Fi Action', 'genre_Family Comedy', 'genre_Family Adventure', 'genre_Action Thriller', 'genre_Fantasy', 'genre_Crime Drama', 'genre_Action Horror', 'genre_Music Drama', 'genre_Other'])
data_lebanon = data_all.reindex(columns=['Lebanon','title', 'dtg', 'country', 'key', 'gdp', 'production budget', 'year', 'genre', 'rating_r', 'rating_g', 'rating_pg13', 'rating_pg', 'rating_unrated', 'favorability', 'genre_Foreign', 'genre_Drama', 'genre_Comedy', 'genre_Horror', 'genre_Animation', 'genre_Thriller', 'genre_Romantic Comedy', 'genre_Action', 'genre_Action / Adventure', 'genre_Documentary', 'genre_Comedy / Drama', 'genre_Romance', 'genre_Action Comedy', 'genre_Drama / Thriller', 'genre_Period Drama', 'genre_Sci-Fi Action', 'genre_Family Comedy', 'genre_Family Adventure', 'genre_Action Thriller', 'genre_Fantasy', 'genre_Crime Drama', 'genre_Action Horror', 'genre_Music Drama', 'genre_Other'])
data_mexico = data_all.reindex(columns=['Mexico','title', 'dtg', 'country', 'key', 'gdp', 'production budget', 'year', 'genre', 'rating_r', 'rating_g', 'rating_pg13', 'rating_pg', 'rating_unrated', 'favorability', 'genre_Foreign', 'genre_Drama', 'genre_Comedy', 'genre_Horror', 'genre_Animation', 'genre_Thriller', 'genre_Romantic Comedy', 'genre_Action', 'genre_Action / Adventure', 'genre_Documentary', 'genre_Comedy / Drama', 'genre_Romance', 'genre_Action Comedy', 'genre_Drama / Thriller', 'genre_Period Drama', 'genre_Sci-Fi Action', 'genre_Family Comedy', 'genre_Family Adventure', 'genre_Action Thriller', 'genre_Fantasy', 'genre_Crime Drama', 'genre_Action Horror', 'genre_Music Drama', 'genre_Other'])
data_poland = data_all.reindex(columns=['Poland','title', 'dtg', 'country', 'key', 'gdp', 'production budget', 'year', 'genre', 'rating_r', 'rating_g', 'rating_pg13', 'rating_pg', 'rating_unrated', 'favorability', 'genre_Foreign', 'genre_Drama', 'genre_Comedy', 'genre_Horror', 'genre_Animation', 'genre_Thriller', 'genre_Romantic Comedy', 'genre_Action', 'genre_Action / Adventure', 'genre_Documentary', 'genre_Comedy / Drama', 'genre_Romance', 'genre_Action Comedy', 'genre_Drama / Thriller', 'genre_Period Drama', 'genre_Sci-Fi Action', 'genre_Family Comedy', 'genre_Family Adventure', 'genre_Action Thriller', 'genre_Fantasy', 'genre_Crime Drama', 'genre_Action Horror', 'genre_Music Drama', 'genre_Other'])
data_russia = data_all.reindex(columns=['Russia','title', 'dtg', 'country', 'key', 'gdp', 'production budget', 'year', 'genre', 'rating_r', 'rating_g', 'rating_pg13', 'rating_pg', 'rating_unrated', 'favorability', 'genre_Foreign', 'genre_Drama', 'genre_Comedy', 'genre_Horror', 'genre_Animation', 'genre_Thriller', 'genre_Romantic Comedy', 'genre_Action', 'genre_Action / Adventure', 'genre_Documentary', 'genre_Comedy / Drama', 'genre_Romance', 'genre_Action Comedy', 'genre_Drama / Thriller', 'genre_Period Drama', 'genre_Sci-Fi Action', 'genre_Family Comedy', 'genre_Family Adventure', 'genre_Action Thriller', 'genre_Fantasy', 'genre_Crime Drama', 'genre_Action Horror', 'genre_Music Drama', 'genre_Other'])
data_spain = data_all.reindex(columns=['Spain','title', 'dtg', 'country', 'key', 'gdp', 'production budget', 'year', 'genre', 'rating_r', 'rating_g', 'rating_pg13', 'rating_pg', 'rating_unrated', 'favorability', 'genre_Foreign', 'genre_Drama', 'genre_Comedy', 'genre_Horror', 'genre_Animation', 'genre_Thriller', 'genre_Romantic Comedy', 'genre_Action', 'genre_Action / Adventure', 'genre_Documentary', 'genre_Comedy / Drama', 'genre_Romance', 'genre_Action Comedy', 'genre_Drama / Thriller', 'genre_Period Drama', 'genre_Sci-Fi Action', 'genre_Family Comedy', 'genre_Family Adventure', 'genre_Action Thriller', 'genre_Fantasy', 'genre_Crime Drama', 'genre_Action Horror', 'genre_Music Drama', 'genre_Other'])
data_uk = data_all.reindex(columns=['United Kingdom','title', 'dtg', 'country', 'key', 'gdp', 'production budget', 'year', 'genre', 'rating_r', 'rating_g', 'rating_pg13', 'rating_pg', 'rating_unrated', 'favorability', 'genre_Foreign', 'genre_Drama', 'genre_Comedy', 'genre_Horror', 'genre_Animation', 'genre_Thriller', 'genre_Romantic Comedy', 'genre_Action', 'genre_Action / Adventure', 'genre_Documentary', 'genre_Comedy / Drama', 'genre_Romance', 'genre_Action Comedy', 'genre_Drama / Thriller', 'genre_Period Drama', 'genre_Sci-Fi Action', 'genre_Family Comedy', 'genre_Family Adventure', 'genre_Action Thriller', 'genre_Fantasy', 'genre_Crime Drama', 'genre_Action Horror', 'genre_Music Drama', 'genre_Other'])

data_egypt = data_egypt[data_egypt['Revenue'] > 0]
data_france = data_france[data_france['Revenue'] > 0]
data_germany = data_germany[data_germany['Revenue'] > 0]
data_japan = data_japan[data_japan['Revenue'] > 0]
data_jordan = data_jordan[data_jordan['Revenue'] > 0]
data_lebanon = data_lebanon[data_lebanon['Revenue'] > 0]
data_mexico = data_mexico[data_mexico['Revenue'] > 0]
data_poland = data_poland[data_poland['Revenue'] > 0]
data_russia = data_russia[data_russia['Revenue'] > 0]
data_spain = data_spain[data_spain['Revenue'] > 0]
data_uk = data_uk[data_uk['Revenue'] > 0]

import matplotlib.pyplot as plt
%pylab inline

x_egypt_simple = data_egypt[list(['production budget', 'gdp', 'favorability'])]
x_france_simple = data_france[list(['production budget', 'gdp', 'favorability'])]
x_germany_simple = data_germany[list(['production budget', 'gdp', 'favorability'])]
x_japan_simple = data_japan[list(['production budget', 'gdp', 'favorability'])]
x_jordan_simple = data_jordan[list(['production budget', 'gdp', 'favorability'])]
x_lebanon_simple = data_lebanon[list(['production budget', 'gdp', 'favorability'])]
x_mexico_simple = data_germany[list(['production budget', 'gdp', 'favorability'])]
x_poland_simple = data_poland[list(['production budget', 'gdp', 'favorability'])]
x_russia_simple = data_russia[list(['production budget', 'gdp', 'favorability'])]
x_spain_simple = data_spain[list(['production budget', 'gdp', 'favorability'])]
x_uk_simple = data_uk[list(['production budget', 'gdp', 'favorability'])]

data_egypt=data_egypt.rename(columns = {'Egypt':'Revenue'})
data_france=data_france.rename(columns = {'France':'Revenue'})
data_germany=data_germany.rename(columns = {'Germany':'Revenue'})
data_japan=data_japan.rename(columns = {'Japan':'Revenue'})
data_jordan=data_jordan.rename(columns = {'Jordan':'Revenue'})
data_lebanon=data_lebanon.rename(columns = {'Lebanon':'Revenue'})
data_mexico=data_mexico.rename(columns = {'Mexico':'Revenue'})
data_poland=data_poland.rename(columns = {'Poland':'Revenue'})
data_russia=data_russia.rename(columns = {'Russia':'Revenue'})
data_spain=data_spain.rename(columns = {'Spain':'Revenue'})
data_uk=data_uk.rename(columns = {'United Kingdom':'Revenue'})

y_egypt = data_egypt['Revenue']
y_france = data_france['Revenue']
y_germany = data_germany['Revenue']
y_japan = data_japan['Revenue']
y_jordan = data_jordan['Revenue']
y_lebanon = data_lebanon['Revenue']
y_mexico = data_mexico['Revenue']
y_poland = data_poland['Revenue']
y_russia = data_russia['Revenue']
y_spain = data_spain['Revenue']
y_uk = data_uk['Revenue']

model_uk_simple = sm.OLS(y_uk,x_uk_simple).fit().summary()
model_uk_simple
model_egypt_simple = sm.OLS(y_egypt,x_egypt_simple).fit().summary()
model_egypt_simple
model_france_simple = sm.OLS(y_france,x_france_simple).fit().summary()
model_france_simple
model_germany_simple = sm.OLS(y_germany,x_germany_simple).fit().summary()
model_germany_simple
model_japan_simple = sm.OLS(y_japan,x_japan_simple).fit().summary()
model_japan_simple
model_jordan_simple = sm.OLS(y_jordan,x_jordan_simple).fit().summary()
model_jordan_simple
model_lebanon_simple = sm.OLS(y_lebanon,x_lebanon_simple).fit().summary()
model_lebanon_simple
model_mexico_simple = sm.OLS(y_mexico,x_mexico_simple).fit().summary()
model_mexico_simple
model_poland_simple = sm.OLS(y_poland,x_poland_simple).fit().summary()
model_poland_simple
model_russia_simple = sm.OLS(y_russia,x_russia_simple).fit().summary()
model_russia_simple
model_spain_simple = sm.OLS(y_spain,x_spain_simple).fit().summary()
model_spain_simple