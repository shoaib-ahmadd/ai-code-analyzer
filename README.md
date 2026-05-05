# AI Code Analyzer

A web-based tool to analyze code quality, detect issues, and suggest improvements using an AI-assisted backend.  
It combines a clean code editor UI with a FastAPI backend to provide quick and practical feedback.

---

## 🚀 Live Demo

Frontend:  
https://ai-code-analyzer-shoaib.netlify.app  

Backend API Docs:  
https://ai-code-analyzer-gdt2.onrender.com/docs  

---

## 📌 Overview

This project allows users to write or upload code and get:

- Code quality score  
- Identified issues  
- Improvement suggestions  

It works like a lightweight code review assistant.

---

## ✨ Features

- Interactive code editor (Monaco)
- File upload support
- AI-based code analysis
- Score visualization with issue breakdown
- Clean and responsive UI
- FastAPI backend with structured responses

---

## 🛠️ Tech Stack

Frontend  
- HTML, CSS, JavaScript  
- Monaco Editor  

Backend  
- Python  
- FastAPI  
- Uvicorn  

Deployment  
- Netlify (Frontend)  
- Render (Backend)  

---

## 📁 Project Structure

ai-code-analyzer/  
│  
├── backend/  
│   ├── main.py  
│   ├── analyzer.py  
│   └── requirements.txt  
│  
├── frontend/  
│   ├── index.html  
│   ├── style.css  
│   └── app.js  
│  
├── screenshots/  
│   ├── AI1.png  
│   └── AI2.png  
│  
└── README.md  

---

## 🖼️ Screenshots

### Code Editor with Analysis Output  
![Screenshot](./screenshots/AI1.png)

### Clean Editor View  
![Screenshot](./screenshots/AI2.png)

---

## ⚙️ How It Works

1. User writes or uploads code  
2. Frontend sends request to `/analyze`  
3. Backend processes the code  
4. Returns score, issues, and suggestions  
5. Results are displayed instantly  

---

## 🔌 API Endpoint

POST /analyze  

Request:
{
  "code": "your code here",
  "language": "python"
}

Response:
{
  "score": 6.5,
  "issues": [],
  "suggestions": "..."
}

---

## 💻 Setup (Local)

Backend:
cd backend  
pip install -r requirements.txt  
uvicorn main:app --host 0.0.0.0 --port 10000  

Frontend:  
Open index.html in browser (or use Live Server)

---

## 🧠 Notes

- CORS is enabled for frontend-backend communication  
- Render free tier may cause slight delay (cold start)  
- Frontend is static and connects to deployed API  

---

## 🔮 Future Improvements

- Multi-language support  
- Better scoring algorithm  
- Authentication system  
- Save analysis history  
- UI enhancements  

---

## 👤 Author

Shoaib Ahmad  
https://github.com/shoaib-ahmadd  

---

## 📄 License

Open-source project for learning and demonstration purposes.
