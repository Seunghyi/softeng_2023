# 팩토리얼 구하기: 재귀함수
import tkinter as tk
from tkinter import simpledialog

ROOT = tk.Tk()


def simple_gui_input(text='값을 입력하세요.'):
    return simpledialog.askstring(title="!",
                                  prompt=text)

def fact(num):
    if num == 1:
        return 1
    # result = 1
    # for i in range(1, num+1):
    #    result *= i         # result = result * i
    # return result        
    return num * fact(num - 1)


def main():
    a = int(simple_gui_input())
    print(f"{a}!은 {fact(a)}입니다.")


if __name__ == "__main__":
    main()
