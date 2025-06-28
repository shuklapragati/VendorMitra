from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS vendors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    phone TEXT,
    category TEXT,
    location TEXT,
    location_lat TEXT,
    location_lng TEXT
    )''')
    conn.commit()
    conn.close()
init_db()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        category = request.form['category']
        location = request.form['location']
        location_lat = request.form['location_lat']
        location_lng = request.form['location_lng']

        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute("INSERT INTO vendors (name, phone, category, location, location_lat, location_lng) VALUES (?, ?, ?, ?, ?, ?)", 
                  (name, phone, category, location, location_lat, location_lng))
        conn.commit()
        conn.close()
        return redirect('/')
    return render_template('register.html')

@app.route('/map')
def map_page():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT name, phone, location_lat, location_lng FROM vendors WHERE location_lat IS NOT NULL AND location_lng IS NOT NULL")
    vendors = c.fetchall()
    conn.close()
    return render_template('map.html', vendors=vendors)

@app.route('/govt')
def govt_scheme():
    return render_template ('govt.html')  

@app.route('/vendors')
def show_vendors():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT name, phone, category, location, location_lat, location_lng, id FROM vendors")
    vendors = c.fetchall()
    conn.close()
    return render_template('vendors.html', vendors=vendors)

@app.route('/delete_vendor/<int:id>', methods=['POST'])
def delete_vendor(id):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("DELETE FROM vendors WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    return redirect('/vendors')          

if __name__ == '__main__':
    app.run(debug=True)