"""
O meu intuito com os métodos contidos nesse exercício de construção de algoritmo não é, de forma alguma, competir
com bibliotecas de terceiros ou soluções já existentes para cálculos estatísticos, assim como: SciPy, NumPy, statistics
ou pacotes proprietários; pois, sei da ampla capacidade dessas bibliotecas ou soluções de fornecer soluções práticas
e totalmente utilizáveis em variadas condições de aplicabilidade, fornecendo um resultado conciso e satisfatório.

O meu intuito e objetivo com os métodos contidos nesse exercício de construção de algoritmo é puramente com a
finalidade de estudo, utilizando-o para estudar lógica de programação, estrutura e análise de dados e como pode ser
feita a documentação de programas, dessa forma, podendo fortalecer as minhas HardSkills.


Esse é um exercício de construção de algoritmo que realiza cálculos estatísticos de Média, Moda, Mediana, Quartil,
Decil, Percentil, Variância, Desvio padrão, Coeficiente de Variação de Pearson, Coeficiente de Assimetria de Pearson e
Coeficiente Percentilico de Curtose para dados numéricos com base em dados fornecidos a ele por meio de arquivos .txt,
.csv ou excel(.xlsx / .xml / .xls);

No momento ele realiza os cálculos apenas para dados agrupados com e sem intervalo de classe;

Exemplo de como os dados devem ser fornecidos ao algoritmo por meio de um arquivo .txt ou .csv:

Sem Intervalo:      Com Intervalo:
xi,fi               xi,fi
10,5                1-2,5
20,9                2-3,9
30,7                3-4,7
40,8                4-5,8

A minha sugestão é que faça em um arquivo .txt principalmente para dados com intervalo.
"""
import pandas as pd
import numpy as np
import unicodedata as ud


def import_file_dados(file_local):
    """Realiza a leitura por meio da biblioteca `Pandas` de um arquivo contido em sua máquina local, podendo ser esse arquivo um `.txt, .csv ou excel(.xlsx / .xml / .xls)` contendo nele os dados numéricos que deseja calcular já separados em colunas `xi` e `fi`, assim o método transforma o arquivo em um objeto `DataFrame` da biblioteca `Pandas`, e antes de retornar o resultado também acrescenta nele a coluna de Frequência Acumulada `fac`.

    :param file_local: parâmetro que recebe uma string com o endereço local em sua máquina de um arquivo contendo os dados numéricos que deseja realizar os cálculos sendo que os dados já devem estar separados em duas colunas sendo elas a `xi` e a coluna `fi`
    :return: df --> Retorna um objeto `DataFrame` criado com a biblioteca `Pandas` contendo os dados numéricos disponibilizados pelo arquivo local para a realização dos cálculos
    """
    arquivo_xlsx = '.xlsx'
    arquivo_xml = '.xml'
    arquivo_xls = '.xls'
    if arquivo_xlsx in file_local or arquivo_xml in file_local or arquivo_xls in file_local:
        df = pd.read_excel(file_local)
    else:
        df = pd.read_csv(file_local)

    list_fac = []
    val = 0
    for items in df['fi']:
        val = items + val
        list_fac.append(val)
    df['fac'] = list_fac
    return df


# Metodo que realiza o calculo da Média para dados agrupados com e sem intervalo
def calculo_media_agrupados(df: pd.DataFrame):
    """Realiza o cálculo da Média para dados numéricos agrupados.

    :param df: parâmetro que recebe um objeto `DataFrame` criado com a biblioteca `Pandas` contendo os dados numéricos para a realização dos cálculos
    :return: me --> Resultado do cálculo da Média
    """
    lista_exi = []
    for item in df['xi']:
        item = str(item)
        separando_intervalo = item.split('-')
        if len(separando_intervalo) > 1:
            soma = float(separando_intervalo[0]) + float(separando_intervalo[1])
            xi = soma / 2
            lista_exi.append(xi)
        else:
            xi = float(separando_intervalo[0])
            lista_exi.append(xi)

    df['xi'] = lista_exi
    xi_fi = df['xi'] * df['fi']
    exi_fi = sum(xi_fi)
    efi = sum(df['fi'])
    me = exi_fi / efi
    return me


