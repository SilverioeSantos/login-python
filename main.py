import customtkinter as ctk

# Configuração aparência
ctk.set_default_color_theme("blue")

# Criação das funções de funcionalidades
def validar_login():
    usuario = entry_usuario.get()
    senha = entry_senha.get()
    
    # Validação simples de login
    if usuario == "LucasSilverio" and senha == "123456":
        resultado.configure(text="Login bem-sucedido!", text_color="green")
    else:
        resultado.configure(text="Usuário ou senha inválidos", text_color="red")

# Criação da janela principal
app = ctk.CTk()
app.title("Sistema de Login")
app.geometry("400x400")
app.resizable(False, False)

# Container principal
frame = ctk.CTkFrame(app, corner_radius=15)
frame.pack(pady=30, padx=30, fill="both", expand=True)

# Título da tela
titulo = ctk.CTkLabel(frame, text="Bem-vindo", font=("Arial", 20, "bold"))
titulo.pack(pady=20)

# Label e Entry para o usuário
label_usuario = ctk.CTkLabel(frame, text="Usuário:")
label_usuario.pack(pady=5)
entry_usuario = ctk.CTkEntry(frame, placeholder_text="Digite seu usuário", width=250)
entry_usuario.pack(pady=5)

# Label e Entry para a senha
label_senha = ctk.CTkLabel(frame, text="Senha:")
label_senha.pack(pady=5)
entry_senha = ctk.CTkEntry(frame, placeholder_text="Digite sua senha", show="*", width=250)
entry_senha.pack(pady=5)

# Botão de login
button_login = ctk.CTkButton(frame, text="Login", command=validar_login, width=250)
button_login.pack(pady=20)

# Campo feedback de login
resultado = ctk.CTkLabel(frame, text="", font=("Arial", 12))
resultado.pack(pady=10)

# Iniciar a aplicação
app.mainloop()