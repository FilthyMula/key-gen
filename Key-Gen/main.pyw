import random, string, pyperclip, json, os, sys, webbrowser, random, array
from tkinter import *


with open('Utils/keys.json') as f:
    config = json.load(f)
    default = config.get('default')
    custom = config.get('custom')
    upper_c = config.get('upper_c')
    lower_c = config.get('lower_c')
    symbols = config.get('symbols')
    digitzz = config.get('digitzz')
    

gen = Tk()
gen.iconbitmap("Utils/key.ico")
gen.title("Key generator")
gen.config(bg='grey20')
w = 797
h = 486
screen_width = gen.winfo_screenwidth()
screen_height = gen.winfo_screenheight()
x = (screen_width/2) - (w/2)
y = (screen_height/2) - (h/2)
gen.geometry('%dx%d+%d+%d' % (w, h, x, y))
gen.resizable(False,False)

def restart():
    os.execv(sys.executable, ['python'] + sys.argv)
    
def custom_key_on():
    with open('Utils/keys.json', 'r') as f: 
        data = json.load(f) 
        data['custom'] = 'on'
        data['default'] = 'off'
                
    with open('Utils/keys.json', 'w') as f: 
        json.dump(data, f, indent=4)
    restart()

def default_key_on():
    with open('Utils/keys.json', 'r') as f: 
        data = json.load(f) 
        data['default'] = 'on' 
        data['custom'] = 'off'
                
    with open('Utils/keys.json', 'w') as f: 
        json.dump(data, f, indent=4)
    restart()
    
def add_key():
    if default == 'on':
        key = (''.join(random.choices(string.ascii_letters + string.digits, k=4)).upper() + '-' + ''.join(random.choices(string.ascii_letters + string.digits, k=4)).upper() + '-' + ''.join(random.choices(string.ascii_letters + string.digits, k=4)).upper() + '-' + ''.join(random.choices(string.ascii_letters + string.digits, k=4)).upper())
        key_list_box.insert(END, key)
        status_bar.config(text='Generated key')
    elif custom == 'on':
        try:
            custom_key()
            status_bar.config(text='Generated custom key')
        except:
            status_bar.config(text='minimum digits for custom key: 4')
    else:
        status_bar.config(text='Key type has not been selected')
        
def copy_key():
    f = key_list_box.get(ANCHOR)
    pyperclip.copy(f)
    if f == '':
        status_bar.config(text='Key must be selected to copy')
    else:
        status_bar.config(text='Copied key')
        
def copy_all_keys():
    f = key_list_box.get(0, END)
    if f:
        pyperclip.copy(str(f).replace(" ", "\n").replace(",", "").replace("'", "").replace("(", "").replace(")", ""))
        status_bar.config(text='Copied all keys')
    else:
        status_bar.config(text='No keys to copy')

def delete_key():
    if key_list_box.get(0, END):
        key_list_box.delete(ANCHOR)
        status_bar.config(text='Deleted key')
    else:
        status_bar.config(text='Key must be selected to delete')

def delete_all_keys():
    if key_list_box.get(0, END):
        key_list_box.delete(0, END)
        status_bar.config(text='Deleted all keys')
    else:
        status_bar.config(text='No keys to delete')

def save_keys():
    keys = key_list_box.get(0, END)
    if keys:
        f = open('Utils/keys.txt', 'a+')
        f.write(str(keys).replace(" ", "\n").replace(",", "").replace("'", "").replace("(", "").replace(")", "") + '\n')
        f.close()
        key_list_box.delete(0, END)
        status_bar.config(text='Saved all keys')
    else:
        status_bar.config(text='No keys to save')

def delete_all_keys_from_txt():
    open('Utils/keys.txt', 'w').close()
    view_keys_w.destroy()

def copy_all_keys_from_txt():
    f = open('Utils/keys.txt', 'r').read()
    pyperclip.copy(f)

