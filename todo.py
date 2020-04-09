import tkinter as tk
from tkinter import Entry
from tkinter import Label
from tkinter import ttk
####################Графическая оболочка###########################


class Main_win: #основное окно
	def __init__(self):
		self.root = tk.Tk()
		self.root.title('ToDo List')
		self.root.geometry("900x600")
		self.root.resizable(False, False)
		toolbar = tk.Frame(bg = 'Grey', width = 900, height = 100)
		toolbar.place ( x =0, y = 0)

		self.make_button(toolbar)

	def make_button(self, perent):
		btn_open_add = tk.Button(perent,
								text = "Add Task",
								width = 14,
								height = 10,
								command = lambda:self.make_add(),
								bg = "Green",
								bd=3)
		
		btn_change = tk.Button(perent,
								text = "Change",
								width = 14,
								height = 10,
								command = lambda:self.make_add(),
								bg = "Green",
								bd=3)

		btn_important = tk.Button(perent,
								text = "important",
								width = 14,
								height = 10,
								command = lambda:self.make_add(),
								bg = "Green",
								bd=3)

		btn_delete = tk.Button(perent,
								text = "delete",
								width = 14,
								height = 10,
								command = lambda:self.make_add(),
								bg = "Green",
								bd=3)
		btn_make_performed = tk.Button(perent,
								text = "perfomed",
								width = 14,
								height = 10,
								command = lambda:self.make_add(),
								bg = "Green",
								bd=3)

		btn_delete_performed = tk.Button(perent,
								text = "del perfomed",
								width = 14,
								height = 10,
								command = lambda:self.delete_performed(),
								bg = "Green",
								bd=3)

		btn_enter = tk.Button(perent,
							 	text = "Enter",
							 	width = 13,
							 	height = 1,
							 	command = lambda:self.regist(),
							 	bg = "Green",
							 	bd=3)




		btn_open_add.place 			(x = 0,   y = 0)
		btn_change.place   			(x = 115, y = 0) 
		btn_delete.place			(x = 230, y = 0)	
		btn_important.place 		(x = 345, y = 0)
		btn_make_performed.place 	(x = 460, y = 0)
		btn_delete_performed.place 	(x = 575, y = 0)
		btn_enter.place             (x = 795, y = 70)

	def run(self):
		self.root.mainloop()

########Тест чтобы вызвать дочернее окно , потом назначить на кнопку##

	def make_add(self):
		Add(self.root)

	def regist(self):
		Regist(self.root)
        
	def delete_performed(self):
		DelPerf(self.root)


class Add: #дочернее окно
	def __init__(self, perent):
		self.root2 = tk.Toplevel(perent)
		self.root2.title('Add Task')
		self.root2.geometry("300x200")
		self.root2.resizable(False, False)

		problem = Entry(self.root2, width = 40)
		problem.grid(row=2, column=1)
		Label(self.root2, text = 'Задача').grid(row=1, column=0)

		Date_end = Entry(self.root2, width = 40)
		Date_end.grid(row = 5, column = 1)

		self.focuse()

	def focuse(self):
		self.root2.grab_set()
		self.root2.focus_set()
		self.root2.wait_window()

class Regist: 
	def __init__(self, perent):
		self.root3 = tk.Toplevel(perent)
		self.root3.title('Войти')
		self.root3.geometry("300x250")
		self.root3.resizable(False, False)

		Label(self.root3, text = 'Введите Ваше имя в поле ниже:').place(relx=.2, rely=.1)
        
		name = Entry(self.root3, width = 40)
		name.place(relx=.1, rely=.3)

		self.focuse()

	def focuse(self):
		self.root3.grab_set()
		self.root3.focus_set()
		self.root3.wait_window()
        
class DelPerf: 
	def __init__(self, perent):
		self.root4 = tk.Toplevel(perent)
		self.root4.title('Удалить выполненные задачи')
		self.root4.geometry("350x250")
		self.root4.resizable(False, False)

		Label(self.root4, text = 'Вы уверены?').place(relx=.4, rely=.1)
		btn_yes = tk.Button(self.root4,
							 	text = "Да",
							 	width = 3,
							 	height = 1,
							 	command = lambda:self.root4.destroy(),
							 	bg = "Green",
							 	bd=3)
		btn_yes.place(relx = .3, rely = .4)
		btn_no = tk.Button(self.root4,
							 	text = "Нет",
							 	width = 3,
							 	height = 1,
							 	command = lambda:self.root4.destroy(),
							 	bg = "Green",
							 	bd=3)
		btn_no.place(relx = .6, rely = .4)
		self.focuse()

	def focuse(self):
		self.root4.grab_set()
		self.root4.focus_set()
		self.root4.wait_window()
        



if __name__ == "__main__":
	main_win = Main_win()
	#main_win.make_add()
	main_win.run()
	

