from flask import Flask, request, Response
import requests
import os

app = Flask(__name__)

# NgrokのURL（テスト用）
TARGET_URL = "https://your-ngrok-url.ngrok.io"

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>', methods=['GET', 'POST'])
def proxy(path):
    url = f"{TARGET_URL}/{path}"

    try:
        if request.method == 'POST':
            resp = requests.post(url, data=request.form)
        else:
            resp = requests.get(url, params=request.args)

        return Response(resp.content, status=resp.status_code, headers=dict(resp.headers))
    except Exception as e:
        return f"Error: {e}", 500

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # ← ここ重要！
    app.run(host="0.0.0.0", port=port)
