from tkinter import *
from tkinter import scrolledtext
from tkinter.ttk import Combobox
from tkinter import messagebox

def clicked():
    txt_original = txt.get("1.0", 'end-1c')
    txt2.delete(1.0, END)
    eng_upp_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    eng_low_alphabet = 'abcdefghijklmnopqrstuvwxyz'
    rus_upp_alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    rus_low_alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    step=int(spin.get())

    for i in txt_original:
        index=-5
        for j in range(0, 1):
            index = eng_upp_alphabet.find(i, 0)
            if (index!=-1):
                alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
                alphabet_size=26
                break
            if (index==-1):
                index = eng_low_alphabet.find(i, 0)
                if(index != -1):
                    alphabet = 'abcdefghijklmnopqrstuvwxyz'
                    alphabet_size = 26
                    break
                if (index == -1):
                    index = rus_upp_alphabet.find(i, 0)
                    if (index != -1):
                        alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
                        alphabet_size = 33
                        break
                    if (index == -1):
                        index = rus_low_alphabet.find(i, 0)
                        if (index != -1):
                            alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
                            alphabet_size = 33
                            break
                        #if (index != '/n'):
                        #    messagebox.showinfo('Ошибка!', f'Вы ввели неизвестный символ!)')
        if index == -1:
            txt2.insert(INSERT, i)
        else:
            if ((combo2.get()=='Зашифровать') | (combo2.get()=='Расшифровать')):
                if combo2.get()=='Зашифровать':
                    txt2.insert(INSERT, alphabet[(index + step) % alphabet_size])
                if combo2.get() == 'Расшифровать':
                    txt2.insert(INSERT, alphabet[(index - step) % alphabet_size])
            else:
                messagebox.showinfo('Ошибка!', f'Вы неверно ввели действие! (Зашифровать или Расшифровать)')


window = Tk()
window.title("Шифр Цезаря")
window.geometry('500x200')

lbl = Label(window, text="Сдвиг")
lbl.grid(column=0, row=2)

spin = Spinbox(window, from_=0, to=100, width=5)
spin.grid(column=0, row=3)


combo2 = Combobox(window)
combo2['values'] = ("Зашифровать", "Расшифровать")
combo2.current(0)
combo2.grid(column=0, row=4)



btn = Button(window, text="Получить ответ", command=clicked)
btn.grid(column=0, row=5)
lbl = Label(window)


txt = scrolledtext.ScrolledText(window, width=40, height=1)
txt.grid(column=2, row=0)

txt2 = scrolledtext.ScrolledText(window, width=40, height=1)
txt2.grid(column=2, row=6)


window.mainloop()

