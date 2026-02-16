# StudentSwap

A Django-based student marketplace for buying, selling, and exchanging second-hand items. Implements core cart and product functionality, with planned support for item exchange and price adjustment.

---

## 🌐 Live Demo

**http://ecommerce-dev.ap-south-1.elasticbeanstalk.com**

Deployed on AWS Elastic Beanstalk with RDS and S3 integration.

---

## 🏗️ Production Deployment Architecture

- **AWS Elastic Beanstalk** – Application Hosting  
- **AWS EC2** – Underlying Compute Infrastructure  
- **AWS RDS (PostgreSQL)** – Production Database  
- **AWS S3** – Media Storage  
- **AWS IAM** – Access Control & Security  
- **Environment Variables** – Secure Configuration Management  

---

## 🛠️ Tech Stack

### Backend
- Python
- Django

### Frontend
- HTML
- CSS
- Bootstrap
- JavaScript (Fetch API)

### Database
- SQLite (Development)
- PostgreSQL via AWS RDS (Production)

### Email
- SMTP (Email Verification)

---

## ⚙️ Local Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/studentswap.git
cd studentswap
```

### 2️⃣ Create a Virtual Environment

```bash
python -m venv .venv
```

### 3️⃣ Activate the Virtual Environment

**Windows:**
```bash
.venv\Scripts\activate
```

**Mac/Linux:**
```bash
source .venv/bin/activate
```

### 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔐 Configure Environment Variables

Create a `.env` file in the project root directory.

Copy `.env.example` and fill in your credentials.

Example configuration:

```env
DJANGO_SECRET_KEY=your_secret_key
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=your_db_host
DB_PORT=5432

EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your_email@gmail.com
EMAIL_HOST_PASSWORD=your_app_password
```

⚠️ **Do NOT commit your `.env` file to version control.**

---

## 🗄️ Apply Database Migrations

```bash
python manage.py migrate
```

---

## ▶️ Run the Development Server

```bash
python manage.py runserver
```

Visit:

```
http://127.0.0.1:8000/
```

---

## 📧 Email Verification

- When a new user registers, a verification email is sent.
- The user must click the verification link to activate the account.
- SMTP credentials must be configured in the `.env` file.

---

## 🔒 Security Practices

- Sensitive credentials stored in environment variables
- AWS IAM roles used for service access control
- No hardcoded secrets in source code
- `.env` excluded via `.gitignore`

---

