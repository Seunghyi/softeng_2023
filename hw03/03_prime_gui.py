# 소수 판별하기: 함수, 조건문(break 등)
import tkinter as tk
from tkinter import simpledialog

ROOT = tk.Tk()


def simple_gui_input(text='값을 입력하세요.'):
    return simpledialog.askstring(title="GUI 창",
                                  prompt=text)

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):         # for () in ()
        if num % i == 0:
            return False
    return True


def main():
    num = int(simple_gui_input())

    if is_prime(num):
        print(f"{num}은/는 소수입니다.")
    else:
        print(f"{num}은/는 소수가 아닙니다.")


if __name__ == "__main__":
    main()
