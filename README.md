\# ML API with FastAPI \& Docker 🚀



\## 📌 Project Overview

This project is a machine learning API built using FastAPI and Docker.



\##  Features

\- FastAPI backend

\- Docker containerization

\- ML model prediction endpoint



\## 🚀 How to Run



\### Build Docker Image

docker build -t ml-api .



\### Run Container

docker run -p 8000:8000 ml-api



\### Access API

http://localhost:8000/docs



\## 📥 Sample Input

POST /predict



{

&#x20; "features": \[5]

}



\## 📤 Output

{

&#x20; "prediction": \[50]

}

