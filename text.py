import tkinter as tk


key_value = dict()

def cmd():
    global key_value
    with open("text.txt", "w") as file:
        pass
    
    text = entry_name.get()
    text1 = entry_surname.get()
    text2 = entry_username.get().lower()
    text3 = entry_password.get()
    text4 = entry_email.get()
    text5 = entry_phone.get()
    text6 = entry_address.get()
    text7 = entry_city.get()
    text8 = entry_country.get()
    
    key_value = {
        "Username": text2, 
        "Password": text3
    }
    
    
    if text and text.strip():
        with open("text.txt", "a") as file:
            file.write(f"Name: {text.capitalize()}\n")
    else:
        title_label.config(text="Error!!!!", font=("Verdana", 20), bg="red")
        return 

    if text1 and text1.strip():
        with open("text.txt", "a") as file:
            file.write(f"Surname: {text1.capitalize()}\n")
    else:
        title_label.config(text="Error!!!!", font=("Verdana", 20), bg="red")
        return

    if text2 and text2.strip():
        with open("text.txt", "a") as file:
            file.write(f"Username: {text2}\n")
    else:
        title_label.config(text="Error!!!!", font=("Verdana", 20), bg="red")
        return

    if text3 and text3.strip():
        with open("text.txt", "a") as file:
            file.write(f'Password: {text3}\n')
    else:
        title_label.config(text="Error!!!!", font=("Verdana", 20), bg="red")
        return

    if text4 and text4.strip():
        with open("text.txt", "a") as file:
            file.write(f"Email: {text4}\n")
    else:
        title_label.config(text="Error!!!!", font=("Verdana", 20), bg="red")
        return

    if text5 and text5.strip():
        with open("text.txt", "a") as file:
            file.write(f"Phone number: {text5}\n")
    else:
        with open("text.txt", "a") as file:
            file.write(f"Phone number: None\n")

    if text6 and text6.strip():
        with open("text.txt", "a") as file:
            file.write(f"Address: {text6.capitalize()}\n")
    else:
        with open("text.txt", "a") as file:
            file.write(f"Address: None\n")

    if text7 and text7.strip():
        with open("text.txt", "a") as file:
            file.write(f"City: {text7.capitalize()}\n")
    else:
        with open("text.txt", "a") as file:
            file.write(f"City: None\n")

    if text8 and text8.strip():
        with open("text.txt", "a") as file:
            file.write(f"Country: {text8.capitalize()}\n")
    else:
        with open("text.txt", "a") as file:
            file.write(f"Country: None\n")
    
    
    frame1.pack_forget()
    frame2.pack(fill="both", expand=True)
    

    label_name_2.config(text=f"Name: {text.capitalize()}")
    label_surname_2.config(text=f"Surname: {text1.capitalize()}")
    label_username_2.config(text=f"Username: {text2}")
    label_email_2.config(text=f"Email: {text4}")
    label_phone_2.config(text=f"Phone number: {text5 if text5 else 'None'}")
    label_address_2.config(text=f"Address: {text6.capitalize() if text6 else 'None'}")
    label_city_2.config(text=f"City: {text7.capitalize() if text7 else 'None'}")
    label_country_2.config(text=f"Country: {text8.capitalize() if text8 else 'None'}")


def toggle_password():
    if entry_password.cget('show') == '':
        entry_password.config(show='*')
        button_password.config(text="Show\npassword")
    else:
        entry_password.config(show='')
        button_password.config(text="Hide\nPassword")
        
def toggle_password1():
    if password_entry.cget('show') == '':
        password_entry.config(show='*')
        password_button.config(text="Show\npassword")
    else:
        password_entry.config(show='')
        password_button.config(text="Hide\nPassword")

def go_to_registr():
    frame2.pack_forget()
    frame1.pack(fill="both", expand=True)
    
def go_to_login():
    frame2.pack_forget()
    frame3.pack(fill="both", expand=True)
    
def login():
    user_text = user_entry.get().lower()
    pass_text = password_entry.get()
    first_value = key_value.get("Username", "")
    second_value = key_value.get("Password", "")
    if user_text == first_value:
        if pass_text == second_value:
            title_log.config(text="Congratulation", bg="green", font=("Verdana", 20))
    if user_text == first_value:
        if pass_text != second_value:
            title_log.config(text="Oups. Error password", bg="red", font=("Verdana", 20))
    if user_text != first_value:
        title_log.config(text="Oups. Error username", bg="red", font=("Verdana", 20))

root = tk.Tk()
root.title("REGESTRACJA")
root.geometry("300x500")

frame1 = tk.Frame(root)
frame1.pack(fill="both", expand=True)

label_name = tk.Label(frame1, text="Name:")
entry_name = tk.Entry(frame1, width=20, highlightbackground="red", highlightcolor="red", highlightthickness=2)

label_name.grid(row=3, column=0, padx=5, pady=5, sticky='e')
entry_name.grid(row=3, column=1, padx=5, pady=5)


label_surname = tk.Label(frame1, text="Surname:")
entry_surname = tk.Entry(frame1, width=20, highlightbackground="red", highlightcolor="red", highlightthickness=2)

