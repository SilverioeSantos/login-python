import customtkinter as ctk

# Configuração aparência
ctk.set_appearance_mode("dark")

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
app.geometry("400x300")

# Criação dos campos
# Label e Entry para o usuário
label_usuario = ctk.CTkLabel(app, text="Usuário")
label_usuario.pack(pady=10)
entry_usuario = ctk.CTkEntry(app, placeholder_text="Digite seu usuário")
entry_usuario.pack(pady=10)

# Label e Entry para a senha
label_senha = ctk.CTkLabel(app, text="Senha")
label_senha.pack(pady=10)
entry_senha = ctk.CTkEntry(app, placeholder_text="Digite sua senha")
entry_senha.pack(pady=10)

# Button para login
button_login = ctk.CTkButton(app, text="Login", command=validar_login)
button_login.pack(pady=20)

# Campo feedback de login
resultado = ctk.CTkLabel(app, text="")
resultado.pack(pady=10)

# Iniciar a aplicação
app.mainloop()