import random
import flet as ft

def randomize_number(start, end):
    if start >= end:
        return None, "Invalid range: Start must be less than end."
    return random.randint(int(start), int(end)), None

def main(page: ft.Page):
    range_slider = ft.RangeSlider(
        min=0,
        max=100,
        start_value=20,
        divisions=20,
        end_value=80,
        inactive_color=ft.colors.BLUE_300,
        active_color=ft.colors.BLUE_700,
        overlay_color=ft.colors.BLUE_100,
        label="{value}",
    )
    result_text = ft.Text("", size=16, color="black")

    def generate_number(e):
        start, end = range_slider.start_value, range_slider.end_value
        random_number, error = randomize_number(start, end)

        if error:
            result_text.value = error
            result_text.color = "red"
        else:
            result_text.value = f"Random Number: {random_number}"
            result_text.color = "green"
        
        page.update()

    generate_button = ft.ElevatedButton(
        text="Generate Random Number",
        on_click=generate_number
    )
    page.add(
        ft.Column(
            controls=[
                ft.Container(height=30),
                range_slider,
                generate_button,
                result_text,
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )

ft.app(main)

