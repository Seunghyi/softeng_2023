# 팩토리얼 구하기: 재귀함수
def fact(num):
    result = 1
    for i in range(1, num+1):
        result *= i
    return result        


def main():
    print(f"10!은 {fact(10)}입니다.")


if __name__ == "__main__":
    main()

# chatGPT 사용하였습니다.
