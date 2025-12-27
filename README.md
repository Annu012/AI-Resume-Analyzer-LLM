🧠 AI Resume Analyzer — LLM-Powered Resume Screening Platform

A full-stack Generative AI application that evaluates resumes against job descriptions to produce job-fit scores, skill gap analysis, resume ranking, and recruiter insights using LLMs + RAG.

Built with FastAPI, LangChain, OpenAI, React, and AWS.

🚀 Key Features

🔐 JWT-based Recruiter Authentication

📄 PDF Resume Parsing

🤖 LLM-Powered Resume Evaluation

📊 Job Fit Scoring & Resume Ranking

🧠 RAG-Based Job Description Grounding

🗄️ Persistent Storage (SQL Database)

📈 Recruiter Dashboard (React)

☁️ Deployed on AWS EC2

🏗️ System Architecture
Recruiter (Browser)
        ↓
React Frontend (Dashboard)
        ↓ JWT
FastAPI Backend
        ↓
PDF Parser → RAG Pipeline → LLM
        ↓
Database (Results & Rankings)
        ↓
Dashboard APIs

🧩 Tech Stack
Backend

FastAPI

Python

LangChain

OpenAI API

SQLAlchemy

JWT Authentication

FAISS / Vector DB

AWS EC2

Frontend

React

Axios

JWT Auth

Minimal ATS-safe UI

📂 Project Structure:

ai-resume-analyzer-llm/

│
├── app/

│   ├── main.py          # FastAPI entry point

│   ├── config.py        # Environment config

│   ├── database.py     # DB connection

│   ├── models.py       # SQLAlchemy models

│   ├── auth.py         # JWT + hashing

│   ├── dependencies.py # Auth guards

│
├── requirements.txt

├── .env.example

└── README.md

🔑 API Endpoints
Method	Endpoint	Description

POST	/register	Recruiter registration

POST	/login	JWT login

POST	/analyze-pdf	Upload & analyze resume

GET	/dashboard	Ranked candidates

GET	/health	Service health check

⚙️ Setup & Run Locally

1️⃣ Clone Repository
git clone https://github.com/your-username/ai-resume-analyzer-llm.git
cd ai-resume-analyzer-llm

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Configure Environment
cp .env.example .env

4️⃣ Run Backend
uvicorn app.main:app --reload

5️⃣ Open API Docs
http://localhost:8000/docs

🧠 How Resume Analysis Works:

Recruiter uploads resume PDF

PDF text is extracted

Job description is embedded

RAG pipeline retrieves relevant JD context

LLM evaluates resume using structured prompts

Results are scored, ranked, and stored

Recruiter views insights on dashboard

🧪 Sample Output (LLM Response)


{
  "job_fit_score": 82,
  
  "matched_skills": ["Python", "FastAPI", "SQL"],
  
  "missing_skills": ["Docker", "AWS"],
  
  "improvement_suggestions": [
    "Add cloud deployment experience",
    
    "Include system design projects"
  ]
}

☁️ Deployment

Backend: AWS EC2 (Uvicorn + Gunicorn)

Frontend: AWS S3 + CloudFront / EC2

Secrets: Environment variables

Scalability: Modular AI pipeline

🎯 Why This Project Matters

✔ Real-world GenAI use case

✔ Demonstrates RAG, prompt engineering, system design

✔ Recruiter-grade dashboard

✔ FAANG interview-ready architecture



📌 Future Improvements

Multi-tenant company support

Resume-to-resume comparison

Interview question generation

Analytics charts

Docker + CI/CD

👤 Author

Anisa Shaikh
GenAI / AI Engineer / Java Developer
