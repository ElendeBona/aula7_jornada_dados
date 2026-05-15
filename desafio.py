import csv
path_do_arquivo = 'vendas.csv'

# função Ler o arquivo CSV


def ler_csv(nome_do_arquivo: str) -> list[dict]:
    '''
    Função para ler um arquivo CSV e retornar os dados como uma lista de dicionários.

    :param nome_do_arquivo: O nome do arquivo CSV a ser lido.
    :return: Uma lista de dicionários, onde cada dicionário representa uma linha do CSV.
    '''
    with open(nome_do_arquivo, mode='r', encoding='utf-8') as arquivo:
        leitor_csv = csv.DictReader(arquivo, skipinitialspace=True)
        return list(leitor_csv)

# Função processar os dados em um dicionário


def processar_dados(dados: list[dict]) -> dict[str, list[dict]]:
    produtos = {}
    for item in dados:
        produto = item.get('produto')
        if produto not in produtos:
            produtos[produto] = []
        produtos[produto].append(item)
    return produtos

# Função para calcular o total de vendas de total por produto/categoria


def calcular_total_vendas_por_produto(dados: dict[str, list[dict]]) -> dict[str, float]:
    vendas_por_produto = {}
    for produto, itens in dados.items():
        # total_vendas = sum(float(item.get('preco', 0)) * (int(item.get('quantidade', 0))) for item in itens)'
        total_vendas = sum(float(item.get('preco', 0)) for item in itens)
        vendas_por_produto[produto] = total_vendas
    return vendas_por_produto


def calcular_total_geral(dados: list[dict]) -> float:
    '''
    Calcula o somatório total de todos os produtos
    '''
    return sum(float(item.get('preco', 0)) for item in dados)


# função principal para integrar as funções anteriores
def main():
    nome_do_arquivo = 'vendas.csv'
    dados = ler_csv(nome_do_arquivo)
    dados_processados = processar_dados(dados)
    vendas_por_produto = calcular_total_vendas_por_produto(
        dados_processados)
    for produto, total_vendas in vendas_por_produto.items():
        print(f"Produto: {produto}, Total de Vendas: {total_vendas:.2f}")
    total_geral = calcular_total_geral(dados)
    print(f"\nTotal Geral de Vendas: {total_geral:.2f}")


if __name__ == "__main__":
    main()
