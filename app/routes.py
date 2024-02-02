from flask import Flask, render_template, request, jsonify
from app import app

# 간단한 홈페이지 렌더링
@app.route('/')
def index():
    return {"members": [{ "id" : 1, "name" : "yerin" },
    					{ "id" : 2, "name" : "dalkong" }]}

# 채팅 API 엔드포인트
@app.route('/api/chat', methods=['POST'])
def chat():
    user_input = request.json['user_input']

    # 여기서 입력을 처리하고 채팅 로직을 구현
    # 예: 단순히 입력을 반대로 뒤집는 예제
    bot_output = 'not implemented'

    return jsonify({'bot_output': bot_output})