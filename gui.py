from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Label
from calculator import Calculator
from tkinter.font import Font


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "assets"


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("411x823")
window.configure(bg = "#212020")


canvas = Canvas(
    window,
    bg = "#212020",
    height = 823,
    width = 411,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    291.0,
    411.0,
    823.0,
    fill="#F0F0F3",
    outline="")

oswald_font = Font(family='Oswald', size=24)

display_label = Label(window, text="", font=oswald_font, bg="#F0F0F3", anchor="e")
display_label.place(x=20, y=20, width=371, height=50)

calculator = Calculator()

def button_click(value):
    if value in "0123456789":
        calculator.set_operand(value)
        display_label.config(text=calculator.operand)
    elif value in "+-*/%":
        calculator.set_operator(value)
        display_label.config(text=value)
    elif value == "C":
        calculator.clear()
        display_label.config(text="")
    elif value == "=":
        calculator.calculate()
        display_label.config(text=str(calculator.get_current_value()))
    print(calculator.get_current_value())

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: button_click("1"),
    relief="flat"
)
button_1.place(
    x=38.0,
    y=631.8974609375,
    width=72.0,
    height=70.1025390625
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: button_click("2"),
    relief="flat"
)
button_2.place(
    x=128.0,
    y=631.8974609375,
    width=71.0,
    height=70.1025390625
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: button_click("3"),
    relief="flat"
)
button_3.place(
    x=218.0,
    y=631.8974609375,
    width=71.0,
    height=70.1025390625
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: button_click("+"),
    relief="flat"
)
button_4.place(
    x=308.0,
    y=631.8974609375,
    width=71.0,
    height=70.1025390625
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: button_click("4"),
    relief="flat"
)
button_5.place(
    x=38.0,
    y=537.8974609375,
    width=72.0,
    height=70.1025390625
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: button_click("5"),
    relief="flat"
)
button_6.place(
    x=128.0,
    y=537.8974609375,
    width=71.0,
    height=70.1025390625
)

button_image_7 = PhotoImage(
    file=relative_to_assets("button_7.png"))
button_7 = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: button_click("6"),
    relief="flat"
)
button_7.place(
    x=218.0,
    y=537.8974609375,
    width=71.0,
    height=70.1025390625
)

button_image_8 = PhotoImage(
    file=relative_to_assets("button_8.png"))
button_8 = Button(
    image=button_image_8,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: button_click("-"),
    relief="flat"
)
button_8.place(
    x=308.0,
    y=537.8974609375,
    width=71.0,
    height=70.1025390625
)

button_image_9 = PhotoImage(
    file=relative_to_assets("button_9.png"))
button_9 = Button(
    image=button_image_9,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: button_click("7"),
    relief="flat"
)
button_9.place(
    x=38.0,
    y=443.8974304199219,
    width=72.0,
    height=70.10256958007812
)

button_image_10 = PhotoImage(
    file=relative_to_assets("button_10.png"))
button_10 = Button(
    image=button_image_10,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: button_click("8"),
    relief="flat"
)
button_10.place(
    x=128.0,
    y=443.8974304199219,
    width=71.0,
    height=70.10256958007812
)

button_image_11 = PhotoImage(
    file=relative_to_assets("button_11.png"))
button_11 = Button(
    image=button_image_11,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: button_click("9"),
    relief="flat"
)
button_11.place(
    x=218.0,
    y=443.8974304199219,
    width=71.0,
    height=70.10256958007812
)

button_image_12 = PhotoImage(
    file=relative_to_assets("button_12.png"))
button_12 = Button(
    image=button_image_12,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: button_click("*"),
    relief="flat"
)
button_12.place(
    x=308.0,
    y=443.8974304199219,
    width=71.0,
    height=70.10256958007812
)

button_image_13 = PhotoImage(
    file=relative_to_assets("button_13.png"))
button_13 = Button(
    image=button_image_13,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: button_click("C"),
    relief="flat"
)
button_13.place(
    x=38.0,
    y=349.8974304199219,
    width=72.0,
    height=70.10256958007812
)

button_image_14 = PhotoImage(
    file=relative_to_assets("button_14.png"))
button_14 = Button(
    image=button_image_14,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: button_click("/"),
    relief="flat"
)
button_14.place(
    x=308.0,
    y=349.8974304199219,
    width=71.0,
    height=70.10256958007812
)

button_image_15 = PhotoImage(
    file=relative_to_assets("button_15.png"))
button_15 = Button(
    image=button_image_15,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: button_click("%"),
    relief="flat"
)
button_15.place(
    x=218.0,
    y=349.8974304199219,
    width=71.0,
    height=70.10256958007812
)

button_image_16 = PhotoImage(
    file=relative_to_assets("button_16.png"))
button_16 = Button(
    image=button_image_16,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: button_click("+/-"),
    relief="flat"
)
button_16.place(
    x=128.0,
    y=349.8974304199219,
    width=71.0,
    height=70.10256958007812
)

button_image_17 = PhotoImage(
    file=relative_to_assets("button_17.png"))
button_17 = Button(
    image=button_image_17,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: button_click("0"),
    relief="flat"
)
button_17.place(
    x=39.0,
    y=725.8974609375,
    width=250.0,
    height=70.1025390625
)

button_image_18 = PhotoImage(
    file=relative_to_assets("button_18.png"))
button_18 = Button(
    image=button_image_18,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: button_click("0"),
    relief="flat"
)
button_18.place(
    x=308.0,
    y=725.8974609375,
    width=71.0,
    height=70.1025390625
)
window.resizable(False, False)
window.mainloop()
