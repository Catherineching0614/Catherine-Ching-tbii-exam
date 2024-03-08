import tkinter as tk
from helpers import set_background, clear_widgets
from tkinter import messagebox
from PIL import Image, ImageTk, ImageSequence
import pygame as pg
import random
import colorsys

# Build the gui root
root = tk.Tk()
root.title("Colours in my eye")
root.geometry("1000x650")
pg.init()

# Give the background image
set_background(root, "images/color-wheel-2.png")

# Set background music
pg.mixer.music.load("music/milk and sugar chill.mp3")
pg.mixer.music.set_volume(0.3)
pg.mixer.music.play()
pg.mixer.music.play(-1)
mute_icon = tk.PhotoImage(file="images/mute.png")
sound_icon = tk.PhotoImage(file="images/sound.png")


# Creating button to mute or turn on the music
def toggle_music():
    if pg.mixer.music.get_busy():
        # If music is playing, stop it and show mute icon
        pg.mixer.music.stop()
        music_button.config(image=mute_icon)
    else:
        # If music is muted or stopped, play it and show sound icon
        pg.mixer.music.play(-1)
        music_button.config(image=sound_icon)


music_button = tk.Button(root, image=sound_icon, width=30, height=30, command=toggle_music)
music_button.place(x=20, y=20)

# Title label
name_label = tk.Label(root,
                      text="Colours in my eye",
                      bg="#eee9c2",
                      fg="#392642",
                      font="arial 30 bold"
                      )
name_label.place(relx=0.5, anchor="center", y=177)

# Label to ask user for their name
name_label = tk.Label(root,
                      text="Please Enter Your Name",
                      bg="#bfe8ea",
                      font="arial 10 bold"
                      )
name_label.place(relx=0.5, anchor="center", y=285)

# Create a box where the user can enter their name
name = tk.StringVar()  # variable to store the name
name_box = tk.Entry(root,
                    textvar=name,
                    font="arial 15 italic",
                    fg="black",
                    bg="#A7C5F9")
name_box.place(relx=0.5, anchor="center", y=310)

# Button that will enter the game when the user clicks on it
play_button = tk.Button(root,
                        text="Let's Try",
                        font='lucida 10 bold',
                        command=lambda: mainpage(root)
                        )
play_button.place(relx=0.5, anchor="center", y=350)


def entergame(event):
    mainpage(root)


# Add code that will enter the game when you press enter
name_box.bind('<Return>',
              entergame)


