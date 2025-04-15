# 🔍 Loan Defaulter Prediction

A machine learning-powered web application to predict potential loan defaulters using user-inputted financial and demographic data. This end-to-end project includes data processing, model training, API development, frontend interface, CI/CD automation, containerization (backend only), and cloud deployment.

---

## 🚀 Project Features

- 🔢 **Data Collection & Processing:** Clean and analyze customer data to identify patterns of defaulters.
- 📊 **Exploratory Data Analysis (EDA):** Uncover insights using visualizations and statistics.
- 🧠 **Model Training:** Trained machine learning models for classification (Logistic Regression, Random Forest, etc.).
- 🌐 **Frontend with Streamlit:** Interactive UI for users to input data and view predictions.
- 🛠️ **Backend with FastAPI:** Lightweight and fast REST API for serving ML predictions.
- 🐳 **Backend Containerized with Docker:** Easily deployable and platform-independent backend.
- ⚙️ **CI/CD with GitHub Actions:** Automated build, test, and deploy pipeline.
- ☁️ **Deployed on AWS EC2:** Live and accessible application hosted on a cloud server.

---

## 🧰 Tech Stack

| Layer      | Tools / Frameworks                                |
| ---------- | ------------------------------------------------- |
| ML & EDA   | Python, Pandas, Scikit-learn, Matplotlib, Seaborn |
| API        | FastAPI                                           |
| Frontend   | Streamlit                                         |
| DevOps     | Docker (Backend), GitHub Actions                  |
| Deployment | AWS EC2 (Ubuntu), Nginx (optional)                |

---

## 📁 Project Structure

```
loan-defaulter-prediction/
│
├── .github/workflows/       # GitHub Actions CI/CD configuration
├── data/                    # Raw and processed datasets
├── mlartifacts/             # ML models, encoders, etc.
├── mlruns/                  # MLflow experiment tracking
├── Research/                # EDA notebooks, experiments
├── tests/                   # Unit and integration tests
├── venv/                    # Virtual environment (not pushed to repo)
├── app.py                   # Streamlit frontend entry point
├── main.py                  # FastAPI backend entry point
├── best_model_gb.pkl        # Trained model file
├── Dockerfile               # Backend Docker image definition
├── requirements.txt         # Python dependencies
├── .dockerignore
├── .gitignore
└── README.md
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/ka1817/loan-defaulter-prediction.git
cd loan-defaulter-prediction
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run Backend (FastAPI)

```bash
uvicorn main:app --reload
```

### 5. Run Frontend (Streamlit)

```bash
streamlit run app.py
```

---

## 🐳 Docker (Backend Only)

### Build and Run Backend Container

```bash
docker build -t pranavreddy123/loan-defaulter-app .

docker run -p 8000:8000 pranavreddy123/loan-defaulter-app
```

You can also pull the image directly:

```bash
docker pull pranavreddy123/loan-defaulter-app
```

---

## ⚙️ CI/CD (GitHub Actions)

GitHub Actions automatically builds and tests the code on every push. On merge to `main`, the CI/CD workflow:

- Builds Docker image for backend
- Pushes image to Docker Hub: `pranavreddy123/loan-defaulter-app`
- Deploys to AWS EC2 (via SSH or webhook)

Configure secrets like `AWS_HOST`, `SSH_KEY`, etc., in your GitHub repo settings.

---

## ☁️ Deployment on AWS EC2

1. Create an EC2 instance (Ubuntu).
2. Install Docker and Git.
3. Clone this repository.
4. Pull the Docker image or build from source.
5. Run the backend container:

```bash
docker run -p 8000:8000 pranavreddy123/loan-defaulter-app
```

6. Run Streamlit manually:

```bash
streamlit run app.py
```

7. (Optional) Set up Nginx as a reverse proxy for domain + HTTPS.

---

## 📜 License

This project is licensed under the MIT License. See `LICENSE` file for details.

---

## 🙌 Acknowledgements

- [Scikit-learn](https://scikit-learn.org/)
- [Streamlit](https://streamlit.io/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [AWS](https://aws.amazon.com/)


