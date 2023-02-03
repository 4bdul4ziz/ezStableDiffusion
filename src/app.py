import os
import tkinter as tk
import customtkinter as ctk
from PIL import ImageTk
from authtoken import auth_token
import torch
from torch import autocast
from diffusers import StableDiffusionPipeline, LMSDiscreteScheduler

# Create the app
app = tk.Tk()
app.geometry("532x632")
app.title("ezStableDiffusion")
ctk.set_appearance_mode("dark")

prompt = ctk.CTkEntry(app, height = 40, width = 512, font = ('Arial', 20), text_color="black", fg_color="white")
prompt.place(x=10, y=10)

lmain = ctk.CTkLabel(app, height=512, width=512)
lmain.place(x=10, y=110)

lms = LMSDiscreteScheduler(
    beta_start=0.00085, 
    beta_end=0.012, 
    beta_schedule="scaled_linear"
)

pipe = StableDiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5")
pipe = pipe.to("mps")
pipe.enable_attention_slicing()



def generate():
    _ = pipe(prompt.get(), num_inference_steps=1)
    image = pipe(prompt).images[0]
    image.save('generated.png')
    img = ImageTk.PhotoImage(image)
    lmain.configure(image=img)


trigger = ctk.CTkButton(app, height = 40, width = 120, font = ('Arial', 20), text_color="white", fg_color="blue", command=generate)
trigger.configure(text="Generate") 
trigger.place(x=206, y=60)

app.mainloop()