from tkinter.ttk import Frame, Label, Entry, Button, Treeview


class ApplicationUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Упрощённый метод Ньютона")

        input_frame = Frame(root, padding="10")
        input_frame.grid(row=0, column=0)

        Label(input_frame, text="Функция f(x): ").grid(row=0, column=0, stick='w')
        self.function_entry = Entry(input_frame, width=40)
        self.function_entry.grid(row=0, column=1, pady=4, stick='w')

        Label(input_frame, text="Начало отрезка (а): ").grid(row=1, column=0, stick='w')
        self.start_entry = Entry(input_frame)
        self.start_entry.grid(row=1, column=1, pady=4, stick='w')

        Label(input_frame, text="Конец отрезка (b): ").grid(row=2, column=0, stick='w')
        self.end_entry = Entry(input_frame)
        self.end_entry.grid(row=2, column=1, pady=4, stick='w')

        Label(input_frame, text="Точность (ε): ").grid(row=3, column=0, stick='w')
        self.eps_entry = Entry(input_frame)
        self.eps_entry.grid(row=3, column=1, pady=4, stick='w')

        Label(input_frame, text="Максимальное число итераций (Nmax): ").grid(row=4, column=0, stick='w')
        self.max_iter_entry = Entry(input_frame)
        self.max_iter_entry.grid(row=4, column=1, pady=4, stick='w')

        Label(input_frame, text="Шаг деления отрезка (h): ").grid(row=5, column=0, stick='w')
        self.n_max_entry = Entry(input_frame)
        self.n_max_entry.grid(row=5, column=1, pady=4, stick='w')

        Button(input_frame, text="Рассчитать", command=self.solve).grid(row=6, column=0, columnspan=2, pady=4)

        self.results_table = Treeview(root, columns=("n", "interval", "x", "fx", "iter_count", "error"), show='headings')
        self.results_table.grid(row=1, column=0, pady=4)

        self.results_table.heading("n", text="№ корня")
        self.results_table.heading("interval", text="[xi; xi+1]")
        self.results_table.heading("x", text="x'")
        self.results_table.heading("fx", text="f(x')")
        self.results_table.heading("iter_count", text="Кол-во итер")
        self.results_table.heading("error", text="Код ошибки")


    def solve(self):
        pass




