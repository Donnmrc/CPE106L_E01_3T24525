# main.py
import flet as ft
import httpx

API_BASE = "http://127.0.0.1:8000"
DEFAULT_USER = "test123"

ACCENT = ft.Colors.BLUE_100
FONT_COLOR = ft.Colors.GREY_900

def dashboard_view(page):
    # Card: Today's Mood
    mood_text = ft.Text("Not tracked yet", size=20, weight=ft.FontWeight.BOLD, color=FONT_COLOR)

    def load_today_mood():
        try:
            resp = httpx.get(f"{API_BASE}/stats", params={"username": DEFAULT_USER})
            stats = resp.json()["mood_stats"]
            if stats:
                mood, count = max(stats.items(), key=lambda x: x[1])
                mood_text.value = f"{mood.capitalize()} ({count})"
            else:
                mood_text.value = "Not tracked yet"
            page.update()
        except Exception:
            mood_text.value = "Not tracked yet"
            page.update()
    load_today_mood()

    # Card: Mood Streak
    streak_text = ft.Text("0 days", size=20, weight=ft.FontWeight.BOLD, color=FONT_COLOR)

    def load_streak():
        try:
            resp = httpx.get(f"{API_BASE}/stats", params={"username": DEFAULT_USER})
            stats = resp.json()["mood_stats"]
            total = sum(stats.values())
            streak_text.value = f"{total} days"
            page.update()
        except Exception:
            streak_text.value = "0 days"
            page.update()
    load_streak()

    # Card: Journal Entries
    journal_count = ft.Text("0", size=20, weight=ft.FontWeight.BOLD, color=FONT_COLOR)

    def load_journal_count():
        try:
            resp = httpx.get(f"{API_BASE}/stats", params={"username": DEFAULT_USER})
            # For demo, count moods as journal entries (replace with journal count endpoint if available)
            stats = resp.json()["mood_stats"]
            journal_count.value = str(sum(stats.values()))
            page.update()
        except Exception:
            journal_count.value = "0"
            page.update()
    load_journal_count()

    # Summary cards row
    summary_row = ft.Row([
        ft.Container(
            ft.Column([
                ft.Text("Today's Mood", size=14, color=ft.Colors.GREY_700),
                mood_text,
                ft.Text("Track your first mood", size=12, color=ft.Colors.GREY_500),
            ], spacing=2),
            bgcolor=ft.Colors.WHITE,
            border_radius=12,
            padding=16,
            expand=1,
            shadow=ft.BoxShadow(blur_radius=8, color=ft.Colors.GREY_200)
        ),
        ft.Container(
            ft.Column([
                ft.Text("Mood Streak", size=14, color=ft.Colors.GREY_700),
                streak_text,
                ft.Text("Start your journey today", size=12, color=ft.Colors.GREY_500),
            ], spacing=2),
            bgcolor=ft.Colors.WHITE,
            border_radius=12,
            padding=16,
            expand=1,
            shadow=ft.BoxShadow(blur_radius=8, color=ft.Colors.GREY_200)
        ),
        ft.Container(
            ft.Column([
                ft.Text("Journal Entries", size=14, color=ft.Colors.GREY_700),
                journal_count,
                ft.Text("Total reflections written", size=12, color=ft.Colors.GREY_500),
            ], spacing=2),
            bgcolor=ft.Colors.WHITE,
            border_radius=12,
            padding=16,
            expand=1,
            shadow=ft.BoxShadow(blur_radius=8, color=ft.Colors.GREY_200)
        ),
    ], spacing=16)

    # Quick Mood Check card
    def show_mood_dialog(e):
        dialog = ft.AlertDialog(
            title=ft.Text("Mood Window"),
            content=ft.Text("hello"),
            actions=[
                ft.TextButton("Close", on_click=lambda _: page.dialog.dismiss())
            ]
        )
        page.dialog = dialog
        dialog.open = True
        page.update()

    quick_mood_card = ft.Container(
        ft.Column([
            ft.Text("Quick Mood Check", size=16, weight=ft.FontWeight.BOLD, color=FONT_COLOR),
            ft.Text("How are you feeling right now? Track your mood in seconds.", size=12, color=ft.Colors.GREY_600),
            ft.ElevatedButton("Track My Mood", on_click=show_mood_dialog, bgcolor=ft.Colors.BLUE_300, color=ft.Colors.WHITE),
        ], spacing=8),
        bgcolor=ACCENT,
        border_radius=12,
        padding=16,
        expand=1,
        shadow=ft.BoxShadow(blur_radius=8, color=ft.Colors.BLUE_50)
    )

    # Daily Reflection card
    daily_reflection_card = ft.Container(
        ft.Column([
            ft.Text("Daily Reflection", size=16, weight=ft.FontWeight.BOLD, color=FONT_COLOR),
            ft.Text("Take a moment to reflect on your day and thoughts.", size=12, color=ft.Colors.GREY_600),
            ft.ElevatedButton("Write in Journal", on_click=lambda _: page.go("/journal"), bgcolor=ft.Colors.BLUE_50, color=ft.Colors.BLUE_900),
        ], spacing=8),
        bgcolor=ft.Colors.WHITE,
        border_radius=12,
        padding=16,
        expand=1,
        shadow=ft.BoxShadow(blur_radius=8, color=ft.Colors.GREY_100)
    )

    # Main dashboard layout
    return ft.View(
        "/",
        controls=[
            ft.Text("Welcome back! 👋", size=28, weight=ft.FontWeight.BOLD, color=FONT_COLOR),
            ft.Text("How are you feeling today? Let's check in with yourself.", size=16, color=ft.Colors.GREY_700),
            ft.Container(summary_row, margin=ft.Margin(0, 0, 0, 16)),
            ft.Row([quick_mood_card, daily_reflection_card], spacing=16),
        ],
        padding=24,
        spacing=24,
        vertical_alignment=ft.MainAxisAlignment.START
    )

