import hashlib
import tkinter as tk
from tkinter import messagebox

def get_md5_hash(input_str, upper_case=False):
    hash_obj = hashlib.md5(input_str.encode())
    hash_str = hash_obj.hexdigest()
    return hash_str.upper() if upper_case else hash_str

def generate_key(email):
    """
    生成原理如下
    """
    num_array1 = [1, 2, 5, 7, 9, 11, 12, 13, 15, 16, 17, 19, 21, 22, 24, 25, 26, 29, 30, 31]
    num_array2 = [22, 23, 28, 32, 13, 33, 24, 30, 21, 29, 34, 17, 20, 27, 10, 4, 26, 11, 14, 8]
    calculated_hash_upper = get_md5_hash(email + ":fazilkapunjabcivillinestuneblade", upper_case=True)
    generated_key = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
    for index in range(len(num_array2)):
        num2 = num_array2[index]
        num1 = num_array1[index]
        generated_key = generated_key[:num2] + calculated_hash_upper[num1] + generated_key[num2 + 1:]
    
    return generated_key

def on_generate_button_click():
    email = email_entry.get()
    if email:
        generated_key = generate_key(email)
        output_var.set(generated_key)
    else:
        messagebox.showerror("错误", "请输入有效的邮箱地址！")
root = tk.Tk()
root.title("TuneBlade密钥生成器|By AkiACG.Akizuki")
tk.Label(root, text="请输入邮箱：").grid(row=0, column=0, padx=10, pady=10)
email_entry = tk.Entry(root, width=40)
email_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="输出：").grid(row=1, column=0, padx=10, pady=10)
output_var = tk.StringVar()
output_entry = tk.Entry(root, width=40, textvariable=output_var, state="readonly")
output_entry.grid(row=1, column=1, padx=10, pady=10)

generate_button = tk.Button(root, text="生成！", command=on_generate_button_click)
generate_button.grid(row=2, column=0, columnspan=2, pady=20)

# 启动！
root.mainloop()
