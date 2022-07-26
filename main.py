"""
O meu intuito com os métodos contidos nesse algoritmo não é, de forma alguma, competir com bibliotecas de terceiros ou
soluções já existentes para cálculos estatísticos, assim como: SciPy, NumPy, statistics ou pacotes proprietários; pois,
sei da ampla capacidade dessas bibliotecas ou soluções de fornecer soluções práticas e totalmente utilizáveis em
variadas condições de aplicabilidade, fornecendo um resultado conciso e satisfatório.

O meu intuito e objetivo com os métodos contidos nesse algoritmo é puramente com a finalidade de estudo,
utilizando-o para estudar lógica de programação, estrutura e análise de dados e como pode ser feita a documentação de
programas, dessa forma, podendo fortalecer as minhas HardSkills.


Esse é um algoritmo que realiza cálculos estatísticos de Média, Moda, Mediana, Quartil, Decil, Percentil, Variância,
Desvio padrão, Coeficiente de Variação de Pearson, Coeficiente de Assimetria de Pearson e Coeficiente Percentilico de
Curtose para dados numéricos com base em dados fornecidos a ele por meio de arquivos .txt, .csv ou
excel(.xlsx / .xml / .xls);

No momento ele realiza os cálculos apenas para dados agrupados com e sem intervalo de classe;

Exemplo de como os dados devem ser fornecidos ao algoritmo por meio de um arquivo .txt ou .csv:

Sem Intervalo:      Com Intervalo:
xi,fi               xi,fi
10,5                1-2,5
20,9                2-3,9
30,7                3-4,7
40,8                4-5,8

A minha sugestão é que faça em um arquivo .txt principalmente para dados com intervalo.

Fica aqui alguns exemplos de como realizar a chamada dos métodos criados para estudo e utilizar eles para estudo.
"""
from calculo_estatistico_agrupados import *


def main():
    file = r'exemplo_teste_intervalos_dois.txt'

    df = import_file_dados(file)
    print(df)
    me = calculo_media_agrupados(df)
    print('Média: ', me)

    df = import_file_dados(file)
    mo = calculo_moda_agrupados(df)
    print('Moda: ', mo)

    df = import_file_dados(file)
    md = calcula_mediana_agrupados(df)
    print('Mediana: ', md)

    df = import_file_dados(file)
    quartil = 1
    qk = calculo_quartil_agrupados(quartil, df)
    print(f'Quartil({quartil}): ', qk)

    df = import_file_dados(file)
    decil = 8
    dk = calculo_decil_agrupados(decil, df)
    print(f'Decil({decil}): ', dk)

    df = import_file_dados(file)
    percentil = 80
    pk = calculo_percentil_agrupados(percentil, df)
    print(f'Percentil({percentil}): ', pk)

    df = import_file_dados(file)
    s2 = calculo_variancia_agrupados(pa='populacao', df=df)
    print('Variância: ', s2)

    s = calculo_desvio_padrao_agrupados(s2)
    print('Desvio Padrão: ', s)

    cv = calculo_coeficiente_variacao_agrupados(s, me)
    print('Coeficiente de Variação: ', cv)

    ca = calculo_coeficiente_assimetria_agrupados(me, md, s)
    print('Coeficiente de Assimetria: ', ca)

    df = import_file_dados(file)
    c = calculo_curtose_agrupados(df)
    print('Curtose: ', c)


if __name__ == '__main__':
    main()

