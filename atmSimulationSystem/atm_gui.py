import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
from atm import ATM

class ATMGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("ATM Simulation System")
        self.root.geometry("500x400")
        self.root.configure(bg='#f0f4f7')
        self.atm = ATM.get_instance()

        self.style = ttk.Style()
        self.style.configure("TLabel", font=('Segoe UI', 12), background='#f0f4f7')
        self.style.configure("TButton", font=('Segoe UI', 11), padding=6)

        self.login_frame()

    def login_frame(self):
        self.clear_window()

        ttk.Label(self.root, text="ATM Login", font=('Segoe UI', 18, 'bold')).pack(pady=20)

        form_frame = tk.Frame(self.root, bg='#f0f4f7')
        form_frame.pack(pady=10)

        ttk.Label(form_frame, text="Account Number:").grid(row=0, column=0, sticky='e', padx=5, pady=5)
        self.acc_entry = ttk.Entry(form_frame, width=30)
        self.acc_entry.grid(row=0, column=1, pady=5)

        ttk.Label(form_frame, text="PIN:").grid(row=1, column=0, sticky='e', padx=5, pady=5)
        self.pin_entry = ttk.Entry(form_frame, width=30, show="*")
        self.pin_entry.grid(row=1, column=1, pady=5)

        ttk.Button(self.root, text="Login", command=self.authenticate).pack(pady=20)

    def authenticate(self):
        acc = self.acc_entry.get()
        pin = self.pin_entry.get()

        if self.atm.authenticate(acc, pin):
            messagebox.showinfo("Success", "Login successful!")
            self.transaction_menu()
        else:
            messagebox.showerror("Error", "Invalid credentials")

    def transaction_menu(self):
        self.clear_window()
        ttk.Label(self.root, text="Select Transaction", font=('Segoe UI', 16, 'bold')).pack(pady=20)

        menu_frame = tk.Frame(self.root, bg='#f0f4f7')
        menu_frame.pack(pady=10)

        ttk.Button(menu_frame, text="Check Balance", command=self.check_balance, width=25).grid(row=0, column=0, pady=5)
        ttk.Button(menu_frame, text="Withdraw", command=self.withdraw, width=25).grid(row=1, column=0, pady=5)
        ttk.Button(menu_frame, text="Deposit", command=self.deposit, width=25).grid(row=2, column=0, pady=5)
        ttk.Button(menu_frame, text="Logout", command=self.login_frame, width=25).grid(row=3, column=0, pady=20)

    def check_balance(self):
        balance = self.atm.perform_transaction("balance")
        messagebox.showinfo("Balance", f"Your current balance is: ${balance}")

    def withdraw(self):
        amount = simpledialog.askinteger("Withdraw", "Enter amount to withdraw:")
        if amount is not None:
            if self.atm.perform_transaction("withdraw", amount):
                messagebox.showinfo("Success", f"${amount} withdrawn successfully.")
            else:
                messagebox.showerror("Failed", "Insufficient funds.")

    def deposit(self):
        amount = simpledialog.askinteger("Deposit", "Enter amount to deposit:")
        if amount is not None:
            self.atm.perform_transaction("deposit", amount)
            messagebox.showinfo("Success", f"${amount} deposited successfully.")

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = ATMGUI(root)
    root.mainloop()
