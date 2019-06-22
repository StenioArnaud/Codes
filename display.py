import tkinter as tk
from tkinter import ttk

# Variáveis
Fonte_grande = ("Verdana", 12)
width = 800
height = 500
center = 2


class Inicio(tk.Tk):  # Main Class
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # Configurações da janela.
        tk.Tk.wm_title(self, "Filtro")
        tk.Tk.wm_geometry(self, "500x500+10+10")
        tk.Tk.update_idletasks(self)
        x = (tk.Tk.winfo_screenwidth(self) // center) - (width // center)
        y = (tk.Tk.winfo_screenheight(self) // center) - (height // center)
        tk.Tk.geometry(self, '{}x{}+{}+{}'.format(width, height, x, y))

        # Frame principal
        teste = tk.Frame(self)
        teste.pack(side="top", fill="both", expand=True)
        teste.grid_rowconfigure(0, weight=1)
        teste.grid_columnconfigure(0, weight=1)

        self.frames = {}

        # Lista de telas
        for F in (StartPage, PageOne, PageTwo):
            frame = F(teste, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    # Atualizador dos frames
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):  # frame inicial
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Página inicial", font=Fonte_grande)
        label.pack(pady=10, padx=10)

        btn = ttk.Button(self, text="Filtros",
                        command=lambda: controller.show_frame(PageOne))
        btn.pack()
        btn2 = ttk.Button(self, text="Nomes",
                        command=lambda: controller.show_frame(PageTwo))
        btn2.pack()


class PageOne(tk.Frame):  # Frame primeira pagina
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Filtros", font=Fonte_grande)
        label.pack(pady=10, padx=10)

        btn = ttk.Button(self, text="Ir para PageTwo",
                        command=lambda: controller.show_frame(PageTwo))
        btn.pack()

        btn2 = ttk.Button(self, text="Voltar ao inicio",
                        command=lambda: controller.show_frame(StartPage))
        btn2.pack()


class PageTwo(tk.Frame):  # frame segunda pagina
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="nomes", font=Fonte_grande)
        label.pack(pady=10, padx=10)

        btn = ttk.Button(self, text="Ir para PageOne",
                        command=lambda: controller.show_frame(PageOne))
        btn.pack()

        btn2 = ttk.Button(self, text="Voltar ao inicio",
                        command=lambda: controller.show_frame(StartPage))
        btn2.pack()


# Inicialização
Programa = Inicio()
Programa.mainloop()
