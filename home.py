from flet import *
import a1

def Home(page:Page):
    page.window.width = 360
    page.window.height = 640
    page.window.top = 1
    page.window.left = 960
    page.scroll = ScrollMode.HIDDEN

    def aa1(e):
        page.views.append(View(controls=a1.AA1(page)))

    B1 = SafeArea(
            content=Row(
                alignment="center",
                controls=[
                    Container(
                        content=Image(src="b1.png"),
                        margin=5,
                        padding=10,
                        bgcolor="green",
                        width=150,
                        height=150,
                        border_radius=10,
                        ink=True,
                        on_click=lambda _:print("True")
                    )
                ]
            )
        )

    A1 = SafeArea(
            content=Row(
                alignment="center",
                controls=[
                    Container(
                        content=Image(src="Adaptateur pour Embout Stop Vis Akifix.png"),
                        margin=5,
                        padding=10,
                        bgcolor="green",
                        width=150,
                        height=150,
                        border_radius=10,
                        ink=True,
                        on_click=aa1
                    )
                ]
            )
        )

    B2 = SafeArea(
            content=Row(
                alignment="center",
                controls=[
                    Container(
                        content=Image(src="b2.png"),
                        margin=5,
                        padding=10,
                        bgcolor="green",
                        width=150,
                        height=150,
                        border_radius=10,
                        ink=True,
                        on_click=lambda _:print("True")
                    )
                ]
            )
        )

    C1 = SafeArea(
            content=Row(
                alignment="center",
                controls=[
                    Container(
                        content=Image(src="c1.png"),
                        margin=5,
                        padding=10,
                        bgcolor="green",
                        width=150,
                        height=150,
                        border_radius=10,
                        ink=True,
                        on_click=lambda _:print("True")
                    )
                ]
            )
        )

    C2 = SafeArea(
            content=Row(
                alignment="center",
                controls=[
                    Container(
                        content=Image(src="c2.png"),
                        margin=5,
                        padding=10,
                        bgcolor="green",
                        width=150,
                        height=150,
                        border_radius=10,
                        ink=True,
                        on_click=lambda _:print("True")
                    )
                ]
            )
        )

    C3 = SafeArea(
            content=Row(
                alignment="center",
                controls=[
                    Container(
                        content=Image(src="c3.png"),
                        margin=5,
                        padding=10,
                        bgcolor="green",
                        width=150,
                        height=150,
                        border_radius=10,
                        ink=True,
                        on_click=lambda _:print("True")
                    )
                ]
            )
        )

    B3 = SafeArea(
            content=Row(
                alignment="center",
                controls=[
                    Container(
                        content=Image(src="b3.png"),
                        margin=5,
                        padding=10,
                        bgcolor="green",
                        width=150,
                        height=150,
                        border_radius=10,
                        ink=True,
                        on_click=lambda _:print("True")
                    )
                ]
            )
        )

    B4 = SafeArea(
            content=Row(
                alignment="center",
                controls=[
                    Container(
                        content=Image(src="b4.png"),
                        margin=5,
                        padding=10,
                        bgcolor="green",
                        width=150,
                        height=150,
                        border_radius=10,
                        ink=True,
                        on_click=lambda _:print("True")
                    )
                ]
            )
        )

    return[
        Row([A1,B1,B2,C1],scroll=ScrollMode.HIDDEN,spacing=1),
        Row([C2,C3,B3,B4],scroll=ScrollMode.HIDDEN,spacing=1),
        Row([A1,B1,B2,C1],scroll=ScrollMode.HIDDEN,spacing=1),
        Row([C2,C3,B3,B4],scroll=ScrollMode.HIDDEN,spacing=1),
    ]
