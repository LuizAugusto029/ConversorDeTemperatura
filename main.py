from Funções import interaçao_com_usuario as intu
from Funções import temperaturas as temp

# Vizualização do Menu
print('------------- CONVERSOR DE TEMPERATURA -------------')
print('AQUI VOCÊ ESCOLHER SE QUER COCNVERTER DE:\n'
      '[1] °Celsiuis para °Fahrenheint ou para °Kelvin\n'
      '[2] °Fahrenheint para °Celsius ou para °Kelvin\n'
      '[3] °Kelvin para °Celsius ou para °Fahrenheint\n'
      '[4] ENCERRAR PROGAMA')
print()

while True:
    # Escolha das opções do Menu
    valor_opcao = intu.opção('Qual das opções você quer?\n'
                             'Escolha [1, 2, 3 ou 4(SAIR)] >>> ')
    # Encerrar progama
    if valor_opcao == 4:
        break
    else:
        print()
        while True:
            if valor_opcao == 1:
                # Aqui é onde o usuário irá informar o valor da temperatura em Celisius
                valor_em_celsius = intu.valor_temp('Digite a Temperatura em Graus Celisius >  ')
                conv_C_em_F = temp.celsius_fahr(valor_em_celsius)         # Converte a temperatura de Celsius para Fahrenheint
                conv_C_em_K = temp.celsius_kelvin(valor_em_celsius)       # Converte a temperatura de Celsius para Kelvin
                print()
                intu.tabela_conversor('C', valor_em_celsius, conv_C_em_F, conv_C_em_K)   # Mostrar um tabela com os valores já convertidosem °F e °K
                print()
                saida = intu.saida('Para mudar a conversão digite [0], se quiser continuar aperter ENTER > ')   # Se quer continuar a converter °C ou mudar a conversão
                if saida == 0:
                    break
                else:
                    continue
            elif valor_opcao == 2:
                # Aqui é onde o usuário irá informar o valor da temperatura em Fahrenheint
                valor_em_fahr = intu.valor_temp('Digite a temperatura em Graus Fahrenheint > ')
                conv_F_em_C = temp.fahr_celsius(valor_em_fahr)         # Converte a temperatura de Fahrenheint para Celsius
                conv_F_em_K = temp.fahr_kelvin(valor_em_fahr)          # Converter a temperatura de Fahrenheint para Kelvin
                print()
                intu.tabela_conversor('F', valor_em_fahr, conv_F_em_C, conv_F_em_K)    # Mostrar um tabela com os valores já convertidos em °C e °K
                print()
                saida = intu.saida('Para mudar a conversão digite [0], se quiser continuar aperter ENTER > ')
                if saida == 0:
                    break
                else:
                    continue
            elif valor_opcao == 3:
                # Aqui é onde o usuário irá informar o valor da temperatura em Kelvin
                valor_em_kelvin = intu.valor_temp('Digite a temperatura em Graus Kelvin > ')
                conv_K_em_C = temp.kelvin_celsius(valor_em_kelvin)         # Converte a temperatura de Kelvin para Celsius
                conv_K_em_F = temp.kelvin_fahr(valor_em_kelvin)            # Converter a temperatura de Kelvin para Fahrenheint
                print()
                intu.tabela_conversor('K', valor_em_kelvin, conv_K_em_F, conv_K_em_C)    # Mostrar um tabela com os valores já convertidos em °F e °C
                print()
                saida = intu.saida('Para mudar a conversão digite [0], se quiser continuar aperter ENTER > ')
                if saida == 0:
                    break
                else:
                    continue

print('\033[31mPROGAMA ENCERRADO!!\033[m')
