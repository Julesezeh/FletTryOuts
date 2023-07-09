import flet as ft
import time

def main(page: ft.Page):
    for i in range(10):
        page.controls.append(ft.Text(value=f"Text number {i}"))
        if i>4:
            page.controls.pop(0)
        page.update()
        time.sleep(1)

ft.app(target=main)