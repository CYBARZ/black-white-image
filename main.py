from tkinter import *
import tkinter as tk
from tkinter import ttk
import os
import glob
import moviepy.editor as mp
from tkinter import filedialog
from PIL import ImageTk,Image
import numpy as np
import cv2
import datetime
import time
import argparse
from os.path import isfile, join
from colorsample import *



splash_root = Tk()

# setting up our main windwo alignment
app_width = 1060
app_height = 600
screen_width = splash_root.winfo_screenwidth()
screen_height = splash_root.winfo_screenheight()

#finding the center of the screen
x = (screen_width / 2) - (app_width / 2)
y = (screen_height / 2 ) - (app_height / 2)

splash_root.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
splash_root.title("Splash Screen!!")
# Hide the title bar
splash_root.overrideredirect(True)


splashbg = PhotoImage(file="assets\images\samplebg.png")
my_labelbg=Label(splash_root, image=splashbg)
my_labelbg.place(x=0,y=0,relwidth=1,relheight=1)


file="assets\images\preloader.gif"
info = Image.open(file)

frames = info.n_frames  # gives total number of frames that gif contains

# creating list of PhotoImage objects for each frames
im = [tk.PhotoImage(file=file,format=f"gif -index {i}") for i in range(frames)]

count = 0
anim = None
def animation(count):
    global anim
    im2 = im[count]

    gif_label.configure(image=im2)
    count += 1
    if count == frames:
        count = 0
    anim = splash_root.after(50,lambda :animation(count))

gif_label = tk.Label(splash_root,image="")
gif_label.pack(side=RIGHT,padx=100)

animation(count)




def main_window():
	# Kill the splash screen
	splash_root.destroy()
	





	# setting up our main windwo alignment
	root=Tk()
	app_width = 1060
	app_height = 600
	screen_width = root.winfo_screenwidth()
	screen_height = root.winfo_screenheight()

	#finding the center of the screen
	x = (screen_width / 2) - (app_width / 2)
	y = (screen_height / 2 ) - (app_height / 2)

	root.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
	root.title('A Deep Learning Method for Coloring Black and White Videos and Images')
	#root.iconbitmap('c:/gui/colorise.ico')



	
	

