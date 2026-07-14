import tkinter as tk
from tkinter import messagebox

from gui.window import MainWindow


def main():
    #Запуск приложения.

    root = tk.Tk()

    # Создаем главное окно
    app = MainWindow(root)

    # Запускаем цикл обработки событий
    root.mainloop()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Приложение остановлено пользователем.")
    except Exception as error:
        messagebox.showerror(
            title="Ошибка",
            message=f"Произошла непредвиденная ошибка:\n\n{error}"
        )
