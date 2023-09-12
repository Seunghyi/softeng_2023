# 소수 구하기: 함수, 반복문
import tkinter as tk
from tkinter import simpledialog

ROOT = tk.Tk()


def simple_gui_input(text='값을 입력하세요.'):
    return simpledialog.askstring(title="primelist",
                                  prompt=text)

def is_prime(num):

    if num >= 1 and num <= 3:
        return True
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
            else:
                return True



def main():
    a = int(simple_gui_input())
    list_prime = [x for x in range(1, a+1) if is_prime(x)]
    print(f"1-{a}까지 중 소수는 {list_prime}입니다.")
    print(f"1-{a}까지 중 소수의 갯수는 {len(list_prime)}입니다.")


if __name__ == "__main__":
    main()
