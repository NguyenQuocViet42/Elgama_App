import menu.gui as menu_gui
import decoder.gui as decoder_gui
import encoder.gui as encoder_gui
import tkinter as tk
import random
random.seed(40)
window = tk.Tk()
flag = menu_gui.menu_window(window)
while True :
    if flag == 'go_to_quit':
        break
    elif flag == 'go_to_encoder':
        flag = encoder_gui.encoder_window(window)   
    elif flag == "go_back":
        flag = menu_gui.menu_window(window)
    elif flag == 'go_to_decoder':
        flag = decoder_gui.decoder_window(window)