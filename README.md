# Vendorमित्र

**Vendorमित्र** is a web-based platform built using **Python Flask** to empower **street vendors** in cities like **Lucknow** by giving them a digital identity, helping them register, connect with local customers, and access government schemes — all in one place.

---

## 🧾 Features

- 🧭 **Location Mapping** using OpenStreetMap (Leaflet.js)  
- 📝 **Easy Vendor Registration** with a simple form  
- 📍 **Vendor Directory with Editable Map View**  
- 🛠️ **Access to Government Schemes** (static information page)  
- 💬 **Customer Connect** to digitally list vendor presence  
- 🌐 Multilingual touch — supports both **Hindi and English**

---

## 🔧 Tech Stack

- **Frontend**: HTML, CSS, Bootstrap  
- **Backend**: Python (Flask)  
- **Database**: SQLite  
- **Map API**: OpenStreetMap via Leaflet.js  
- **Deployment Ready**: Structure compatible for Render or PythonAnywhere

---

## 📂 Folder Structure

VendorMitra/ ├── app.py ├── database.db ├── requirements.txt ├── templates/ │   ├── base.html │   ├── index.html │   ├── register.html │   ├── govt.html │   ├── map.html │   └── vendors.html ├── static/ │   ├── style.css │   └── images/ └── README.md

---

## How to Run

```bash
pip install -r requirements.txt
python app.py
