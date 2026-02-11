import flet as ft

def main(page: ft.Page):
    page.title = "Meu Primeiro app Flet"
    page.bgcolor = "#118df2"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.add(
        ft.Text(value="Victor"),
        ft.ElevatedButton('Clique aqui')

    )

ft.run(main)
    
