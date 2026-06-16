import flet as ft
import base64
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def load_b64(filename):
    for name in [filename, filename.replace(".jpg", ".jpeg"), filename.replace(".jpeg", ".jpg")]:
        path = os.path.join(BASE_DIR, "assets", "certificates", name)
        try:
            with open(path, "rb") as f:
                return base64.b64encode(f.read()).decode("utf-8")
        except Exception:
            continue
    return None


ACCENT = "#58a6ff"
TEAL   = "#0cb5a1"
PURPLE = "#a371f7"
GOLD   = "#e3b341"
BG     = "#0d1117"
CARD   = "#161b22"
BORDER = "#30363d"
TEXT   = "#e6edf3"
MUTED  = "#8b949e"
DIM    = "#484f58"

CERTIFICATES = [
    {
        "title": "MATLAB Onramp",
        "file": "MATLAB_ONRAMP.png",
        "percent": 100,
        "date": "27 April 2026",
        "desc": "Introductory course covering MATLAB syntax, variables, arrays, and basic plotting.",
    },
    {
        "title": "Make and Manipulate Matrices",
        "file": "Make_and_Manipulate_Matrices.png",
        "percent": 100,
        "date": "27 April 2026",
        "desc": "Creating, indexing, reshaping, and manipulating matrices in MATLAB.",
    },
    {
        "title": "Calculations with Vectors and Matrices",
        "file": "Calculations_with_Vectors___Matrices.png",
        "percent": 100,
        "date": "27 April 2026",
        "desc": "Performing element-wise and matrix operations, linear algebra fundamentals.",
    },
    {
        "title": "Explore Data with MATLAB Plots",
        "file": "Explore_Data_with_Matlab_Plots.png",
        "percent": 100,
        "date": "29 April 2026",
        "desc": "Visualizing and exploring datasets using MATLAB's plotting tools.",
    },
    {
        "title": "Simulink Onramp",
        "file": "Simulink_ONRAMP.png",
        "percent": 48,
        "date": "29 April 2026",
        "desc": "Introduction to building and simulating block diagram models in Simulink.",
    },
]


def matlab_page(page: ft.Page = None):

    def stat_card(value, label, color, icon):
        return ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text(icon, size=22),
                    ft.Text(str(value), size=28, color=TEXT, weight="bold"),
                    ft.Text(label, size=11, color=MUTED),
                ],
                horizontal_alignment="center",
                spacing=4,
            ),
            bgcolor=CARD,
            border=ft.border.all(1, color + "88"),
            border_radius=12,
            padding=ft.padding.symmetric(vertical=20, horizontal=12),
            expand=True,
            shadow=ft.BoxShadow(blur_radius=12, color=color + "22", spread_radius=1),
        )

    completed = sum(1 for c in CERTIFICATES if c["percent"] == 100)
    in_progress = sum(1 for c in CERTIFICATES if c["percent"] < 100)
    avg = round(sum(c["percent"] for c in CERTIFICATES) / len(CERTIFICATES))

    stats_row = ft.Row(
        controls=[
            stat_card(len(CERTIFICATES), "Certificates", ACCENT, "🎓"),
            stat_card(completed, "Completed", TEAL, "✅"),
            stat_card(in_progress, "In Progress", GOLD, "⏳"),
            stat_card(f"{avg}%", "Avg. Score", PURPLE, "📊"),
        ],
        spacing=14,
    )

    def cert_card(cert):
        img_b64 = load_b64(cert["file"])
        percent = cert["percent"]
        is_done = percent == 100
        badge_color = TEAL if is_done else GOLD

        image_widget = (
            ft.Image(src_base64=img_b64, width=280, height=197, fit="cover", border_radius=8)
            if img_b64
            else ft.Container(
                content=ft.Text("Certificate image\nnot found", size=12, color=MUTED, text_align="center"),
                width=280, height=197,
                bgcolor=BG,
                border_radius=8,
                alignment=ft.alignment.center,
            )
        )

        return ft.Container(
            content=ft.Row(
                controls=[
                    ft.Container(
                        content=image_widget,
                        border=ft.border.all(1, BORDER),
                        border_radius=8,
                        clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
                    ),
                    ft.Column(
                        controls=[
                            ft.Row(
                                controls=[
                                    ft.Text("MathWorks", size=11, color=ACCENT, weight="bold"),
                                    ft.Text("Training Services", size=11, color=MUTED, italic=True),
                                ],
                                spacing=6,
                            ),
                            ft.Text(cert["title"], size=17, color=TEXT, weight="bold"),
                            ft.Text(cert["desc"], size=12, color="#c9d1d9"),
                            ft.Row(
                                controls=[
                                    ft.Container(
                                        content=ft.Text(
                                            f"{'✔ ' if is_done else '⏳ '}{percent}% complete",
                                            size=11, color=badge_color, weight="bold",
                                        ),
                                        bgcolor=badge_color + "18",
                                        border=ft.border.all(1, badge_color),
                                        border_radius=20,
                                        padding=ft.padding.symmetric(horizontal=12, vertical=4),
                                    ),
                                    ft.Text(cert["date"], size=11, color=DIM),
                                ],
                                spacing=10,
                                vertical_alignment="center",
                            ),
                        ],
                        spacing=8,
                        expand=True,
                    ),
                ],
                spacing=20,
                vertical_alignment="center",
            ),
            bgcolor=CARD,
            border=ft.border.all(1, BORDER),
            border_radius=12,
            padding=20,
        )

    section_label = ft.Container(
        content=ft.Row(
            controls=[
                ft.Container(width=4, height=22, bgcolor=ACCENT, border_radius=2),
                ft.Text("MathWorks Certificates", size=20, color=TEXT, weight="bold"),
            ],
            spacing=10,
            vertical_alignment="center",
        ),
    )

    return ft.Column(
        controls=[
            ft.Text("MATLAB & Simulink", size=28, color=TEXT, weight="bold"),
            ft.Text(
                "Self-paced MathWorks training completed as part of building numerical and "
                "modelling fluency for engineering coursework.",
                size=14,
                color=MUTED,
            ),
            ft.Divider(color="#21262d"),
            stats_row,
            section_label,
            ft.Column(controls=[cert_card(c) for c in CERTIFICATES], spacing=16),
        ],
        spacing=20,
        scroll="auto",
    )
