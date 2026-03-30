# Features
- FastAPI backend
- Docker containerization
- ML model prediction endpoint

##  How to Run

### Build Docker Image
docker build -t ml-api .

### Run Container
docker run -p 8000:8000 ml-api

### Access API
http://localhost:8000/docs

##  Sample Input
POST /predict

{
  "features": [5]
}

##  Output
{
  "prediction": [50]
}

##  Live API
https://mlops-exp-5.onrender.com/docs





