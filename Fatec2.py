import customtkinter as ctk
from Fatec import recomendacao_livro
ctk.set_appearance_mode("light")

class StoryBrookeApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("StoryBrooke")
        self.geometry("500x300")
        # Pergunta
        self.label_question = ctk.CTkLabel(self, text="StoryBrooke", font=ctk.CTkFont(size=20, weight="bold"))
        self.label_question.pack(pady=(20, 10))
        # Caixa de texto para o usuário digitar o livro
        self.entry_book = ctk.CTkEntry(self, width=350, font=ctk.CTkFont(size=16))
        self.entry_book.pack(pady=(0, 20))
        # Botão para mostrar resultado
        self.btn_show = ctk.CTkButton(self, text="Mostrar resultado", fg_color="#b5865b", hover_color="#cf9967", command=self.show_result)
        self.btn_show.pack(pady=(0, 15))
        # Caixa de texto para mostrar o resultado (multi-line)
        # self.text_result = ctk.CTkTextbox(self, width=400, height=100, font=ctk.CTkFont(size=14))
        # self.text_result.pack(pady=(0, 20))
        

    def show_result(self):
                        # Frame para a tabela
        self.table_frame = ctk.CTkFrame(self)
        self.table_frame.pack(pady=(10,20), padx=80, fill="both", expand=True)
        # Tabela: 4 colunas de cabeçalho
        columns = ["Livro", "Editora", "Autor(a)", "Similaridade"]
        self.headers = []
        for i, col_name in enumerate(columns):
            header = ctk.CTkLabel(self.table_frame, text=col_name, width=140, height=25,
                                  fg_color="white", corner_radius=6, font=ctk.CTkFont(size=14, weight="bold"))
            header.grid(row=0, column=i, padx=5, pady=5, sticky="nsew")
            self.headers.append(header)
        # Adicionando linhas em branco inicialmente (exemplo: 5 linhas)
        self.rows = []
        similar = recomendacao_livro(book)
        for _, row in similar.head(10):
            row_items = []
            for col in range(4):
                cell = ctk.CTkLabel(self.table_frame, text="", width=140, height=25,
                                    fg_color="#b5865b", corner_radius=6, font=ctk.CTkFont(size=13))
                cell.grid(row=row, column=col, padx=5, pady=3, sticky="nsew")
                row_items.append(cell)
            self.rows.append(row_items)
        # Configuração para que as colunas se expandam igualmente
        for col in range(4):
            self.table_frame.grid_columnconfigure(col, weight=1)
        # Limpar o conteúdo anterior
        # Mostrar o texto na caixa de resultado
        similar = recomendacao_livro(book)
        # print(f"\n🔍 Livros mais semelhantes a: '{titles[idx]}'\n")
        print(similar.head(10).to_string(index=False))
        self.text_result.insert("0.0", similar.head(10).to_string(index=False))
if __name__ == "__main__":
    app = StoryBrookeApp()
    app.mainloop()