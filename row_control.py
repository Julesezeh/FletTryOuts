import flet as ft
import time

def main(page: ft.Page):
    page.add(ft.Row(
        controls=[
            ft.Text(value="12"),
            ft.Text(value="123")
        ]
    ))
    page.update()
    time.sleep(2)
    page.add(ft.Row(controls=[
        ft.TextField(label="Como te llamas?"),
        ft.ElevatedButton(text="Pronounce name")
    ]))
    page.update()

ft.app(target=main)