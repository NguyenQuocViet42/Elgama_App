from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

flag_menu = 0

def on_exit(window):
    global flag_menu
    # Thực hiện các tác vụ cần thiết trước khi thoát
    window.quit()
    flag_menu = "go_to_quit"
    
def go_to_encoder(window_menu):
    global flag_menu
    flag_menu = 'go_to_encoder'
    window_menu.quit()

def go_to_decoder(window_menu):
    global flag_menu
    flag_menu = 'go_to_decoder'
    window_menu.quit()

def go_to_quit(window_menu):
    global flag_menu
    flag_menu = 'go_to_quit'
    window_menu.quit()


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / \
    Path(r"D:\\Study\\20222\\An_toan_thong_tin\\BTL\\code\\menu\\assets\\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def menu_window(window_menu):
    window_menu.title("Menu")
    window_menu.geometry("928x620")
    window_menu.configure(bg="#FFFFFF")

    canvas = Canvas(
        window_menu,
        bg="#FFFFFF",
        height=620,
        width=928,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )
    canvas.place(x=0, y=0)
    image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        464.0,
        310.0,
        image=image_image_1
    )

    canvas.create_text(
        368.0,
        29.0,
        anchor="nw",
        text="MENU",
        fill="#33FF00",
        font=("Kavoon Regular", 64 * -1)
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command = lambda:go_to_encoder(window_menu),
        relief="flat"
    )
    button_1.place(
        x=278.0,
        y=178.0,
        width=371.0,
        height=76.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: go_to_decoder(window_menu),
        relief="flat"
    )
    button_2.place(
        x=278.0,
        y=298.0,
        width=371.0,
        height=76.0
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda:go_to_quit(window_menu),
        relief="flat"
    )
    button_3.place(
        x=272.0,
        y=418.0,
        width=371.0,
        height=76.0
    )
    window_menu.resizable(False, False)
    window_menu.protocol("WM_DELETE_WINDOW",lambda: on_exit(window_menu))
    window_menu.mainloop()
    return flag_menu