import flet as ft
import threading
import time
import base64
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def load_b64(filename):
    # Try both .jpeg and .jpg extensions
    for name in [filename, filename.replace(".jpg", ".jpeg"), filename.replace(".jpeg", ".jpg")]:
        path = os.path.join(BASE_DIR, "assets", name)
        try:
            with open(path, "rb") as f:
                return base64.b64encode(f.read()).decode("utf-8")
        except Exception:
            continue
    return None


TIMELINE_ENTRIES = [
    {
        "week": "Week 1",
        "date": "13 Mar – 26 Mar 2026",
        "title": "Distribution Of Roles",
        "contributions": [
            "it focuses making the software easy to use.",
            "creates mwireframes or mockups before coding begins.",
        ],
        "module": "UI/UX LEADER",
        "commits": 3,
        "icon": "🎨",
    },
    {
        "week": "Week 6",
        "date": "3 – 16 May 2026",
        "title": "Attempted File Submissions",
        "contributions": [
            "Submitted the UI documentation report.",
            "Reviewed design handoff with dev team.",
        ],
        "module": "UI/UX LEADER",
        "commits": 12,
        "icon": "📁",
    },
]

MODULE_COLORS = {
    "UI/UX LEADER": "#0cb5a1",
    "Portfolio / Assessment": "#a371f7",
}

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


