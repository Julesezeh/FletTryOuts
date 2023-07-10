import flet as ft

def main(page: ft.Page):
    first_name = ft.TextField(label="First name")
    last_name = ft.TextField(label="Last name")
    c = ft.Column(controls=[
        first_name,
        last_name
    ])
    c.disabled = True   

    page.add(c)

ft.app(target=main)