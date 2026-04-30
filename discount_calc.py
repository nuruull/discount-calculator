import tkinter as tk
from tkinter import messagebox


def calculate_discount():
    try:
        # ambil input dari user
        price = float(entry_price.get())
        discount = float(entry_discount.get())
        quantity = int(entry_quantity.get())

        # hitung total
        total_price = price * quantity
        discount_amount = total_price * (discount / 100)
        final_price = total_price - discount_amount

        # tampilkan hasil
        result_label.config(
            text=f"Total Before Discount: {total_price}\n"
            f"Discount Amount: {discount_amount}\n"
            f"Final Price: {final_price}"
        )

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers!")


# window utama
root = tk.Tk()
root.title("Discount Calculator")
root.geometry("400x350")

# judul
title_label = tk.Label(root, text="Discount Calculator", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

# input price
tk.Label(root, text="Product Price:").pack()
entry_price = tk.Entry(root)
entry_price.pack()

# input discount
tk.Label(root, text="Discount Percentage (%):").pack()
entry_discount = tk.Entry(root)
entry_discount.pack()

# input quantity
tk.Label(root, text="Quantity:").pack()
entry_quantity = tk.Entry(root)
entry_quantity.pack()

# tombol calculate
calculate_button = tk.Button(root, text="Calculate", command=calculate_discount)
calculate_button.pack(pady=15)

# hasil
result_label = tk.Label(root, text="", font=("Arial", 11))
result_label.pack(pady=10)

# jalankan program
root.mainloop()
