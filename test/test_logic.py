"""Testes para o módulo de lógica de credenciais."""

import sys
import os
from logic import validar_credenciais
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))



def test_login_correto():
    """Teste de login com usuário e senha corretos."""
    assert validar_credenciais("LucasSilverio", "123456")

def test_login_usuario_incorreto():
    """Teste de login com usuário incorreto."""
    assert not validar_credenciais("OutroUsuario", "123456")

def test_login_senha_incorreta():
    """Teste de login com senha incorreta."""
    assert not validar_credenciais("LucasSilverio", "senhaErrada")

def test_login_ambos_incorretos():
    """Teste de login com usuário e senha incorretos."""
    assert not validar_credenciais("user", "123")

def test_login_campos_vazios():
    """Teste de login com campos vazios."""
    assert not validar_credenciais("", "")
