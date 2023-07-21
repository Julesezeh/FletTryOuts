import flet as ft
import os

os.environ["FLET_WS_MAX_MESSAGE_SIZE"] =  "8000000"

def main(page: ft.Page):

    gv = ft.GridView(expand=True,max_extent=150,child_aspect_ratio=1)
    page.add(gv)
    
    for i in range(5000):
        gv.controls.append(
            ft.Container(
                ft.Text(f"Text {i}"),
                alignment=ft.alignment.center,
                bgcolor=ft.colors.TEAL_400,
                border= ft.border.all(1,ft.colors.WHITE30),
                border_radius=ft.border_radius.all(5)

            )
        )
    page.update()


ft.app(target=main)