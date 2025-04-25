from flask import Flask, request, Response
import requests

app = Flask(__name__)

# ngrokで公開されたURLをここに入れる
TARGET_URL = "https://your-ngrok-url.ngrok.io"

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>', methods=['GET', 'POST'])
def proxy(path):
    url = f"{TARGET_URL}/{path}"
    
    # リクエストをそのまま転送
    if request.method == 'POST':
        resp = requests.post(url, data=request.form)
    else:
        resp = requests.get(url, params=request.args)

    # レスポンスもそのまま返す
    return Response(resp.content, status=resp.status_code, headers=dict(resp.headers))

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
