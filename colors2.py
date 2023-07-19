import flet as ft

def main(page: ft.Page):

    page.add(
        ft.Container(
            width=300,
            height=300,
            border= ft.border.all(1,ft.colors.GREEN_200),
            content= ft.FilledButton("Primary Color"),
            theme=ft.Theme(color_scheme=ft.ColorScheme(primary=ft.colors.GREEN_300))
        )
    )

ft.app(target=main)