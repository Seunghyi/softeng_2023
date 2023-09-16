from flask import Flask

app = Flask(__name__)

@app.route('/')
def title():
    return ("<h1 style='color: white; background-color: black; text-align: center'>전라도 가을 명소</h1> "
            "<nav style='color: black; background-color: orange; font-size: 150%; text-align: center'>"
            "<a href='/Jeongeup'>정읍</a> <a href='/Hampyeong'>함평</a> "
            "<a href='/Suncheon'>순천</a> <a href='/Imsil'>임실</a></nav>")

@app.route('/Jeongeup')
def Jeongeup():
    return ("<h2>전라북도 정읍시</h2> <hr/>"
            "<img src='https://search.pstatic.net/common?src=https%3A%2F%2Fsearch.pstatic.net%2Fcommon%2F%3Fsrc%3Dhttp%253A%252F%252Fblogfiles.naver.net%252FMjAyMjA5MjdfMTk5%252FMDAxNjY0Mjg3NjE5MTY2.rA0KJRclDvTfOQVrhwYXJBaiGdYr12sEa-cOZ98urmcg.BTfhRIEqfyXB60TTGq81yzap4VxE12i3R4r-_zvKXPAg.JPEG.sj1313579%252F%2525C1%2525A4%2525C0%2525BE_%2525B3%2525BB%2525C0%2525E5%2525BB%2525EA_%2525C5%2525C2%2525B1%2525B3-15.jpg%26type%3Dsc960_832&type=f1040_576_domesearch'>"
            "<p>정읍은 최고의 가을 풍경을 자부한다. 정읍의 내장산은 우리나라 제1의 단풍 관광지로 뽑힐 만큼 가을 대표 명소이다.</p>"
            "<p>내장사 역시 가을이 아름다운 사찰로 손꼽히며, 옥정호 구절초 테마공원에 구절초 꽃이 피어나면 가을이 다가옴을 알리는 구절초 축제가 열린다.</p>"
            "<h4>정읍 명소</h4> <p>내장산 국립공원케이블카, 내장산국립공원우화정, 정읍구절초지방정원, 정읍사문화공원</p>"
            "<a href='/'>첫 화면으로 가기</a>")

@app.route('/Hampyeong')
def Hampyeong():
    return ("<h2>전라남도 함평군</h2> <hr/>"
            "<img src='https://search.pstatic.net/common?src=https%3A%2F%2Fsearch.pstatic.net%2Fcommon%2F%3Fsrc%3Dhttp%253A%252F%252Fblogfiles.naver.net%252FMjAyMjEwMDZfMjc2%252FMDAxNjY1MDM5NTIyMzQ0.HKM7abeV4apzTYCKLK84dar108QgX-QuAkePaltxpdIg.ElC8fC5gBkc6UJXCxG-SeiWxoR_5gwTYGjRtNnmRPJwg.JPEG.greenjeonnam%252F9._20221002_122012.jpg%26type%3Dsc960_832&type=f1040_576_domesearch'>"
            "<p>함평군은 자연과 조화를 이룬 생태관광의 메카이다. 매년 5월에 열리는 '함평 나비 대축제'에서는 유채꽃 물결 사이로 날갯짓하는 나비들의 모습을 볼 수 있다.</p>"
            "<p>공원 천지가 홍색 치마를 두른 듯한 장관이 펼쳐지는 용천사 꽃무릇공원은 관광객으로 하여금 탄성을 자아내게 만든다.</p>"
            "<h4>함평 명소</h4> <p>함평엑스포공원, 주포지구한옥전원마을, 꽃무릇공원, 돌머리해수욕장, 함평자연생태공원</p>"
            "<a href='/'>첫 화면으로 가기</a>")

@app.route('/Suncheon')
def Suncheon():
    return("<h2>전라남도 순천시</h2> <hr/>"
           "<img src='https://search.pstatic.net/common?src=https%3A%2F%2Fsearch.pstatic.net%2Fcommon%2F%3Fsrc%3Dhttp%253A%252F%252Fpost.phinf.naver.net%252FMjAyMjA5MjBfMjA4%252FMDAxNjYzNjM3ODkwNzkw.ek1d3XbzbiTTkiM5ubEcdriaTCKCT_d3AiCg08Q0ncAg.iy1ZQqY75ZdJ67UtB7jI6dosjT4KZYYVIXGE7JNP5aYg.JPEG%252FITT2MmfeYOid2bG3bs4iXqN7vENI.jpg%26type%3Dsc960_832&type=f1040_576_domesearch'>"
           "<p>순천시는 살아숨쉬는 생태 수도라고 불린다. 세계 5대 습지이자 철새들의 도래지인 순천만 습지의 갈대밭은 매년 가을마다  더욱 몽환적인 모습으로 무장한다.</p>"
           "<p>이를 보호하고자 만든 순천만 국가 정원에서는 다양한 생태 식물들을 관찰할 수 있어 또 다른 자연의 아름다움을 느낄 수 있다.</p>"
           "<h4>순천 명소</h4> <p>와온해변, 송광사, 순천드라마촬영장, 순천만습지, 순천만국가정원</p>"
           "<a href='/'>첫 화면으로 가기</a>")

@app.route('/Imsil')
def Imsil():
    return("<h2>전라북도 임실군</h2> <hr/>"
           "<img src='https://search.pstatic.net/common?src=https%3A%2F%2Fpostfiles.pstatic.net%2FMjAyMzA5MDFfMTIy%2FMDAxNjkzNTUwMjE0NDc1.IfMmFRGo8nCLPP67aeoNE1MKopSgvj3OZOPSCGBLPk0g.QBoOKxevVvuyhLQe4pNJqTMtZO2UH12byMGK31iKyBQg.JPEG.kimcoco1%2F010.jpg%3Ftype%3Dw773&type=f1040_576_domesearch'>"
           "<p>임실은 한국 치즈의 발상지이다. 가장 대표적인 임실 치즈마을에서는 치즈 만들기와 초지 낙농체험이 가능하다.</p>"
           "<p>직접 피자도 만들며 맛보는 재미에 아이와 함께 가족단위로 찾는 경우가 많다. 거대한 인공호수 옥정호는 새벽 물안개가 피어나는 풍경이 아름다워 출사지로 유명해졌다.</p>"
           "<h4>임실 명소</h4> <p>임실치즈테마파크, 옥정호 출렁다리, 임실치즈마을, 사선대, 국사봉전망대</p>"
           "<a href='/'>첫 화면으로 가기</a>")


app.run(host="0.0.0.0")