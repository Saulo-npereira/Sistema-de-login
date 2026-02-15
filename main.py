import csv
import pandas as pd
import hashlib
import os

while True:
    print("""
    1 - Cadastrar usuário
    2 - Listar usuários
    3 - Login
    4 - Listar seu usuário
    5 - Sair
    
    """)

    while True:
        try:
            op = int(input('digite um número entre 1 e 5: '))
            if op>5 or op<1:
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
            with open('arquivo.csv', 'x', newline='', encoding='utf-8') as arquivo:
                writer = csv.writer(arquivo)
                writer.writerow(['nome', 'email', 'senha'])
        except FileExistsError:
            pass 

        with open('arquivo.csv', 'a', newline = '', encoding = 'utf-8') as arquivo:
            writer = csv.writer(arquivo)
            writer.writerow([nome, email, senha])
        os.system('cls')
    if op == 2:
        os.system('cls')
        tabela = pd.read_csv('arquivo.csv')
        print(tabela)

    if op == 3:
        usuario_encontrado = False
        nome_login = str(input('digite seu nome: '))
        email_login = str(input('digite seu email: '))
        senha_login = str(input('digite sua senha: '))
        senha_login = hashlib.sha256(senha_login.encode()).hexdigest()
        with open('arquivo.csv', 'r', encoding='utf-8') as arquivo:
            reader = csv.reader(arquivo)
    
            next(reader)  # pula o cabeçalho
            os.system('cls')
            for linha in reader:
                if email_login == linha[1] and nome_login == linha[0] and senha_login ==linha[2]:
                    print('usuario logado')
                    usuario_encontrado = True
                    break
                else:
                    continue
            if not usuario_encontrado:
                print('Dados incorretos')

    if op==4:
        usuario_encontrado = False
        nome_login = str(input('digite seu nome: '))
        email_login = str(input('digite seu email: '))
        senha_login = str(input('digite sua senha: '))
        senha_login = hashlib.sha256(senha_login.encode()).hexdigest()
        with open('arquivo.csv', 'r', encoding='utf-8') as arquivo:
            reader = csv.reader(arquivo)
    
            next(reader)  # pula o cabeçalho
            os.system('cls')
    
            for linha in reader:
                if email_login == linha[1] and nome_login == linha[0] and senha_login ==linha[2]:
                    print(linha)
                    usuario_encontrado = True
                    break
                else:
                    continue
                
            if not usuario_encontrado:
                print('Dados incorretos')

    if op == 5:
        break