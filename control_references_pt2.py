import flet as ft

def main(page: ft.Page):
    first_name = ft.Ref[ft.TextField]()
    last_name = ft.Ref[ft.TextField]()
    greetings = ft.Ref[ft.Column]()


    def event_handler(e):
        greetings.controls.append(
            ft.Text(f"Hello {first_name.value} of house {last_name.value}")
        )

    pass

ft.app(target=main, view=ft.WEB_BROWSER)