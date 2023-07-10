import flet as ft

def main(page: ft.Page):
    first_name = ft.TextField(label="First Name")
    last_name = ft.TextField(label="Last Name")
    greetings = ft.Column()

    def btn_click(e):
        greetings.controls.append(ft.Text(value=f"Hello {first_name.value} {last_name.value}!"))
        first_name.value = ""
        last_name.value = ""
        page.update()
        first_name.focus()

    page.add(
        first_name,
        last_name,
        greetings,
        ft.ElevatedButton("Say Hello!", on_click=btn_click)
    )

ft.app(target=main)