def view_keys():
    global view_keys_w
    f = open('Utils/keys.txt')
    view_keys_w = Tk()
    view_keys_w.resizable(False,False)
    view_keys_w.iconbitmap("Utils/key.ico")
    view_keys_w.title('All keys')
    view_keys_w.config(bg='grey20')
    width = 498  
    height = 500
    screen_width = view_keys_w.winfo_screenwidth()
    screen_height = view_keys_w.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    view_keys_w.geometry('%dx%d+%d+%d' % (width, height, x, y))
    
    h = Scrollbar(view_keys_w, orient = 'horizontal')
    h.pack(side = BOTTOM, fill = X)
    v = Scrollbar(view_keys_w)
    v.pack(side = RIGHT, fill = Y)

    shownotes = Text(view_keys_w, bg='grey10', fg='lightgreen', font='consolas 12', wrap = NONE,xscrollcommand = h.set,yscrollcommand = v.set, width=53, height=23)
    shownotes.insert(END, f.read())
    shownotes.pack(side=TOP, fill=X)
    h.config(command=shownotes.xview)
    v.config(command=shownotes.yview)
    
    delete_all = Button(view_keys_w, text='Delete all', bg='grey20', fg='white', bd=2, width=15, command=delete_all_keys_from_txt)
    delete_all.place(x=5,y=450)
    
    copy_all = Button(view_keys_w, text='Copy all', bg='grey20', fg='white', bd=2, width=15, command=copy_all_keys_from_txt)
    copy_all.place(x=135,y=450)
    
    view_keys_w.mainloop()

upper_is_on = True
def upper_switch():
    global upper_is_on
    if upper_is_on:
        upper_case.config(text='off')
        upper_is_on = False
        with open('Utils/keys.json', 'r') as f: 
            data = json.load(f) 
            data['upper_c'] = 'off'
            
        with open('Utils/keys.json', 'w') as f: 
            json.dump(data, f, indent=4)
        restart()
    else:
        upper_case.config(text='on')
        upper_is_on = True
        with open('Utils/keys.json', 'r') as f: 
            data = json.load(f) 
            data['upper_c'] = 'on'
            
        with open('Utils/keys.json', 'w') as f: 
            json.dump(data, f, indent=4)
        restart()

lower_is_on = True
def lower_switch():
    global lower_is_on
    if lower_is_on:
        lower_case.config(text='off')
        lower_is_on = False
        with open('Utils/keys.json', 'r') as f: 
            data = json.load(f) 
            data['lower_c'] = 'off'
            
        with open('Utils/keys.json', 'w') as f: 
            json.dump(data, f, indent=4)
        restart()
    else:
        lower_case.config(text='on')
        lower_is_on = True
        with open('Utils/keys.json', 'r') as f: 
            data = json.load(f) 
            data['lower_c'] = 'on'
            
        with open('Utils/keys.json', 'w') as f: 
            json.dump(data, f, indent=4)
        restart()
        
symbols_is_on = True
def symbolss_switch():
    global symbols_is_on
    if symbols_is_on:
        symbolss.config(text='off')
        symbols_is_on = False
        with open('Utils/keys.json', 'r') as f: 
            data = json.load(f) 
            data['symbols'] = 'off'
            
        with open('Utils/keys.json', 'w') as f: 
            json.dump(data, f, indent=4)
        restart()
    else:
        symbolss.config(text='on')
        symbols_is_on = True
        with open('Utils/keys.json', 'r') as f: 
            data = json.load(f) 
            data['symbols'] = 'on'
            
        with open('Utils/keys.json', 'w') as f: 
            json.dump(data, f, indent=4)
        restart()

digitss_is_on = True
def digitss_switch():
    global digitss_is_on
    if digitss_is_on:
        digitss.config(text='off')
        digitss_is_on = False
        with open('Utils/keys.json', 'r') as f: 
            data = json.load(f) 
            data['digitzz'] = 'off'
            
        with open('Utils/keys.json', 'w') as f: 
            json.dump(data, f, indent=4)
        restart()
    else:
        digitss.config(text='on')
        digitss_is_on = True
        with open('Utils/keys.json', 'r') as f: 
            data = json.load(f) 
            data['digitzz'] = 'on'
            
        with open('Utils/keys.json', 'w') as f: 
            json.dump(data, f, indent=4)
            
        restart()

def custom_key():
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] 
    lower_chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                        'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                        'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                        'z']
    
    upper_chars = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                        'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q',
                        'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                        'Z']
    
    symbolz = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
            '*', '(', ')', '<']
    
    if upper_c == 'on':
        combined = upper_chars
    if upper_c and lower_c == 'on':
        combined = upper_chars + lower_chars 
    if upper_c and lower_c and symbols == 'on':
        combined = upper_chars + lower_chars + symbolz
    if upper_c and lower_c and symbols and digitss == 'on':
        combined = upper_chars + lower_chars + symbolz + digitzz

    rand_digit = random.choice(digits)
    rand_upper = random.choice(upper_chars)
    rand_lower = random.choice(lower_chars)
    rand_symbol = random.choice(symbolz)

    if upper_c == 'on':
        temp_pass = rand_upper
    if upper_c and lower_c == 'on':
        temp_pass = rand_upper + rand_lower
    if upper_c and lower_c and symbols == 'on':
        temp_pass = rand_upper + rand_lower + rand_symbol
    if upper_c and lower_c and symbols and digitzz == 'on':
        temp_pass = rand_upper + rand_lower + rand_symbol + rand_digit

    key_length = (int(custom_key_length.get()))
    equal_key = 3
    Subtract = int(key_length) -int(equal_key)
    for x in range(int(Subtract)):
        temp_pass = temp_pass + random.choice(combined)

        temp_pass_list = array.array('u', temp_pass)
        random.shuffle(temp_pass_list)

    password = ""
    for x in temp_pass_list:
            password = password + x

    key_list_box.insert(END, password)

        
