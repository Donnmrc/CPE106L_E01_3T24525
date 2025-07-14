import flet as ft
import httpx

API_BASE = "http://127.0.0.1:8000"  # Adjust if your FastAPI runs elsewhere

# Global state
current_user = {"username": ""}

def login_view(page):
    username_field = ft.TextField(label="Username")
    password_field = ft.TextField(label="Password", password=True)

    def handle_register(e):
        try:
            response = httpx.post(f"{API_BASE}/register", json={
                "username": username_field.value,
                "password": password_field.value
            })
            if response.status_code == 200:
                current_user["username"] = username_field.value
                page.go("/mood")
            else:
                page.snack_bar = ft.SnackBar(ft.Text(response.json()["detail"]))
                page.snack_bar.open = True
                page.update()
        except Exception as err:
            page.snack_bar = ft.SnackBar(ft.Text(str(err)))
            page.snack_bar.open = True
            page.update()

    return ft.View(
        "/",
        controls=[
            ft.Text("Mindful Balance", size=24, weight=ft.FontWeight.BOLD),
            username_field,
            password_field,
            ft.Row([
                ft.ElevatedButton("Register", on_click=handle_register),
            ])
        ],
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )

def mood_view(page):
    mood_dropdown = ft.Dropdown(label="Mood", options=[
        ft.dropdown.Option("Happy"),
        ft.dropdown.Option("Sad"),
        ft.dropdown.Option("Stressed"),
        ft.dropdown.Option("Calm"),
    ])
    tags_field = ft.TextField(label="Tags (comma-separated)")

    def submit_mood(e):
        httpx.post(f"{API_BASE}/mood", json={
            "username": current_user["username"],
            "mood": mood_dropdown.value,
            "tags": tags_field.value.split(",")
        })
        page.go("/journal")

    return ft.View(
        "/mood",
        controls=[
            ft.Text("How are you feeling today?", size=20),
            mood_dropdown,
            tags_field,
            ft.ElevatedButton("Submit Mood", on_click=submit_mood)
        ]
    )

def journal_view(page):
    journal_field = ft.TextField(label="Write your thoughts...", multiline=True, height=200)

    def save_journal(e):
        httpx.post(f"{API_BASE}/journal", json={
            "username": current_user["username"],
            "content": journal_field.value
        })
        page.go("/insights")

    return ft.View(
        "/journal",
        controls=[
            ft.Text("Journal Entry", size=20),
            journal_field,
            ft.ElevatedButton("Save Entry", on_click=save_journal)
        ]
    )

def insights_view(page):
    def load_stats():
        try:
            response = httpx.get(f"{API_BASE}/stats", params={"username": current_user["username"]})
            stats = response.json()["mood_stats"]
            stat_texts = [ft.Text(f"{mood}: {count}") for mood, count in stats.items()]
            page.views[-1].controls.extend(stat_texts)
            page.update()
        except Exception as err:
            page.snack_bar = ft.SnackBar(ft.Text(str(err)))
            page.snack_bar.open = True
            page.update()

    return ft.View(
        "/insights",
        controls=[
            ft.Text("Your Mood Stats", size=20),
            ft.ElevatedButton("Load Stats", on_click=lambda _: load_stats()),
            ft.ElevatedButton("Back to Home", on_click=lambda _: page.go("/"))
        ]
    )

def main(page: ft.Page):
    page.title = "Mindful Balance"
    page.window_width = 400
    page.window_height = 600
    page.window_resizable = False

    def route_change(e: ft.RouteChangeEvent):
        page.views.clear()
        if page.route == "/":
            page.views.append(login_view(page))
        elif page.route == "/mood":
            page.views.append(mood_view(page))
        elif page.route == "/journal":
            page.views.append(journal_view(page))
        elif page.route == "/insights":
            page.views.append(insights_view(page))
        page.update()

    page.on_route_change = route_change
    page.go(page.route)

ft.app(target=main)
