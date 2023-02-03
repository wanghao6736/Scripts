"""
@name: 文件重命名脚本
@detail: 将脚本目录下的文件夹和文件按输入的正则表达式重命名
@example: 
    python rename.py "file_path" "abc" "def" ".txt"
    将指定目录下所有文件夹/文件名中的字符 "abc" 替换为 "def"，同时删除 txt 文件
    python rename.py "file_path" "wezz(\d).(\d).png" "wezz0\1.\2.png" ".txt"
    分组匹配
@author: wanghao
@date: 2023.02.03
"""
import os
import re
import sys

"""
@detail: 重命名文件夹/文件名
@param base: 文件夹/文件所在目录
@param src : 文件夹/文件名
"""
def ren_dir_file(base: str, src: str) -> None:
    dst = reg.sub(sub, src)
    src = os.path.join(base, src)
    dst = os.path.join(base, dst)

    if src != dst:
        if not os.path.exists(dst):
            os.rename(src, dst)
            print(f"rename {src} to {dst}")
        else:
            os.remove(src)
            print(f"file {dst} exists, file {src} removed.")

"""
@detail: 删除指定后缀的文件
@param src: 包含路径的文件名
@param ext: 指定的后缀名，默认为 .txt
@retval: 删除成功返回 True
"""
def remove_ext(src: str, ext='.txt') -> bool:
    if os.path.splitext(src)[1] == ext:
        os.remove(src)
        print(f"file {src} removed.")
        return True
    return False

# the root directory
root = sys.argv[1]

# argv[1] : the regex expression
reg = re.compile(sys.argv[2])

# argv[2] : new string to replace strings that match regex expression
sub = sys.argv[3]

# argv[3] : the extension name
fext = sys.argv[4] if len(sys.argv) == 4 else '.txt'

for rt, dirs, files in os.walk(root):
    for d in dirs:
        if d is None:
            continue
        ren_dir_file(rt, d)

    for f in files:
        if remove_ext(os.path.join(rt, f), fext):
            continue
        ren_dir_file(rt, f)