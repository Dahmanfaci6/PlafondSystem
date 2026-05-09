from flet import *

def AA1(page:Page):
    page.window.width = 360
    page.window.height = 640
    page.window.top = 1
    page.window.left = 960
    page.scroll = ScrollMode.HIDDEN

    def PLUS(e):
        Num.value += 1
        DZD.value += 300

    def MIN(e):
        Num.value -= 1
        DZD.value -= 300

    def MRC(e):
        DZD.value = MMC.value

    Num = Text(value=1,size=30)
    PB = IconButton(icon=Icons.ADD,icon_color="green",on_click=PLUS)
    MB = IconButton(icon=Icons.REMOVE,icon_color="red",on_click=MIN)
    DZD = Text(value=300)
    DIS = Text("Accessoire Akifix pour visseuse: cet adaptateur stop-vis limite la profondeur de vissage, évite de percer trop loin le BA13 et garantit une finition propre et régulière sur vos plaques de plâtre.",expand=True)

    BUY = Button("Ajouter au panier",bgcolor="blue",color="white",width=250,on_click=MRC,style=ButtonStyle(shape=ContinuousRectangleBorder(radius=10)))
    MMC = Text(size=30,bgcolor="green",color="green")

    Cnum = Container(
        content=Num,
        alignment=Alignment.CENTER,
        margin=5,
        padding=10,
        bgcolor="green",
        width=200,
        height=70,
        border_radius=10,
    )

    A1 = Container(
        content=Image(src="Adaptateur pour Embout Stop Vis Akifix.png"),
        margin=5,
        padding=10,
        bgcolor="green",
        width=300,
        height=300,
        border_radius=10,
    )

    return[
        Row([A1],alignment="center"),
        Row([MB,Cnum,PB],alignment="center"),
        Row([Text("Total:"),DZD],alignment="center"),
        Row([DIS],alignment="center"),
        Row([BUY],alignment="center"),
        Row([Text("Merci Pour Achter",size=15),MMC],alignment="center"),
    ]