# Create a mainpage def that will just clear everything
def mainpage(root):
    # The clear widgets kills everything
    clear_widgets(root)

    set_background(root, "images/background-2.jpg")

    # Welcome and instruction messages label on the page
    welcome = tk.Label(root,
                       text=f"Welcome {name.get().capitalize()}, "
                            f"to experience views from my perspective\nor learn more about colours ",
                       font="arial 20 bold",
                       bg="#c4a7e7",
                       fg="white",
                       borderwidth=10
                       )
    welcome.place(relx=0.5, anchor="center", y=60)

    second_message = tk.Label(root,
                              text="Please choose the following situation",
                              font="arial 15 bold",
                              bg="#c5dca0",
                              fg="#5b647d",
                              borderwidth=6
                              )
    second_message.place(relx=0.18, y=115)

    third_message = tk.Label(root,
                             text="or play a game",
                             font="arial 15 bold",
                             bg="#c5dca0",
                             fg="#5b647d",
                             borderwidth=6
                             )
    third_message.place(x=635, y=115)

    forth_message = tk.Label(root,
                             text="or some other tools",
                             font="arial 15 bold",
                             bg="#c5dca0",
                             fg="#5b647d",
                             borderwidth=6
                             )
    forth_message.place(x=617, y=265)

    # Add some buttons the player can select
    usual_button = tk.Button(root,
                             text="Usual",
                             font="arial 14 bold",
                             height=1,
                             width=15,
                             bg="#f5f2b8",
                             command=lambda: [press("Usual"), clear_widgets]
                             )
    usual_button.place(relx=0.25, y=175)

    deuteranamoly_button = tk.Button(root,
                                     text="Deuteranamoly",
                                     font="arial 14 bold",
                                     height=1,
                                     width=15,
                                     bg="#f5f2b8",
                                     command=lambda: [press("Deuteranamoly"), clear_widgets]
                                     )
    deuteranamoly_button.place(relx=0.25, y=225)

    protanomaly_button = tk.Button(root,
                                   text="Protanomaly",
                                   font="arial 14 bold",
                                   height=1,
                                   width=15,
                                   bg="#f5f2b8",
                                   command=lambda: [press("Protanomaly"), clear_widgets]
                                   )
    protanomaly_button.place(relx=0.25, y=275)

    tritanomaly_button = tk.Button(root,
                                   text="Tritanomaly",
                                   font="arial 14 bold",
                                   height=1,
                                   width=15,
                                   bg="#f5f2b8",
                                   command=lambda: [press("Tritanomaly"), clear_widgets]
                                   )
    tritanomaly_button.place(relx=0.25, y=325)

    monochromacy_button = tk.Button(root,
                                    text="Monochromacy",
                                    font="arial 14 bold",
                                    height=1,
                                    width=15,
                                    bg="#f5f2b8",
                                    command=lambda: [press("Monochromacy"), clear_widgets]
                                    )
    monochromacy_button.place(relx=0.25, y=375)

    magenta_game = tk.Button(root,
                             text="Magenta",
                             font="arial 14 bold",
                             height=1,
                             width=15,
                             bg="#f9dad0",
                             command=lambda: [press("Magenta"), clear_widgets]
                             )
    magenta_game.place(x=620, y=175)

    color_mix = tk.Button(root,
                          text="Color mixing tool",
                          font="arial 14 bold",
                          height=1,
                          width=15,
                          bg="#f9dad0",
                          command=lambda: [press("Color mixing tool"), clear_widgets]
                          )
    color_mix.place(x=620, y=325)

    HSV_button = tk.Button(root,
                           text="HSV",
                           font="arial 14 bold",
                           height=1,
                           width=15,
                           bg="#f9dad0",
                           command=lambda: [press("HSV"), clear_widgets]
                           )
    HSV_button.place(x=620, y=375)

    # Button to close the gui
    exit_button = tk.Button(root,
                            text="Exit",
                            command=root.destroy
                            )
    exit_button.place(x=950, y=600)


# Create a definition to make photo buttons so that message appears when button pressed
def photo_button():
    global msg
    clear_widgets(root)
    set_background(root, background_picture)
    # Load an image
    photo = tk.PhotoImage(file=picture)
    button_image = tk.Button(root,
                             image=photo,
                             command=message_appear,
                             bd=0)
    button_image.image = photo  # To prevent garbage collection
    button_image.pack(pady=10)
    msg = None


def message_appear():
    global msg

    if msg is None:
        msg = tk.Message(root, text=fact, width=575)
        msg.pack()
    else:
        msg.config(text=fact)


# Create definition for inputting pictures in the magenta game
def input_pictures(root, trial):
    global label
    img = Image.open(f"images/{trial}.png")
    resized_img = img.resize((350, 350), resample=Image.Resampling.LANCZOS)
    photo = ImageTk.PhotoImage(resized_img)
    label = tk.Label(root, image=photo)
    label.image = photo  # To prevent garbage collection
    label.place(relx=0.5, rely=0.471, anchor="center")


# Input hp health bar
def input_pictures1(root, trial):
    global label1
    img1 = Image.open(f"images/hp {trial}.png")
    resized_img1 = img1.resize((150, 40), resample=Image.Resampling.LANCZOS)
    photo1 = ImageTk.PhotoImage(resized_img1)
    label1 = tk.Label(root, image=photo1, bd=0, highlightthickness=0)
    label1.image = photo1  # To prevent garbage collection
    label1.place(x=835, y=15)


