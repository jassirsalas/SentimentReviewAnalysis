import spacy
import joblib
import pandas as pd
from pathlib import Path
from nltk.corpus import stopwords
from sklearn.pipeline import Pipeline
from preprocessing import PreprocessText
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction import DictVectorizer

def load_spacy_model(model_name):
    try:
        return spacy.load(model_name)
    except OSError:
        print(f"model not loaded. downloading model: '{model_name}'...")
        spacy.cli.download(model_name)
        return spacy.load(model_name)

nlp = load_spacy_model("es_core_news_sm")

DATA_PATH = Path('./data/dataset.csv')
df = pd.read_csv(DATA_PATH)

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
