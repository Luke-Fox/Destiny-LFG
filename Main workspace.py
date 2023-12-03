import customtkinter
import random

from customtkinter import CTkFrame

"""try:
    f = open("bingo_op.txt", "r")
    data = f.read()
    data = data
except FileNotFoundError:
    f = open('bingo_op.txt', 'w')
    data = []
    f.write(str(data))
f.close()"""
data = [
    "Thunderlord",
    "Thunder crash",
    "Saves CP",
    "Lore",
    "Chaos Reach",
    "I'll be add \nclear",
    "Double\n Primary",
    "Clears ego",
    "OOB",
    "Open mic",
    '"There goes \nflawless"',
    "Xbox 360 Mic",
    "Gamer Girl!",
    "Shared Fate",
    "Wipe for DMG",
    "Wipe for Flag",
    "Raid Exotic \nDrops",
    "No Debuff",
    '"Enrage is \nnear"',
    "Sherpa",
    "Wipe > 5 times",
    "Forgets to \nRed Border",
    "API time\nEgo",
    "TOS",
    "Silent leaver",
    "2 Hour Clear",
    "All 6 Clear \nJump puzzle",
    '"Just pull me"',
    "Yap session",
    "Singer",
    "Retrofit \nEscapade",
    "God Roll \n Brag",
    "D1 pro \nrefresher",
    "Child",
    "Push players \noff",
    "AFK",
    "Crayon",
    "2+ No Mic",
    "Try Hard",
    "1st Try",
    "Flawless \nEncounter",
]


