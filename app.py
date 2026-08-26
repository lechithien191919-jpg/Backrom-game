from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# API tạm thời khi chưa có database
@app.route('/save_score', methods=['POST'])
def save_score():
    data = request.json
    username = data.get('username')
    score = data.get('score')
    print(f"Nhận được điểm từ {username}: {score}s")
    return jsonify({"status": "success", "message": "Đã nhận điểm (chưa lưu db)!"})

if __name__ == '__main__':
    app.run(debug=True)
    
