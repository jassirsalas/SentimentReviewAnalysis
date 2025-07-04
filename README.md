# Sentiment Reviews Analysis
In this project I created a sentiment analysis model based on reviews labeled as **positive** or **negative**. It provides a simple way to know the sentiment of the review/comment. The model uses Multinomial Naive Bayes for classifcation and it was trained on a provided dataset.

The service is hosted through and API with one endpoint `POST /predecir` which recieves a JSON with the field `comentario`. Th response is the sentiment of the given review.

# How to run
## Setup
First let's set the enviroment. In the command line and in the main folder run:
```
python -m venv api
```
This will create an python enviroment called api

Then, execute it. Run the following in the command line:

For Linux:
```
source api/bin/activate
```

For Windows CMD:
```
.\api\Scripts\activate.bat
```

For Windows Powershell:
```
.\api\Scripts\activate.ps1
```

And finally install all the dependecies through:
```
pip install -r requirements.txt
```
Now you can run the main code and the API 

## Running the main code
Locate on the root folder and run:

To train the model and then run the API
```
python main.py
python app.py
```
The API is listenin in port :5000

You can test it on local via terminal using `curl` or via Postman. For example running the command:
```
curl -X POST http://localhost:5000/predecir -H "Content-Type: application/json"  -d '{"comentario":"excelente calidad, muy buen servicio"}'
```

# Docker
To create the Docker image run the container:
```
docker build -t sentiment-api .
docker run -d -p 5000:5000  --name my-api sentiment-api
```
