""" 
main.py: Módulo principal da aplicação que gerencia a interface gráfica.
"""

import customtkinter as ctk
from logic import validar_credenciais  # Importa a função de validação


# Configuração aparência
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

# Função que conecta a interface com a lógica de login
def validar_login():
    """Valida o login do usuário usando a lógica separada."""
    usuario = entry_usuario.get()
    senha = entry_senha.get()
    if validar_credenciais(usuario, senha):
        resultado.configure(text="Login bem-sucedido!", text_color="#32CD32")
    else:
        resultado.configure(text="Usuário ou senha inválidos", text_color="#FF4500")

# Criação da janela principal
app = ctk.CTk()
app.title(" Sistema de Login ")
app.geometry("450x500")
app.resizable(False, False)
app.configure(bg="#1E1E1E")

# Container principal
frame = ctk.CTkFrame(app, corner_radius=20, fg_color="#2C2F33")
frame.pack(pady=40, padx=40, fill="both", expand=True)

# Título da tela
titulo = ctk.CTkLabel(frame, text="Bem-vindo ao Sistema!",
                      font=("Arial", 22, "bold"),
                      text_color="#00BFFF")
titulo.pack(pady=20)

# Label e Entry para o usuário
label_usuario = ctk.CTkLabel(frame, text="Usuário:",
                             font=("Arial", 14, "bold"), text_color="white")
label_usuario.pack(pady=5)
entry_usuario = ctk.CTkEntry(frame, placeholder_text="Digite seu usuário",
                             width=280, height=35, fg_color="#3A3F44", text_color="white")
entry_usuario.pack(pady=5)

# Label e Entry para a senha
label_senha = ctk.CTkLabel(frame, text="Senha:", font=("Arial", 14, "bold"), text_color="white")
label_senha.pack(pady=5)
entry_senha = ctk.CTkEntry(frame, placeholder_text="Digite sua senha",
                           show="*",
                           width=280,
                           height=35,
                           fg_color="#3A3F44",
                           text_color="white")
entry_senha.pack(pady=5)

# Botão de login
button_login = ctk.CTkButton(frame, text="Entrar",
                             command=validar_login,
                             width=280, height=40,
                             fg_color="#00BFFF",
                             hover_color="#1E90FF",
                             font=("Arial", 14, "bold"))
button_login.pack(pady=20)

# Campo feedback de login
resultado = ctk.CTkLabel(frame, text="", font=("Arial", 14, "bold"))
resultado.pack(pady=10)

# Iniciar a aplicação
app.mainloop()

# Autor: Lucas Silverio
