import spacy
from sklearn.base import BaseEstimator, TransformerMixin

class PreprocessText(BaseEstimator, TransformerMixin):
    def __init__(self, nlp_model):
        self.nlp = nlp_model
    
    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        preprocessed_texts = [self._preprocess(text) for text in X]
        return preprocessed_texts

    def _preprocess(self, text):
        # minux, removing stop words, tokenize 
        nlp = spacy.load('es_core_news_sm')
        
        text = text.lower()
        doc = nlp(text)

        tokens = [token.lemma_.lower() for token in doc if not token.is_stop and not token.is_punct]

        preprocessed_text = ' '.join(tokens)
        
        doc = nlp(preprocessed_text)
        
        features = {}
        for token in doc:
            if not token.is_stop and not token.is_punct:
                key = token.lemma_.lower()
                features[key] = features.get(key, 0) + 1
        return features