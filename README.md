# Vedic Gajendra Sharma — Astrology Consultation & Appointment Booking Website

A complete, production-ready Full Stack Astrology Consultation website built with
**Django, Bootstrap 5, HTML5, CSS3, JavaScript, and MySQL**.

**Astrologer:** Gajendra Sharma
**Phone/WhatsApp:** +91 7748044076
**Email:** gurmitSharma09@gmail.com
**Instagram:** @vedic_gajendra_sharma
**Address:** Village Kherkheda, Kaleshwar Mandir, Sitamau–Suwasra Road, Tehsil Sitamau, District Mandsaur, Madhya Pradesh

---

## 🌟 Features

- Beautiful, responsive, luxury UI (Dark Navy Blue + Royal Gold + White + Cream theme)
- Home, About, Services, Book Appointment, Gallery, Blog, Reviews, FAQ, Contact pages
- User Registration & Login (Django Auth) with extended Profile model
- User Dashboard with appointment stats & history
- Full Appointment Booking system (service, date, time, mode, birth details)
- 12 pre-loaded astrology services (Janam Kundli, Kundli Matching, Vastu, Numerology, etc.)
- Blog with categories, Gallery with categories, Reviews with star ratings
- Contact form saved to database + admin panel visibility
- Django Admin Dashboard to manage Users, Appointments, Services, Blog Posts,
  Gallery Images, Reviews, FAQs and Contact Messages
- WhatsApp chat button & Call Now floating buttons
- Site-wide Search
- Custom 404 error page
- Privacy Policy & Terms and Conditions pages
- Scroll-to-top button, loading animation, hover/scroll animations
- Pagination on Services, Blog, Gallery, Reviews
- Form validation (client-side + server-side)
- Astrologer photo and promotional posters (provided by client) already integrated
  into the Hero section, About page, and Gallery

---

## 🛠️ Tech Stack

| Layer       | Technology                          |
|-------------|--------------------------------------|
| Backend     | Python, Django (ORM, Auth, Admin)    |
| Frontend    | HTML5, CSS3, JavaScript, Bootstrap 5 |
| Database    | MySQL                                |
| Icons       | Font Awesome 6                       |
| Fonts       | Google Fonts (Cinzel + Poppins)      |

No React, Node.js, PHP, Laravel, Flask, MongoDB, Firebase, or AI features are used.

---

## 📁 Project Structure

```
vedic_astro/
├── manage.py
├── requirements.txt
├── database.sql
├── README.md
├── vedic_astro/          # Project settings, urls, wsgi
├── core/                 # Home, About, Contact, FAQ, Privacy, Terms, Search, 404
├── accounts/             # Register, Login, Profile, Dashboard
├── services/             # Astrology services (list/detail)
├── appointments/         # Appointment booking & history
├── blog/                 # Blog posts & categories
├── gallery/               # Gallery images & categories
├── reviews/               # Client reviews & ratings
├── templates/             # All HTML templates (base.html + app templates)
├── static/                # CSS, JS, images (incl. astrologer photo & posters)
└── media/                 # User-uploaded content (profile pics, gallery, blog images)
```

---

## 🚀 Setup Instructions

### 1. Extract the ZIP and create a virtual environment

```bash
cd vedic_astro
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

> **Note:** `mysqlclient` requires MySQL development headers.
> - **Ubuntu/Debian:** `sudo apt-get install python3-dev default-libmysqlclient-dev build-essential`
> - **Windows:** Install MySQL Connector/C or use a prebuilt wheel.
> - **macOS:** `brew install mysql-client` then set the required env vars (see mysqlclient docs).

### 3. Create the MySQL database

```bash
mysql -u root -p < database.sql
```

This creates the `vedic_gajendra_sharma` database and an optional dedicated MySQL user.

### 4. Configure database credentials

Edit `vedic_astro/settings.py` (or set environment variables) with your MySQL credentials:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'vedic_gajendra_sharma',
        'USER': 'root',
        'PASSWORD': 'your_mysql_password',
        'HOST': 'localhost',
        'PORT': '3306',
        'OPTIONS': {'charset': 'utf8mb4'},
    }
}
```

Or set these environment variables before running the server:
`DB_NAME`, `DB_USER`, `DB_PASSWORD`, `DB_HOST`, `DB_PORT`.

### 5. Run migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create an admin (superuser) account

```bash
python manage.py createsuperuser
```

### 7. (Optional) Load demo/sample data

This loads 12 sample services, FAQs, gallery images (using the provided posters),
and 3 sample blog posts:

```bash
python manage.py seed_data
```

### 8. Run the development server

```bash
python manage.py runserver
```

Visit:
- Website: http://127.0.0.1:8000/
- Admin Dashboard: http://127.0.0.1:8000/admin/

---

## 🖼️ Adding More Images

- **Astrologer photo:** already placed at `static/img/astrologer.jpeg` (used in Hero & About).
- **Promotional posters:** placed at `static/img/poster1.jpeg` – `poster4.jpeg` and also
  loaded into the Gallery app via `seed_data`.
- To add more content, log into `/admin/` and add Services, Gallery Images, Blog Posts,
  FAQs, or Reviews — all support image uploads directly from the admin panel.

---

## 🔐 Default Admin Login (after createsuperuser)

Use the username/password you set with `createsuperuser`. From the Admin Dashboard you can:
- Approve/manage appointments and update their status
- Add/edit/delete services, blog posts, gallery images, FAQs
- Approve customer reviews before they go live
- View and respond to contact form messages
- Manage registered users and their profiles

---

## ⚠️ Before Going to Production

1. Set `DEBUG = False` in `settings.py`.
2. Set a strong, unique `SECRET_KEY`.
3. Update `ALLOWED_HOSTS` with your actual domain.
4. Configure a real email backend (SMTP) instead of the console backend.
5. Serve static/media files via a proper web server (Nginx/Apache) or a CDN.
6. Use HTTPS.

---

## 📞 Support

For any questions about this codebase, refer to inline code comments across all
`models.py`, `views.py`, and `forms.py` files — every app is fully commented for
easy customization.
