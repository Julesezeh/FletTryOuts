import flet as ft

def main(page: ft.Page):
    first_name = ft.Ref[ft.TextField]()
    last_name = ft.Ref[ft.TextField]()
    greetings = ft.Ref[ft.Column]()


    def event_handler(e):
        greetings.controls.append(
            ft.Text(f"Hello {first_name.current.value} of house {last_name.current.value}")
        )
        first_name.current.value = ""
        last_name.current.value = ""
        page.update()
        first_name.current.focus()


    page.add(
        ft.TextField(ref=first_name,label="First Name", autofocus=True),
        ft.TextField(ref=last_name,label="Last Name", autofocus=True),
        ft.ElevatedButton("Say Hello!",on_click=event_handler),
        ft.Column(ref=greetings),
    )
ft.app(target=main, view=ft.WEB_BROWSER)