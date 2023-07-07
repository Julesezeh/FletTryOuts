import flet as ft

def main(page: ft.Page):
    t = ft.Text(value="Hello World", color="light green")
    page.controls.append(t)
    page.update()

ft.app(target=main)