#------Image coloring module page-------
	def imagecolorise():

		
		#functions in this module
		def browseFiles():
			
			filename = filedialog.askopenfilename(initialdir = "/",
											title = "Select a File",
											filetypes = (("all files",
															"*.*"),("Image files",
															"*.png*")))
														
		

			#creating ui elements  showing input image and its properties)
			section_3 = LabelFrame(window,padx=10, pady=10, text="Input image",highlightbackground="#6285E2",highlightthickness=3)
			section_3.pack(side=LEFT,padx=60)

			
			
			input_image = PhotoImage(file=filename)
			my_canvas4 = Canvas(section_3, width=430, height=300)
			my_canvas4.pack(fill="both", expand=True)
			my_canvas4.create_image(0,0, image=input_image, anchor="nw")
			


			#showing properties of the selected image
			section_4 = LabelFrame(window, padx=10, pady=20,text="File selected",background="#6285E2", highlightbackground="#6285E2",highlightthickness=2)
			section_4.pack(side=RIGHT,padx=20)
			print(filename)
			#labels inside section_4 (image properties,button,progressbar)
			label_image_opened_data = Label(section_4,
								text = "File opened : "+ filename,
								fg = "black",height=2 ).pack()
			opened_time=datetime.datetime.now()
			label_image_height = Label(section_4,
								text = "Opened time : "+ opened_time.strftime( "%y-%m-%d %H: %M :%S" ),
								fg = "black",height=2 ).pack()
			#progress bar
			bar = ttk.Progressbar(section_4, orient=HORIZONTAL,length=400, mode='determinate')
			bar.pack(pady=20)
			download = 0
			speed = 1
			while(download<100):
				time.sleep(0.05)
				bar['value']+=(speed/100)*100
				download+=speed
				section_4.update_idletasks()
			bar.destroy()
			open_image_in_cv_browser=cv2.imread(filename)
			cv2.imshow("window3",open_image_in_cv_browser)
			cv2.waitKey(0)
			window.destroy()
			color(filename)
			#cv2.destroyWindow()
			#button_colorize = Button(section_4,
					##		text = "Colorize now",bd=8,
					#		bg="#6285E2",
					#		fg="white",
					#		activeforeground="Orange",
					#		activebackground="green",
					#		font="Andalus",
					#		highlightcolor="purple"	justify="right",
					#		padx=50,
					#		relief="groove", command = color(filename)).pack()'''
			
		


			


			
			

		#destroying previous window and setting our image coloring window    
		root.destroy()
		window = Tk()


		# setting up our second windwo alignment
		app_width = 1060
		app_height = 600
		screen_width = window.winfo_screenwidth()
		screen_height = window.winfo_screenheight()

		#finding the center of the screen
		x = (screen_width / 2) - (app_width / 2)
		y = (screen_height / 2 ) - (app_height / 2)

		window.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
		

		bgnm = PhotoImage(file="assets\images\img1.png")
		my_labelbg=Label(window, image=bgnm)
		my_labelbg.place(x=0,y=0,relwidth=1,relheight=1)
		#Create a canvas for image
		section_1 = Frame(window,highlightbackground="red",padx=50, pady=15,background="#6285E2")
		section_1.pack(side=TOP,fill=X,pady=20,padx=20)
		label_1= Label(section_1,text = "SELECT AN IMAGE TO BE COLORED ",fg = "white",font=("Times", 18, "bold"),background="#6285E2",
							).pack()

		section_2 = LabelFrame(window,highlightbackground="red",background="#6285E2",padx=50, pady=10)
		section_2.pack(side=TOP,fill=X,pady=10,padx=20)
		label_file_explorer = Label(section_2,
								text = "*********** NB: Image should be in .png format *********** ",
								bg="#6285E2",
								fg = "yellow",height=2 )
		button_explore = Button(section_2,
							text = "Browse Files",bd=8,
							bg="black",
							fg="green",
							activeforeground="Orange",
							activebackground="green",
							font="Andalus",
							highlightcolor="purple",
							justify="right",
							padx=50,
							relief="groove", command = browseFiles)
		label_file_explorer.pack(side=LEFT,padx=50)
		button_explore.pack(side=RIGHT)
		


		
		
		
		
		
		window.mainloop()


	#------Video coloring module page-------
	def videocolorise():
		print("hello")
	# #pending code










		

	# ------OUR MAIN HOME PAGE DESIGN STARTS HERE---------

	# Define image for background

	bgn = PhotoImage(file="assets\images\img1.png")
		# Create a canvas for display the backround image
	my_canvas = Canvas(root, width=1000, height=600)
	my_canvas.pack(fill="both", expand=True)

		# Setting background image in canvas
	my_canvas.create_image(0,0, image=bgn, anchor="nw")

		# Addig all labels here
	my_canvas.create_text(540, 140, text="A Deep Learning Method for Coloring Black and White", font=("Helvetica", 25, "bold"), fill="white")
	my_canvas.create_text(540, 175, text="Videos and Images", font=("Helvetica", 25,"bold"), fill="white")
	my_canvas.create_text(540, 275, text="Sometimes all you need is a little splash of color.", font=("Times", 16,"bold"), fill="white")
	my_canvas.create_text(530, 390, text="or", font=("Times", 16,"bold"), fill="white")
	my_canvas.create_text(530, 550, text="Version : 1.0", font=("Times", 16), fill="white")

		#setting images for buttons
	imgbtn = PhotoImage(file="assets\images\imgsample.png")
	vidbtn = PhotoImage(file="assets\images\imgsample2.png")
		# adding  buttons
	button1 = Button(root, image=imgbtn,border=0, width=220,height=50,command=imagecolorise)
	button2 = Button(root, image=vidbtn,border=0,width=220,height=50,command=videocolorise)
	button1_window = my_canvas.create_window(380, 390, anchor="center", window=button1)
	button2_window = my_canvas.create_window(690, 390, anchor="center", window=button2)


	root.mainloop()
		


# Splash Screen Timer
splash_root.after(3000, main_window)
splash_root.mainloop()








