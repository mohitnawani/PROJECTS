from tkinter import *
import random
from tkinter import ttk 
from tkinter import messagebox
import mysql.connector
from mysql.connector import Error
from PIL import Image, ImageTk 

class Cust_Win:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x550+230+220")

        #====================variables==================
        self.var_ref = StringVar()
        x = random.randint(1000, 9999)
        self.var_ref.set(str(x))

        self.var_cust_name = StringVar()
        self.var_mother_name = StringVar()
        self.var_gender = StringVar()
        self.var_postcode = StringVar()
        self.var_mobile = StringVar()
        self.var_email = StringVar()
        self.var_nationality = StringVar()
        self.var_id_proof = StringVar()
        self.var_id_number = StringVar()
        self.var_address = StringVar()

        # Title Label
        lbl_title = Label(self.root, text="ADD CUSTOMER DETAILS", font=("times new roman", 18, "bold"), bg="black", fg="gold", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1295, height=50)

        # Logo or Secondary Image
        img2 = Image.open(r"images/images.jpeg")
        img2 = img2.resize((100, 40), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        lblimg2 = Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE)
        lblimg2.place(x=5, y=6, width=100, height=40)

        # Label Frame for Customer Details
        labelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, font=("arial", 12, "bold"), text="Customer Details", padx=2)
        labelframeleft.place(x=5, y=50, width=425, height=490)

        # Labels and Entry Fields
        lbl_cust_ref = Label(labelframeleft, text="Customer Ref", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_cust_ref.grid(row=0, column=0, sticky=W)
        entry_ref = ttk.Entry(labelframeleft, textvariable=self.var_ref, width=29, font=("arial", 13, "bold"), state="readonly")
        entry_ref.grid(row=0, column=1)

        # Customer Name
        lbl_cust_name = Label(labelframeleft, text="Customer Name", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_cust_name.grid(row=1, column=0, sticky=W)
        entry_name = ttk.Entry(labelframeleft, textvariable=self.var_cust_name, width=29, font=("arial", 13, "bold"))
        entry_name.grid(row=1, column=1)

        # Mother Name
        lbl_mother_name = Label(labelframeleft, text="Mother Name", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_mother_name.grid(row=2, column=0, sticky=W)
        entry_mother = ttk.Entry(labelframeleft, textvariable=self.var_mother_name, width=29, font=("arial", 13, "bold"))
        entry_mother.grid(row=2, column=1)

        # Gender Combobox
        label_gender = Label(labelframeleft, text="Gender", font=("arial", 12, "bold"), padx=2, pady=6)
        label_gender.grid(row=3, column=0, sticky=W)
        combo_gender = ttk.Combobox(labelframeleft, textvariable=self.var_gender, width=27, font=("arial", 12, "bold"), state="readonly")
        combo_gender["values"] = ("Male", "Female", "Other")
        combo_gender.grid(row=3, column=1)

        # Postcode
        lbl_postcode = Label(labelframeleft, text="Postcode", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_postcode.grid(row=4, column=0, sticky=W)
        entry_postcode = ttk.Entry(labelframeleft, textvariable=self.var_postcode, width=29, font=("arial", 13, "bold"))
        entry_postcode.grid(row=4, column=1)

        # Mobile Number
        lbl_mobile = Label(labelframeleft, text="Mobile Number", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_mobile.grid(row=5, column=0, sticky=W)
        entry_mobile = ttk.Entry(labelframeleft, textvariable=self.var_mobile, width=29, font=("arial", 13, "bold"))
        entry_mobile.grid(row=5, column=1)

        # Email
        lbl_email = Label(labelframeleft, text="Email Id", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_email.grid(row=6, column=0, sticky=W)
        entry_email = ttk.Entry(labelframeleft, textvariable=self.var_email, width=29, font=("arial", 13, "bold"))
        entry_email.grid(row=6, column=1)

        # Nationality
        lbl_nationality = Label(labelframeleft, text="Nationality", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_nationality.grid(row=7, column=0, sticky=W)
        combo_nationality = ttk.Combobox(labelframeleft, textvariable=self.var_nationality, font=("arial", 12, "bold"), width=27, state="readonly")
        combo_nationality["values"] = ("Indian", "American", "British")
        combo_nationality.current(0)
        combo_nationality.grid(row=7, column=1)

        # ID Proof Type Combobox
        lbl_id_proof = Label(labelframeleft, text="ID Proof Type", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_id_proof.grid(row=8, column=0, sticky=W)
        combo_id_proof = ttk.Combobox(labelframeleft, textvariable=self.var_id_proof, width=27, font=("arial", 12, "bold"), state="readonly")
        combo_id_proof["values"] = ("Passport", "Driving License", "Aadhar Card")
        combo_id_proof.grid(row=8, column=1)

        # ID Number
        lbl_id_number = Label(labelframeleft, text="ID Number", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_id_number.grid(row=9, column=0, sticky=W)
        entry_id_number = ttk.Entry(labelframeleft, textvariable=self.var_id_number, width=29, font=("arial", 13, "bold"))
        entry_id_number.grid(row=9, column=1)

        # Address
        lbl_address = Label(labelframeleft, text="Address", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_address.grid(row=10, column=0, sticky=W)
        entry_address = ttk.Entry(labelframeleft, textvariable=self.var_address, width=29, font=("arial", 13, "bold"))
        entry_address.grid(row=10, column=1)

        # Button Frame
        btn_frame = Frame(labelframeleft, bd=3, relief=RIDGE)
        btn_frame.place(x=0, y=400, width=412, height=40)

        # Add Button
        btnAdd = Button(btn_frame, text="Add", command=self.add_data, font=("arial", 11, "bold"), bg="black", fg="gold", width=10)
        btnAdd.grid(row=0, column=0, padx=1)

        # Update Button
        btnUpdate = Button(btn_frame, text="Update", font=("arial", 11, "bold"), bg="black", fg="gold", width=10)
        btnUpdate.grid(row=0, column=1, padx=1)

        # Delete Button
        btnDelete = Button(btn_frame, text="Delete", font=("arial", 11, "bold"), bg="black", fg="gold", width=10)
        btnDelete.grid(row=0, column=2, padx=1)

        # Reset Button
        btnReset = Button(btn_frame, text="Reset", command=self.reset_fields, font=("arial", 11, "bold"), bg="black", fg="gold", width=10)
        btnReset.grid(row=0, column=3, padx=1)

        # Table Frame
        Table_Frame = LabelFrame(self.root, bd=2, relief=RIDGE, font=("arial", 12, "bold"), text="View Customer Details", padx=2)
        Table_Frame.place(x=435, y=50, width=850, height=490)

        # Scroll Bar
        scroll_x = ttk.Scrollbar(Table_Frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(Table_Frame, orient=VERTICAL)

        self.Customer_table = ttk.Treeview(Table_Frame, column=("ref", "name", "mother", "gender", "postcode", "mobile", "email", "nationality", "idproof", "idnumber", "address"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.Customer_table.xview)
        scroll_y.config(command=self.Customer_table.yview)

        # Defining columns
        self.Customer_table.heading("ref", text="Customer Ref")
        self.Customer_table.heading("name", text="Customer Name")
        self.Customer_table.heading("mother", text="Mother Name")
        self.Customer_table.heading("gender", text="Gender")
        self.Customer_table.heading("postcode", text="Postcode")
        self.Customer_table.heading("mobile", text="Mobile Number")
        self.Customer_table.heading("email", text="Email Id")
        self.Customer_table.heading("nationality", text="Nationality")
        self.Customer_table.heading("idproof", text="ID Proof")
        self.Customer_table.heading("idnumber", text="ID Number")
        self.Customer_table.heading("address", text="Address")

        self.Customer_table["show"] = "headings"

        # Adjusting column width
        for column in self.Customer_table["columns"]:
            self.Customer_table.column(column, width=100)

        self.Customer_table.pack(fill=BOTH, expand=1)

    # Function to add customer data to the database
    def add_data(self):
        if (self.var_cust_name.get() == "" or self.var_mobile.get() == "" or self.var_id_number.get() == ""):
            messagebox.showerror("Error", "All Fields are required")
        else:
            try:
                # Replace with your actual MySQL connection details
                conn = mysql.connector.connect(host="localhost", user="root", password="mohit", database="management")
                cursor = conn.cursor()
                cursor.execute(
                    "INSERT INTO customers (customer_ref, customer_name, mother_name, gender, postcode, mobile, email, nationality, id_proof, id_number, address) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                    (self.var_ref.get(), self.var_cust_name.get(), self.var_mother_name.get(), self.var_gender.get(),
                     self.var_postcode.get(), self.var_mobile.get(), self.var_email.get(), self.var_nationality.get(),
                     self.var_id_proof.get(), self.var_id_number.get(), self.var_address.get())
                )
                conn.commit()
                messagebox.showinfo("Success", "Customer added successfully")
            except Error as e:
                messagebox.showerror("Error", f"Error occurred: {e}")
            finally:
                if conn.is_connected():
                    cursor.close()
                    conn.close()

    def reset_fields(self):
        self.var_cust_name.set("")
        self.var_mother_name.set("")
        self.var_gender.set("")
        self.var_postcode.set("")
        self.var_mobile.set("")
        self.var_email.set("")
        self.var_nationality.set("")
        self.var_id_proof.set("")
        self.var_id_number.set("")
        self.var_address.set("")

# Running the application
if __name__ == "__main__":
    root = Tk()
    obj = Cust_Win(root)
    root.mainloop()
