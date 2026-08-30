import sqlite3
import os
from datetime import datetime

db_path = os.path.join(os.path.dirname(__file__), 'db.sqlite3')
if not os.path.exists(db_path):
    print("db.sqlite3 not found!")
    exit(1)

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# 1. Update Vastu Shanti price to 0 (remove price)
cursor.execute("UPDATE services_service SET price = 0 WHERE slug = 'vastu-shanti' OR title LIKE '%Vastu%'")
print(f"Updated Vastu Shanti price to 0 (rows affected: {cursor.rowcount})")

# 2. Add or update Kaal Sarp Dosh Shanti Puja (Price: 3100)
cursor.execute("SELECT id FROM services_service WHERE slug = 'kaal-sarp-dosh-puja'")
row = cursor.fetchone()
if row:
    cursor.execute("""
        UPDATE services_service 
        SET price = 3100, title = 'Kaal Sarp Dosh Shanti Puja', is_active = 1
        WHERE id = ?
    """, (row[0],))
    print("Updated existing Kaal Sarp Dosh Puja")
else:
    cursor.execute("""
        INSERT INTO services_service (title, slug, short_description, description, icon, price, is_active, "order", created_at)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        'Kaal Sarp Dosh Shanti Puja',
        'kaal-sarp-dosh-puja',
        'Vedic rituals and anushthan for complete Kaal Sarp Dosh Nivaran.',
        'Authentic Kaal Sarp Dosh Shanti Puja performed according to Vedic scriptures with complete mantras, havan, and anushthan to remove obstacles, bring peace, prosperity, and spiritual growth.',
        'fa-solid fa-fire',
        3100.0,
        1,
        1,
        now
    ))
    print("Inserted Kaal Sarp Dosh Shanti Puja")

# 3. Add or update Mangal Bhat Puja (Price: 3100)
cursor.execute("SELECT id FROM services_service WHERE slug = 'mangal-puja'")
row = cursor.fetchone()
if row:
    cursor.execute("""
        UPDATE services_service 
        SET price = 3100, title = 'Mangal Bhat Puja', is_active = 1
        WHERE id = ?
    """, (row[0],))
    print("Updated existing Mangal Bhat Puja")
else:
    cursor.execute("""
        INSERT INTO services_service (title, slug, short_description, description, icon, price, is_active, "order", created_at)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        'Mangal Bhat Puja',
        'mangal-puja',
        'Sacred Mangal Bhat Puja & Manglik Dosh Shanti Anushthan.',
        'Special Vedic Mangal Bhat Puja and Manglik Dosh Nivaran Vidhi performed to resolve marriage delays, relationship harmony, career obstacles, and planetary afflictions of Mars.',
        'fa-solid fa-fire',
        3100.0,
        1,
        2,
        now
    ))
    print("Inserted Mangal Bhat Puja")

conn.commit()

# Print current active services
print("\n--- All Active Services ---")
cursor.execute("SELECT id, title, price, slug FROM services_service WHERE is_active = 1 ORDER BY id")
for s in cursor.fetchall():
    print(f"ID: {s[0]} | Title: {s[1]} | Price: ₹{s[2]} | Slug: {s[3]}")

conn.close()