def calculo_moda_agrupados(df: pd.DataFrame):
    """Realiza o cálculo da Moda para dados numéricos agrupados.

    :param df: parâmetro que recebe um objeto `DataFrame` criado com a biblioteca `Pandas` contendo os dados numéricos para a realização dos cálculos
    :return: mo --> Resultado do cálculo da Moda
    """
    lista_xi1 = []
    lista_xi2 = []
    for item in df['xi']:
        item = str(item)
        separando_intervalo = item.split('-')
        if len(separando_intervalo) > 1:
            xi1 = float(separando_intervalo[0])
            xi2 = float(separando_intervalo[1])
            lista_xi1.append(xi1)
            lista_xi2.append(xi2)
        else:
            xi1 = float(separando_intervalo[0])
            lista_xi1.append(xi1)

    df['xi'] = lista_xi1
    if lista_xi2:
        df['xi2'] = lista_xi2

        classe_modal = df['fi'].max()
        index_classe_modal = df['fi'].idxmax()
        index_class_ant = df['fi'].idxmax() - 1
        index_class_post = df['fi'].idxmax() + 1
        d1 = classe_modal - df['fi'][index_class_ant]
        d2 = classe_modal - df['fi'][index_class_post]
        d = d1 / (d1 + d2)

        hamplitude_mo = df['xi2'][0] - df['xi'][0]

        limiteant_mo = df['xi'][index_classe_modal]

        mo = d * hamplitude_mo
        mo = limiteant_mo + mo
        return mo
    else:
        mo = df['fi'].max()
        return mo


def formula_padrao_mediana_agrupados_intevalo(pos, df: pd.DataFrame):
    """Método contendo a fórmula padrão do cálculo da `Mediana` para dados `numéricos agrupados e com intervalo`, ele facilita o cálculo da mediana em seu respectivo método, assim como, o cálculo de outras formulas estatísticas que possuem estrutura semelhante como `Quartil`, `Decil` e `Percentil`.

    :param pos: parâmetro que recebe o valor do cálculo da posição da minha mediana
    :param df: parâmetro que recebe um objeto `DataFrame` criado com a biblioteca `Pandas` contendo os dados numéricos para a realização dos cálculos
    :return: x --> Resultado do cálculo da mediana dentro da fórmula para dados agrupados com intervalo
    """
    list_index_fac = []
    for item in df['fac']:
        if pos <= item:
            fac_pos = df['fac'] == item
            lista_pos_fac = [fac_pos]
            id_fac = np.where(lista_pos_fac)[1]
            id_fac = id_fac[0]
            list_index_fac.append(id_fac)
    index_fac = list_index_fac[0]
    fac_ant = df['fac'][index_fac - 1]
    fi_pos = df['fi'][index_fac]
    hamplitude_pos = df['xi2'][0] - df['xi'][0]
    limiteant_pos = df['xi'][index_fac]

    x = pos - fac_ant
    x = x / fi_pos
    x = x * hamplitude_pos
    x = x + limiteant_pos
    return x


def calcula_mediana_agrupados(df: pd.DataFrame):
    """Realiza o cálculo da Mediana para dados numéricos agrupados.

    :param df: parâmetro que recebe um objeto `DataFrame` criado com a biblioteca `Pandas` contendo os dados numéricos para a realização dos cálculos
    :return: md --> Resultado do cálculo da Mediana
    """
    lista_xi1 = []
    lista_xi2 = []
    for item in df['xi']:
        item = str(item)
        separando_intervalo = item.split('-')
        if len(separando_intervalo) > 1:
            xi1 = float(separando_intervalo[0])
            xi2 = float(separando_intervalo[1])
            lista_xi1.append(xi1)
            lista_xi2.append(xi2)
        else:
            xi1 = float(separando_intervalo[0])
            lista_xi1.append(xi1)

    df['xi'] = lista_xi1

    efi = 0
    for i in df['fi']:
        efi += i

    pos = efi / 2
    if lista_xi2:
        df['xi2'] = lista_xi2

        md = formula_padrao_mediana_agrupados_intevalo(pos, df)
        return md
    else:
        for items in df['fac']:
            if pos <= items:
                fac_pos = df['fac'] == items
                lista_fac = [fac_pos]
                id_fac = np.where(lista_fac)[1]
                md = df['xi'][id_fac[0]]
                return md


