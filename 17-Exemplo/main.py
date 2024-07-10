import flet as ft

def main(page: ft.Page):
    page.scroll = "always"

    #filtro de numero
    filtro_numero = ft.InputFilter('^[0-9]*')
    filtro_vazio  = ft.InputFilter('')

    #digitacao do usuario
    prod = ft.Dropdown(label="Produto", options=[ft.dropdown.Option("produto 1"),
                                                 ft.dropdown.Option("produto 2"),
                                                 ft.dropdown.Option("produto 3")
                                                ])
    qtd = ft.TextField(label="Quantidade", input_filter=filtro_numero, min_lines=1)
    
    seq = ft.Text("")
   
    produtos_list = [] #vou criar isso aqui pra faze a validacao de inserção

    #tabela
    tabela = ft.DataTable(
        border=ft.border.all(1, "black"),
        vertical_lines=ft.BorderSide(1, "black"),
        horizontal_lines=ft.BorderSide(1, "black"),
        column_spacing=100,
        heading_row_height=100,
        columns=[
            ft.DataColumn(ft.Text("Sequencia")),
            ft.DataColumn(ft.Text("Produto")),
            ft.DataColumn(ft.Text("Quantidade")),
            ],
            rows=[]
        )

    #metodos
    def editindex(e,r,j):
        prod.value = r
        qtd.value = j
        seq.value = int(e)
        page.update()
    
    def addnewdata(e):
        while True:
            if (prod.value in produtos_list): 
                #produto já esta na lista
                page.snack_bar = ft.SnackBar(ft.Text("Este produto já foi inserido", size=30), bgcolor="Red")
                page.snack_bar.open = True
                prod.value = ""
                qtd.value = ""
                page.update()
                break
            elif prod.value==None or qtd.value=="":
                page.snack_bar = ft.SnackBar(ft.Text("Não é permintido inserir campos em branco", size=30), bgcolor="Red")
                page.snack_bar.open = True
                prod.value = ""
                qtd.value = ""
                page.update()
                break
            else:
                #produto ainda nao esta na lista
                tabela.rows.append(
                ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(len(tabela.rows))), 
                    ft.DataCell(ft.Text(prod.value)),
                    ft.DataCell(ft.Text(qtd.value)),  
                ],
                on_select_changed = lambda e:editindex(e.control.cells[0].content.value, 
                                                        e.control.cells[1].content.value, 
                                                        e.control.cells[2].content.value)
                 )
                )
                produtos_list.append(prod.value)

                prod.value = ""
                qtd.value = ""
                page.update()
                break
            break

    def editandsave(e):
        while True:
            if prod.value==None or qtd.value=="":
                page.snack_bar = ft.SnackBar(ft.Text("Não é permintido alterar o campo para vazio", size=30), bgcolor="Red")
                page.snack_bar.open = True
                prod.value = ""
                qtd.value = ""
                page.update()
                break
            else:
                tabela.rows[seq.value].cells[2].content = ft.Text(qtd.value)
                page.snack_bar = ft.SnackBar(ft.Text("Item editado com sucesso", size=30), bgcolor="Green")
                page.snack_bar.open = True
                prod.value = ""
                qtd.value = ""
                page.update()
                order_index()#fundamental
                break
            break   
    
    def removeindex(e):
        produtos_list.remove(prod.value)#delete da lista antes da tabela
        del tabela.rows[seq.value]        
        page.snack_bar = ft.SnackBar(ft.Text("Item excluido com sucesso", size=30), bgcolor="Red")
        page.snack_bar.open = True
        prod.value = ""
        qtd.value = ""
        page.update()
        order_index()
    
    def order_index():
        i=0
        for i in range(len(tabela.rows)):
            tabela.rows[i].cells[0].content = ft.Text(str(i))
            i+=1
        page.update()     
    
    def show_info(e):
        #codigo de barra e fornecedor por enquanto# 
        if prod.value=='produto1':
            dlg = ft.AlertDialog(title=ft.Text('produto1'), content=ft.Text('Fornecedor: CERPA S/A\nCod. Barras: 111'))
            page.open(dlg)
        elif prod.value=='produto2':
            dlg = ft.AlertDialog(title=ft.Text('produto2'), content=ft.Text('Fornecedor: CERPA S/A\nCod. Barras: 222'))
            page.open(dlg)
        elif prod.value=='produto3':
            dlg = ft.AlertDialog(title=ft.Text('produto3'), content=ft.Text('Fornecedor: CERPA S/A\nCod. Barras: 333'))
            page.open(dlg)

    def convert(e):
        g = open(r"\storage\emulated\0\Download\arq.csv", "w")
        try:
            g.write("")
        finally:
            g.close()
        f = open(r"\storage\emulated\0\Download\arq.csv", "a")
        for i in range(len(tabela.rows)):    
          produto = tabela.rows[i].cells[1].content.value #produto
          quantidade = tabela.rows[i].cells[2].content.value #quantidade
          linha = produto + "," + quantidade + "\n"
          f.write(linha)
        page.snack_bar = ft.SnackBar(ft.Text("arquivo exportado com sucesso", size=30), bgcolor="blue")
        page.snack_bar.open = True
        page.update()
        f.close()
          
    #botoes
    addButton = ft.ElevatedButton("Adicionar", bgcolor="blue", color="black", on_click=addnewdata)
    deletebutton = ft.ElevatedButton("Excluir", bgcolor="red", color="black", on_click=removeindex)
    editbutton = ft.ElevatedButton("Editar", bgcolor="orange", color="black", on_click=editandsave)
    export = ft.ElevatedButton("Exportar", bgcolor="green", color="black", on_click=convert)
    info = ft.IconButton(icon=ft.icons.DIALPAD, on_click=show_info, data=prod.value) #DETAILS BALLOT DIALPAD  data=prod.value#

    #front do app#
    page.add(
        ft.Column([
            ft.Text("Digitação", size=40, weight="bold"),
            prod,
            qtd,
            info,
            ft.Row([addButton, deletebutton, editbutton]),
            tabela,
            export
        ])
    )

ft.app(target=main)