# 소수 판별하기: 함수, 조건문(break 등)
def is_prime(num):
    
    for i in range(2, num):
        if num % i == 0:
            return False
        else:
            return True

def main():
    num = 7

    if is_prime(num):
        print(f"{num}은/는 소수입니다.")
    else:
        print(f"{num}은/는 소수가 아닙니다.")


if __name__ == "__main__":
    main()

# chatGPT 사용하였습니다.
