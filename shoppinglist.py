import flet as ft

def main(page: ft.Page):
    page.title = "Shopping List App"
    page.scroll = ft.ScrollMode.AUTO

    shopping_list = []

    def update_list():
        list_view.controls.clear()
        for item in shopping_list:
            list_view.controls.append(ft.ListTile(title=ft.Text(item)))
        page.update()

    def add_item(e):
        item_name = item_input.value.strip()
        if not item_name:
            page.snack_bar = ft.SnackBar(ft.Text("Item name cannot be empty!"), open=True)
        else:
            shopping_list.append(item_name)
            item_input.value = ""
            update_list()

    def remove_item(e):
        if not shopping_list:
            page.snack_bar = ft.SnackBar(ft.Text("The list is empty!"), open=True)
        else:
            try:
                selected_index = int(selected_item.value)
                shopping_list.pop(selected_index)
                selected_item.value = ""
                update_list()
            except (ValueError, IndexError):
                page.snack_bar = ft.SnackBar(ft.Text("Invalid selection!"), open=True)

    def clear_list(e):
        if not shopping_list:
            page.snack_bar = ft.SnackBar(ft.Text("The list is already empty!"), open=True)
        else:
            shopping_list.clear()
            update_list()

    item_input = ft.TextField(label="Item Name:", expand=True)
    add_button = ft.ElevatedButton("Add Item", on_click=add_item)
    selected_item = ft.TextField(label="Selected Index to Remove (from 0):")
    remove_button = ft.ElevatedButton("Remove Selected Item", on_click=remove_item)
    clear_button = ft.ElevatedButton("Clear All Items", on_click=clear_list)

    list_view = ft.Column(scroll=ft.ScrollMode.AUTO, expand=True)

    page.add(
        ft.Column([
            ft.Row([item_input, add_button], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
            ft.Row([selected_item, remove_button], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
            clear_button,
            ft.Divider(),
            list_view,
        ], expand=True)
    )

ft.app(target=main)