def calculo_quartil_agrupados(q: int, df: pd.DataFrame):
    """Realiza o cálculo do Quartil para dados numéricos agrupados.

    :param q: parâmetro que recebe um valor inteiro referente ao Quartil que deseja calcular
    :param df: parâmetro que recebe um objeto `DataFrame` criado com a biblioteca `Pandas` contendo os dados numéricos para a realização dos cálculos
    :return: qk --> Resultado do cálculo do Quartil
    """
    lista_xi1 = []
    lista_xi2 = []
    for item in df['xi']:
        item = str(item)
        separando_intervalo = item.split('-')
        if len(separando_intervalo) > 1:
            xi1 = float(separando_intervalo[0])
            xi2 = float(separando_intervalo[1])
            lista_xi1.append(xi1)
            lista_xi2.append(xi2)
        else:
            xi1 = float(separando_intervalo[0])
            lista_xi1.append(xi1)

    df['xi'] = lista_xi1

    efi = 0
    for i in df['fi']:
        efi += i

    pos = q * efi
    pos = pos / 4
    if lista_xi2:
        df['xi2'] = lista_xi2

        qk = formula_padrao_mediana_agrupados_intevalo(pos, df)
        return qk
    else:
        for items in df['fac']:
            if pos <= items:
                fac_pos = df['fac'] == items
                lista_fac = [fac_pos]
                id_fac = np.where(lista_fac)[1]
                qk = df['xi'][id_fac[0]]
                return qk


def calculo_decil_agrupados(d: int, df: pd.DataFrame):
    """Realiza o cálculo do Decil para dados numéricos agrupados.

    :param d: parâmetro que recebe um valor inteiro referente ao Decil que deseja calcular
    :param df: parâmetro que recebe um objeto `DataFrame` criado com a biblioteca `Pandas` contendo os dados numéricos para a realização dos cálculos
    :return: dk --> Resultado do cálculo do Decil
    """
    lista_xi1 = []
    lista_xi2 = []
    for item in df['xi']:
        item = str(item)
        separando_intervalo = item.split('-')
        if len(separando_intervalo) > 1:
            xi1 = float(separando_intervalo[0])
            xi2 = float(separando_intervalo[1])
            lista_xi1.append(xi1)
            lista_xi2.append(xi2)
        else:
            xi1 = float(separando_intervalo[0])
            lista_xi1.append(xi1)

    df['xi'] = lista_xi1

    efi = 0
    for i in df['fi']:
        efi += i

    pos = d * efi
    pos = pos / 10
    if lista_xi2:
        df['xi2'] = lista_xi2

        dk = formula_padrao_mediana_agrupados_intevalo(pos, df)
        return dk
    else:
        for items in df['fac']:
            if pos <= items:
                fac_pos = df['fac'] == items
                lista_fac = [fac_pos]
                id_fac = np.where(lista_fac)[1]
                dk = df['xi'][id_fac[0]]
                return dk


def calculo_percentil_agrupados(p: int, df: pd.DataFrame):
    """Realiza o cálculo do Percentil para dados numéricos agrupados.

    :param p: parâmetro que recebe um valor inteiro referente ao Percentil que deseja calcular
    :param df: parâmetro que recebe um objeto `DataFrame` criado com a biblioteca `Pandas` contendo os dados numéricos para a realização dos cálculos
    :return: pk --> Resultado do cálculo do Percentil
    """
    lista_xi1 = []
    lista_xi2 = []
    for item in df['xi']:
        item = str(item)
        separando_intervalo = item.split('-')
        if len(separando_intervalo) > 1:
            xi1 = float(separando_intervalo[0])
            xi2 = float(separando_intervalo[1])
            lista_xi1.append(xi1)
            lista_xi2.append(xi2)
        else:
            xi1 = float(separando_intervalo[0])
            lista_xi1.append(xi1)

    df['xi'] = lista_xi1
    efi = 0
    for i in df['fi']:
        efi += i

    pos = p * efi
    pos = pos / 100
    if lista_xi2:
        df['xi2'] = lista_xi2

        pk = formula_padrao_mediana_agrupados_intevalo(pos, df)
        return pk
    else:
        for items in df['fac']:
            if pos <= items:
                fac_pos = df['fac'] == items
                lista_fac = [fac_pos]
                id_fac = np.where(lista_fac)[1]
                pk = df['xi'][id_fac[0]]
                return pk


