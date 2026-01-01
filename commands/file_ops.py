import os
import shutil

SAFE_ROOT = "D:/AI_ASSISTANT_DATA/safe_files"

def is_safe_path(path):
    return os.path.abspath(path).startswith(os.path.abspath(SAFE_ROOT))

def open_path(path):
    if not is_safe_path(path):
        return "❌ Access denied. Unsafe path."
    os.startfile(path)
    return f"Opened {path}"

def copy_file(src, dst):
    if not (is_safe_path(src) and is_safe_path(dst)):
        return "❌ Copy blocked. Unsafe path."
    shutil.copy(src, dst)
    return "✅ File copied successfully."
