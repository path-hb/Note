import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox


# 함수 정의
# 1. 상태확인
def check_save():
    content = area.get("1.0", tk.END). strip()
    if content:
        ans = messagebox.askyesnocancel("확인", "변경 내용을 저장하시겠습니까?")
        if ans is True:
            save_file()
            return True
        elif ans is False:
            return True
        else:
            return False
    return True

# 2. 메뉴 함수 정의
def new_file():
    if check_save():
        area.delete("1.0", tk.END)
        root.title("이름없는 메모장")
    
def open_file():
    if check_save():
        path = filedialog.askopenfilename()
        if path:
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()
            area.delete("1.0", tk.END)
            area.insert("1.0", content)
            root.title(f"{path} - 메모장")

def save_file():
    path = filedialog.asksaveasfilename(defaultextension=".txt")
    if path:
        content = area.get("1.0", tk.END)
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)

        root.title(f"{path} - 메모장")

# 창 만들기
root = tk.Tk()
root.title("이름없는 메모장")
root.geometry("800x600")

# 세로스크롤 장착
frame = tk.Frame(root) # 프레임 설치
frame.pack(fill=tk.BOTH, expand=True) # 프레임을 가로세로 모두 채우고, 창이 커지면 같이 커짐
scrollbar = tk.Scrollbar(frame) # 스크롤바생성
scrollbar.pack(side=tk.RIGHT, fill=tk.Y) # 창 오른쪽에 붙이고, 세로로 채움

# Text 부품 만들기
area = tk.Text(frame, font=("맑은 고딕", 12), yscrollcommand=scrollbar.set)
area.pack(fill=tk.BOTH, expand=True)
scrollbar.config(command=area.yview)

# 메뉴바 생성
menu_bar = tk.Menu(root)

# '파일'메뉴 생성
file_menu = tk.Menu(menu_bar, tearoff=0)

# 세부 메뉴 생성
file_menu.add_command(label="새로만들기", command=new_file)
file_menu.add_command(label="열기", command=open_file)
file_menu.add_command(label="저장", command=save_file)
file_menu.add_command(label="종료", command=root.quit)

# 창에 메뉴바 장착
menu_bar.add_cascade(label="파일", menu=file_menu)
root.config(menu=menu_bar)



root.mainloop()
