import openpyxl

#Carregamento de arquivos
book = openpyxl.load_workbook('Planilha de Produtos.xlsx')
Produtos_page = book['Produtos']

for rows in Produtos_page.iter_rows(min_row=2, max_row=4):
    #Gerar os dados:
    print(f'{rows[0].value}, {rows[1].value}, {rows[2].value}')

    #Fazer mudanças de valores nas células:
    for cell in rows:
        if cell.value == 'Fone':
            cell.value = 'Carregador'

book.save('Planilha de Compras v2.xlsx')