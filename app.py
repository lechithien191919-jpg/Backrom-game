from flask import Flask, render_template
app = Flask(__name__, template_folder='.') # Cho phép đọc file html ngay tại thư mục hiện tại luôn

@app.route('/')
def home():
    return render_template('index.html')
    
