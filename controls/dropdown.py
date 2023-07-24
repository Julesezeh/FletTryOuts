import flet as ft

def main(page: ft.Page):
    def event_handler(e):
        output_text.value = f"Your choice is {dropdown.value}"
        page.update()
    output_text = ft.Text()
    submit_button = ft.ElevatedButton("Make choice", on_click=event_handler)
    dropdown = ft.Dropdown(
        width=100,
        options=[
            ft.dropdown.Option("Pink"),
            ft.dropdown.Option("Red"),
            ft.dropdown.Option("Purple"),
            ft.dropdown.Option("Green")
        ]
    )

    page.add(dropdown,submit_button,output_text)


ft.app(target=main)