import flet as ft
import time
def study1(page:ft.Page):
    word = ft.Text(value="Hello, world!", color="green")
    page.add(word)
    # page.controls.append(word)
    # page.update()
def study2(page:ft.Page):
    step = ft.Text()
    for i in range(10):
        step.value = f"Step {i}"
        page.add(step)
        time.sleep(1)

def study3(page: ft.Page):
    page.add(
        ft.Row(controls=[
            ft.Text("A"),
            ft.Text("B"),
            ft.Text("C"),
            ft.TextField(label="Your name"),
            ft.ElevatedButton(text="Say my name!")
        ])
    )

def study4(page: ft.Page):
    for i in range(10):
        page.add(ft.Text(f"Line {i}"))
        #page.controls.append(ft.Text(f"Line {i}"))
        if i > 4:
            page.controls.pop(0)
        page.update()
        time.sleep(0.3)

def study5(page: ft.Page):
    def button_clicked(e):
        page.add(ft.Text("Clicked!"))
    page.add(ft.ElevatedButton(text="Click me", on_click=button_clicked))


def study6(page: ft.Page):
    def add_clicked(e):
        page.add(ft.Checkbox(label=new_task.value))
        new_task.value = ""
        new_task.focus()
        new_task.update()

    new_task = ft.TextField(hint_text="Whats needs to be done?", width=300)
    page.add(ft.Row([new_task, ft.ElevatedButton("Add", on_click=add_clicked)]))

def study7(page: ft.Page):
    first_name = ft.TextField(label="Hello")
    last_name = ft.TextField(label="World")
    # first_name.visible = True
    # last_name.visible = True
    # page.add(first_name, last_name)
    m = ft.Column(controls=[first_name,last_name])
    m.disabled = False
    page.add(m)


def study8(page: ft.Page):

    first_name = ft.TextField(label="First name", autofocus=True)
    last_name = ft.TextField(label="Last name")
    greetings = ft.Column()

    def btn_click(e):
        greetings.controls.append(ft.Text(f"Hello, {first_name.value} {last_name.value}!"))
        first_name.value = "liu"
        last_name.value = "kai"
        page.update()
        first_name.focus()

    page.add(
        first_name,
        last_name,
        ft.ElevatedButton("Say hello!", on_click=btn_click),
        greetings
    )

def study9(page: ft.Page):
    first_name = ft.Ref[ft.TextField]()
    last_name = ft.Ref[ft.TextField]()
    greetings = ft.Ref[ft.Column]()
    def btn_click(e):
        greetings.current.controls.append(ft.Text(f"Hello, {first_name.current.value} {last_name.current.value}!"))
        first_name.current.value = "liu"
        last_name.current.value = "kai"
        page.update()
        first_name.current.focus()

    page.add(
        ft.TextField(ref=first_name,label="First name", autofocus=True),
        ft.TextField(ref=last_name,label="Last name"),
        ft.ElevatedButton("Say hello!", on_click=btn_click),
        ft.Column(ref=greetings)
    )
ft.app(target=study9)