def calculo_variancia_agrupados(pa: str, df: pd.DataFrame):
    """Realiza o cálculo da Variância para dados numéricos agrupados, podendo ser esses dados uma população ou uma amostra.

    :param pa: parâmetro que recebe uma string dizendo se os seus dados são uma `amostra` ou uma `população` - Ex: pa = `amostra` -- Ex2: pa = `populacao`
    :param df: parâmetro que recebe um objeto `DataFrame` criado com a biblioteca `Pandas` contendo os dados numéricos para a realização dos cálculos
    :return: s2 --> Resultado do cálculo da Variância
    """

    lista_xi1 = []
    lista_xi2 = []
    for item in df['xi']:
        item = str(item)
        separando_intervalo = item.split('-')
        if len(separando_intervalo) > 1:
            xi1 = float(separando_intervalo[0])
            xi2 = float(separando_intervalo[1])
            lista_xi1.append(xi1)
            lista_xi2.append(xi2)
        else:
            xi1 = float(separando_intervalo[0])
            lista_xi1.append(xi1)

    df['xi'] = lista_xi1
    if lista_xi2:
        df['xi2'] = lista_xi2

        lista_xi_sum = []
        for index, item in df.iterrows():
            xi = item['xi'] + item['xi2']
            xi = xi / 2
            lista_xi_sum.append(xi)
        df['xi_sum'] = lista_xi_sum

        xi_fi = df['xi_sum'] * df['fi']
        exi_fi = sum(xi_fi)
        exi_fi_quad = exi_fi ** 2

        xi_quad = df['xi_sum'] ** 2
        xi_quad_fi = xi_quad * df['fi']
        exi_quad_fi = sum(xi_quad_fi)

        efi = sum(df['fi'])

        div_exi_fi_quad = exi_fi_quad / efi

        subtracao = exi_quad_fi - div_exi_fi_quad

        pa = pa.lower()
        pa = ud.normalize('NFKD', pa).encode('ASCII', 'ignore').decode('ASCII')
        if pa == 'populacao':
            s2 = subtracao * (1 / efi)
            return s2
        elif pa == 'amostra':
            s2 = subtracao * (1 / (efi - 1))
            return s2
        elif pa == '' or pa == ' ' or pa == '   ':
            msg = 'Não foi possivel realizar o calculo pois foi inserido uma string vazia no método para o argumento ´pa´.'
            return ValueError(f'ValueError: {pa}', msg)
        else:
            msg = 'Foi inserido um valor não valido para o argumento ´pa´ ele deve equivaler à string ´amostra´ ou ´população´.'
            return ValueError(f'ValueError: {pa}', msg)
    else:
        xi_fi = df['xi'] * df['fi']
        exi_fi = sum(xi_fi)
        exi_fi_quad = exi_fi ** 2

        xi_quad = df['xi'] ** 2
        xi_quad_fi = xi_quad * df['fi']
        exi_quad_fi = sum(xi_quad_fi)

        efi = sum(df['fi'])

        div_exi_fi_quad = exi_fi_quad / efi

        subtracao = exi_quad_fi - div_exi_fi_quad

        pa = pa.lower()
        pa = ud.normalize('NFKD', pa).encode('ASCII', 'ignore').decode('ASCII')
        if pa == 'populacao':
            s2 = subtracao * (1 / efi)
            return s2
        elif pa == 'amostra':
            s2 = subtracao * (1 / (efi - 1))
            return s2
        elif pa == '' or pa == ' ' or pa == '   ':
            msg = 'Não foi possivel realizar o calculo pois foi inserido uma string vazia no método para o argumento ´pa´.'
            return ValueError(f'ValueError: {pa}', msg)
        else:
            msg = 'Foi inserido um valor não valido para o argumento ´pa´ ele deve equivaler à string ´amostra´ ou ´população´.'
            return ValueError(f'ValueError: {pa}', msg)


