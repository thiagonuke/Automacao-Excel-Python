import openpyxl

#Planilha(book)

book = openpyxl.Workbook()

book.create_sheet('Produtos')

Produtos_page = book['Produtos']
Produtos_page.append(['Produto', 'Qntd', 'Preço'])
Produtos_page.append(['Mouse', '5', 'R$10,99'])
Produtos_page.append(['Teclado', '8','R$20,50'])
Produtos_page.append(['Fone', '10', 'R$12.99'])

book.save('Planilha de Produtos.xlsx')
