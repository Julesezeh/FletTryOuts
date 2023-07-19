import flet as ft


def main(page: ft.Page):
    first_name = ft.Ref[ft.TextField]()
    last_name = ft.Ref[ft.TextField]()
    greetings = ft.Ref[ft.Column]()

    def make_greeting(e):
        greetings.current.controls.append(ft.Text(f"Hello {first_name.current.value} of house {last_name.current.value}"))
        first_name.current.value = ""
        last_name.current.value = ""
        page.update()
        first_name.current.focus()



    page.add(
        ft.TextField(ref=first_name,label='First name', autofocus = True),
        ft.TextField(ref=last_name,label="Last name"),
        ft.Column(ref=greetings),
        ft.ElevatedButton("Say Hello", on_click=make_greeting)
    )

ft.app(target=main)