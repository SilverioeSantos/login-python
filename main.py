import customtkinter as ctk

# Configuração aparência
ctk.set_appearance_mode("dark")

# Estilização do tema

# Criação da janela principal
app = ctk.CTk()
app.title("Sistema de Login")
app.geometry("400x300")

# Criação dos campos
label_usuario = ctk.CTkLabel(app, text="Usuário")
label_usuario.pack(pady=10)
entry_usuario = ctk.CTkEntry(app, placeholder_text="Digite seu usuário")
entry_usuario.pack(pady=10)

label_senha = ctk.CTkLabel(app, text="Senha")
label_senha.pack(pady=10)
entry_senha = ctk.CTkEntry(app, placeholder_text="Digite sua senha")
entry_senha.pack(pady=10)

button_login = ctk.CTkButton(app, text="Login")

# Criação das funções de funcionalidades

# Iniciar a aplicação
app.mainloop()