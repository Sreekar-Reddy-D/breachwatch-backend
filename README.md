# breachwatch-backend

---

# 🔐 BreachWatch – Flask API

This is the backend API service for **BreachWatch**, a simple and secure app to check whether a password has been exposed in a known data breach using the HaveIBeenPwned (HIBP) API.

---

## 🌐 Live Backend URL

> `https://<your-render-subdomain>.onrender.com`

---

## 🛠️ Tech Stack

- Python 3.10+
- Flask
- Flask-CORS
- Gunicorn (production server)
- Hosted on Render

---

## 🚀 API Endpoints

### `POST /check_password`

Checks whether the given password hash suffix has been found in known breaches.

**Request JSON:**
```json
{
  "prefix": "5BAA6",
  "suffix": "1E4C9B93F3F0682250B6CF8331B7EE68FD8"
}
````

**Response JSON:**

```json
{
  "pwned": true,
  "count": "6099453"
}
```

---

## 🔧 Setup Instructions

### 1. Clone and Install

```bash
git clone https://github.com/<your-username>/breachwatch-backend.git
cd breachwatch-backend
pip install -r requirements.txt
```

### 2. Run Locally

```bash
python app.py
# or for production:
gunicorn app:app --bind 0.0.0.0:10000
```

---

## 📄 `requirements.txt`

```
flask
requests
gunicorn
flask-cors
```

---

## 🔐 Security Note

* Passwords are hashed client-side using SHA1.
* Only a 5-character prefix of the hash is sent to the backend.
* This preserves user privacy by using HIBP’s [k-anonymity](https://haveibeenpwned.com/API/v3#SearchingPwnedPasswordsByRange) model.

---
