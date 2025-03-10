import flet as ft

current_password = ""
stored_password = ""

def main(page: ft.Page):
    def on_button_click(e):
        global current_password
        current_password += e.control.data
        status_text.value = ""
        page.update()

    def set_password(e):
        global stored_password, current_password
        stored_password = current_password
        status_text.value = "New password saved."
        current_password = ""
        page.update()

    def verify_password(e):
        global current_password, stored_password
        if current_password == stored_password:
            status_text.value = "Password correct."
        else:
            status_text.value = "Password incorrect."
        current_password = ""
        page.update()

    def change_password(e):
        global stored_password, current_password
        stored_password = current_password
        status_text.value = "Password changed."
        current_password = ""
        page.update()
        
    status_text = ft.Text("")

    button_1 = ft.FilledButton(text="1", width=55, height=55, data="1", on_click=on_button_click)
    button_2 = ft.FilledButton(text="2", width=55, height=55, data="2", on_click=on_button_click)
    button_3 = ft.FilledButton(text="3", width=55, height=55, data="3", on_click=on_button_click)
    button_4 = ft.FilledButton(text="4", width=55, height=55, data="4", on_click=on_button_click)
    button_5 = ft.FilledButton(text="5", width=55, height=55, data="5", on_click=on_button_click)
    button_6 = ft.FilledButton(text="6", width=55, height=55, data="6", on_click=on_button_click)
    button_7 = ft.FilledButton(text="7", width=55, height=55, data="7", on_click=on_button_click)
    button_8 = ft.FilledButton(text="8", width=55, height=55, data="8", on_click=on_button_click)
    button_9 = ft.FilledButton(text="9", width=55, height=55, data="9", on_click=on_button_click)

    set_button = ft.FilledButton(text="Set Password", on_click=set_password)
    verify_button = ft.FilledButton(text="Verify Password", on_click=verify_password)
    change_button = ft.FilledButton(text="Change Password", on_click=change_password)

    column_1 = ft.Column(controls=[button_1, button_4, button_7])
    column_2 = ft.Column(controls=[button_2, button_5, button_8])
    column_3 = ft.Column(controls=[button_3, button_6, button_9])
    row = ft.Row(controls=[column_1, column_2, column_3])

    page.add(row, status_text, set_button, verify_button, change_button)

ft.app(target=main)


