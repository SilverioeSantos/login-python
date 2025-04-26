# test.py
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from logic import validar_credenciais

def test_login_correto():
    assert validar_credenciais("LucasSilverio", "123456") == True

def test_login_usuario_incorreto():
    assert validar_credenciais("OutroUsuario", "123456") == False

def test_login_senha_incorreta():
    assert validar_credenciais("LucasSilverio", "senhaErrada") == False

def test_login_ambos_incorretos():
    assert validar_credenciais("user", "123") == False

def test_login_campos_vazios():
    assert validar_credenciais("", "") == False