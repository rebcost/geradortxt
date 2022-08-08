def gerar_txt(nome_arquivo="padrao.txt", corpo_arquivo=""):
    with open(nome_arquivo, 'w') as file:
        file.writelines(corpo_arquivo)
