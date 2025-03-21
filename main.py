import sys
import subprocess
import shutil
import tkinter as tk
from tkinter import messagebox, filedialog


def modify_file(param_value, file_path, output_path, search_str, replace_str):
    """
    修改指定文件的指定参数，并保存为新文件
    """
    with open(file_path, 'r') as file:
        lines = file.readlines()

    for i, line in enumerate(lines):
        if search_str in line:
            lines[i] = replace_str.format(param_value)
            break

    with open(output_path, 'w') as file:
        file.writelines(lines)


def run_external_script(exe_path, config_file):
    """
    运行外部 .exe 文件，并传入配置文件
    """
    process = subprocess.Popen(exe_path, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                               text=True)
    process.communicate(input=config_file)  # 将 modified_file 传入 exe


def select_file(entry):
    filename = filedialog.askopenfilename()
    entry.delete(0, tk.END)
    entry.insert(0, filename)


def start_processing():
    try:
        start_value = float(start_entry.get())
        end_value = float(end_entry.get())
        step = float(step_entry.get())

        config_file = config_entry.get()
        modified_file = "../modified_config.txt"
        external_script = exe_entry.get()
        output_file = "datcom.out"

        search_str = search_entry.get()
        replace_str = replace_entry.get() + "\n"

        current_value = start_value
        while current_value <= end_value:
            modify_file(current_value, config_file, modified_file, search_str, replace_str)
            run_external_script(external_script, modified_file)
            renamed_file = f"{search_str}_{current_value:.2f}.out"

            if shutil.move(output_file, renamed_file):
                log_text.insert(tk.END, f"Output file renamed to {renamed_file}\n")
            else:
                log_text.insert(tk.END, "Error: Unable to rename file\n")

            current_value += step

        messagebox.showinfo("完成", "所有任务已执行完毕！")
    except Exception as e:
        messagebox.showerror("错误", str(e))


# 创建 GUI 界面
root = tk.Tk()
root.title("参数修改工具")
root.geometry("500x450")

tk.Label(root, text="起始值:").pack()
start_entry = tk.Entry(root)
start_entry.pack()

tk.Label(root, text="结束值:").pack()
end_entry = tk.Entry(root)
end_entry.pack()

tk.Label(root, text="步长:").pack()
step_entry = tk.Entry(root)
step_entry.pack()

tk.Label(root, text="搜索字符串:").pack()
search_entry = tk.Entry(root)
search_entry.pack()

tk.Label(root, text="替换字符串 (用 {} 代表数值):").pack()
replace_entry = tk.Entry(root)
replace_entry.pack()

tk.Label(root, text="选择配置文件:").pack()
config_entry = tk.Entry(root)
config_entry.pack()
tk.Button(root, text="浏览", command=lambda: select_file(config_entry)).pack()

tk.Label(root, text="选择 .exe 文件:").pack()
exe_entry = tk.Entry(root)
exe_entry.pack()
tk.Button(root, text="浏览", command=lambda: select_file(exe_entry)).pack()

tk.Button(root, text="开始执行", command=start_processing).pack()

log_text = tk.Text(root, height=10)
log_text.pack()

root.mainloop()