import flet as ft
from pages.timeline import timeline_page
from pages.matlab import matlab_page
from pages.blog import blog_page
from pages.github import github_page

ACCENT = "#58a6ff"
TEAL   = "#0cb5a1"
PURPLE = "#a371f7"
BG     = "#0d1117"
CARD   = "#161b22"
BORDER = "#30363d"
TEXT   = "#e6edf3"
MUTED  = "#8b949e"


def main(page: ft.Page):
    page.title = "Pokolo Ananias — Portfolio 2026"
    page.bgcolor = BG
    page.padding = 0
    page.scroll = "auto"
    page.fonts = {}

    nav_buttons = []
    active_index = [0]

    # Top accent stripe
    top_stripe = ft.Container(
        height=3,
        gradient=ft.LinearGradient(
            colors=[PURPLE, ACCENT, TEAL],
            begin=ft.alignment.center_left,
            end=ft.alignment.center_right,
        ),
    )

    def switch_page(index):
        if active_index[0] == index:
            return
        active_index[0] = index
        for i, btn in enumerate(nav_buttons):
            btn.style = ft.ButtonStyle(
                color=ACCENT if i == index else MUTED,
                overlay_color="#58a6ff11",
                padding=ft.padding.symmetric(horizontal=16, vertical=10),
            )
            btn.update()
        builders = [
            lambda: timeline_page(page),
            lambda: matlab_page(page),
            lambda: blog_page(),
            lambda: github_page(page),
        ]
        content_area.controls.clear()
        content_area.controls.append(builders[index]())
        page.update()

    labels = [
        ("🗓", "Timeline"),
        ("🔢", "MATLAB"),
        ("📝", "Blog"),
        ("🐙", "GitHub"),
    ]

    for i, (icon, label) in enumerate(labels):
        btn = ft.TextButton(
            content=ft.Row(
                controls=[
                    ft.Text(icon, size=14),
                    ft.Text(label, size=13, weight="bold" if i == 0 else "normal"),
                ],
                spacing=6,
                tight=True,
            ),
            on_click=lambda e, idx=i: switch_page(idx),
            style=ft.ButtonStyle(
                color=ACCENT if i == 0 else MUTED,
                overlay_color="#58a6ff11",
                padding=ft.padding.symmetric(horizontal=16, vertical=10),
            ),
        )
        nav_buttons.append(btn)

    logo = ft.Row(
        controls=[
            ft.Container(
                content=ft.Text("PA", size=13, color=BG, weight="bold"),
                bgcolor=ACCENT,
                border_radius=8,
                width=32, height=32,
                alignment=ft.alignment.center,
            ),
            ft.Column(
                controls=[
                    ft.Text("Pokolo Ananias", size=14, color=TEXT, weight="bold"),
                    ft.Text("Portfolio 2026", size=10, color=MUTED),
                ],
                spacing=0,
            ),
        ],
        spacing=10,
        vertical_alignment="center",
    )

    navbar = ft.Container(
        content=ft.Row(
            controls=[
                logo,
                ft.Row(controls=nav_buttons, spacing=2),
            ],
            alignment="spaceBetween",
            vertical_alignment="center",
        ),
        bgcolor=CARD,
        border=ft.border.only(bottom=ft.BorderSide(1, BORDER)),
        padding=ft.padding.symmetric(horizontal=32, vertical=10),
    )

    content_area = ft.Column(
        controls=[timeline_page(page)],
        scroll="auto",
        expand=True,
    )

    page.add(top_stripe)
    page.add(navbar)
    page.add(
        ft.Container(
            content=content_area,
            padding=ft.padding.symmetric(horizontal=32, vertical=24),
            expand=True,
        )
    )


ft.app(target=main, port=3000, view="web_browser", assets_dir="assets")
