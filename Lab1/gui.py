import tkinter as tk
from tkinter import font
from logic import *


class CalculatorGUI:
    def __init__(self, root):
        self.root = root
        self.custom_font = font.Font(size=14)
        self.frame = tk.Frame(root)
        self.frame.grid(row=0, column=0)
        root.geometry("400x500")
        root.title("Calculator")

        # Поле ввода
        self.input_entry = tk.Entry(self.frame, width=32,
                                    font=self.custom_font,
                                    bd=7,
                                    relief=tk.SUNKEN)
        self.input_entry.grid(row=0, column=0, columnspan=4,
                              padx=10, pady=10, sticky="nsew")

        # Настройка стилей кнопок
        self.button_style = {"font": self.custom_font, "width": 5,
                             "height": 2, "borderwidth": 5,
                             "relief": tk.RAISED}

        buttons = [
            '+', 'C', '+',
            '-', 'Info', '-',
            '0', '<-', '=',
        ]
        row, col = 1, 0
        for button in buttons:
            if button == '<-':
                tk.Button(self.frame, text=button,
                          command=self.delete_last_character,
                          **self.button_style).grid(row=row, column=col,
                                                    padx=5, pady=5,
                                                    sticky="nsew")
            elif button == 'Info':
                tk.Button(self.frame, text=button, command=self.show_info,
                          **self.button_style).grid(row=row, column=col,
                                                    padx=5, pady=5,
                                                    sticky="nsew")
            else:
                tk.Button(self.frame, text=button,
                          command=lambda b=button: self.click(b),
                          **self.button_style).grid(row=row, column=col,
                                                    padx=5, pady=5,
                                                    sticky="nsew")
            col += 1
            if col > 2:
                col = 0
                row += 1

    def click(self, button):
        if button == '=':
            try:
                result = self.calculate()
                self.input_entry.delete(0, tk.END)
                self.input_entry.insert(tk.END, result)
            except Exception as e:
                self.input_entry.delete(0, tk.END)
                self.input_entry.insert(tk.END, f"Ошибка {e}")
        elif button == 'C':
            self.input_entry.delete(0, tk.END)
        else:
            self.input_entry.insert(tk.END, button)

    def calculate(self):
        expression = self.input_entry.get()
        if '+' in expression:
            num1, num2 = expression.split('+')
            if is_valid_sym_ternary(num1.strip(), num2.strip()):
                result = add_sym_ternary(num1.strip(), num2.strip())
            else:
                result = None
        elif '-' in expression:
            num1, num2 = expression.split('-')
            if is_valid_sym_ternary(num1.strip(), num2.strip()):
                result = sub_sym_ternary(num1.strip(), num2.strip())
            else:
                result = None

        # Возвращаем результат или сообщение об ошибке
        if result is not None:
            return result
        else:
            return "Ошибка: Число нельзя перевести в 4 систему счисления"

    def delete_last_character(self):
        current_text = self.input_entry.get()
        if current_text:
            updated_text = current_text[:-1]
            self.input_entry.delete(0, tk.END)
            self.input_entry.insert(tk.END, updated_text)

    def show_info(self):
        info = """
        Это калькулятор для работы с вещественными числами
        в четверичной системе счисления.
        Он позволяет выполнять операции сложения и вычитания над числами,
        представленными в четверичной системе.
        Автор: Костяева Екатерина ИУ7-23Б
        """

        info_window = tk.Toplevel(self.root)
        info_window.title("Информация о приложении")

        label = tk.Label(info_window, text=info, font=self.custom_font)
        label.pack(padx=10, pady=10)


def main():
    root = tk.Tk()
    CalculatorGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
