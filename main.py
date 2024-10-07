from flask import Flask, request, jsonify
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
import requests

app = Flask(__name__)
scheduler = BackgroundScheduler()
scheduler.start()

app = Flask(__name__)

@app.route('/set-times', methods=['POST'])
def set_times():
    data = request.json
    start_time = data['startTime']  # 上班打卡的日期時間 (ISO 8601)
    end_time = data['endTime']      # 下班打卡的日期時間 (ISO 8601)
    
    # 解析日期時間字符串
    start_time_dt = datetime.fromisoformat(start_time)
    end_time_dt = datetime.fromisoformat(end_time)
    return jsonify({"start_time_dt": start_time_dt,"end_time_dt": end_time_dt})

if __name__ == '__main__':
    app.run(debug=True)