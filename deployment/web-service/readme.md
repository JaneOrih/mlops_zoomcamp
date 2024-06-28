
termial commands
gunicorn --bind=0.0.0.0:9696 predict:app

pipenv install waitress
waitress-serve --listen=*:8000 app:app

pipenv install --dev requests

docker build -t ride-duration-prediction-service:v1 .
docker run -it --rm -p 9696:9696 ride-duration-prediction-service:v1

mlflow server --backend-store-url=sqlite:///mlflow.db --default-artifact-root=s3://mlflow-models/