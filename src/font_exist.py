import customtkinter as ctk
from tkinter import font

def has_font(font_name: str):
    
    font_name = 'Times New Roman'
    
    # Main Window Object
    root = ctk.CTk()
    
    # Check if it has the font require
    if font.families(root).__contains__(font_name):
        print(f'{font_name} exist as a font.')
    else:
        print(f'No font {font_name} exist')