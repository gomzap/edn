nome_produto = "Cadeira Infantil"
preco_unitario = 12.40
quantidade = int(input("Digite a quantidade de produtos: "))
preco_total = preco_unitario * quantidade

print("Produto:", nome_produto)
print("Preço unitário: R$ {:.2f}".format(preco_unitario))
print("Quantidade:", quantidade)
print("Preço total: R$ {:.2f}".format(preco_total))