# Update the frame of gif
def update_gif(frame):
    global gif_frames, gif_index, gif_after_id, canvas

    canvas.itemconfig(gif_display, image=gif_frames[gif_index])
    gif_index = (gif_index + 1) % len(gif_frames)
    gif_after_id = canvas.after(100, update_gif, frame + 1)


# Display the cat gif
def display_gif(root):
    global gif_display, gif_frames, gif_index, canvas
    canvas = tk.Canvas(root, width=250, height=300, bg="white")
    canvas.place(relx=0.5, rely=0.45, anchor="center")
    gif_frames = []
    gif = Image.open(f"images/cat-cool.gif")
    for frame in ImageSequence.Iterator(gif):
        gif_frames.append(ImageTk.PhotoImage(frame))
    gif_index = 0
    gif_display = canvas.create_image(125, 150, anchor=tk.CENTER, image=gif_frames[gif_index])
    update_gif(0)


# Send out warning box when player input more than one letter into guess box
def check_length(guessed_letter):
    if len(guessed_letter) > 1:
        messagebox.showwarning("Warning", "Please enter only one letter")


# List of random mockery when player has a wrong guess
def generate_random_mockery1():
    mockery = [
        "Are you sure? :)",
        "OMG, you were so close... Well actually not at all",
        "Success is not final, failure is not fatal. But you are still wrong :)",
        "Not to offend, but do better",
        "It's not that hard, it's just a word",
        "Get you cat here, I bet it can do better than you"]
    return random.choice(mockery)


# List of random mockery when players is still guessing wrong after the forth guess
def generate_random_mockery2():
    mockery = [
        "OMG! I'm sure you have just type in the correct answer",
        "You are sooooo smart. I believe in you totally!",
        "Are you a genius? How can you even do that?,"
        "Smarter then Albert Einstein :)"]
    return random.choice(mockery)


# Secret button that will change the guessing word and the final message after the game
def secret_button_click():
    global secret_word, text_message
    secret_word = "pinhong"
    text_message = "Pinhong is the Chinese saying of magenta\nIt is different from REDDDD"


# Reveal random correct letter even when the guessing is wrong after the forth try
def reveal_incorrect_letter():
    global display_word, secret_word, display, guessed_letter

    # Find indices of incorrect letters in the secret word
    incorrect_indices = [i for i, letter in enumerate(secret_word)
                         if guessed_letter != letter and display_word[i] == "-"]

    # Choose a random incorrect index if available
    if incorrect_indices:
        random_index = random.choice(incorrect_indices)

        # Update the display_word to reveal the incorrect letter
        display_word[random_index] = secret_word[random_index]

        # Update the display label to show the current state of the word
        display.configure(text=display_word)


# Function to start the magenta game
def play_magenta():
    global guessed_letter, secret_word, display_word, display, title, letter_entry, \
        trial, label1, hidden_button

    check_length(guessed_letter.get())
    random_mockery1 = generate_random_mockery1()
    random_mockery2 = generate_random_mockery2()

    if guessed_letter.get() in secret_word:
        for i in range(len(secret_word)):
            if list(secret_word)[i] == guessed_letter.get():
                display_word[i] = guessed_letter.get()
        display.configure(text=display_word)
        if "".join(display_word) == secret_word:
            title.configure(text="YOU WON!!!")
            letter_entry.destroy()
            now_you_know(root)
            play_button.configure(text="Exit")
            play_button.configure(text="Exit", command=root.destroy)
            hidden_button.destroy()
            if trial == 0:
                title.configure(text="Brilliant:) but you missed out the fun (of being played)",
                                font="Geneva 20 bold")
                if label is not None:
                    label.destroy()
                display_gif(root)
                if label1 is not None:
                    label1.destroy()
    else:
        if trial < 4:
            trial += 1
        if label is not None:
            label.destroy()
        input_pictures(root, trial)
        input_pictures1(root, trial)
        if trial < 4:
            messagebox.showwarning("Mr/Ms. Brilliant", f"{random_mockery1}")
        if trial == 4:
            title.configure(text="YOU ARE ON THE CORRECT PATH! I guess",
                            font="Geneva 17 bold")

            reveal_incorrect_letter()

            messagebox.showwarning("Mr/Ms. Brilliant", f"{random_mockery2}")
            if "".join(display_word) == secret_word:
                title.configure(text="YOU WON!!!",
                                font="Geneva 20 bold")
                letter_entry.destroy()
                now_you_know(root)
                play_button.configure(text="Exit")
                play_button.configure(text="Exit", command=root.destroy)
                hidden_button.destroy()


