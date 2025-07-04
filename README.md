# Sentiment Reviews Analysis
In this project I created a sentiment analysis model based on reviews labeled as **positive** or **negative**. It provides a simple way to know the sentiment of the review/comment. The model uses Multinomial Naive Bayes for classifcation and it was trained on a provided dataset.

The service is hosted through and API with one endpoint `POST /predecir` which recieves a JSON with the field `comentario`. Th response is the sentiment of the given review.

# How to run
Locate on the root folder and run:
1. To train the model and then run the API
```
python main.py
python app.py
```
The API is listenin in port :5000

You can test it on local via terminal using `curl` or via Postman. For example running the command:
```
curl -X POST http://localhost:5000/predecir -H "Content-Type: application/json"  -d '{"comentario":"excelente calidad, muy buen servicio"}'
```

2. To create the Docker image run the container:
```
docker build -t sentiment-api .
docker run -d -p 5000:5000  --name my-api sentiment-api
```


# Structure
.
└── SentimentReviewAnalysis/
    ├── data/
    │   ├── dataset.csv
    │   └── testdata.csv
    ├── notebooks/
    │   ├── model.ipynb
    │   ├── ExperimentNotebook.ipynb
    │   └── model.pkl
    ├── Dockerfile
    ├── LICENSE
    ├── README.md
    ├── app.py
    ├── main.py
    ├── preprocessing.py
    ├── trained_model.pkl
    └── requirements.txt
