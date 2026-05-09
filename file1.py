from flet import *
import home

def FileOne(page:Page):
    page.window.width = 360
    page.window.height = 640
    page.window.top = 1
    page.window.left = 960
    page.scroll = ScrollMode.HIDDEN

    def Login(e):
        page.views.pop()

    def SignIN(e):
        if name.value == "" or pass1.value == "" or fname.value == "" or cpass1.value == "" or gmail.value == "":
            E.value = "Your Idenity is Worng"
        else:
            E.value = ""
            page.views.append(View(controls=home.Home(page)))
    
    name = TextField(label="Name",icon=Icons.PERSON,border_radius=30,expand=True)
    fname = TextField(label="FamillyName",icon=Icons.FAMILY_RESTROOM,border_radius=30,expand=True)
    gmail = TextField(label="Email",icon=Icons.EMAIL,suffix="@gmail.com",border_radius=30,expand=True) 
    pass1 = TextField(label="Password",icon=Icons.PASSWORD,password=True,can_reveal_password=True,border_radius=30,expand=True)
    cpass1 = TextField(label="Confrim Password",icon=Icons.PASSWORD,password=True,can_reveal_password=True,border_radius=30,expand=True)
    S = Button("Sign Up",on_click=SignIN,width=250,bgcolor="blue",color="white",style=ButtonStyle(shape=ContinuousRectangleBorder(radius=10)))
    L = TextButton("You Already Have Account?",on_click=Login)
    E = Text(color="red")
    
    return[
        Row([Text("Bienvenue",size=20)],alignment="center"),
        Row([Image(src="sarlogo.png",width=300,height=150)],alignment="center"),
        Row([name],alignment="center"),
        Row([fname],alignment="center"),
        Row([gmail],alignment="center"),
        Row([pass1],alignment="center"),
        Row([cpass1],alignment="center"),
        Row([S],alignment="center"),
        Row([L],alignment="center"),
        Row([E],alignment="center")
    ]

if __name__ == "__main__":
    run(FileOne)
