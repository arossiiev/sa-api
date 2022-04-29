import time
import os

from keras.preprocessing.sequence import pad_sequences
from keras.models import load_model
from joblib import load

KERAS_MODEL = os.path.abspath("app/model/model.h5")
TOKENIZER_MODEL = os.path.abspath("app/model/tokenizer.pkl")

# KERAS
SEQUENCE_LENGTH = 300

# SENTIMENT
POSITIVE = "POSITIVE"
NEGATIVE = "NEGATIVE"
NEUTRAL = "NEUTRAL"
SENTIMENT_THRESHOLDS = (0.4, 0.7)


class PredictionService:

    def __init__(self):
        self.model = load_model(KERAS_MODEL)
        self.tokenizer = load(TOKENIZER_MODEL)

    def predict(self, text, include_neutral=True):
        start_at = time.time()

        x_test = pad_sequences(self.tokenizer.texts_to_sequences([text]), maxlen=SEQUENCE_LENGTH)

        score = self.model.predict([x_test])[0]

        label = self.decode_sentiment(score, include_neutral=include_neutral)

        return {"label": label, "score": float(score),
                "elapsed_time": time.time() - start_at}

    def decode_sentiment(self, score, include_neutral=True):
        if include_neutral:
            label = NEUTRAL
            if score <= SENTIMENT_THRESHOLDS[0]:
                label = NEGATIVE
            elif score >= SENTIMENT_THRESHOLDS[1]:
                label = POSITIVE

            return label
        else:
            return NEGATIVE if score < 0.5 else POSITIVE
