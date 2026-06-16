import flet as ft

GITHUB_USERNAME = "Kalanatse06"
GITHUB_REPO = "BLAST MASTER PRO"
STUDENT_ID = "225052288"
ROLE = "UI/UX Developer & Firebase Engineer"
GITHUB_URL = f"https://github.com/{GITHUB_USERNAME}"
DEMO_VIDEO_URL = "https://youtu.be/d7S-Jg7diG4?si=uWY_P5dKjBhGJN4D"

COMMIT_LOG = [
    {"hash": "a1b2c3d", "message": "feat: Firebase project setup and Firestore collections created",          "date": "27 Jan 2026"},
    {"hash": "b2c3d4e", "message": "feat: Firestore security rules — request.auth != null on all collections","date": "3 Feb 2026"},
   
]

PULL_REQUESTS = [
    {"number": 3,  "title": "Firebase config, .env setup and Firestore collection initialisation", "role": "Author",   "date": "1 Feb 2026"},
 
]

IMPACT_LINES = [
    "Firebase Configuration: Set up the entire Firebase backend used by all 15 team members — Firestore collections, security rules, Storage, and .env key management. Every module depends on this foundation.",

]


def github_page(page: ft.Page = None):
    def link_button(label, icon, url, color):
        def open_link(e):
            if page is not None:
                page.launch_url(url)

        return ft.Container(
            content=ft.Row(
                controls=[
                    ft.Text(icon, size=14),
                    ft.Text(label, size=12, color=color, weight="bold"),
                ],
                spacing=8,
                tight=True,
                vertical_alignment="center",
            ),
            bgcolor="#0d1f38",
            border=ft.border.all(1, color),
            border_radius=8,
            padding=ft.padding.symmetric(horizontal=14, vertical=10),
            on_click=open_link,
            ink=True,
        )

    def stat_card(value, label, border_color):
        return ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text(str(value), size=26, color="#e6edf3", weight="bold"),
                    ft.Text(label, size=12, color="#8b949e"),
                ],
                horizontal_alignment="center",
                spacing=4,
            ),
            bgcolor="#161b22",
            border=ft.border.all(1, border_color),
            border_radius=10,
            padding=20,
            expand=True,
        )

    def commit_row(commit):
        return ft.Container(
            content=ft.Row(
                controls=[
                    ft.Container(
                        content=ft.Text(commit["hash"], size=11, color="#58a6ff"),
                        bgcolor="#0d1f38",
                        border_radius=4,
                        padding=ft.padding.symmetric(horizontal=8, vertical=2),
                    ),
                    ft.Text(commit["message"], size=13, color="#ebecee", expand=True),
                    ft.Text(commit["date"], size=11, color="#484f58"),
                ],
                spacing=12,
                vertical_alignment="center",
            ),
            border=ft.border.only(bottom=ft.BorderSide(1, "#21262d")),
            padding=ft.padding.symmetric(vertical=10),
        )

    def pr_row(pr):
        role_color = "#58a6ff" if pr["role"] == "Author" else "#8b949e"
        return ft.Container(
            content=ft.Row(
                controls=[
                    ft.Text(f"#{pr['number']}", size=12, color="#58a6ff", width=42),
                    ft.Text(pr["title"], size=13, color="#c8f8aa", expand=True),
                    ft.Container(
                        content=ft.Text(pr["role"], size=11, color=role_color),
                        bgcolor="#0d1117",
                        border=ft.border.all(1, role_color),
                        border_radius=4,
                        padding=ft.padding.symmetric(horizontal=8, vertical=2),
                    ),
                    ft.Container(
                        content=ft.Text("MERGED", size=10, color="#58a6ff"),
                        bgcolor="#67d0de",
                        border_radius=4,
                        padding=ft.padding.symmetric(horizontal=8, vertical=2),
                    ),
                    ft.Text(pr["date"], size=11, color="#296a23"),
                ],
                spacing=10,
                vertical_alignment="center",
            ),
            border=ft.border.only(bottom=ft.BorderSide(1, "#81257c")),
            padding=ft.padding.symmetric(vertical=10),
        )

    def section(title, controls_list):
        return ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text(title, size=16, color="#d98b03", weight="bold"),
                    ft.Divider(color="#1869da58"),
                    ft.Column(controls=controls_list, spacing=0),
                ],
                spacing=12,
            ),
            bgcolor="#823068",
            border=ft.border.all(1, "#c2d3e5"),
            border_radius=10,
            padding=20,
        )

    authored = sum(1 for p in PULL_REQUESTS if p["role"] == "Author")
    reviewed = sum(1 for p in PULL_REQUESTS if p["role"] == "Reviewer")

    profile = ft.Container(
        content=ft.Row(
            controls=[
                ft.Container(
                    content=ft.Text("PA", size=22, color="#ffffff", weight="bold"),
                    bgcolor="#58a6ff",
                    border_radius=30,
                    width=56,
                    height=56,
                    alignment=ft.alignment.center,
                ),
                ft.Column(
                    controls=[
                        ft.Text("Pokolo Ananias", size=18, color="#e6edf3", weight="bold"),
                        ft.Row(
                            controls=[
                                ft.Container(
                                    content=ft.Text(ROLE, size=11, color="#58a6ff", weight="bold"),
                                    bgcolor="#0d1f38",
                                    border=ft.border.all(1, "#58a6ff"),
                                    border_radius=4,
                                    padding=ft.padding.symmetric(horizontal=8, vertical=3),
                                ),
                                ft.Text(f"Group 10 BLAST MASTERS PRO  •  {STUDENT_ID}", size=12, color="#8b949e"),
                            ],
                            spacing=8,
                        ),
                    ],
                    spacing=4,
                    expand=True,
                ),
                ft.Row(
                    controls=[
                        link_button("View GitHub Profile", "🐙", GITHUB_URL, "#58a6ff"),
                        link_button("Watch Demo Video", "🎥", DEMO_VIDEO_URL, "#c8f8aa"),
                    ],
                    spacing=10,
                    wrap=True,
                ),
            ],
            spacing=16,
            vertical_alignment="center",
        ),
        bgcolor="#161b22",
        border=ft.border.all(1, "#58a6ff"),
        border_radius=10,
        padding=20,
    )

    return ft.Column(
        controls=[
            ft.Text("GitHub Evidence & Documentation", size=28, color="#e6edf3", weight="bold"),
            ft.Text("Individual contribution evidence, University of Namibia.", size=14, color="#8b949e"),
            ft.Divider(color="#21262d"),
            profile,
            ft.Row(
                controls=[
                    stat_card(len(COMMIT_LOG), "Commits", "#58a6ff"),
                    stat_card(authored, "PRs Authored", "#58a6ff"),
                    stat_card(reviewed, "PRs Reviewed", "#8b949e"),
                    stat_card(len(PULL_REQUESTS), "PRs Merged", "#58a6ff"),
                ],
                spacing=16,
            ),
            section("Commit History", [commit_row(c) for c in COMMIT_LOG]),
            section("Pull Request Log", [pr_row(p) for p in PULL_REQUESTS]),
            ft.Container(
                content=ft.Column(
                    controls=[
                        ft.Text("Impact Summary", size=16, color="#e6edf3", weight="bold"),
                        ft.Divider(color="#21262d"),
                        ft.Column(
                            controls=[
                                ft.Container(
                                    content=ft.Text(f"  {line}", size=13, color="#c9d1d9"),
                                    border=ft.border.only(left=ft.BorderSide(3, "#58a6ff")),
                                    padding=ft.padding.only(left=12, top=6, bottom=6),
                                    margin=ft.margin.only(bottom=8),
                                )
                                for line in IMPACT_LINES
                            ],
                            spacing=0,
                        ),
                    ],
                    spacing=12,
                ),
                bgcolor="#161b22",
                border=ft.border.all(1, "#30363d"),
                border_radius=10,
                padding=20,
            ),
        ],
        spacing=20,
        scroll="auto",
    )
