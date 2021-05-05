from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/healthz", methods=["GET"])
def healthCheck():
    return "", 200


# TODO(everyone): GET 메소드로 더하기, 빼기, 곱하기, 나누기 함수 라우트 완성하기


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='80', debug=True)