label_surname.grid(row=4, column=0, padx=5, pady=5, sticky='e')
entry_surname.grid(row=4, column=1, padx=5, pady=5)


label_username = tk.Label(frame1, text="Username:")
entry_username = tk.Entry(frame1, width=20, highlightbackground="red", highlightcolor="red", highlightthickness=2)

label_username.grid(row=5, column=0, padx=5, pady=5, sticky='e')
entry_username.grid(row=5, column=1, padx=5, pady=5)


label_password = tk.Label(frame1, text="Password:")
entry_password = tk.Entry(frame1, width=20, highlightbackground="red", highlightcolor="red", highlightthickness=2, show="*")
button_password = tk.Button(frame1, text="Show\npassword", command=toggle_password)

label_password.grid(row=6, column=0, padx=5, pady=5, sticky="e")
entry_password.grid(row=6, column=1, padx=5, pady=5)
button_password.grid(row=6, column=2, padx=5, pady=5)


label_email = tk.Label(frame1, text="Email:")
entry_email = tk.Entry(frame1, width=20, highlightbackground="red", highlightcolor="red", highlightthickness=2)

label_email.grid(row=7, column=0, padx=5, pady=5, sticky='e')
entry_email.grid(row=7, column=1, padx=5, pady=5)


label_phone = tk.Label(frame1, text="Phone \nnumber:")
entry_phone = tk.Entry(frame1, width=20)

label_phone.grid(row=8, column=0, padx=5, pady=5, sticky="e")
entry_phone.grid(row=8, column=1, padx=5, pady=5)


label_address = tk.Label(frame1, text="Address:")
entry_address = tk.Entry(frame1, width=20)

label_address.grid(row=9, column=0, padx=5, pady=5, sticky="e")
entry_address.grid(row=9, column=1, padx=5, pady=5)


label_city = tk.Label(frame1, text="City:")
entry_city = tk.Entry(frame1, width=20)

label_city.grid(row=10, column=0, padx=5, pady=5, sticky="e")
entry_city.grid(row=10, column=1, padx=5, pady=5)


label_country = tk.Label(frame1, text="Country:")
entry_country = tk.Entry(frame1, width=20)

label_country.grid(row=11, column=0, padx=5, pady=5, sticky="e")
entry_country.grid(row=11, column=1, padx=5, pady=5)


title_label = tk.Label(frame1, text="REGESTRACJA", font=("Verdana", 15))
title_label.grid(row=0, column=0, columnspan=5, pady=10)

entry = tk.Entry(frame1, width=10, highlightbackground="red", highlightcolor="red", highlightthickness=2)
label = tk.Label(frame1, text=" - entry with a red border \nmust be filled out")

entry.grid(row=1, column=0, pady=5, padx=5, sticky="e")
label.grid(row=1, column=1, pady=5, padx=5)

register_button = tk.Button(frame1, text="To register", width=20, font=("Verdana", 12), command=cmd)
register_button.grid(row=12, column=0, columnspan=4, pady=10, sticky="ns")

frame2 = tk.Frame(root)

title = tk.Label(frame2, text="YOUR DATA", font=("Verdana", 12))
title.pack(pady=10)

label_name_2 = tk.Label(frame2, text="")
label_name_2.pack()

label_surname_2 = tk.Label(frame2, text="")
label_surname_2.pack()

label_username_2 = tk.Label(frame2, text="")
label_username_2.pack()

label_email_2 = tk.Label(frame2, text="")
label_email_2.pack()

label_phone_2 = tk.Label(frame2, text="")
label_phone_2.pack()

label_address_2 = tk.Label(frame2, text="")
label_address_2.pack()

label_city_2 = tk.Label(frame2, text="")
label_city_2.pack()

label_country_2 = tk.Label(frame2, text="")
label_country_2.pack()

button_back = tk.Button(frame2, text="Back", width=15, command=go_to_registr )
button_back.pack(side='left')

button_go = tk.Button(frame2, text="Login", width=15, command=go_to_login)
button_go.pack(side="right")

frame3 = tk.Frame(root)

title_log = tk.Label(frame3, text="LOG IN", font=("Verdana", 12))
title_log.grid(row=0,column=0, columnspan=5, pady=10)

user_label = tk.Label(frame3, text="Username: ")
user_entry = tk.Entry(frame3, width=20)

user_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")
user_entry.grid(row=1, column=1, padx=5, pady=5)

password_label = tk.Label(frame3, text="Password: ")
password_entry = tk.Entry(frame3, width=20, show="*")
password_button = tk.Button(frame3, text="Show\n password", command=toggle_password1)

password_label.grid(row=2, column=0, padx=5, pady=5, sticky="e")
password_entry.grid(row=2, column=1, padx=5, pady=5)
password_button.grid(row=2, column=2, padx=5, pady=5)

login_button = tk.Button(frame3, text="Log In", command=login)
login_button.grid(row=3, column=0, columnspan=5, padx=10, pady=10)

root.mainloop()