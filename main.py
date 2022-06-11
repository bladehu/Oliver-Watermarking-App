from tkinter import *
import PIL
from PIL import Image, ImageFont, ImageDraw
from tkinter import filedialog
from tkinter import messagebox


window = Tk()
window.title("Watermarking")
window.config(padx=10, pady=10)


# Upload image - check if the file is a supported format
def upload_image():
    global im
    file_name = filedialog.askopenfilename()
    try:
        im = Image.open(file_name)
    except PIL.UnidentifiedImageError:
        messagebox.showinfo(title="Error", message="Unsupported file format.\n Please open an image file.")


# Upload logo - check if the file is a supported format
def upload_logo():
    global logo
    logo_name = filedialog.askopenfilename()
    try:
        logo = Image.open(logo_name)
    except PIL.UnidentifiedImageError:
        messagebox.showinfo(title="Error", message="Unsupported file format.\n Please open an image file.")


# Watermark image with text
def watermark_text():
    text = add_watermark_text.get()
    if len(text) != 0:
        draw = ImageDraw.Draw(im)
        font = ImageFont.truetype("arial.ttf", 50)

        # text add watermark
        draw.text((im.width, im.height), text, fill="white", font=font, anchor="rb")
        im.show()
        messagebox.showinfo(title="Success", message="The image has a watermark text on it now.")


# Watermark image with logo
def watermark_logo():
    try:
        wm_logo = logo
    except NameError:
        messagebox.showinfo(title="Error", message="Please upload a logo")
    else:
        im.paste(wm_logo)
        im.show()
        messagebox.showinfo(title="Success", message="The image has a watermark logo on it now.")


# Save image - User can decide the file name
def save_image():
    save_name = filedialog.asksaveasfile(filetypes=[('Images', '*.png')], defaultextension="*.png")
    im.save(save_name.name)


canvas = Canvas(width=300, height=50, highlightthickness=0)
canvas.grid()

open_label = Label(text="Open image here:")
open_label.grid(column=0, row=1)

open_button = Button(text="Open image", command=upload_image)
open_button.grid(column=1, row=1, columnspan=2)

add_watermark_label = Label(text="Add text here:")
add_watermark_label.grid(column=0, row=3)

add_watermark_text = Entry(width=39)
add_watermark_text.grid(column=1, row=3)

open_logo_label = Label(text="Or open logo here:")
open_logo_label.grid(column=0, row=4)

open_logo_button = Button(text="Open logo", command=upload_logo)
open_logo_button.grid(column=1, row=4, columnspan=2)

text_watermark_button = Button(text="WATERMARK with text", command=watermark_text)
text_watermark_button.grid(column=0, row=5)

logo_watermark_button = Button(text="WATERMARK with logo", command=watermark_logo)
logo_watermark_button.grid(column=1, row=5)

save_button = Button(text="Save", command=save_image)
save_button.grid(column=1, row=6, columnspan=2)

window.mainloop()
