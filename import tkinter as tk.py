import tkinter as tk

class BillManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Bill Management System")

        self.items = []
        self.total = 0.0

        self.create_ui()

    def create_ui(self):
        self.label_item = tk.Label(self.root, text="Item:")
        self.label_item.grid(row=0, column=0, padx=10, pady=10)

        self.entry_item = tk.Entry(self.root)
        self.entry_item.grid(row=0, column=1, padx=10, pady=10)

        self.label_quantity = tk.Label(self.root, text="Quantity:")
        self.label_quantity.grid(row=1, column=0, padx=10, pady=10)

        self.entry_quantity = tk.Entry(self.root)
        self.entry_quantity.grid(row=1, column=1, padx=10, pady=10)

        self.label_price = tk.Label(self.root, text="Price:")
        self.label_price.grid(row=2, column=0, padx=10, pady=10)

        self.entry_price = tk.Entry(self.root)
        self.entry_price.grid(row=2, column=1, padx=10, pady=10)

        self.add_button = tk.Button(self.root, text="Add Item", command=self.add_item)
        self.add_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        self.listbox = tk.Listbox(self.root)
        self.listbox.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

        self.calculate_button = tk.Button(self.root, text="Calculate Total", command=self.calculate_total)
        self.calculate_button.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

        self.label_total = tk.Label(self.root, text="Total:")
        self.label_total.grid(row=6, column=0, padx=10, pady=10)

        self.total_label = tk.Label(self.root, text="")
        self.total_label.grid(row=6, column=1, padx=10, pady=10)

    def add_item(self):
        item = self.entry_item.get()
        quantity = int(self.entry_quantity.get())
        price = float(self.entry_price.get())

        self.items.append((item, quantity, price))
        self.listbox.insert(tk.END, f"{item} x{quantity} - ${price:.2f}")

        self.entry_item.delete(0, tk.END)
        self.entry_quantity.delete(0, tk.END)
        self.entry_price.delete(0, tk.END)

    def calculate_total(self):
        self.total = sum(quantity * price for _, quantity, price in self.items)
        self.total_label.config(text=f"${self.total:.2f}")

if __name__ == "__main__":
    root = tk.Tk()
    app = BillManagementApp(root)
    root.mainloop()
