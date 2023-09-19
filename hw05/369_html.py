from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def title():
    return """
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewpoint">
    <title>Flask Home Page</title>
</head>
<body>
    <form method="GET" action="/369">
        <h1 style='color: white; background-color: pink; text-align: center'>369 GAME</h1> <hr/>
        <p>숫자를 입력하면 그 숫자까지의 369 게임을 보여준다. 박수 횟수에 맞게 -가 출력된다.</p>
        <label>숫자 입력: </label>
            <input type="text" name="N">
        <button type="submit">출력</button>
    </form>
</body>
</html>
    """

@app.route('/369')
def game():
    N = int(request.args.get('N'))
    resp = ""
    resp += "<html>\n"
    resp += '<meta charset = "UTF-8">'
    resp += "<body>\n"
    resp += f"<h2>{N}까지 369 게임</h2>\n"
    resp += "<div>\n"
    result = []
    for num in range(1, N + 1):
        num_str = str(num)
        cnt = num_str.count('3') + num_str.count('6') + num_str.count('9')
        if cnt > 0:
            result.append('-' * cnt)
        else:
            result.append(str(num))

    resp = ' '.join(result)

    resp += "</div>\n"
    resp += "</body>\n"
    resp += "</html>\n"

    return resp

app.run(host="0.0.0.0")
