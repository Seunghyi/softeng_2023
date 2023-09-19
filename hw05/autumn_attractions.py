from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def title():
    return """
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewpoint">
    <title>전라도 가을 명소</title>
</head>
<body>
    <form method="GET" action="/city_name">
        <h1 style='color: white; background-color: orange; text-align: center'>전라도 가을 명소</h1>
        <p>다음 도시 중 궁금한 도시를 검색하세요: 정읍, 함평, 순천, 임실</p>
        <label>도시 이름: </label>
            <input type="text" name="city_name">
        <button type="submit">검색</button>
    </form>
</body>
</html>
    """

@app.route('/city_name')
def show_detail():
    city_name = request.args.get('city_name')
    city_info = {
        "정읍": {'name': '전라북도 정읍시',
                'img_url': 'https://search.pstatic.net/common?src=https%3A%2F%2Fsearch.pstatic.net%2Fcommon%2F%3Fsrc%3Dhttp%253A%252F%252Fblogfiles.naver.net%252FMjAyMjA5MjdfMTk5%252FMDAxNjY0Mjg3NjE5MTY2.rA0KJRclDvTfOQVrhwYXJBaiGdYr12sEa-cOZ98urmcg.BTfhRIEqfyXB60TTGq81yzap4VxE12i3R4r-_zvKXPAg.JPEG.sj1313579%252F%2525C1%2525A4%2525C0%2525BE_%2525B3%2525BB%2525C0%2525E5%2525BB%2525EA_%2525C5%2525C2%2525B1%2525B3-15.jpg%26type%3Dsc960_832&type=f1040_576_domesearch',
                'text': '정읍은 최고의 가을 풍경을 자부한다. 정읍의 내장산은 우리나라 제1의 단풍 관광지로 뽑힐 만큼 가을 대표 명소이다. '
                        '내장사 역시 가을이 아름다운 사찰로 손꼽히며, 옥정호 구절초 테마공원에 구절초 꽃이 피어나면 가을이 다가옴을 알리는 구절초 축제가 열린다.',
                'attraction': '내장산 국립공원케이블카, 내장산국립공원우화정, 정읍구절초지방정원, 정읍사문화공원'},
        "함평": {'name': '전라남도 함평군',
                'img_url': 'https://search.pstatic.net/common?src=https%3A%2F%2Fsearch.pstatic.net%2Fcommon%2F%3Fsrc%3Dhttp%253A%252F%252Fblogfiles.naver.net%252FMjAyMjEwMDZfMjc2%252FMDAxNjY1MDM5NTIyMzQ0.HKM7abeV4apzTYCKLK84dar108QgX-QuAkePaltxpdIg.ElC8fC5gBkc6UJXCxG-SeiWxoR_5gwTYGjRtNnmRPJwg.JPEG.greenjeonnam%252F9._20221002_122012.jpg%26type%3Dsc960_832&type=f1040_576_domesearch',
                'text': "함평군은 자연과 조화를 이룬 생태관광의 메카이다. 매년 5월에 열리는 '함평 나비 대축제'에서는 유채꽃 물결 사이로 날갯짓하는 나비들의 모습을 볼 수 있다. "
                        "공원 천지가 홍색 치마를 두른 듯한 장관이 펼쳐지는 용천사 꽃무릇공원은 관광객으로 하여금 탄성을 자아내게 만든다.",
                'attraction': '함평엑스포공원, 주포지구한옥전원마을, 꽃무릇공원, 돌머리해수욕장, 함평자연생태공원'},
        "순천": {"name": "전라남도 순천시",
                "img_url": 'https://search.pstatic.net/common?src=https%3A%2F%2Fsearch.pstatic.net%2Fcommon%2F%3Fsrc%3Dhttp%253A%252F%252Fpost.phinf.naver.net%252FMjAyMjA5MjBfMjA4%252FMDAxNjYzNjM3ODkwNzkw.ek1d3XbzbiTTkiM5ubEcdriaTCKCT_d3AiCg08Q0ncAg.iy1ZQqY75ZdJ67UtB7jI6dosjT4KZYYVIXGE7JNP5aYg.JPEG%252FITT2MmfeYOid2bG3bs4iXqN7vENI.jpg%26type%3Dsc960_832&type=f1040_576_domesearch',
                'text': "순천시는 살아숨쉬는 생태 수도라고 불린다. 세계 5대 습지이자 철새들의 도래지인 순천만 습지의 갈대밭은 매년 가을마다  더욱 몽환적인 모습으로 무장한다. "
                        "이를 보호하고자 만든 순천만 국가 정원에서는 다양한 생태 식물들을 관찰할 수 있어 또 다른 자연의 아름다움을 느낄 수 있다.",
                'attraction': "와온해변, 송광사, 순천드라마촬영장, 순천만습지, 순천만국가정원"},
        '임실': {'name': "전라북도 임실군",
                "img_url": 'https://search.pstatic.net/common?src=https%3A%2F%2Fpostfiles.pstatic.net%2FMjAyMzA5MDFfMTIy%2FMDAxNjkzNTUwMjE0NDc1.IfMmFRGo8nCLPP67aeoNE1MKopSgvj3OZOPSCGBLPk0g.QBoOKxevVvuyhLQe4pNJqTMtZO2UH12byMGK31iKyBQg.JPEG.kimcoco1%2F010.jpg%3Ftype%3Dw773&type=f1040_576_domesearch',
                'text': "임실은 한국 치즈의 발상지이다. 가장 대표적인 임실 치즈마을에서는 치즈 만들기와 초지 낙농체험이 가능하다. "
                        "직접 피자도 만들며 맛보는 재미에 아이와 함께 가족단위로 찾는 경우가 많다. 거대한 인공호수 옥정호는 새벽 물안개가 피어나는 풍경이 아름다워 출사지로 유명해졌다.",
                'attraction': "임실치즈테마파크, 옥정호 출렁다리, 임실치즈마을, 사선대, 국사봉전망대"}

    }

    if city_name == '정읍' or city_name == '함평' or city_name == '순천' or city_name == '임실':
        return (f"<h2>{city_info[city_name]['name']}</h2> <hr/>"
                f"<img src='{city_info[city_name]['img_url']}'>"
                f"<p>{city_info[city_name]['text']}</p>"
                f"<h3>명소: </h3> <p>{city_info[city_name]['attraction']}</p>"
                "<a href='/'>첫 화면으로 가기</a>")
    else:
        return ("<h4>아직 등록되지 않은 도시입니다.</h4>"
                "<a href='/'>첫 화면으로 가기</a>")

app.run(host="0.0.0.0")
