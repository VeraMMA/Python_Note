from tkinter import *
from tkinter import messagebox 

root = Tk()
root.title('Заметки')
root.geometry('600x700')

def note_exit():
    answer = messagebox.askokcancel('Выход','Выйти из программы?')
    if answer:
        root.destroy()

main_menu = Menu(root)
    

file_menu = Menu(main_menu, tearoff=0)
file_menu.add_command(label='Открыть')
file_menu.add_command(label='Сохранить')
file_menu.add_separator()
file_menu.add_command(label='Закрыть', command=note_exit)

root.config(menu=file_menu)

main_menu.add_cascade(label='Меню', menu=file_menu)

root.config(menu=main_menu)

f_text = Frame(root)
f_text.pack(fill=BOTH, expand=1)

text_fild = Text(f_text, bg='black', fg='ivory', padx=15, pady=15, 
                 wrap=WORD, insertbackground='yellow', selectbackground='#9D928B', spacing3=10)
text_fild.pack(expand=1, fill=BOTH, side=LEFT)

root.mainloop()