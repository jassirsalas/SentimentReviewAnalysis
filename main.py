import joblib
import spacy
import pandas as pd
from nltk.corpus import stopwords
from sklearn.pipeline import Pipeline
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction import DictVectorizer
from preprocessing import PreprocessText


try:
    nlp = spacy.load("es_core_news_sm")
except OSError:
    print("El modelo 'es_core_news_sm' de spaCy no está descargado. Por favor, ejecuta:")
    print("python -m spacy download es_core_news_sm")
    exit()

df = pd.read_csv("./data/dataset.csv")

X = df["comentario"]
y = df["sentimiento"]

model = Pipeline([
    ('preprocess', PreprocessText(nlp_model=nlp)),
    ('dictVec', DictVectorizer()),
    ('bayesNB', MultinomialNB(class_prior=[0.5, 0.5]))
])

model.fit(X, y)
print('training model...')

joblib.dump(model, "./trained_model.pkl")
print('model trained successfully')
