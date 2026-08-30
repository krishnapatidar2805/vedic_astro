-- ============================================================
-- Vedic Gajendra Sharma - Astrology Website
-- MySQL Database Setup Script
-- ============================================================
-- HOW TO USE:
-- 1. Make sure MySQL Server is installed and running.
-- 2. Run this file to create the database:
--       mysql -u root -p < database.sql
-- 3. Update the DB_NAME / DB_USER / DB_PASSWORD in your
--    environment (or directly in vedic_astro/settings.py).
-- 4. Django will create all the required TABLES automatically
--    when you run:
--       python manage.py makemigrations
--       python manage.py migrate
--    You do NOT need to manually create tables — Django's ORM
--    migrations handle that. This script only prepares the
--    empty database + a dedicated MySQL user for the project.
-- ============================================================

CREATE DATABASE IF NOT EXISTS vedic_gajendra_sharma
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_unicode_ci;

-- Optional: create a dedicated MySQL user for this project
-- (Recommended instead of using root in production)
CREATE USER IF NOT EXISTS 'vedic_user'@'localhost' IDENTIFIED BY 'ChangeThisPassword123!';
GRANT ALL PRIVILEGES ON vedic_gajendra_sharma.* TO 'vedic_user'@'localhost';
FLUSH PRIVILEGES;

USE vedic_gajendra_sharma;

-- ============================================================
-- NOTE: All application tables (users, appointments, services,
-- blog posts, gallery images, reviews, FAQs, contact messages,
-- profiles, etc.) are created automatically by Django's
-- migration system based on the models defined in:
--    core/models.py
--    accounts/models.py
--    services/models.py
--    appointments/models.py
--    blog/models.py
--    gallery/models.py
--    reviews/models.py
--
-- Run the following after configuring settings.py:
--    python manage.py makemigrations
--    python manage.py migrate
--    python manage.py createsuperuser
--    python manage.py seed_data      (optional: loads demo data)
-- ============================================================
