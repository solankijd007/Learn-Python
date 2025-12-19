# FastAPI Project - शुरुआत से सीखें

यह एक basic FastAPI project है जो Python में बनाया गया है।

## 📋 Prerequisites

- Python 3.12.3 ✅ (Installed)
- pip3 ✅ (Installed)

## 🚀 Installation Steps

### 1. Virtual Environment बनाएं
```bash
python3 -m venv venv
```

### 2. Virtual Environment को Activate करें
```bash
source venv/bin/activate
```

### 3. Dependencies Install करें
```bash
pip install -r requirements.txt
```

## ▶️ Application को Run करें

### Development Server Start करें
```bash
uvicorn main:app --reload
```

**Options:**
- `main`: Python file का naam (main.py)
- `app`: FastAPI instance का naam
- `--reload`: Code change होने पर automatically restart होगा

### Custom Host और Port के साथ Run करें
```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

## 🌐 API Endpoints

Application run होने के बाद ये URLs access कर सकते हैं:

### 1. Home Page
```
GET http://localhost:8000/
```

### 2. Interactive API Documentation (Swagger UI)
```
http://localhost:8000/docs
```
यहां आप सभी endpoints को test कर सकते हैं!

### 3. Alternative API Documentation (ReDoc)
```
http://localhost:8000/redoc
```

### 4. Item Endpoint (Path Parameter)
```
GET http://localhost:8000/items/1
GET http://localhost:8000/items/1?q=search_term
```

### 5. Create Item (POST Request)
```
POST http://localhost:8000/items/?name=Laptop&price=50000
```

### 6. User Endpoint
```
GET http://localhost:8000/users/123
```

### 7. Health Check
```
GET http://localhost:8000/health
```

## 📚 Project Structure

```
FastAPI/
├── venv/                 # Virtual environment
├── main.py              # Main application file
├── requirements.txt     # Dependencies
└── README.md           # Yeh file
```

## 🎯 Next Steps

1. **Pydantic Models**: Data validation के लिए models बनाएं
2. **Database**: SQLAlchemy या MongoDB integrate करें
3. **Authentication**: JWT tokens के साथ user authentication add करें
4. **CORS**: Frontend integration के लिए CORS enable करें
5. **Testing**: Pytest के साथ tests लिखें

## 📖 Useful Commands

### Virtual Environment Deactivate करें
```bash
deactivate
```

### Dependencies को Update करें
```bash
pip install --upgrade fastapi uvicorn
```

### Installed Packages देखें
```bash
pip list
```

### Requirements File Generate करें
```bash
pip freeze > requirements.txt
```

## 🔧 Troubleshooting

### Port already in use error
अगर port 8000 already use में है, तो दूसरा port use करें:
```bash
uvicorn main:app --port 8001 --reload
```

### Virtual Environment activate नहीं हो रहा
सुनिश्चित करें कि आप सही directory में हैं:
```bash
cd /home/jd/Python/FastAPI
source venv/bin/activate
```

## 📝 Notes

- हमेशा virtual environment activate करके काम करें
- Code changes automatically reload होंगे `--reload` flag की वजह से
- Production में `--reload` flag use न करें

## 🎓 Learning Resources

- [FastAPI Official Documentation](https://fastapi.tiangolo.com/)
- [FastAPI Tutorial](https://fastapi.tiangolo.com/tutorial/)
- [Pydantic Documentation](https://docs.pydantic.dev/)

---

**Happy Coding! 🚀**
