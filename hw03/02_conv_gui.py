#  단위변환(온도, 길이 등): 함수, 포맷팅
import tkinter as tk
from tkinter import simpledialog

ROOT = tk.Tk()


def simple_gui_input(text='온도(F)를 입력하세요.'):
    return simpledialog.askstring(title="F -> ℃",
                                  prompt=text)

def f2c(temp_f):
    return (temp_f - 32) / 1.8

def main():
    temp_f = int(simple_gui_input())
    temp_c = f2c(temp_f)
    print(f'{temp_f}F -> {temp_c:.2f}℃')

if __name__ == "__main__":
    main()
