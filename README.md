```markdown
# ✅ Task Management System – REST API with PostgreSQL & JWT Auth

A powerful and secure **Task Management System** built using Django, Django REST Framework, and PostgreSQL. This application enables users to **Create**, **Read**, **Update**, and **Delete** (CRUD) their tasks, with features to manage **status**, **priority**, and **authentication** using **JWT**. Perfect for boosting productivity and staying organized.

---

## 📸 Project Preview

![Task Dashboard](https://via.placeholder.com/800x400?text=Dashboard+Preview)
> *Preview of user-specific tasks, status badges, and actions like edit/delete.*

---

## 🚀 Features

### 🔐 Authentication
- ✅ User registration & login via **JWT (JSON Web Tokens)**
- ✅ Secure token-based authentication (access + refresh)
- ✅ Only logged-in users can manage their tasks

### 📝 Task Management
- ✅ Create / Read / Update / Delete tasks (CRUD)
- ✅ Tasks linked to individual users
- ✅ Task **status** options: `Pending`, `In Progress`, `Completed`
- ✅ Task **priority** levels: `Low`, `Medium`, `High`
- ✅ Timestamps: `created_at`, `updated_at`

### 🔍 Filtering & Sorting
- 🔎 Filter tasks by status or priority
- 🔄 Sort tasks by creation or update time
- 🔍 Search tasks by title or description

---

## 🧰 Tech Stack

| Layer        | Tools Used                                     |
|--------------|------------------------------------------------|
| Backend      | Django 5.x, Django REST Framework              |
| Database     | PostgreSQL                                     |
| Auth         | JWT (SimpleJWT)                                |
| Filtering    | `django-filter`                                |
| API Docs     | DRF Schema / Browsable API                     |
| Dev Tools    | Postman, VS Code, GitHub                       |

---

## 🔧 Installation Guide

1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/task-management-system.git
cd task-management-system
````

2️⃣ Create a Virtual Environment

```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

4️⃣ Set Up PostgreSQL

* Create a PostgreSQL database (e.g., `task_db`)
* Update `settings.py` with:

```python
DATABASES = {
  'default': {
      'ENGINE': 'django.db.backends.postgresql',
      'NAME': 'task_db',
      'USER': 'your_db_user',
      'PASSWORD': 'your_db_password',
      'HOST': 'localhost',
      'PORT': '5432',
  }
}
```

5️⃣ Run Migrations

```bash
python manage.py migrate
```

6️⃣ Start the Server

```bash
python manage.py runserver
```

---

## 🔐 JWT Authentication

### 🔸 Register

```http
POST /api/register/
```

```json
{
  "username": "john_doe",
  "email": "john@example.com",
  "password": "StrongPassword123"
}
```

### 🔸 Login

```http
POST /api/token/
```

```json
{
  "username": "john_doe",
  "password": "StrongPassword123"
}
```

### 🔄 Refresh Token

```http
POST /api/token/refresh/
```

```json
{
  "refresh": "<your_refresh_token>"
}
```

---

## 📚 API Endpoints

| Method | Endpoint            | Description                 | Auth Required |
| ------ | ------------------- | --------------------------- | ------------- |
| POST   | /api/register/      | Register a new user         | ❌             |
| POST   | /api/token/         | Get access & refresh tokens | ❌             |
| POST   | /api/token/refresh/ | Refresh access token        | ❌             |
| GET    | /api/tasks/         | List user’s tasks           | ✅             |
| POST   | /api/tasks/         | Create a new task           | ✅             |
| GET    | /api/tasks/{id}/    | Retrieve a task             | ✅             |
| PUT    | /api/tasks/{id}/    | Update a task               | ✅             |
| DELETE | /api/tasks/{id}/    | Delete a task               | ✅             |

---

## 🌟 Filtering & Searching Examples

| Feature            | Example                            |
| ------------------ | ---------------------------------- |
| Filter by status   | `/api/tasks/?status=completed`     |
| Filter by priority | `/api/tasks/?priority=high`        |
| Search by title    | `/api/tasks/?search=meeting`       |
| Order by date      | `/api/tasks/?ordering=-updated_at` |

---

## 🛡️ Security Practices

* ✅ JWT authentication for API endpoints
* ✅ CSRF protection on applicable views
* ✅ Password validation rules
* ✅ User-specific task data isolation

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more info.

---

## 🤝 Connect with Me

> Made with ❤️ by **Muhammad Ahmed**

🔗 [LinkedIn](https://www.linkedin.com/in/muhammad-ahmed-5b7850340/)
📬 Feel free to connect, fork, star, and build upon this project!

---
