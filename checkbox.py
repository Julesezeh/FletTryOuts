import flet as ft

def main(page: ft.Page):
    def ticked_box_handler(e):
        if todo_checkbox.value:
            previous_label =  todo_checkbox.label
            output_text.value = f"Done with task--> {previous_label}"
            page.update()
        else:
            output_text.value = ""
            page.update()

    output_text = ft.Text()
    header = ft.Text("TO-DO LIST")
    todo_checkbox = ft.Checkbox(label="ToDo: Wash Plates", value=False, on_change=ticked_box_handler)

    page.add(todo_checkbox,output_text)

ft.app(target=main)