#menu
my_menu = Menu(gen)
gen.config(menu=my_menu)

#main menu
main_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Menu",menu=main_menu)
main_menu.add_command(label='Copy key', command=copy_key)
main_menu.add_command(label='Copy all keys', command=copy_all_keys)
main_menu.add_separator()
main_menu.add_command(label='Delete key', command=delete_key)
main_menu.add_command(label='Delete all keys', command=delete_all_keys)
main_menu.add_separator()
main_menu.add_command(label='Save keys', command=save_keys)
main_menu.add_command(label='View keys', command=view_keys)

#key menu
key_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Key type",menu=key_menu)
key_menu.add_command(label='XXXX-XXXX-XXXX-XXXX', command=default_key_on)
key_menu.add_separator()
key_menu.add_command(label='Custom keys', command=custom_key_on)

def discord_url():
    d_url = 'https://discord.gg/uYjVJmXQGt'
    webbrowser.open(d_url)
    
#custom keys
if custom == 'on':
    #length
    Label(gen, text='Length', bg='grey20', fg='white', font='consolas 12').place(x=12,y=0)
    custom_key_length = Entry(gen, width=10)
    custom_key_length.place(x=10,y=25)
    
    #upper case on/off
    f = open('Utils/keys.json')
    data = json.load(f)
    value = data['upper_c']
    Label(gen, text='Upper case', bg='grey20', fg='white', font='consolas 12').place(x=99,y=0)
    upper_case = Button(gen, text=value, bg='grey10', fg='white', activebackground='grey20', width=13, bd=0, command=upper_switch)
    upper_case.place(x=100,y=25)
    f.close()
    
    #lower case on/off
    f = open('Utils/keys.json')
    data = json.load(f)
    value = data['lower_c']
    Label(gen, text='Lower case', bg='grey20', fg='white', font='consolas 12').place(x=205,y=0)
    lower_case = Button(gen, text=value, bg='grey10', fg='white', activebackground='grey20', width=13, bd=0, command=lower_switch)
    lower_case.place(x=205,y=25)
    f.close()
    
    #symbols on/off
    f = open('Utils/keys.json')
    data = json.load(f)
    value = data['symbols']
    Label(gen, text='Symbols', bg='grey20', fg='white', font='consolas 12').place(x=325,y=0)
    symbolss = Button(gen, text=value, bg='grey10', fg='white', activebackground='grey20', width=13, bd=0, command=symbolss_switch)
    symbolss.place(x=310,y=25)
    f.close()
    
    #digits on/off
    f = open('Utils/keys.json')
    data = json.load(f)
    value = data['digitzz']
    Label(gen, text='Digits', bg='grey20', fg='white', font='consolas 12').place(x=433,y=0)
    digitss = Button(gen, text=value, bg='grey10', fg='white', activebackground='grey20', width=13, bd=0, command=digitss_switch)
    digitss.place(x=415,y=25)
    f.close()

else:
    Label(gen, text='Complex Services Key Generator - Version 1.0', bg='grey20', fg='lightgreen', font='consolas 15').place(x=5,y=1)
    Button(gen, text='Complex Discord', bg='grey10', fg='lightgreen', width=30, bd=0, command=discord_url).place(x=5,y=35)

#generate key button
gen_key_btn = Button(gen,
                     text='Generate key',
                     width=30,
                     bg='grey10', 
                     fg='lightgreen',
                     bd=0,
                     command=add_key)
gen_key_btn.place(x=5,y=95)

#key list box
key_list_box = Listbox(gen,
                       bg="black",
                       fg="lightgreen",
                       width=72,
                       height=13,
                       font='consolas 15',
                       selectbackground="lightgreen",
                       selectforeground="black",
                       bd=0)
key_list_box.place(x=1,y=120)

#stastus bar
status_bar = Label(gen,
                   text='',
                   bd=0,
                   bg='grey10',
                   fg='lightgreen',
                   relief=GROOVE,
                   font='consolas 15')
status_bar.pack(fill=X, side=BOTTOM, ipady=2)


gen.mainloop()