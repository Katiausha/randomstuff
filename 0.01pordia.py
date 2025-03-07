def main():
    valor = 0.01
    dias = 1
    print("=================\nQuantos dias você deseja contar?\n=================")
    pergunta = float(input())

    while dias < pergunta:
        valor = valor*2
        dias += 1

    print("=================\nTotal:"+str(valor)+" Dólares do Zimbábue | Pressione qualquer tecla para resetar.\n=================")
    input()
    main()
    
main()
