# 1-100까지 짝수의 합 구하기: 반복문, 조건문, 지능형 리스트, 수학함수
import tkinter as tk
from tkinter import simpledialog

ROOT = tk.Tk()


def simple_gui_input(text='값을 입력하세요.'):
    return simpledialog.askstring(title="GUI 창",
                                  prompt=text)

def is_even(a):
    return a % 2 == 0

def main():
    a = int(simple_gui_input())
    evens = [x for x in range(1, a+1) if is_even(x)]        # 지능형 리스트: [x for x in ()]
    sum_even = sum(evens)

    print(f"1-{a}까지 숫자 중 짝수의 합은 {sum_even}입니다.")

if __name__ == "__main__":
    main()