# Clear the letter after pressing the button
def clear_entry():
    guessed_letter.set("")  # Set the StringVar associated with the Entry to an empty string


# Designing the page layout of the game
def call_hangman_game(root):
    global guessed_letter, secret_word, display, title, display_word, letter_entry, \
        trial, combined_commands, text_message

    # Clear all widgets from the root
    clear_widgets(root)

    # Input background
    set_background(root, "images/background-3.png")

    # Shows the number o trial when first started
    trial = 0

    input_pictures(root, trial)
    input_pictures1(root, trial)

    # Create label that welcomes the user
    title = tk.Label(root,
                     text="Guess the Word",
                     fg="#5b647d",
                     font="Geneva 30 bold"
                     )
    title.place(relx=0.5, anchor="center", y=25)

    # Create a secret word
    secret_word = "magenta"
    # Create a message after the game
    text_message = "Now REMEMBER the three principal colour in printing and with ink is Cyan, " \
                   "Yellow, and MAGENTAAAA!!!\nDon't you ever call it RED ever again"

    # Show dashes in place of the secret word and store these dashes as a list
    display_word = list("-" * len(secret_word))

    # Create a box for user to enter letter
    guessed_letter = tk.StringVar()
    letter_entry = tk.Entry(root,
                            textvariable=guessed_letter,
                            fg="black",
                            font="Geneva 30 bold"
                            )
    letter_entry.place(relx=0.5, anchor="center", y=550)
    # Entering letter by pressing the "enter" button
    letter_entry.bind('<Return>', combined_commands)

    # Display the dashes
    display = tk.Label(root,
                       text=display_word,
                       fg="black",
                       font="Geneva 40 bold")
    display.place(relx=0.5, anchor="center", y=75)

    secret_button(root)

    play_magenta()

    enter_letter_button(root)


# Putting a secret button that will give a hidden ending
def secret_button(root):
    global hidden_button
    hidden_button = tk.Button(root,
                              text="    .    ",
                              fg="#5b647d",
                              command=secret_button_click,
                              font="Geneva 20",
                              bd=0,
                              highlightthickness=0
                              )
    hidden_button.place(x=20, y=20)


# Combined commands to clear guessed letter in the entry box and activate the game function
def combined_commands(event):
    play_magenta()
    clear_entry()


def enter_letter_button(root):
    global play_button
    play_button = tk.Button(root,
                            text="LET'S PLAY",
                            command=lambda: (play_magenta(), clear_entry()),
                            font="Geneva 15"
                            )
    play_button.place(x=20, y=575)


# Create a label to explain the message of the game
def now_you_know(root):
    global text_message

    message = tk.Label(root,
                       text=text_message,
                       fg="red",
                       bg="#c4a7e7",
                       font="Geneva 14 bold"
                       )
    message.place(relx=0.5, anchor="center", y=530)


# Color changing function for the color mixing widget
def update_color1():
    # Get the RGB values from the sliders
    red = int(red_slider.get())
    green = int(green_slider.get())
    blue = int(blue_slider.get())

    # Create a hexadecimal color code and update the canvas background
    color_code = f'#{red:02X}{green:02X}{blue:02X}'
    color_canvas.config(bg=color_code)
    color_label.config(text=f'Color: {color_code}')


