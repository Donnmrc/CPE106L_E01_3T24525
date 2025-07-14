import flet as ft
import httpx

API_BASE = "http://127.0.0.1:8000"
DEFAULT_USER = "test123"

# Reusable accent color
ACCENT = ft.Colors.BLUE_100
FONT_COLOR = ft.Colors.GREY_900

def mood_view(page):
    mood_dropdown = ft.Dropdown(
        label="Mood",
        options=[
            ft.dropdown.Option("Happy"),
            ft.dropdown.Option("Sad"),
            ft.dropdown.Option("Stressed"),
            ft.dropdown.Option("Calm"),
        ],
        filled=True,
        bgcolor=ACCENT,
        border_radius=8
    )
    tags_field = ft.TextField(
        label="Tags (comma-separated)",
        filled=True,
        bgcolor=ACCENT,
        border_radius=8
    )

    def submit_mood(e):
        httpx.post(f"{API_BASE}/mood", json={
            "username": DEFAULT_USER,
            "mood": mood_dropdown.value,
            "tags": tags_field.value.split(",")
        })
        page.go("/journal")

    return ft.View(
        "/mood",
        controls=[
            ft.Text("Mood Check-In", size=24, weight=ft.FontWeight.BOLD, color=FONT_COLOR),
            mood_dropdown,
            tags_field,
            ft.ElevatedButton("Submit", on_click=submit_mood, bgcolor=ft.Colors.BLUE_300, color=ft.Colors.WHITE),
        ],
        padding=20,
        spacing=20,
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )

def journal_view(page):
    journal_field = ft.TextField(
        label="Write your thoughts...",
        multiline=True,
        height=200,
        filled=True,
        bgcolor=ACCENT,
        border_radius=8
    )

    def save_journal(e):
        httpx.post(f"{API_BASE}/journal", json={
            "username": DEFAULT_USER,
            "content": journal_field.value
        })
        page.go("/insights")

    return ft.View(
        "/journal",
        controls=[
            ft.Text("Journal Entry", size=24, weight=ft.FontWeight.BOLD, color=FONT_COLOR),
            journal_field,
            ft.ElevatedButton("Save", on_click=save_journal, bgcolor=ft.Colors.BLUE_300, color=ft.Colors.WHITE),
        ],
        padding=20,
        spacing=20,
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )

def insights_view(page):
    stats_column = ft.Column(scroll=ft.ScrollMode.AUTO)

    def load_stats():
        try:
            response = httpx.get(f"{API_BASE}/stats", params={"username": DEFAULT_USER})
            stats = response.json()["mood_stats"]
            stats_column.controls.clear()
            for mood, count in stats.items():
                stats_column.controls.append(ft.Text(f"{mood}: {count}", color=FONT_COLOR, size=18))
            page.update()
        except Exception as err:
            page.snack_bar = ft.SnackBar(ft.Text(str(err)))
            page.snack_bar.open = True
            page.update()

    return ft.View(
        "/insights",
        controls=[
            ft.Text("Mood Insights", size=24, weight=ft.FontWeight.BOLD, color=FONT_COLOR),
            ft.ElevatedButton("Load Stats", on_click=lambda _: load_stats(), bgcolor=ft.Colors.BLUE_200),
            stats_column,
            ft.ElevatedButton("Back to Mood", on_click=lambda _: page.go("/mood"), bgcolor=ft.Colors.GREY_200),
        ],
        padding=20,
        spacing=20,
        vertical_alignment=ft.MainAxisAlignment.START
    )

def main(page: ft.Page):
    page.title = "Mindful Balance"
    page.window_width = 400
    page.window_height = 600
    page.window_resizable = False
    page.bgcolor = ft.Colors.WHITE

    def route_change(e: ft.RouteChangeEvent):
        page.views.clear()
        if page.route == "/mood":
            page.views.append(mood_view(page))
        elif page.route == "/journal":
            page.views.append(journal_view(page))
        elif page.route == "/insights":
            page.views.append(insights_view(page))
        else:
            page.go("/mood")

        page.update()

    page.on_route_change = route_change
    page.go(page.route)

ft.app(target=main)
