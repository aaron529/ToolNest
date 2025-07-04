import customtkinter as tk
from forms.login import LoginForm
        
app = tk.CTk()

# configuration
tk.set_appearance_mode("dark")
app.iconbitmap("images/icon.ico")
app.resizable(False, False)

# bg = ("#ebebeb", "#1D1D1D")
# primary = ("#C7C7C7", "#1D1D1D")
# secondary = ("#B6B6B6", "#161616")

def switch_theme():
    themeSwitch.configure(text=f"{themeSwitch.get().capitalize()}")
    tk.set_appearance_mode(themeSwitch.get())

# theme switcher
theme = tk.StringVar(value="dark")
themeSwitch = tk.CTkSwitch(app, text="Dark", font=("Arial Bold", 15), variable=theme, onvalue="dark", offvalue="light", progress_color="black", command=switch_theme)
themeSwitch.place(x=1, y=0)

# initiate login form
LoginForm(app).initialize()

app.mainloop()