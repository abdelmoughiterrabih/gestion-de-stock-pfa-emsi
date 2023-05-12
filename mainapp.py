import tkinter as tk
from tkinter import scrolledtext
from tkinter import ttk
import sqlite3
from PIL import ImageTk, Image
import os

def main(master=None):
	if master is None:
		root = tk.Tk()
	else:
		root = master
	root.title("Stock Management")
	tabcontrol = ttk.Notebook(root)
	Inventory = ttk.Frame(tabcontrol)
	labelFrame = ttk.LabelFrame(Inventory,text="Inventory Management")
	labelFrame.grid(column=0,row=0,padx=8,pady=4,sticky="N")

	#*************************************************************



	tabcontrol1 = ttk.Notebook(root)
	Inventory1 = ttk.Frame(tabcontrol1)

	labelFrame1 = ttk.LabelFrame(Inventory,text="Product List",borderwidth=6)
	#labelFrame1.grid_propagate(0)

	labelFrame1.grid(row=0,column=1,padx=8,pady=4,sticky="N")

	Inventory1.pack()


	#******************************** Get DATA *******************************
	'''i=0
	def Get_data():
		global i
		global j
		i=0
		tree.delete(*tree.get_children())
		db = sqlite3.connect('test.db')
		cursor = db.execute('select * from stock')
		for row in cursor:
			tree.insert('', 'end', text="Item_"+str(i), values=(row[0],row[1],row[2],row[3], row[4], row[5]))
			i=i+1*'''

	'''def Get_data():
		global i
		global j
		i=0
		tree.delete(*tree.get_children())
		db = sqlite3.connect('test.db')
		cursor = db.execute('SELECT * FROM stock WHERE Product_Id=? or Product_Name=? or Sell_Price=? or Quantity=? or Date_in=? or Date_out=?', (PRODUCT_ID_VALUE.get(),PRODUCT_NAME_VALUE.get(),PRODUCT_PRICE_VALUE.get(),PRODUCT_QUANTITY_VALUE.get(), PRODUCT_DATEIN_VALUE.get(),PRODUCT_DATEOUT_VALUE.get()))
		cursor = db.execute('SELECT * FROM stock WHERE Product_Id=? or Product_Name=? or Sell_Price=? or Quantity=? or Date_in=? or Date_out=?', (PRODUCT_ID_VALUE.get(),PRODUCT_NAME_VALUE.get(),PRODUCT_PRICE_VALUE.get(),PRODUCT_QUANTITY_VALUE.get(), PRODUCT_DATEIN_VALUE.get(),PRODUCT_DATEOUT_VALUE.get()))
		for row in cursor:
			tree.insert('', 'end', text="Item_"+str(i), values=(row[0],row[1],row[2],row[3], row[4], row[5]))
			i=i+1'''
	def Get_data():
		global i
		i = 0
		tree.delete(*tree.get_children())
		db = sqlite3.connect('test.db')
		cursor = db.execute('SELECT * FROM stock WHERE Product_Id=? or Product_Name=? or Sell_Price=? or Quantity=? or Date_in=? or Date_out=?',
							(PRODUCT_ID_VALUE.get(),PRODUCT_NAME_VALUE.get(),PRODUCT_PRICE_VALUE.get(),PRODUCT_QUANTITY_VALUE.get(), PRODUCT_DATEIN_VALUE.get(),PRODUCT_DATEOUT_VALUE.get()))
		for row in cursor:
			tree.insert('', 'end', text="Item_"+str(i), values=(row[0],row[1],row[2],row[3], row[4], row[5]))
			i += 1


	def Insert_data():
		db = sqlite3.connect('test.db')
		db.execute('insert into stock (Product_Id,Product_Name,Sell_Price,Quantity,Date_in,Date_out) values (?,?,?,?,?,?)',[PRODUCT_ID_VALUE.get(),PRODUCT_NAME_VALUE.get(),PRODUCT_PRICE_VALUE.get(),PRODUCT_QUANTITY_VALUE.get(), PRODUCT_DATEIN_VALUE.get(),PRODUCT_DATEOUT_VALUE.get()])
		db.commit()

	def Update_data():
		db = sqlite3.connect('test.db')
		db.execute('update stock set Product_Id = ? ,Product_Name = ?,Sell_Price = ?,Quantity = ?,Date_in = ?, Date_out = ?  where Product_Id = ?',(PRODUCT_ID_VALUE.get(),PRODUCT_NAME_VALUE.get(),PRODUCT_PRICE_VALUE.get(),PRODUCT_QUANTITY_VALUE.get(), PRODUCT_DATEIN_VALUE.get(),PRODUCT_DATEOUT_VALUE.get()))
		db.commit()

	def Delete_data():
		db = sqlite3.connect('test.db')
		db.execute('delete from stock where Product_Id = ?',(PRODUCT_ID_VALUE.get(),))
		db.commit()


	#************************************ TREE VIEW *******************************************

	tree = ttk.Treeview(labelFrame1, columns=('Product Id', 'Product Name','Sell Price','Quantity', 'Entry date', 'Out date'),height=25)
	tree.place(x=30, y=90)

	tree.heading('#0', text='Item no.')
	tree.heading('#1', text='Product id')
	tree.heading('#2', text='Name')
	tree.heading('#3', text='Sell Price')
	tree.heading('#4', text='Quantity')
	tree.heading('#5', text='Entry date')
	tree.heading('#6', text='OUT date')
	tree.column('#1', stretch=tk.YES)
	tree.column('#2', stretch=tk.YES)
	tree.column('#0', stretch=tk.YES)
	tree.column('#3', stretch=tk.YES)
	tree.column('#4', stretch=tk.YES)
	tree.column('#5', stretch=tk.YES)
	tree.column('#6', stretch=tk.YES)
	tree.grid(row=11, columnspan=6, sticky='nsew')
	tabcontrol1.pack(expand=0,fill="both")



	#*********************************************************8
	global PRODUCT_QUANTITY_VALUE
	global PRODUCT_ID_VALUE
	global PRODUCT_PRICE_VALUE
	global PRODUCT_NAME_VALUE
	global PRODUCT_DATEIN_VALUE
	global PRODUCT_DATEOUT_VALUE

	PRODUCT_ID_VALUE = tk.StringVar()
	PRODUCT_NAME_VALUE = tk.StringVar()
	PRODUCT_PRICE_VALUE = tk.StringVar()
	PRODUCT_QUANTITY_VALUE = tk.StringVar()
	PRODUCT_DATEIN_VALUE = tk.StringVar()
	PRODUCT_DATEOUT_VALUE = tk.StringVar()

	productId = ttk.Label(labelFrame,text="Product ID: ")
	productId.config(font=("courier", 15)) 
	productIdEntry = ttk.Entry(labelFrame,textvariable=PRODUCT_ID_VALUE)
	productIdEntry.grid(column=0,row=1,sticky='W')
	productIdEntry.config(font=("courier", 20))

	productName = ttk.Label(labelFrame,text="Product Name : ")
	productName.config(font=("Courier",15))
	productNameEntry = ttk.Entry(labelFrame,textvariable=PRODUCT_NAME_VALUE)
	productNameEntry.config(font=("Courier",20))

	productPrice = ttk.Label(labelFrame,text="Sell Price : ")
	productPrice.config(font=("Courier",15))
	productPriceEntry = ttk.Entry(labelFrame,textvariable=PRODUCT_PRICE_VALUE)
	productPriceEntry.config(font=("Courier",20))
	productPriceEntry.grid(column=0,row=5,sticky='W')

	productQuantity = ttk.Label(labelFrame,text="Quantity : ")
	productQuantity.config(font=("Courier",15))
	productQuantityEntry = ttk.Entry(labelFrame,textvariable=PRODUCT_QUANTITY_VALUE)
	productQuantityEntry.config(font=("Courier",20))
	productQuantityEntry.grid(column=0,row=7,sticky="W")
	
	productdatein = ttk.Label(labelFrame,text="Entry date : ")
	productdatein.config(font=("Courier",15))
	productdateinEntry = ttk.Entry(labelFrame,textvariable=PRODUCT_DATEIN_VALUE)
	productdateinEntry.config(font=("Courier",20))
	productdateinEntry.grid(column=0,row=7,sticky="W")

	productdateout = ttk.Label(labelFrame,text="Out date : ")
	productdateout.config(font=("Courier",15))
	productdateoutEntry = ttk.Entry(labelFrame,textvariable=PRODUCT_DATEOUT_VALUE)
	productdateoutEntry.config(font=("Courier",20))
	productdateoutEntry.grid(column=0,row=7,sticky="W")

	InsertButton = ttk.Button(labelFrame,text='Add',command=Insert_data)
	ShowButton = ttk.Button(labelFrame,text='Show',command=Get_data)



	style = ttk.Style()
	style.configure('TButton', background='#3498db')


	UpdateButton = ttk.Button(labelFrame,text='Update',command=Update_data,width=20)
	DeleteButton = ttk.Button(labelFrame,text='Delete',command=Delete_data,width=20)
	DeleteButton.grid(column=0,row=15,sticky='W',pady=7)
	UpdateButton.grid(column=0,row=14,sticky='W')
	ShowButton.grid(column=0,row=12,sticky='E')
	InsertButton.grid(column=0,row=12,sticky='W',pady=7)
	productdateout.grid(column=0,row=10,sticky="W")
	productdateoutEntry.grid(column=0,row=11,sticky="W")
	productdatein.grid(column=0,row=8,sticky="W")
	productdateinEntry.grid(column=0,row=9,sticky="W")
	productQuantity.grid(column=0,row=6,sticky="W")
	productPrice.grid(column=0,row=4,sticky='W')
	productNameEntry.grid(column=0,row=3,sticky='W')
	productName.grid(column=0,row=2,sticky='W')
	productId.grid(column=0,row=0,sticky='W')
	tabcontrol.add(Inventory,text='Inventory')
	tabcontrol.pack(expand=1,fill="both")


	root.mainloop()
