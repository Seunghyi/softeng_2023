#  단위변환(온도, 길이 등): 함수, 포맷팅
def f2c(temp_f):
    return (temp_f - 32) / 1.8

def main():
    temp_f = 80
    temp_c = f2c(temp_f)
    print(f'{temp_f}F -> {temp_c}℃')

if __name__ == "__main__":
    main()