class App(customtkinter.CTk):
    frame1: CTkFrame

    def __init__(self):
        super().__init__()
        self.pop_data = random.sample(data, 25)
        self.x_coordinate = 880
        self.y_coordinate = 600
        self.geometry(f"{self.x_coordinate}x{self.y_coordinate}")
        self.title("Destiny 2 LFG Bingo")
        self.font = 13
        self.width = 75
        self.height = 75
        self.first_button_colour = 'grey'
        self.first_hover_colour = "light grey"
        self.second_button_colour = '#028A0F'
        self.second_hover_colour = "#20B20F"
        self.box_grid = self.x_coordinate / 12

        self.frame1 = customtkinter.CTkFrame(master=self)
        self.frame2 = customtkinter.CTkFrame(master=self)
        self.frame3 = customtkinter.CTkFrame(master=self)
        self.frame4 = customtkinter.CTkFrame(master=self)
        self.frame5 = customtkinter.CTkFrame(master=self)
        self.frame6 = customtkinter.CTkFrame(master=self, height=60)
        self.frame7 = customtkinter.CTkFrame(master=self, fg_color='transparent', height=10)
        self.frame6.pack(side="top", fill='x')
        self.frame5.pack(expand=True, fill='both', padx=40)

        self.mode_change_light = customtkinter.CTkButton(self.frame6,
                                                         hover_color="dark blue",
                                                         command=self.change,
                                                         text="Change mode", )
        self.font_update = customtkinter.CTkButton(self.frame6,
                                                   hover_color="dark blue",
                                                   command=self.font_change,
                                                   text="Font Increase", )
        self.font_update_2 = customtkinter.CTkButton(self.frame6,
                                                     hover_color="dark blue",
                                                     command=self.font_change_2,
                                                     text="Font Decrease", )

        """self.nan = customtkinter.CTkButton(self,
                                           hover_color="dark blue",
                                           command=self.nan,
                                           text="nan", )"""

        self.card_changer = customtkinter.CTkButton(self.frame6,
                                                    hover_color="dark blue",
                                                    command=self.scheme,
                                                    text="Create New Card")
        self.mode_change_light.pack(side='left')
        self.font_update.pack(side='left')
        self.font_update_2.pack(side='left')

        self.label = customtkinter.CTkLabel(self.frame5,
                                            text="Welcome to Destiny 2 LFG Bingo",
                                            font=('', 26))
        if "Light" == customtkinter.get_appearance_mode():

            self.background = "light grey"
        else:
            self.background = '#2B2B2B'

        self.label.pack(padx=10, pady=40)
        self.button = customtkinter.CTkButton(self.frame5,
                                              hover_color="grey",
                                              text="Create Bingo Card",
                                              command=self.button_callback,
                                              font=('', 20),
                                              width=50, height=50)

        self.box0 = customtkinter.CTkButton(self.frame5,
                                            hover_color=self.first_hover_colour,
                                            fg_color=self.first_button_colour,
                                            text=self.pop_data[0],
                                            command=self.colour0,
                                            font=('', self.font),
                                            bg_color=self.background)
        self.box1 = customtkinter.CTkButton(self.frame5,
                                            hover_color=self.first_hover_colour,
                                            fg_color=self.first_button_colour,
                                            text=self.pop_data[1],
                                            command=self.colour1,
                                            font=('', self.font))
        self.box2 = customtkinter.CTkButton(self.frame5,
                                            hover_color=self.first_hover_colour,
                                            fg_color=self.first_button_colour,
                                            text=self.pop_data[2],
                                            command=self.colour2,
                                            font=('', self.font))
        self.box3 = customtkinter.CTkButton(self.frame5,
                                            hover_color=self.first_hover_colour,
                                            fg_color=self.first_button_colour,
                                            text=self.pop_data[3],
                                            command=self.colour3,
                                            font=('', self.font))
        self.box4 = customtkinter.CTkButton(self.frame5,
                                            hover_color=self.first_hover_colour,
                                            fg_color=self.first_button_colour,
                                            text=self.pop_data[4],
                                            command=self.colour4,
                                            font=('', self.font))
        self.box5 = customtkinter.CTkButton(self.frame4,
                                            hover_color=self.first_hover_colour,
                                            fg_color=self.first_button_colour,
                                            text=self.pop_data[5],
                                            command=self.colour5,
                                            font=('', self.font))
        self.box6 = customtkinter.CTkButton(self.frame4,
                                            hover_color=self.first_hover_colour,
                                            fg_color=self.first_button_colour,
                                            text=self.pop_data[6],
                                            command=self.colour6,
                                            font=('', self.font))
        self.box7 = customtkinter.CTkButton(self.frame4,
                                            hover_color=self.first_hover_colour,
                                            fg_color=self.first_button_colour,
                                            text=self.pop_data[7],
                                            command=self.colour7,
                                            font=('', self.font))
        self.box8 = customtkinter.CTkButton(self.frame4,
                                            hover_color=self.first_hover_colour,
                                            fg_color=self.first_button_colour,
                                            text=self.pop_data[8],
                                            command=self.colour8,
                                            font=('', self.font))
        self.box9 = customtkinter.CTkButton(self.frame4,
                                            hover_color=self.first_hover_colour,
                                            fg_color=self.first_button_colour,
                                            text=self.pop_data[9],
                                            command=self.colour9,
                                            font=('', self.font))
        self.box10 = customtkinter.CTkButton(self.frame3,
                                             hover_color=self.first_hover_colour,
                                             fg_color=self.first_button_colour,
                                             text=self.pop_data[10],
                                             command=self.colour10,
                                             font=('', self.font))
        self.box11 = customtkinter.CTkButton(self.frame3,
                                             hover_color=self.first_hover_colour,
                                             fg_color=self.first_button_colour,
                                             text=self.pop_data[11],
                                             command=self.colour11,
                                             font=('', self.font))
        self.box12 = customtkinter.CTkButton(self.frame3,
                                             hover_color=self.first_hover_colour,
                                             fg_color=self.first_button_colour,
                                             text=self.pop_data[12],
                                             command=self.colour12,
                                             font=('', self.font))
        self.box13 = customtkinter.CTkButton(self.frame3,
                                             hover_color=self.first_hover_colour,
                                             fg_color=self.first_button_colour,
                                             text=self.pop_data[13],
                                             command=self.colour13,
                                             font=('', self.font))
        self.box14 = customtkinter.CTkButton(self.frame3,
                                             hover_color=self.first_hover_colour,
                                             fg_color=self.first_button_colour,
                                             text=self.pop_data[14],
                                             command=self.colour14,
                                             font=('', self.font))
        self.box15 = customtkinter.CTkButton(self.frame2,
                                             hover_color=self.first_hover_colour,
                                             fg_color=self.first_button_colour,
                                             text=self.pop_data[15],
                                             command=self.colour15,
                                             font=('', self.font))
        self.box16 = customtkinter.CTkButton(self.frame2,
                                             hover_color=self.first_hover_colour,
                                             fg_color=self.first_button_colour,
                                             text=self.pop_data[16],
                                             command=self.colour16,
                                             font=('', self.font))
        self.box17 = customtkinter.CTkButton(self.frame2,
                                             hover_color=self.first_hover_colour,
                                             fg_color=self.first_button_colour,
                                             text=self.pop_data[17],
                                             command=self.colour17,
                                             font=('', self.font))
        self.box18 = customtkinter.CTkButton(self.frame2,
                                             hover_color=self.first_hover_colour,
                                             fg_color=self.first_button_colour,
                                             text=self.pop_data[18],
                                             command=self.colour18,
                                             font=('', self.font))
        self.box19 = customtkinter.CTkButton(self.frame2,
                                             hover_color=self.first_hover_colour,
                                             fg_color=self.first_button_colour,
                                             text=self.pop_data[19],
                                             command=self.colour19,
                                             font=('', self.font))
        self.box20 = customtkinter.CTkButton(self.frame1,
                                             hover_color=self.first_hover_colour,
                                             fg_color=self.first_button_colour,
                                             text=self.pop_data[20],
                                             command=self.colour20,
                                             font=('', self.font))
        self.box21 = customtkinter.CTkButton(self.frame1,
                                             hover_color=self.first_hover_colour,
                                             fg_color=self.first_button_colour,
                                             text=self.pop_data[21],
                                             command=self.colour21,
                                             font=('', self.font))
        self.box22 = customtkinter.CTkButton(self.frame1,
                                             hover_color=self.first_hover_colour,
                                             fg_color=self.first_button_colour,
                                             text=self.pop_data[22],
                                             command=self.colour22,
                                             font=('', self.font))
        self.box23 = customtkinter.CTkButton(self.frame1,
                                             hover_color=self.first_hover_colour,
                                             fg_color=self.first_button_colour,
                                             text=self.pop_data[23],
                                             command=self.colour23,
                                             font=('', self.font))
        self.box24 = customtkinter.CTkButton(self.frame1,
                                             hover_color=self.first_hover_colour,
                                             fg_color=self.first_button_colour,
                                             text=self.pop_data[24],
                                             command=self.colour24,
                                             font=('', self.font))

        self.button.pack(padx=20, pady=20)

    def font_change_2(self):
        self.font -= 1
        self.box0.configure(font=('', self.font))
        self.box1.configure(font=('', self.font))
        self.box2.configure(font=('', self.font))
        self.box3.configure(font=('', self.font))
        self.box4.configure(font=('', self.font))
        self.box5.configure(font=('', self.font))
        self.box6.configure(font=('', self.font))
        self.box7.configure(font=('', self.font))
        self.box8.configure(font=('', self.font))
        self.box9.configure(font=('', self.font))
        self.box10.configure(font=('', self.font))
        self.box11.configure(font=('', self.font))
        self.box12.configure(font=('', self.font))
        self.box13.configure(font=('', self.font))
        self.box14.configure(font=('', self.font))
        self.box15.configure(font=('', self.font))
        self.box16.configure(font=('', self.font))
        self.box17.configure(font=('', self.font))
        self.box18.configure(font=('', self.font))
        self.box19.configure(font=('', self.font))
        self.box20.configure(font=('', self.font))
        self.box21.configure(font=('', self.font))
        self.box22.configure(font=('', self.font))
        self.box23.configure(font=('', self.font))
        self.box24.configure(font=('', self.font))

    def font_change(self):
        self.font += 1
        self.box0.configure(font=('', self.font))
        self.box1.configure(font=('', self.font))
        self.box2.configure(font=('', self.font))
        self.box3.configure(font=('', self.font))
        self.box4.configure(font=('', self.font))
        self.box5.configure(font=('', self.font))
        self.box6.configure(font=('', self.font))
        self.box7.configure(font=('', self.font))
        self.box8.configure(font=('', self.font))
        self.box9.configure(font=('', self.font))
        self.box10.configure(font=('', self.font))
        self.box11.configure(font=('', self.font))
        self.box12.configure(font=('', self.font))
        self.box13.configure(font=('', self.font))
        self.box14.configure(font=('', self.font))
        self.box15.configure(font=('', self.font))
        self.box16.configure(font=('', self.font))
        self.box17.configure(font=('', self.font))
        self.box18.configure(font=('', self.font))
        self.box19.configure(font=('', self.font))
        self.box20.configure(font=('', self.font))
        self.box21.configure(font=('', self.font))
        self.box22.configure(font=('', self.font))
        self.box23.configure(font=('', self.font))
        self.box24.configure(font=('', self.font))

    def change(self):

        if "Light" == customtkinter.get_appearance_mode():

            customtkinter.set_appearance_mode("dark")
            self.background = '#2B2B2B'

        else:
            customtkinter.set_appearance_mode("light")
            self.background = "light grey"

        self.box0.configure(bg_color=self.background)
        self.box1.configure(bg_color=self.background)
        self.box2.configure(bg_color=self.background)
        self.box3.configure(bg_color=self.background)
        self.box4.configure(bg_color=self.background)
        self.box5.configure(bg_color=self.background)
        self.box6.configure(bg_color=self.background)
        self.box7.configure(bg_color=self.background)
        self.box8.configure(bg_color=self.background)
        self.box9.configure(bg_color=self.background)
        self.box10.configure(bg_color=self.background)
        self.box11.configure(bg_color=self.background)
        self.box12.configure(bg_color=self.background)
        self.box13.configure(bg_color=self.background)
        self.box14.configure(bg_color=self.background)
        self.box15.configure(bg_color=self.background)
        self.box16.configure(bg_color=self.background)
        self.box17.configure(bg_color=self.background)
        self.box18.configure(bg_color=self.background)
        self.box19.configure(bg_color=self.background)
        self.box20.configure(bg_color=self.background)
        self.box21.configure(bg_color=self.background)
        self.box22.configure(bg_color=self.background)
        self.box23.configure(bg_color=self.background)
        self.box24.configure(bg_color=self.background)

    def scheme(self):
        self.pop_data.clear()
        self.pop_data = random.sample(data, 25)

        self.box0.configure(text=self.pop_data[0], fg_color=self.first_button_colour)
        self.box1.configure(text=self.pop_data[1], fg_color=self.first_button_colour)
        self.box2.configure(text=self.pop_data[2], fg_color=self.first_button_colour)
        self.box3.configure(text=self.pop_data[3], fg_color=self.first_button_colour)
        self.box4.configure(text=self.pop_data[4], fg_color=self.first_button_colour)
        self.box5.configure(text=self.pop_data[5], fg_color=self.first_button_colour)
        self.box6.configure(text=self.pop_data[6], fg_color=self.first_button_colour)
        self.box7.configure(text=self.pop_data[7], fg_color=self.first_button_colour)
        self.box8.configure(text=self.pop_data[8], fg_color=self.first_button_colour)
        self.box9.configure(text=self.pop_data[9], fg_color=self.first_button_colour)
        self.box10.configure(text=self.pop_data[10], fg_color=self.first_button_colour)
        self.box11.configure(text=self.pop_data[11], fg_color=self.first_button_colour)
        self.box12.configure(text=self.pop_data[12], fg_color=self.first_button_colour)
        self.box13.configure(text=self.pop_data[13], fg_color=self.first_button_colour)
        self.box14.configure(text=self.pop_data[14], fg_color=self.first_button_colour)
        self.box15.configure(text=self.pop_data[15], fg_color=self.first_button_colour)
        self.box16.configure(text=self.pop_data[16], fg_color=self.first_button_colour)
        self.box17.configure(text=self.pop_data[17], fg_color=self.first_button_colour)
        self.box18.configure(text=self.pop_data[18], fg_color=self.first_button_colour)
        self.box19.configure(text=self.pop_data[19], fg_color=self.first_button_colour)
        self.box20.configure(text=self.pop_data[20], fg_color=self.first_button_colour)
        self.box21.configure(text=self.pop_data[21], fg_color=self.first_button_colour)
        self.box22.configure(text=self.pop_data[22], fg_color=self.first_button_colour)
        self.box23.configure(text=self.pop_data[23], fg_color=self.first_button_colour)
        self.box24.configure(text=self.pop_data[24], fg_color=self.first_button_colour)

    def button_callback(self):
        self.button.destroy()
        self.label.destroy()
        self.font_update.pack(side='left')
        self.font_update_2.pack(side='left')
        self.frame6.pack(expand=True)
        self.frame4.pack(expand=True, fill='both', padx=40)
        self.frame3.pack(expand=True, fill='both', padx=40)
        self.frame2.pack(expand=True, fill='both', padx=40)
        self.frame1.pack(expand=True, fill='both', padx=40)
        self.frame7.pack(expand=True, fill='y')
        self.card_changer.pack(side="left")
        self.box0.pack(side="left", expand=True, fill="both", padx=5, pady=5)
        self.box1.pack(side="left", expand=True, fill="both", padx=5, pady=5)
        self.box2.pack(side="left", expand=True, fill="both", padx=5, pady=5)
        self.box3.pack(side="left", expand=True, fill="both", padx=5, pady=5)
        self.box4.pack(side="left", expand=True, fill="both", padx=5, pady=5)
        self.box5.pack(side="left", expand=True, fill="both", padx=5, pady=5)
        self.box6.pack(side="left", expand=True, fill="both", padx=5, pady=5)
        self.box7.pack(side="left", expand=True, fill="both", padx=5, pady=5)
        self.box8.pack(side="left", expand=True, fill="both", padx=5, pady=5)
        self.box9.pack(side="left", expand=True, fill="both", padx=5, pady=5)
        self.box10.pack(side="left", expand=True, fill="both", padx=5, pady=5)
        self.box11.pack(side="left", expand=True, fill="both", padx=5, pady=5)
        self.box12.pack(side="left", expand=True, fill="both", padx=5, pady=5)
        self.box13.pack(side="left", expand=True, fill="both", padx=5, pady=5)
        self.box14.pack(side="left", expand=True, fill="both", padx=5, pady=5)
        self.box15.pack(side="left", expand=True, fill="both", padx=5, pady=5)
        self.box16.pack(side="left", expand=True, fill="both", padx=5, pady=5)
        self.box17.pack(side="left", expand=True, fill="both", padx=5, pady=5)
        self.box18.pack(side="left", expand=True, fill="both", padx=5, pady=5)
        self.box19.pack(side="left", expand=True, fill="both", padx=5, pady=5)
        self.box20.pack(side="left", expand=True, fill="both", padx=5, pady=5)
        self.box21.pack(side="left", expand=True, fill="both", padx=5, pady=5)
        self.box22.pack(side="left", expand=True, fill="both", padx=5, pady=5)
        self.box23.pack(side="left", expand=True, fill="both", padx=5, pady=5)
        self.box24.pack(side="left", expand=True, fill="both", padx=5, pady=5)

    def colour0(self):
        if self.first_button_colour == self.box0.fg_color:
            self.box0.configure(fg_color=self.second_button_colour, hover_color=self.second_hover_colour)
        else:
            self.box0.configure(fg_color=self.first_button_colour, hover_color=self.first_hover_colour)

    def colour1(self):
        if self.first_button_colour == self.box1.fg_color:
            self.box1.configure(fg_color=self.second_button_colour, hover_color=self.second_hover_colour)

        else:
            self.box1.configure(fg_color=self.first_button_colour, hover_color=self.first_hover_colour)

    def colour2(self):
        if self.first_button_colour == self.box2.fg_color:
            self.box2.configure(fg_color=self.second_button_colour, hover_color=self.second_hover_colour)

        else:
            self.box2.configure(fg_color=self.first_button_colour, hover_color=self.first_hover_colour)

    def colour3(self):
        if self.first_button_colour == self.box3.fg_color:
            self.box3.configure(fg_color=self.second_button_colour, hover_color=self.second_hover_colour)

        else:
            self.box3.configure(fg_color=self.first_button_colour, hover_color=self.first_hover_colour)

    def colour4(self):
        if self.first_button_colour == self.box4.fg_color:
            self.box4.configure(fg_color=self.second_button_colour, hover_color=self.second_hover_colour)

        else:
            self.box4.configure(fg_color=self.first_button_colour, hover_color=self.first_hover_colour)

    def colour5(self):
        if self.first_button_colour == self.box5.fg_color:
            self.box5.configure(fg_color=self.second_button_colour, hover_color=self.second_hover_colour)

        else:
            self.box5.configure(fg_color=self.first_button_colour, hover_color=self.first_hover_colour)

    def colour6(self):
        if self.first_button_colour == self.box6.fg_color:
            self.box6.configure(fg_color=self.second_button_colour, hover_color=self.second_hover_colour)

        else:
            self.box6.configure(fg_color=self.first_button_colour, hover_color=self.first_hover_colour)

    def colour7(self):
        if self.first_button_colour == self.box7.fg_color:
            self.box7.configure(fg_color=self.second_button_colour, hover_color=self.second_hover_colour)

        else:
            self.box7.configure(fg_color=self.first_button_colour, hover_color=self.first_hover_colour)

    def colour8(self):
        if self.first_button_colour == self.box8.fg_color:
            self.box8.configure(fg_color=self.second_button_colour, hover_color=self.second_hover_colour)

        else:
            self.box8.configure(fg_color=self.first_button_colour, hover_color=self.first_hover_colour)

    def colour9(self):
        if self.first_button_colour == self.box9.fg_color:
            self.box9.configure(fg_color=self.second_button_colour, hover_color=self.second_hover_colour)

        else:
            self.box9.configure(fg_color=self.first_button_colour, hover_color=self.first_hover_colour)

    def colour10(self):
        if self.first_button_colour == self.box10.fg_color:
            self.box10.configure(fg_color=self.second_button_colour, hover_color=self.second_hover_colour)

        else:
            self.box10.configure(fg_color=self.first_button_colour, hover_color=self.first_hover_colour)

    def colour11(self):
        if self.first_button_colour == self.box11.fg_color:
            self.box11.configure(fg_color=self.second_button_colour, hover_color=self.second_hover_colour)

        else:
            self.box11.configure(fg_color=self.first_button_colour, hover_color=self.first_hover_colour)

    def colour12(self):
        if self.first_button_colour == self.box12.fg_color:
            self.box12.configure(fg_color=self.second_button_colour, hover_color=self.second_hover_colour)

        else:
            self.box12.configure(fg_color=self.first_button_colour, hover_color=self.first_hover_colour)

    def colour13(self):
        if self.first_button_colour == self.box13.fg_color:
            self.box13.configure(fg_color=self.second_button_colour, hover_color=self.second_hover_colour)

        else:
            self.box13.configure(fg_color=self.first_button_colour, hover_color=self.first_hover_colour)

    def colour14(self):
        if self.first_button_colour == self.box14.fg_color:
            self.box14.configure(fg_color=self.second_button_colour, hover_color=self.second_hover_colour)

        else:
            self.box14.configure(fg_color=self.first_button_colour, hover_color=self.first_hover_colour)

    def colour15(self):
        if self.first_button_colour == self.box15.fg_color:
            self.box15.configure(fg_color=self.second_button_colour, hover_color=self.second_hover_colour)

        else:
            self.box15.configure(fg_color=self.first_button_colour, hover_color=self.first_hover_colour)

    def colour16(self):
        if self.first_button_colour == self.box16.fg_color:
            self.box16.configure(fg_color=self.second_button_colour, hover_color=self.second_hover_colour)

        else:
            self.box16.configure(fg_color=self.first_button_colour, hover_color=self.first_hover_colour)

    def colour17(self):
        if self.first_button_colour == self.box17.fg_color:
            self.box17.configure(fg_color=self.second_button_colour, hover_color=self.second_hover_colour)

        else:
            self.box17.configure(fg_color=self.first_button_colour, hover_color=self.first_hover_colour)

    def colour18(self):
        if self.first_button_colour == self.box18.fg_color:
            self.box18.configure(fg_color=self.second_button_colour, hover_color=self.second_hover_colour)

        else:
            self.box18.configure(fg_color=self.first_button_colour, hover_color=self.first_hover_colour)

    def colour19(self):
        if self.first_button_colour == self.box19.fg_color:
            self.box19.configure(fg_color=self.second_button_colour, hover_color=self.second_hover_colour)

        else:
            self.box19.configure(fg_color=self.first_button_colour, hover_color=self.first_hover_colour)

    def colour20(self):
        if self.first_button_colour == self.box20.fg_color:
            self.box20.configure(fg_color=self.second_button_colour, hover_color=self.second_hover_colour)

        else:
            self.box20.configure(fg_color=self.first_button_colour, hover_color=self.first_hover_colour)

    def colour21(self):
        if self.first_button_colour == self.box21.fg_color:
            self.box21.configure(fg_color=self.second_button_colour, hover_color=self.second_hover_colour)

        else:
            self.box21.configure(fg_color=self.first_button_colour, hover_color=self.first_hover_colour)

    def colour22(self):
        if self.first_button_colour == self.box22.fg_color:
            self.box22.configure(fg_color=self.second_button_colour, hover_color=self.second_hover_colour)

        else:
            self.box22.configure(fg_color=self.first_button_colour, hover_color=self.first_hover_colour)

    def colour23(self):
        if self.first_button_colour == self.box23.fg_color:
            self.box23.configure(fg_color=self.second_button_colour, hover_color=self.second_hover_colour)

        else:
            self.box23.configure(fg_color=self.first_button_colour, hover_color=self.first_hover_colour)

    def colour24(self):
        if self.first_button_colour == self.box24.fg_color:
            self.box24.configure(fg_color=self.second_button_colour, hover_color=self.second_hover_colour)

        else:
            self.box24.configure(fg_color=self.first_button_colour, hover_color=self.first_hover_colour)


app = App()
app.mainloop()
