def opção(op):
    """
    -> Escolha de opção de um Menu
    :param op: Quais as opções
    :return: valor da opção
    """
    try:
        opcao = int(input(op))
        if opcao not in range(1, 5):
            print('\033[31mOPÇÃO INVÁLIDA!\033[m')
            return opção(op)
    except:
        print('\033[31mDIGITE A OPÇÃO COM UM VALOR NÚMERICO!\033[m')
        return opção(op)
    else:
        return opcao


def saida(op):
    valor_saida = str(input(op))
    if valor_saida not in '0' or '':
        print('\033[31mOPÇÃO INVÁLIDA! INFORME [0] OU APERTER (ENTER)!\033[m')
        return saida(op)
    if valor_saida == '0':
        return int(valor_saida)
    else:
        return ''


def valor_temp(temp):
    """
    -> Informar o valor da temperatura
    :param temp: Qual o tipo de temperatura
    :return: valor da temperatura
    """
    try:
        valor = float(input(temp).replace(',', '.'))
    except:
        print('DIGITE UM VALOR NÚMERICO VÁLIDO')
        return valor_temp(temp)
    else:
        return valor


def tabela_conversor(tipo_temp='', Toriginal=0, Tconv1=0, Tconv2=0):
    """
    -> Transforma os dados das temperaturas passadas nos parâmetros para um tabela personalizada
    :param tipo_temp: Escolha 'C' para tabela se formatar em função da temperatura em Graus Celsiuis.
    Escolha 'F' para a tabela se formatar em função da temperatura em Graus Fahrenheint.
    Escolha 'K' para a tabela se formatar em função da temperatura em Graus Kelvin
    :param Toriginal: Valor da Temperatura que será convertida
    :param Tconv1: Valor da temperatura já convertida, se tipo_temp ='C' esse valor será em °F.
    Se tipo_temp ='F' esse valor será em °C. Se tipo_temp = 'K' esse valor será em °F
    :param Tconv2: Valor da temperatura já convertido, se tipo_temp = 'C' esse valor será em °K
    Se tipo_temp = 'F' esse valor será em °K. se tipo_temp = 'K' esse valor será em °C
    :return: None
    """
    if tipo_temp == 'C':
        print(f'|{"CONVERSOR DE TEMPERATURA":^38}|\n'
              f'|TEMPERATURA ESCOLHIDA: {Toriginal:>13}°C|\n'
              f'|Em Graus Fahrenheint -> {Tconv1:>12}°F|\n'
              f'|Em Graus Kelvin -> {Tconv2:>17}°K|')
    elif tipo_temp == 'F':
        print(f'|{"CONVERSOR DE TEMPERATURA":^38}|\n'
              f'|TEMPERATURA ESCOLHIDA: {Toriginal:>13}°F|\n'
              f'|Em Graus Celsius -> {Tconv1:>16}°F|\n'
              f'|Em Graus Kelvin -> {Tconv2:>17}°K|')
    elif tipo_temp == 'K':
        print(f'|{"CONVERSOR DE TEMPERATURA":^38}|\n'
              f'|TEMPERATURA ESCOLHIDA: {Toriginal:>13}°K|\n'
              f'|Em Graus Fahrenheint -> {Tconv1:>12}°F|\n'
              f'|Em Graus Celsius -> {Tconv2:>16}°K|')
