import json

def texto_menu():
    return (
        "Sistema de Estoque\n\n"
        "1 - Cadastrar produto\n"
        "2 - Listar produtos\n"
        "3 - Buscar produto\n"
        "4 - Entrada de estoque\n"
        "5 - Saída de estoque\n"
        "6 - Excluir produtos\n"
        "7 - Alterar preço\n"
        "0 - Sair"
    )

def main():

    produtos = carregar_produtos()

    while True:
        print(texto_menu())

        opcao = input("\nEscolha uma opção: ")

        match opcao:
            case "1":
                cadastrar_produto(produtos)

            case "2":
                listar_produtos(produtos)

            case "3":
                buscar_produto(produtos)

            case "4":
                entrada_estoque(produtos)

            case "5":
                saida_estoque(produtos)
            
            case "6":
                excluir_produto(produtos)

            case "7":
                alterar_preco(produtos)

            case "0":
                print("Encerrando o sistema...")
                break

            case _:
                print("Opção inválida!")


def cadastrar_produto(produtos):

    codigo = input("Código: ")

    if localizar_produto(produtos, codigo):
        print("Código já cadastrado.")
        return
    
    nome = input("Nome: ")
    try:
        preco = float(input("Preço: "))
        quantidade = int(input("Quantidade: "))
    except ValueError:
        print("Preço ou quantidade inválidos")
        return

    produto = {
        "codigo": codigo,
        "nome": nome,
        "preco": preco,
        "quantidade": quantidade
}
    produtos.append(produto)
    salva_produtos(produtos)

    print("\n Produto cadastrado com sucesso!\n")

def listar_produtos(produtos):

    if not produtos:
        print("Nenhum produto cadastrado.")
        return

    for produto in produtos:
        mostrar_produto(produto)
            
def buscar_produto(produtos):

    codigo = input("Digite o código: ")

    produto = localizar_produto(produtos, codigo)

    if produto:
        mostrar_produto(produto)
    else:
        print("Produto não encontrado.")
    

def entrada_estoque(produtos):

    codigo = input("Digite o código do produto: ")

    produto = localizar_produto(produtos, codigo)

    if produto:

        try:
            entrada = int(input("Quantidade de entrada: "))
        except ValueError:
            print("Quantidade invádida.")
            return

        produto["quantidade"] += entrada

        salva_produtos(produtos)

        print("\nEstoque atualizado com sucesso!\n")

        mostrar_produto(produto)
        
    else:
        print("Produto não encontrado.")

def saida_estoque(produtos):

    codigo = input("Digite o código do produto: ")

    produto = localizar_produto(produtos, codigo)

    if produto:

        try:
            saida = int(input("Quantidade de saida: "))
        except ValueError:
            print("Quantidade invádida.")
            return

        if saida > produto["quantidade"]:
            print("Estoque insuficiente.")
            return

        produto["quantidade"] -= saida

        salva_produtos(produtos)

        print("\nEstoque atualizado com sucesso!\n")
        mostrar_produto(produto)
        
    else:
        print("Produto não encotrado.")

def excluir_produto(produtos):

    codigo = input("digite o código: ")

    produto = localizar_produto(produtos, codigo)

    if produto:

        mostrar_produto(produto)

        produtos.remove(produto)

        salva_produtos(produtos)

        print("\nProduto excluído com sucesso")

    else:
            print("Produto nçao encontrado.")

def alterar_preco(produtos):

    codigo = input("Digite o código do produto: ")

    produto = localizar_produto(produtos, codigo)

    if produto:

        try:
            novo_preco = float(input("Novo preço: "))
        except ValueError:
            print("Preço inválido.")
            return

        produto["preco"] = novo_preco

        salva_produtos(produtos)

        print("\nPreço atualizado com sucesso!\n")

        mostrar_produto(produto)

    else:
        print("Produto não encontrado.")


def salva_produtos(produtos):
    with open("produtos.json", "w", encoding="utf-8") as arquivo:
        json.dump(produtos, arquivo, indent=4, ensure_ascii=False)

def carregar_produtos():
    try:
        with open("produtos.json", "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)

    except FileNotFoundError:
        return []

def localizar_produto(produtos, codigo):

    for produto in produtos:

        if produto["codigo"] == codigo:
            return produto

    return None

def mostrar_produto(produto):
    print(f"Código: {produto['codigo']}")
    print(f"Nome: {produto['nome']}")
    print(f"Preço: R$ {produto['preco']:.2f}")
    print(f"Quantidade: {produto['quantidade']}")
    print("-" * 30)

main()