from flet import *
import file1
import home

def main(page:Page):
    page.window.width = 360
    page.window.height = 640
    page.window.top = 1
    page.window.left = 960
    page.scrollmode = ScrollMode.HIDDEN

    def SignIN(e):
        page.views.append(View(controls=file1.FileOne(page)))

    def Login(e):
        if user1.value == "" or pass1.value == "":
            E.value = "Username or Password is Worng"
        else:
            E.value = ""
            page.views.append(View(controls=home.Home(page)))

    user1 = TextField(label="Username",icon=Icons.PERSON,border_radius=30,expand=True)
    pass1 = TextField(label="Password",icon=Icons.PASSWORD,password=True,can_reveal_password=True,border_radius=30,expand=True)
    S = TextButton("You Dont Have Account?",on_click=SignIN)
    L = Button("Login",on_click=Login,width=250,bgcolor="blue",color="white",style=ButtonStyle(shape=ContinuousRectangleBorder(radius=10)))
    E = Text(color="red")
    
    page.add(
        Row([Text("Bienvenue",size=20)],alignment="center"),
        Row([Image(src="sarlogo.png",width=300,height=150)],alignment="center"),
        Row([user1],alignment="center"),
        Row([pass1],alignment="center"),
        Row([L],alignment="center"),
        Row([S],alignment=MainAxisAlignment.CENTER),
        Row([E],alignment="center")
    )

if __name__ == "__main__":
    run(main)
