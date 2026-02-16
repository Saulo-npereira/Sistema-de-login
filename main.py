import hashlib
import os
import sqlite3

conexao = sqlite3.connect('usuarios.db')
cursor = conexao.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS usuario (
               nome VARCHAR(100),
               email VARCHAR(100) PRIMARY KEY,
               senha VARCHAR(100)
               )''')
while True:
    print("""
    1 - Cadastrar usuário
    2 - Listar seu usuário
    3 - Login
    4 - Deletar Usuário
    5 - Alterar usuário
    6 - Sair
    """)

    while True:
        try:
            op = int(input('digite um número entre 1 e 6: '))
            if op>6 or op<1:
                raise ValueError
            break
        except ValueError as erro:
            print('Digite um número válido')
    if op == 1:
        nome = str(input('digite seu nome: '))
        email = str(input('digite seu email: '))
        senha = str(input('digite sua senha: '))
        senha = hashlib.sha256(senha.encode()).hexdigest()
        try:
            cursor.execute('INSERT INTO usuario (nome, email, senha) VALUES(?, ?, ?)', (nome, email, senha))
            conexao.commit()
            os.system('cls')
            print('Usuário cadastrado')
        except sqlite3.IntegrityError:
            os.system('cls')
            print('já existe um usuário com esse email, tente novamente')

    if op == 2:
        nome_login = str(input('digite seu nome: '))
        email_login = str(input('digite seu email: '))
        senha_login = str(input('digite sua senha: '))
        senha_login = hashlib.sha256(senha_login.encode()).hexdigest()
        os.system('cls')
        try:
            cursor.execute('SELECT * FROM usuario WHERE nome = ? and email = ? and senha = ?', (nome_login, email_login, senha_login))
            usuario = cursor.fetchone()
            print(f"nome = {usuario[0]}\nemail = {usuario[1]}\nsenha = {usuario[2]}")
        except TypeError:
            os.system('cls')
            print('Usuario não encontrado')

    if op==3:
        usuario_encontrado = False
        nome_login = str(input('digite seu nome: '))
        email_login = str(input('digite seu email: '))
        senha_login = str(input('digite sua senha: '))
        senha_login = hashlib.sha256(senha_login.encode()).hexdigest()
        
        try:
            cursor.execute("SELECT * FROM usuario WHERE nome = ? and email = ? and senha = ?", (nome_login,
                                                                             email_login, senha_login))
            usuario = cursor.fetchone()
            if usuario == None:
                raise TypeError
            print('usuario logado')
        except TypeError:
            os.system('cls')
            print('Usuario não encontrado')
        

    if op == 4:
        nome_delete = str(input('digite seu nome: '))
        email_delete = str(input('digite seu email: '))
        senha_delete = str(input('digite sua senha: '))
        senha_delete = hashlib.sha256(senha_delete.encode()).hexdigest()
        try:
            cursor.execute("SELECT * FROM usuario WHERE nome = ? and email = ? and senha = ?", (nome_delete,
                                                                                email_delete, senha_delete))
            usuario = cursor.fetchone()
            if usuario == None:
                raise TypeError
            else:
                confirmacao = input(f'Para confirmar, digite: {senha_delete[:8]}: ')
                if confirmacao == senha_delete[:8]:
                    cursor.execute('DELETE FROM usuario WHERE email = ?', (email_delete,))
                    conexao.commit()
                    print('Usuário deletado')
                else:
                    print('Digite a confirmação corretamente')
        except TypeError:
            os.system('cls')
            print('Usuario não encontrado')
    
    if op == 5:
        nome_antigo = str(input('digite seu nome: '))
        email_antigo = str(input('digite seu email: '))
        senha_antiga = str(input('digite sua senha: '))
        senha_antiga = hashlib.sha256(senha_antiga.encode()).hexdigest()
        try:
            cursor.execute("SELECT * FROM usuario WHERE nome = ? and email = ? and senha = ?", (nome_antigo,
                                                                                email_antigo, senha_antiga))
            usuario = cursor.fetchone()
            if usuario == None:
                raise TypeError
            else:
                os.system('cls')
                print('usuário encontrado')
                nome_novo = str(input('digite seu novo nome: '))
                email_novo = str(input('digite seu novo email: '))
                senha_nova = str(input('digite sua nova senha: '))
                senha_nova = hashlib.sha256(senha_nova.encode()).hexdigest()
                confirmacao = input(f'Para confirmar, digite: {senha_nova[:8]}: ')

                if confirmacao == senha_nova[:8]:
                    try:
                        cursor.execute('''UPDATE usuario SET nome = ?, email = ?, senha = ? 
                                    WHERE email = ?''', 
                                    (nome_novo, email_novo, senha_nova, email_antigo))
                        conexao.commit()
                        print('Usuário Alterado')
                    except sqlite3.IntegrityError:
                        print('já existe um usuário com esse email, tente novamente')
                else:
                    print('Digite a confirmação corretamente')
        except TypeError:
            os.system('cls')
            print('Usuario não encontrado')
        

    if op == 6:
        print('saindo...')
        conexao.close()
        break