def mood_view(page):
    mood_value = {"value": None}

    def set_mood(mood):
        def handler(e):
            mood_value["value"] = mood
            for btn in mood_buttons:
                btn.bgcolor = ft.Colors.WHITE
                btn.color = FONT_COLOR
            mood_btn_map[mood].bgcolor = ACCENT
            mood_btn_map[mood].color = ft.Colors.BLUE_900
            page.update()
        return handler

    mood_btn_map = {}
    mood_buttons = [
        ft.ElevatedButton(
            content=ft.Column([
                ft.Text("😍", size=32),
                ft.Text("Amazing", size=14, weight=ft.FontWeight.BOLD)
            ], spacing=4, alignment=ft.MainAxisAlignment.CENTER),
            bgcolor=ft.Colors.WHITE,
            color=FONT_COLOR,
            style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=8)),
            on_click=set_mood("Amazing"),
            expand=1,
            height=70
        ),
        ft.ElevatedButton(
            content=ft.Column([
                ft.Text("😊", size=32),
                ft.Text("Good", size=14, weight=ft.FontWeight.BOLD)
            ], spacing=4, alignment=ft.MainAxisAlignment.CENTER),
            bgcolor=ft.Colors.WHITE,
            color=FONT_COLOR,
            style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=8)),
            on_click=set_mood("Good"),
            expand=1,
            height=70
        ),
        ft.ElevatedButton(
            content=ft.Column([
                ft.Text("😐", size=32),
                ft.Text("Neutral", size=14, weight=ft.FontWeight.BOLD)
            ], spacing=4, alignment=ft.MainAxisAlignment.CENTER),
            bgcolor=ft.Colors.WHITE,
            color=FONT_COLOR,
            style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=8)),
            on_click=set_mood("Neutral"),
            expand=1,
            height=70
        ),
        ft.ElevatedButton(
            content=ft.Column([
                ft.Text("😔", size=32),
                ft.Text("Low", size=14, weight=ft.FontWeight.BOLD)
            ], spacing=4, alignment=ft.MainAxisAlignment.CENTER),
            bgcolor=ft.Colors.WHITE,
            color=FONT_COLOR,
            style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=8)),
            on_click=set_mood("Low"),
            expand=1,
            height=70
        ),
        ft.ElevatedButton(
            content=ft.Column([
                ft.Text("😢", size=32),
                ft.Text("Terrible", size=14, weight=ft.FontWeight.BOLD)
            ], spacing=4, alignment=ft.MainAxisAlignment.CENTER),
            bgcolor=ft.Colors.WHITE,
            color=FONT_COLOR,
            style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=8)),
            on_click=set_mood("Terrible"),
            expand=1,
            height=70
        ),
    ]
    for btn in mood_buttons:
        mood_btn_map[btn.content.controls[1].value] = btn

    note_field = ft.TextField(
        label="What's on your mind? How was your day?",
        multiline=True,
        height=80,
        filled=True,
        bgcolor=ft.Colors.WHITE,
        border_radius=8
    )

    def save_mood(e):
        if not mood_value["value"]:
            page.snack_bar = ft.SnackBar(ft.Text("Please select your mood!"))
            page.snack_bar.open = True
            page.update()
            return
        httpx.post(f"{API_BASE}/mood", json={
            "username": DEFAULT_USER,
            "mood": mood_value["value"],
            "tags": [],
        })
        # Optionally save note as journal
        if note_field.value.strip():
            httpx.post(f"{API_BASE}/journal", json={
                "username": DEFAULT_USER,
                "content": note_field.value.strip()
            })
        page.go("/")

    tip_card = ft.Container(
        ft.Column([
            ft.Text("💡 Tip: Regular mood tracking helps you:", size=14, weight=ft.FontWeight.BOLD, color=ft.Colors.GREY_800),
            ft.Text(
                "- Identify patterns in your emotional well-being\n"
                "- Recognize triggers and positive influences\n"
                "- Track your progress over time\n"
                "- Better understand your mental health journey",
                size=12,
                color=ft.Colors.GREY_700
            ),
        ], spacing=4),
        bgcolor=ft.Colors.WHITE,
        border_radius=12,
        padding=16,
        margin=ft.Margin(0, 0, 0, 0),
        shadow=ft.BoxShadow(blur_radius=8, color=ft.Colors.GREY_100)
    )

    return ft.View(
        "/mood",
        controls=[
            ft.Container(
                ft.Column([
                    ft.Icon(name=ft.icons.FAVORITE_BORDER, color=ft.Colors.BLUE_300, size=40),
                    ft.Text("How are you feeling?", size=28, weight=ft.FontWeight.BOLD, color=FONT_COLOR, text_align=ft.TextAlign.CENTER),
                    ft.Text("Take a moment to check in with yourself", size=16, color=ft.Colors.GREY_700, text_align=ft.TextAlign.CENTER),
                    ft.Container(
                        ft.Column([
                            ft.Text("Select Your Mood", size=18, weight=ft.FontWeight.BOLD, color=FONT_COLOR),
                            ft.Text("Choose the option that best describes how you're feeling right now", size=13, color=ft.Colors.GREY_600),
                            ft.Row(mood_buttons, spacing=8),
                            ft.Text("Add a note (optional)", size=13, weight=ft.FontWeight.BOLD, color=ft.Colors.GREY_700, margin=ft.Margin(8,0,0,0)),
                            note_field,
                            ft.ElevatedButton(
                                "Save Mood",
                                on_click=save_mood,
                                bgcolor=ACCENT,
                                color=FONT_COLOR,
                                style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=8)),
                                expand=True,
                                height=40
                            ),
                        ], spacing=10),
                        bgcolor=ft.Colors.WHITE,
                        border_radius=12,
                        padding=20,
                        shadow=ft.BoxShadow(blur_radius=8, color=ft.Colors.GREY_100)
                    ),
                    tip_card,
                    ft.ElevatedButton("Back", on_click=lambda _: page.go("/"), bgcolor=ft.Colors.GREY_200, color=FONT_COLOR, style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=8)), expand=True)
                ], spacing=24),
                alignment=ft.alignment.center,
                padding=24,
                expand=True
            )
        ],
        padding=0,
        spacing=0,
        vertical_alignment=ft.MainAxisAlignment.START,
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
        page.go("/")

    return ft.View(
        "/journal",
        controls=[
            ft.Text("Journal Entry", size=24, weight=ft.FontWeight.BOLD, color=FONT_COLOR),
            journal_field,
            ft.ElevatedButton("Save", on_click=save_journal, bgcolor=ft.Colors.BLUE_300, color=ft.Colors.WHITE),
            ft.ElevatedButton("Back", on_click=lambda _: page.go("/"), bgcolor=ft.Colors.GREY_200),
        ],
        padding=20,
        spacing=20,
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )

def main(page: ft.Page):
    page.title = "Mindful Balance"
    page.window_width = 600
    page.window_height = 700
    page.window_resizable = False
    page.bgcolor = ft.Colors.WHITE

    def route_change(e: ft.RouteChangeEvent):
        page.views.clear()
        if page.route == "/":
            page.views.append(dashboard_view(page))
        elif page.route == "/mood":
            page.views.append(mood_view(page))
        elif page.route == "/journal":
            page.views.append(journal_view(page))
        else:
            page.go("/")
        page.update()

    page.on_route_change = route_change
    page.go(page.route)

ft.app(target=main)