# 홀짝 구분하기: 나머지 연산, 조건문
import tkinter as tk
from tkinter import simpledialog

ROOT = tk.Tk()

def simple_gui_input(text='값을 입력하세요.'):
    return simpledialog.askstring(title="GUI 창",
                                  prompt=text)

def main():
    number = int(simple_gui_input())
    if number % 2 == 0:
        if number % 10 in [2,4,5,9]:
            print(f'{number}는 짝수입니다.')
        else:
            print(f'{number}은 짝수입니다.')
    else:
        if number % 10 in [2,4,5,9]:
            print(f'{number}는 홀수입니다.')
        else:
            print(f'{number}은 홀수입니다.')

if __name__ == "__main__":
    main()