def color_mixing_widget(root):
    global red_slider, green_slider, blue_slider, color_canvas, color_label, color_message

    clear_widgets(root)

    set_background(root, "images/background-4.png")

    # Initialize RGB values
    red_value = tk.IntVar(value=0)
    green_value = tk.IntVar(value=0)
    blue_value = tk.IntVar(value=0)

    # Create sliders for each color component
    red_slider = tk.Scale(root,
                          label="Red",
                          from_=0,
                          to=255,
                          length=400,
                          variable=red_value,
                          orient="horizontal",
                          command=lambda x: update_color1()
                          )
    green_slider = tk.Scale(root,
                            label="Green",
                            from_=0,
                            to=255,
                            length=400,
                            variable=green_value,
                            orient="horizontal",
                            command=lambda x: update_color1()
                            )
    blue_slider = tk.Scale(root,
                           label="Blue",
                           from_=0, to=255,
                           length=400,
                           variable=blue_value,
                           orient="horizontal",
                           command=lambda x: update_color1()
                           )

    # Create a canvas to display the mixed color
    color_canvas = tk.Canvas(root, width=400, height=200)
    color_canvas.place(relx=0.5, anchor="center", y=180)

    # Create a label to display the color code
    color_label = tk.Label(root,
                           font="arial 13",
                           text="Color: #000000")
    color_label.place(relx=0.5, anchor="center", y=295)

    # Place the sliders on the gui
    red_slider.place(relx=0.5, anchor="center", y=340)
    green_slider.place(relx=0.5, anchor="center", y=395)
    blue_slider.place(relx=0.5, anchor="center", y=450)

    color_message = tk.Button(root,
                              text="In additive color mixing (in digital context), "
                                   "different intensities of red, green, and blue light are combined \nto create a wide range of colors.For example, "
                                   "when all three colors are at their maximum intensity, white light is produced.",
                              font="arial 13",
                              command=color_message_button_pressed
                              )
    color_message.place(relx=0.5, anchor="center", y=550)

    update_color1()


# Adding a message button under the color mixing tool
def color_message_button_pressed():
    global color_message
    current_text = color_message.cget("text")
    if current_text == "In additive color mixing (in digital context), different intensities of red, " \
                       "green, and blue light are combined \nto create a wide range of colors. For example, " \
                       "when all three colors are at their maximum intensity, white light is produced.":
        new_text = "The combination of magenta, cyan, and yellow in subtractive color mixing is used in the printing industry," \
                   "\nwhere colors are created by subtracting wavelengths of light through ink absorption."
    else:
        new_text = "In additive color mixing (in digital context), different intensities of red, " \
                   "green, and blue light are combined \nto create a wide range of colors. For example, " \
                   "when all three colors are at their maximum intensity, white light is produced."
    color_message.configure(text=new_text)


# Color changing function for the HSV tool
def update_color2():
    # Get the HSV values from the sliders
    hue = hue_slider.get() / 360.0  # Convert hue to a value between 0 and 1
    saturation = saturation_slider.get() / 100.0
    value = value_slider.get() / 100.0

    # Convert HSV to RGB
    red, green, blue = colorsys.hsv_to_rgb(hue, saturation, value)
    red = int(red * 255)
    green = int(green * 255)
    blue = int(blue * 255)

    # Create a hexadecimal color code and update the canvas background
    color_code = f'#{red:02X}{green:02X}{blue:02X}'
    color_canvas.config(bg=color_code)
    color_label.config(text=f'Color: {color_code}')


