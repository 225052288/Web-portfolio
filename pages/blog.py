import flet as ft

BLOG_POSTS = [
    {
        "id": 1,
        "title": "Understanding Variables & Data Types in Python",
        "date": "15 Feb 2026",
        "tags": ["Python", "Fundamentals"],
        "body": [
            "A variable is a named container that stores a value in memory. Python is dynamically typed — the interpreter infers the type at runtime.",
            "The four primitive types you'll use most often are: int (whole numbers), float (decimals), str (text), and bool (True/False).",
            "Type coercion lets you convert between types using int(), float(), and str(). Always validate user input before coercion to avoid ValueError exceptions.",
        ],
        "video_url": "https://www.youtube.com/embed/cQT33yu9pY8",
        "video_caption": "Python Variables – CS Dojo",
    },
    {
        "id": 2,
        "title": "Control Flow: Conditionals & Loops",
        "date": "17 Apr 2026",
        "tags": ["Python", "Control Flow"],
        "body": [
            "Control flow determines the order statements execute. Python provides conditionals (if/elif/else) and loops (for / while).",
            "for loops iterate over any iterable — lists, ranges, strings, dicts. while loops repeat as long as a condition holds.",
            "break exits a loop early; continue skips the rest of the current iteration. Together they give fine-grained control over iteration.",
        ],
        "video_url": "https://www.youtube.com/embed/6iF8Xb7Z3wQ",
        "video_caption": "Python Loops Explained",
    },
    {
        "id": 3,
        "title": "Functions: Reusable Blocks of Logic",
        "date": "1 Mar 2026",
        "tags": ["Python", "Functions"],
        "body": [
            "A function is a named, reusable block of code that accepts inputs (parameters) and returns an output.",
            "Key concepts: default parameters, *args and **kwargs for variable-length argument lists, and scope (variables inside a function are local).",
            "Defining logic in functions follows the DRY principle — Don't Repeat Yourself — making code easier to test and maintain.",
        ],
        "video_url": "https://www.youtube.com/embed/9Os0o3wzS_I",
        "video_caption": "Python Functions – Programming with Mosh",
    },
]

TAG_COLORS = {
    "Python": "#58a6ff",
    "Fundamentals": "#58a6ff",
    "Control Flow": "#58a6ff",
    "Functions": "#58a6ff",
}


def blog_page():
    def tag_chip(tag):
        color = TAG_COLORS.get(tag, "#30363d")
        return ft.Container(
            content=ft.Text(tag, size=11, color=color),
            bgcolor="#0d1117",
            border=ft.border.all(1, color),
            border_radius=20,
            padding=ft.padding.symmetric(horizontal=10, vertical=3),
        )

    def post_card(post):
        body_controls = [
            ft.Text(f"  {line}", size=13, color="#c9d1d9")
            for line in post["body"]
        ]

        return ft.Container(
            content=ft.Column(
                controls=[
                    ft.Row(
                        controls=[
                            ft.Text(post["title"], size=17, color="#e6edf3", weight="bold", expand=True),
                            ft.Text(post["date"], size=11, color="#484f58"),
                        ],
                    ),
                    ft.Row(controls=[tag_chip(t) for t in post["tags"]], spacing=6),
                    ft.Divider(color="#21262d"),
                    ft.Column(controls=body_controls, spacing=6),
                    ft.Divider(color="#21262d"),
                    ft.Text("📺 Video Reference", size=13, color="#8b949e", weight="bold"),
                    ft.Container(
                        content=ft.Text(
                            f"▶  {post['video_caption']}\n{post['video_url']}",
                            size=12,
                            color="#58a6ff",
                        ),
                        bgcolor="#0d1117",
                        border=ft.border.all(1, "#30363d"),
                        border_radius=8,
                        padding=12,
                    ),
                    ft.Text(
                        "Note: Copy the URL above into your browser to watch the video.",
                        size=11,
                        color="#484f58",
                        italic=True,
                    ),
                ],
                spacing=12,
            ),
            bgcolor="#161b22",
            border=ft.border.all(1, "#30363d"),
            border_radius=10,
            padding=24,
        )

    return ft.Column(
        controls=[
            ft.Text("Technical Blog", size=28, color="#e6edf3", weight="bold"),
            ft.Text(
                "Confidence in Concepts — written explanations of core programming ideas, each paired with a curated video.",
                size=14,
                color="#8b949e",
            ),
            ft.Divider(color="#21262d"),
            ft.Column(controls=[post_card(p) for p in BLOG_POSTS], spacing=24),
        ],
        spacing=20,
        scroll="auto",
    )
