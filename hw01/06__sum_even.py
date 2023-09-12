# 1-100까지 짝수의 합 구하기: 반복문, 조건문, 지능형 리스트, 수학함수
def is_even(a):
    return a % 2 == 0

def main():
    evens = [x for x in range(1, 101) if is_even(x)]
    sum_even = sum(evens)

    print(f"1-100까지 숫자 중 짝수의 합은 {sum_even}입니다.")

if __name__ == "__main__":
    main()