def HSV(root):
    global hue_slider, saturation_slider, value_slider, color_canvas, color_label

    clear_widgets(root)

    set_background(root, "images/background-5.png")

    # Initialize HSV values
    hue_value = tk.IntVar(value=0)  # Initial hue (0-360)
    saturation_value = tk.IntVar(value=100)  # Initial saturation (0-100)
    value_value = tk.IntVar(value=100)  # Initial value (brightness) (0-100)

    # Create sliders for each HSV component
    hue_slider = tk.Scale(root,
                          label="Hue",
                          from_=0,
                          to=360,
                          length=400,
                          variable=hue_value,
                          orient="horizontal",
                          command=lambda x: update_color2()
                          )
    saturation_slider = tk.Scale(root,
                                 label="Saturation",
                                 from_=0,
                                 to=100,
                                 length=400,
                                 variable=saturation_value,
                                 orient="horizontal",
                                 command=lambda x: update_color2()
                                 )
    value_slider = tk.Scale(root,
                            label="Value",
                            from_=0,
                            to=100,
                            length=400,
                            variable=value_value,
                            orient="horizontal",
                            command=lambda x: update_color2()
                            )

    # Create a canvas to display the selected color
    color_canvas = tk.Canvas(root, width=400, height=200)
    color_canvas.place(relx=0.5, anchor="center", y=180)

    # Create a label to display the color code
    color_label = tk.Label(root,
                           font="arial 13",
                           text="Color: #000000")
    color_label.place(relx=0.5, anchor="center", y=295)

    # Place the sliders on the gui
    hue_slider.place(relx=0.5, anchor="center", y=340)
    saturation_slider.place(relx=0.5, anchor="center", y=395)
    value_slider.place(relx=0.5, anchor="center", y=450)

    # Adding a message to introduce HSV
    hsv_message = tk.Label(root,
                           text="These are the HSV bars that are most familiar in image editing software, like Photoshop"
                                "\nThe HSV model is often considered more intuitive for human perception of colors. ",
                           font="arial 13"
                           )
    hsv_message.place(relx=0.5, anchor="center", y=550)

    update_color2()


# Definition of what happens when each button are pressed
def press(user_selects):
    global picture, fact, background_picture, root

    if user_selects == "Usual":
        background_picture = "images/usual-background.png"
        picture = "images/usual.png"
        fact = "Human eye can see about 10 million colours, and blue is most people’s favourite colour"
        photo_button()

    elif user_selects == "Deuteranamoly":
        background_picture = "images/d-background.png"
        picture = "images/d.png"
        fact = "Deuteranomaly is the most common type of red-green color vision deficiency. " \
               "It makes certain shades of green look more red. This usually doesn’t get in the way of normal activities. " \
               "Deuteranopia is the serious situation which someone unable to tell the difference between red and green at all."
        photo_button()

    elif user_selects == "Protanomaly":
        background_picture = "images/p-background.png"
        picture = "images/p.png"
        fact = "Protanomaly makes certain shades of red look more green and less bright. " \
               "This type is mild and usually doesn’t get in the way of normal activities. " \
               "Protanopia is the serious situation which someone unable to tell the difference between red and green at all."
        photo_button()

    elif user_selects == "Tritanomaly":
        background_picture = "images/t-background.png"
        picture = "images/t.png"
        fact = "Tritanomaly is the mild situation where someone is hard to tell the difference between blue and green and between yellow and red. " \
               "Tritanopia makes someone totally unable to tell the difference between blue and green, purple and red, and yellow and pink. " \
               "It also makes colors look less bright."
        photo_button()

    elif user_selects == "Monochromacy":
        background_picture = "images/m-background.png"
        picture = "images/m.png"
        fact = "Monochromacy is rare. It means one have complete color vision deficiency, so one can’t see colors at all. " \
               "Depending on the type, one may also have trouble seeing clearly, and may be more sensitive to light."
        photo_button()

    elif user_selects == "Magenta":
        call_hangman_game(root)

    elif user_selects == "Color mixing tool":
        color_mixing_widget(root)

    elif user_selects == "HSV":
        HSV(root)

    back_button = tk.Button(root,
                            text="Back",
                            command=lambda: mainpage(root)
                            )
    back_button.place(x=950, y=570)


# Code to execute the code
root.mainloop()