def calculo_desvio_padrao_agrupados(s2):
    """Realiza o cálculo do Desvio Padrão com base em dados numéricos resultante do cálculo da `Variância`.

    :param s2: parâmetro que recebe um dado numérico resultante do cálculo do `Variância`
    :return: s --> Resultado do cálculo do Desvio Padrão
    """
    s = pow(s2, 0.5)
    return s


def calculo_coeficiente_variacao_agrupados(s, me):
    """Realiza o cálculo do Coeficiente de Variação de Pearson com base em dados numéricos resultantes do cálculo do `Desvio Padrão` e `Média`.

    :param s: parâmetro que recebe um dado numérico resultante do cálculo do `Desvio Padrão`
    :param me: parâmetro que recebe um dado numérico resultante do cálculo da `Média`
    :return: cv --> Resultado do cálculo do Coeficiente de Variação (cv) / o valor em porcentagem do cv / tipo de dispersão
    """
    cv = s / me
    cv_p = cv * 100
    disp = ''
    if cv_p <= 15:
        disp = 'Dispersão Baixa - Dados Homogêneos'
    elif 15 < cv_p <= 30:
        disp = 'Dispersão Média'
    elif cv_p > 30:
        disp = 'Dispersão Alta - Dados Heterogêneos'

    response = f'{cv} / cv(%): {cv_p}% / Dispersão: {disp}'
    return response


def calculo_coeficiente_assimetria_agrupados(me, md, s):
    """Realiza o cálculo do Coeficiente de Assimetria de Pearson com base em dados numéricos resultantes do cálculo da `Média`, `Mediana` e `Desvio Padrão`.

    :param me: parâmetro que recebe um dado numérico resultante do cálculo da `Média`
    :param md: parâmetro que recebe um dado numérico resultante do cálculo da `Mediana`
    :param s: parâmetro que recebe um dado numérico resultante do cálculo da `Desvio Padrão`
    :return: ca --> Resultado do cálculo do Coeficiente de Assimetria de Pearson / tipo de assimetria
    """
    ca = 3 * (me - md)
    ca = ca / s
    val = ''
    if ca == 0:
        val = 'Nulo - Simétrica'
    elif ca > 0:
        val = 'Positivo - Assimetria Positiva'
    elif ca < 0:
        val = 'Negativo - Assimetria Negativa'

    response = f'{ca} --> {val}'
    return response


def calculo_curtose_agrupados(df: pd.DataFrame):
    """Realiza o cálculo do Coeficiente Percentilico de Curtose com base em dados numéricos agrupados provenientes de um objeto `Pandas DataFrame`.

    :param df: parâmetro que recebe um objeto `DataFrame` criado com a biblioteca `Pandas` contendo os dados numéricos para a realização dos cálculos
    :return: c --> Resultado do cálculo da curtose / tipo de curva
    """
    q1 = calculo_quartil_agrupados(q=1, df=df)
    q3 = calculo_quartil_agrupados(q=3, df=df)
    p10 = calculo_percentil_agrupados(p=10, df=df)
    p90 = calculo_percentil_agrupados(p=90, df=df)

    c1 = q3 - q1
    c2 = 2 * (p90 - p10)
    c = c1 / c2
    val = ''
    response = ''
    if c == 0.263:
        val = 'Mesocúrtica'
        response = f'{c} --> c = 0.263 : {val}'
    elif c < 0.263:
        val = 'Leptocúrtica'
        response = f'{c} --> c < 0.263 : {val}'
    elif c > 0.263:
        val = 'Platicúrtica'
        response = f'{c} --> c > 0.263 : {val}'
    return response

