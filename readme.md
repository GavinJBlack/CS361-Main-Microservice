# 📦 Microservice A - Command Classification API

**For:** Peter Nikitakis  
**Implemented by:** Gavin Black

---

## 🧠 Overview

This microservice classifies terminal commands (e.g., `git`, `docker`, `kubectl`) based on their prefix and returns the associated tool type. It follows REST standards and responds with JSON.

---

## 📬 How to Request and Receive Data

Your application must make an HTTP `POST` request to the following endpoint:

POST http://localhost:5000/classify

### ✅ Request Format:
- Content-Type: `application/json`
- Body:
```json
{
  "command": "git status"
}

```

### ✅ Response Format:

```json
{
  "type": "git"
}
```

If the command does not match any known tool, the response will be:
```json
{
  "type": "unknown"
}
```

## UML Sequence Diagram
![img.png](img.png)