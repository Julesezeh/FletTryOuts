import flet as ft

def main(page: ft.Page):
    def event_handler(e):
        if not first_name.value:
            first_name.error_text = "Please enter your firstname"
            page.update()
        else:
            name = first_name.value
            page.clean()
            page.add(ft.Text(f"Hello Cabron {name}"))
            page.update()

    first_name = ft.TextField(label="First name") 
    page.add(
        first_name,
        ft.ElevatedButton("Say Hello", on_click=event_handler),
        )

ft.app(target=main)