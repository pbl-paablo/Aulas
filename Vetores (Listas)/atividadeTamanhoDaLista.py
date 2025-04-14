lista = []
while True:
    addItem = input('>>')
    if addItem == "Fim":
        break
    lista.append(addItem)
print(f'O tamanho da minha lista é:{len(lista)}')
