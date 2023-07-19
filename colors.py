import flet as ft 

#access flet's available colors from flet.colors.{COLOR_CHOICE}

def main(page: ft.Page):
    def handler(e):
        value = welcome.value
        welcome.value = ""
        page.add(ft.Text(f"Hola {value}", size=80,color=ft.colors.GREEN_400))
        page.update()
        welcome.focus() 
    
    welcome = ft.TextField(label="Como te llamas?", text_size=100, color=ft.colors.GREEN_400)
    page.add(welcome,
             ft.ElevatedButton("Submit", on_click=handler))



    page.theme = ft.Theme(
        color_scheme=ft.ColorScheme(
        primary=ft.colors.GREEN,
        primary_container=ft.colors.GREEN_400
        )
    )
    page.update()


ft.app(target=main)