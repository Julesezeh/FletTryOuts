import flet as ft

def main(page: ft.Page):
    def on_key(e: ft.KeyboardEvent):
        page.add(
            ft.Text(
            #meta is for the macbook's command key
                f"Key {e.key} :::[ Shift clicked-->{e.shift}, CNTRL clicked -->{e.ctrl},  Alt clicked-->{e.alt},   Meta clicked-->{e.meta}]"
            )
        )
    page.on_keyboard_event = on_key
    page.add(
        ft.Text("Press any key with a combination of CNTRL, Shift, ALT and Meta ")
    )


ft.app(target=main)