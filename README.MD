# **Exercício de Cálculo Estatístico para Dados Agrupados**

### Exercício de construção de algoritmo que realiza cálculos estatísticos para dados numéricos agrupados.


## **Sobre:**
---
O meu intuito com os métodos contidos nesse exercício de construção de algoritmo **não é, de forma alguma,** competir com bibliotecas de terceiros ou soluções já existentes para cálculos estatísticos, assim como: SciPy, NumPy, statistics ou pacotes proprietários; pois, sei da ampla capacidade dessas bibliotecas ou soluções de fornecer soluções práticas e totalmente utilizáveis em variadas condições de aplicabilidade, fornecendo um resultado conciso e satisfatório.

**O meu intuito e objetivo com os métodos contidos nesse exercício de construção de algoritmo é puramente com a finalidade de estudo, utilizando-o para estudar lógica de programação, estrutura e análise de dados e como pode ser feita a documentação de programas, dessa forma, podendo fortalecer as minhas HardSkills.**

Esse é um exercício de construção de algoritmo que realiza cálculos estatísticos de Média, Moda, Mediana, Quartil, Decil, Percentil, Variância, Desvio padrão, Coeficiente de Variação de Pearson, Coeficiente de Assimetria de Pearson e Coeficiente Percentilico de Curtose para dados numéricos com base em dados fornecidos a ele por meio de arquivos .txt, .csv ou excel(.xlsx / .xml / .xls).

**Ele realiza os cálculos apenas para dados agrupados com e sem intervalo de classe.**

## **Tecnologias Utilizadas:**
---
- [**Python**](https://www.python.org/) 
- [**Pandas**](https://pandas.pydata.org/)
- [**NumPy**](https://numpy.org/)

## **Requisitos:**
---
 - [**Python 3.10.5**](https://www.python.org/downloads/)

## **Como utilizar:**
---
### **1. Como os dados devem ser fornecidos ao exercício de construção de algoritmo que realiza cálculos estatísticos:**

Os dados devem ser númericos e fornecidos ao exercício de construção de algoritmo que realiza cálculos estatísticos por meio de arquivos que possam estar nos seguintes formatos: `.txt`, `.csv`, `.xlsx`, `.xml` ou `.xls` .

Eu sugiro que os dados sejam fornecidos ao exercício de construção de algoritmo que realiza cálculos estatísticos por meio de um arquivo `.txt` principalmente para dados com intervalo.

### **Exemplo de contrução de um arquivo `.txt` com os dados que deseja utilizar:**
`Sem Intervalo:`
````
xi,fi
10,5
20,9
30,7
40,8
````
`Com Intervalo:`
````
xi,fi
1-2,5
2-3,9
3-4,7
4-5,8
````
--

### **2. Como Utilizar os Métodos e Utilizar o Arquivo com os Dados:**

**Arquivo `main.py`:** É o arquivo principal para incluir o arquivo com os dados e realizar a chamada dos métodos do exercício de construção de algoritmo que realiza cálculos estatísticos assim como a utilização geral do exercício de construção de algoritmo que realiza cálculos estatísticos.

- **Como incluir um arquivo:** Haverá uma variável chamada `file` e nela deverá ser atribuído o nome do arquivo que deseja utilizar ou o caminho para o arquivo que deseja utilizar em sua máquina local (caso o arquivo não esteja no mesmo diretório do código), feito isso, é só realizar as chamadas dos métodos específicos para cada operação. (Observação: Há exemplos no próprio arquivo `main.py` de como é feita essa chamada.)

    ````
    def main():
        file = r'exemplo_teste_intervalos_dois.txt'
        ...
        me = calculo_media_agrupados(variavel_file)
        print('Média: ', me)
        ...
    ```` 
    **Observação: No repositório há três arquivos `.txt` (`exemplo_teste_intervalos_dois.txt`, `exemplo_teste_intervalos.txt` e `exemplo_teste.txt`) de exemplo para observar o funcionamento do exercício de construção de algoritmo que realiza cálculos estatísticos.**

**Arquivo `calculo_estatistico_agrupados.py`:** É o arquivo secundário que utilizei para realizar os cálculos estatísticos do exercício de construção de algoritmo que realiza cálculos estatísticos, nele dividi os diferentes cálculos em métodos para facilitar a utilização. 

**Observação:** Realizei a divisão do exercício de construção de algoritmo que realiza cálculos estatísticos em dois arquivos e em métodos para que ficasse mais organizado e legível.

---
## Bom, é isso, como já disse, a finalidade desse exercício de construção de algoritmo que realiza cálculos estatísticos é puramente para finalidade estudantil (de estudo), o desenvolvi enquanto cursava a disciplina de Estatística Aplicada na universidade, para me ajudar enquanto estudava os conteúdos da disciplina e para estudar lógica de programação, estrutura e análise de dados e como pode ser feita a documentação de programas, dessa forma, podendo fortalecer as minhas HardSkills como desenvolvedor também.



