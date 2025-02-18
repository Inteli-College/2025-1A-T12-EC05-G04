import pandas as pnd

isInputing = True
currentInput = 0

tipoAcao = []
valorGrab = []
posicaoX = []
posicaoY = []
posicaoZ = []


while isInputing:
    tipoAcao.append(input("Digite o tipo de ação (1: movimento, 2: pegar/soltar): \n"))
    valorGrab.append(input("Digite o valor de pegada: \n"))
    posicaoX.append(input("Digite a posição X: \n"))
    posicaoY.append(input("Digite a posição Y: \n"))
    posicaoZ.append(input("Digite a posição Z: \n"))
    finalizar = input("Deseja finalizar? (S/N) \n")
    if finalizar == "S" or finalizar == "s":
        isInputing = False
    else:
        currentInput += 1

fileName = input("Digite o nome do arquivo: \n")
df = pnd.DataFrame({
    'tipoAcao': tipoAcao,
    'valorGrab': valorGrab,
    'x': posicaoX,
    'y': posicaoY,
    'z': posicaoZ
    
})
df.to_json(fileName + ".instructions")