def timeline_page(page: ft.Page = None):
    total_commits = sum(e["commits"] for e in TIMELINE_ENTRIES)
    profile_b64 = load_b64("profile_nobg.jpeg")

    # ── Animated photo with glowing rings ─────────────────────────────────────
    photo_content = (
        ft.Image(src_base64=profile_b64, width=170, height=170, fit="cover")
        if profile_b64
        else ft.Text("PA", size=48, color="#fff", weight="bold")
    )

    photo_circle = ft.Container(
        content=photo_content,
        width=170, height=170,
        border_radius=85,
        clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
        bgcolor=BG,
    )

    ring1 = ft.Container(
        width=182, height=182, border_radius=91,
        border=ft.border.all(2, ACCENT),
        opacity=1.0,
        animate_opacity=ft.animation.Animation(900, "easeInOut"),
        shadow=ft.BoxShadow(blur_radius=16, color="#58a6ff55", spread_radius=2),
    )
    ring2 = ft.Container(
        width=196, height=196, border_radius=98,
        border=ft.border.all(1, TEAL + "66"),
        opacity=0.5,
        animate_opacity=ft.animation.Animation(1100, "easeInOut"),
    )
    ring3 = ft.Container(
        width=210, height=210, border_radius=105,
        border=ft.border.all(1, PURPLE + "33"),
        opacity=0.3,
        animate_opacity=ft.animation.Animation(1300, "easeInOut"),
    )

    def sparkle(size, color):
        return ft.Container(
            width=size, height=size, bgcolor=color,
            border_radius=size // 2, opacity=0.0,
            animate_opacity=ft.animation.Animation(400, "easeInOut"),
            shadow=ft.BoxShadow(blur_radius=6, color=color, spread_radius=1),
        )

    sps = [
        sparkle(10, ACCENT), sparkle(7, "#ffffff"),
        sparkle(10, TEAL),   sparkle(7, ACCENT),
        sparkle(6, "#ffffff"),sparkle(6, TEAL),
        sparkle(5, "#ffffff"),sparkle(5, ACCENT),
    ]
    sp_n, sp_e, sp_s, sp_w, sp_ne, sp_nw, sp_se, sp_sw = sps

    photo_stack = ft.Stack(
        width=220, height=220,
        controls=[
            ft.Container(content=ring3, alignment=ft.alignment.center, width=220, height=220),
            ft.Container(content=ring2, alignment=ft.alignment.center, width=220, height=220),
            ft.Container(content=ring1, alignment=ft.alignment.center, width=220, height=220),
            ft.Container(content=photo_circle, alignment=ft.alignment.center, width=220, height=220),
            ft.Container(content=sp_n,  top=3,    left=105),
            ft.Container(content=sp_s,  bottom=3, left=105),
            ft.Container(content=sp_e,  top=106,  right=3),
            ft.Container(content=sp_w,  top=106,  left=3),
            ft.Container(content=sp_ne, top=24,   right=24),
            ft.Container(content=sp_nw, top=24,   left=24),
            ft.Container(content=sp_se, bottom=24,right=24),
            ft.Container(content=sp_sw, bottom=24,left=24),
        ],
    )

    def shine():
        while True:
            try:
                ring1.opacity = 1.0; ring1.update()
                ring2.opacity = 0.9; ring2.update()
                ring3.opacity = 0.7; ring3.update()
                time.sleep(0.25)
                for sp in sps:
                    sp.opacity = 1.0; sp.update(); time.sleep(0.06)
                time.sleep(0.35)
                for sp in sps:
                    sp.opacity = 0.0; sp.update(); time.sleep(0.04)
                ring1.opacity = 0.3; ring1.update()
                ring2.opacity = 0.12; ring2.update()
                ring3.opacity = 0.08; ring3.update()
                time.sleep(1.1)
            except Exception:
                break

    threading.Thread(target=shine, daemon=True).start()

    # ── HERO — centered, tall, bold ───────────────────────────────────────────
    def badge(text, color, bg="#0d1f38"):
        return ft.Container(
            content=ft.Text(text, size=11, color=color, weight="bold"),
            bgcolor=bg,
            border=ft.border.all(1, color),
            border_radius=20,
            padding=ft.padding.symmetric(horizontal=14, vertical=5),
        )

    hero_bg = ft.Container(
        content=ft.Image(src_base64=profile_b64, fit="cover", width=2000, height=380)
        if profile_b64 else ft.Container(bgcolor=CARD),
        width=2000, height=380,
        clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
        opacity=0.18,
    )

    hero_overlay = ft.Container(
        bgcolor="#0d111799",
        width=2000, height=380,
    )

    # Decorative gradient bar at bottom of hero
    accent_bar = ft.Container(
        height=3,
        gradient=ft.LinearGradient(
            colors=[PURPLE, ACCENT, TEAL],
            begin=ft.alignment.center_left,
            end=ft.alignment.center_right,
        ),
    )

    hero_fg = ft.Container(
        content=ft.Column(
            controls=[
                photo_stack,
                ft.Text("Pokolo Ananias", size=34, color=TEXT, weight="bold",
                        text_align="center"),
                ft.Text("225052288  •  UNAM", size=13, color=MUTED, text_align="center"),
                ft.Row(
                    controls=[
                        badge("🎨  UI/UX Leader", ACCENT),
                        badge("🚀  BLAST MASTER PRO  •  GRP 10", TEAL),
                        badge("🎓  UNAM", "#e03131", "#2d0000"),
                    ],
                    alignment="center",
                    wrap=True,
                    spacing=10,
                    run_spacing=8,
                ),
            ],
            horizontal_alignment="center",
            spacing=14,
        ),
        alignment=ft.alignment.center,
        height=380,
    )

    hero = ft.Container(
        content=ft.Column(
            controls=[
                ft.Stack(
                    controls=[hero_bg, hero_overlay, hero_fg],
                    height=380,
                ),
                accent_bar,
            ],
            spacing=0,
        ),
        border_radius=14,
        clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
        border=ft.border.all(1, BORDER),
        shadow=ft.BoxShadow(blur_radius=32, color="#58a6ff22", spread_radius=2),
    )

    # ── Stat cards ─────────────────────────────────────────────────────────────
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

    stats_row = ft.Row(
        controls=[
            stat_card(len(TIMELINE_ENTRIES), "Weeks Logged", ACCENT, "📅"),
            stat_card(total_commits, "Total Commits", TEAL, "💻"),
            stat_card(4, "PRs Authored", PURPLE, "🔀"),
            stat_card(2, "PRs Reviewed", GOLD, "👁"),
        ],
        spacing=14,
    )

    # ── Timeline section ────────────────────────────────────────────────────────
    card_refs = []

    def entry_card(entry, idx):
        color = MODULE_COLORS.get(entry["module"], BORDER)
        is_left = idx % 2 == 0

        def on_hover(e):
            e.control.border = ft.border.all(1, color if e.data == "true" else BORDER)
            e.control.shadow = (
                ft.BoxShadow(blur_radius=22, color=color + "44", spread_radius=1)
                if e.data == "true" else None
            )
            e.control.scale = ft.transform.Scale(1.01) if e.data == "true" else ft.transform.Scale(1.0)
            e.control.update()

        contributions_col = ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        ft.Container(
                            width=6, height=6,
                            bgcolor=color,
                            border_radius=3,
                            margin=ft.margin.only(top=4),
                        ),
                        ft.Text(c, size=13, color="#c9d1d9", expand=True),
                    ],
                    spacing=10,
                    vertical_alignment="start",
                )
                for c in entry["contributions"]
            ],
            spacing=8,
        )

        card = ft.Container(
            content=ft.Column(
                controls=[
                    ft.Row(
                        controls=[
                            ft.Text(entry["icon"], size=20),
                            ft.Column(
                                controls=[
                                    ft.Text(entry["title"], size=15, color=TEXT, weight="bold"),
                                    ft.Text(
                                        f"{entry['week']}  •  {entry['date']}",
                                        size=11, color=DIM,
                                    ),
                                ],
                                spacing=2,
                                expand=True,
                            ),
                            ft.Container(
                                content=ft.Text(
                                    entry["module"], size=10, color=color, weight="bold"
                                ),
                                bgcolor=BG,
                                border=ft.border.all(1, color),
                                border_radius=20,
                                padding=ft.padding.symmetric(horizontal=10, vertical=3),
                            ),
                        ],
                        spacing=12,
                        vertical_alignment="center",
                    ),
                    ft.Container(
                        height=1,
                        bgcolor=BORDER,
                        margin=ft.margin.symmetric(vertical=4),
                    ),
                    contributions_col,
                    ft.Row(
                        controls=[
                            ft.Container(
                                content=ft.Text(
                                    f"⬡  {entry['commits']} commit{'s' if entry['commits'] != 1 else ''}",
                                    size=11, color=color,
                                ),
                                bgcolor=color + "18",
                                border_radius=6,
                                padding=ft.padding.symmetric(horizontal=10, vertical=4),
                            ),
                        ],
                    ),
                ],
                spacing=10,
            ),
            padding=20,
            bgcolor=CARD,
            border=ft.border.all(1, BORDER),
            border_radius=12,
            on_hover=on_hover,
            opacity=0,
            offset=ft.transform.Offset(-0.1 if is_left else 0.1, 0),
            animate_opacity=ft.animation.Animation(550, "easeOut"),
            animate_offset=ft.animation.Animation(550, "easeOut"),
            animate_scale=ft.animation.Animation(200, "easeOut"),
        )
        card_refs.append(card)
        return card

    # Timeline with a visual connector line
    timeline_items = []
    for idx, entry in enumerate(TIMELINE_ENTRIES):
        color = MODULE_COLORS.get(entry["module"], BORDER)
        dot = ft.Container(
            content=ft.Container(
                width=14, height=14,
                bgcolor=color,
                border_radius=7,
                shadow=ft.BoxShadow(blur_radius=8, color=color + "88", spread_radius=1),
            ),
            width=30,
            alignment=ft.alignment.center,
        )
        line = ft.Container(
            width=2, bgcolor=BORDER, height=24,
            margin=ft.margin.only(left=14),
        ) if idx < len(TIMELINE_ENTRIES) - 1 else ft.Container()

        row = ft.Row(
            controls=[
                ft.Column(
                    controls=[dot, line],
                    spacing=0,
                    horizontal_alignment="center",
                ),
                ft.Container(content=entry_card(entry, idx), expand=True),
            ],
            spacing=14,
            vertical_alignment="start",
        )
        timeline_items.append(row)

    def animate_cards():
        time.sleep(0.5)
        for card in card_refs:
            time.sleep(0.2)
            card.opacity = 1
            card.offset = ft.transform.Offset(0, 0)
            try:
                card.update()
            except Exception:
                pass

    threading.Thread(target=animate_cards, daemon=True).start()

    # ── Skills strip ────────────────────────────────────────────────────────────
    skills = ["Figma", "UI/UX", "Firebase", "Flutter", "Python", "Git"]
    skill_chips = ft.Row(
        controls=[
            ft.Container(
                content=ft.Text(s, size=12, color=MUTED),
                bgcolor=CARD,
                border=ft.border.all(1, BORDER),
                border_radius=20,
                padding=ft.padding.symmetric(horizontal=14, vertical=6),
            )
            for s in skills
        ],
        wrap=True,
        spacing=8,
        run_spacing=8,
    )

    section_label = ft.Container(
        content=ft.Row(
            controls=[
                ft.Container(width=4, height=22, bgcolor=ACCENT, border_radius=2),
                ft.Text("Weekly Contributions", size=20, color=TEXT, weight="bold"),
            ],
            spacing=10,
            vertical_alignment="center",
        ),
    )

    return ft.Column(
        controls=[
            hero,
            stats_row,
            ft.Container(
                content=ft.Column(
                    controls=[
                        ft.Text("Skills", size=13, color=MUTED, weight="bold"),
                        skill_chips,
                    ],
                    spacing=10,
                ),
                bgcolor=CARD,
                border=ft.border.all(1, BORDER),
                border_radius=12,
                padding=20,
            ),
            section_label,
            ft.Column(controls=timeline_items, spacing=0),
        ],
        spacing=20,
        scroll="auto",
    )
