import pandas as pnd

def lerJsonMovimento():
    nomeArquivo = input("Digite o nome do arquivo: \n")
    df = pnd.read_json(nomeArquivo + ".instrucao")
    return df