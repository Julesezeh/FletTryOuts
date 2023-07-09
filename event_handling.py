import flet as ft


    
def main(page: ft.Page):
    def button_clicked(e):
        page.add(ft.Text("Clicked"))

    page.add(ft.ElevatedButton(text="First name",on_click=button_clicked))

ft.app(target=main)