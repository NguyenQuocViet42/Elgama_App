from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import tkinter.font as tkfont
import sys
import tkinter as tk
import random
from tkinter import messagebox
random.seed(40)
sys.path.append('D:\\Study\\20222\\An_toan_thong_tin\\BTL\\code\\Elgamal')
from Elgamal.decoder import decode_text

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"D:\\Study\\20222\\An_toan_thong_tin\\BTL\\code\\decoder\\assets\\frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def tmp():
    pass
flag_decoder = ""

def on_exit(window):
    global flag_decoder
    # Thực hiện các tác vụ cần thiết trước khi thoát
    window.quit()
    flag_decoder = "go_to_quit"

def get_private_key(entry_2):
    try:
        x = int(entry_2.get("1.0", tk.END).strip())
        return x
    except:
        return 'error'
def get_p(entry_3):
    try:
        p = int(entry_3.get("1.0", tk.END).strip())
        return p
    except:
        return 'error'

def set_plain_text(entry_4, plain_text):
    entry_4.delete("1.0", tk.END)  # Xóa toàn bộ nội dung hiện tại
    entry_4.insert(tk.END, plain_text)  # Chèn nội dung mới vào cuối

def get_cypher_text(entry_1):
    cypher_text = entry_1.get("1.0", tk.END).strip()
    size = len(cypher_text)
    size = size // 2
    cypher_text_1 = cypher_text[:size]
    cypher_text_2 = cypher_text[size:]
    return [cypher_text_1, cypher_text_2]

def get_plain_text(entry_1, entry_2, entry_3, entry_4):
    p = get_p(entry_3)
    x = get_private_key(entry_2)
    cypher_text = get_cypher_text(entry_1)
    if p == 'error' or x == 'error':
        messagebox.showinfo("Nhập thiếu dữ liệu", "Hãy nhập đủ p và x")
    else:
        plain_text = decode_text(cypher_text, x, p)
        set_plain_text(entry_4, plain_text)
    


def go_back(window):
    global flag_decoder
    window.quit()
    flag_decoder = "go_back"

def decoder_window(window):
    window.title("Decoder")
    window.geometry("999x563")
    window.configure(bg = "#FFFFFF")


    canvas = Canvas(
        window,
        bg = "#FFFFFF",
        height = 563,
        width = 999,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        499.0,
        281.0,
        image=image_image_1
    )

    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        235.5,
        292.0,
        image=entry_image_1
    )
    entry_1 = Text(
        bd=0,
        bg="#669CCE",
        fg="#000716",
        highlightthickness=0,
        padx = 5,
        pady = 5
    )
    entry_1.place(
        x=37.0,
        y=136.0,
        width=397.0,
        height=310.0
    )
    font = tkfont.Font(size=15)
    entry_image_2 = PhotoImage(
        file=relative_to_assets("entry_2.png"))
    entry_bg_2 = canvas.create_image(
        619.5,
        508.0,
        image=entry_image_2
    )
    entry_2 = Text(
        bd=0,
        bg="#A3D5E0",
        fg="#000716",
        highlightthickness=0,
        padx = 30,
        pady = 5
    )
    entry_2.configure(font=font)
    entry_2.place(
        x=567.0,
        y=491.0,
        width=105.0,
        height=32.0
    )

    entry_image_3 = PhotoImage(
        file=relative_to_assets("entry_3.png"))
    entry_bg_3 = canvas.create_image(
        388.5,
        508.0,
        image=entry_image_3
    )
    entry_3 = Text(
        bd=0,
        bg="#A3D5E0",
        fg="#000716",
        highlightthickness=0,
        padx = 30,
        pady = 5
    )
    entry_3.configure(font=font)
    entry_3.place(
        x=336.0,
        y=491.0,
        width=105.0,
        height=32.0
    )

    entry_image_4 = PhotoImage(
        file=relative_to_assets("entry_4.png"))
    entry_bg_4 = canvas.create_image(
        772.5,
        292.0,
        image=entry_image_4
    )
    entry_4 = Text(
        bd=0,
        bg="#669CCE",
        fg="#000716",
        highlightthickness=0,
        padx = 5,
        pady = 5
    )
    entry_4.place(
        x=574.0,
        y=136.0,
        width=397.0,
        height=310.0
    )

    canvas.create_text(
        180.0,
        105.0,
        anchor="nw",
        text="Cipher Text",
        fill="#DD250C",
        font=("InriaSerif Bold", 20 * -1)
    )

    canvas.create_text(
        615.0,
        520.0,
        anchor="nw",
        text="x",
        fill="#DD250C",
        font=("InriaSerif Bold", 20 * -1)
    )

    canvas.create_text(
        383.0,
        520.0,
        anchor="nw",
        text="p",
        fill="#DD250C",
        font=("InriaSerif Bold", 20 * -1)
    )

    canvas.create_text(
        726.0,
        105.0,
        anchor="nw",
        text="Plain Text",
        fill="#DD250C",
        font=("InriaSerif Bold", 20 * -1)
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: go_back(window),
        relief="flat"
    )
    button_1.place(
        x=16.0,
        y=517.0,
        width=94.0,
        height=32.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: get_plain_text(entry_1, entry_2, entry_3, entry_4),
        relief="flat"
    )
    button_2.place(
        x=441.0,
        y=320.0,
        width=126.0,
        height=44.0
    )

    canvas.create_rectangle(
        451.00947189331055,
        296.13572788238525,
        558.9999961853027,
        300.86431884765625,
        fill="#000000",
        outline="")

    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_3 clicked"),
        relief="flat"
    )
    button_3.place(
        x=416.0,
        y=16.0,
        width=167.0,
        height=48.0
    )
    window.resizable(False, False)
    window.protocol("WM_DELETE_WINDOW",lambda: on_exit(window))
    window.mainloop()
    return flag_decoder