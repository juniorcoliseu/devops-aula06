import jogovelha
import

erroInicializar = False

jogo = jogovelha.inicializar()

if len(jogo) != 3:
    erroInicializar = True
else:
    for linha in jogo:
        if len(linha) != 3:
            erroInicializar = True
        else:
            for elemento in linha:
                if elemento != '.':
                    erroInicializar = True

if erroInicializar:
    sys.exut(1)
else:
    sys.exit(0)
