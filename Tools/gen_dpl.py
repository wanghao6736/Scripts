"""
@detail: 生成 .dpl 格式的 potplayer 播放列表
@param root: 放置专辑的根目录，本文件也放置在这个目录下
@param albums: 根目录下所有专辑所构成的列表
@param file_type: 指定所选列表项目的文件类型
@example:
	python gen_dpl.py .dff .dst
	为脚本目录下所有子目录下的 dff 和 dst 文件生成播放列表，保存至脚本目录下的 playlists 文件夹中
@author: wanghao
@date: 2022.03.21
"""
import os
import sys


root = os.getcwd()
albums = os.listdir(root)
file_type = sys.argv[1:]
playlists = os.path.join(root, "playlists")

if not os.path.exists(playlists):
	os.mkdir(playlists)
	print(f"create directory {playlists}. ")

for album in albums:
	album_path = os.path.join(root, album)
	if album == 'playlists' or os.path.isfile(album_path):
		continue
	files = os.listdir(album_path)
	files = [file for file in files if os.path.splitext(file)[1] in file_type]
	files.sort()

	dpl_name = os.path.join(root, 'playlists', album + '.dpl')
	with open(dpl_name, 'w', encoding='utf-8') as f:
		f.write("DAUMPLAYLIST\nplayname=''\nplaytime=0\ntopindex=0\nsaveplaypos=0\n")
		for i, file in enumerate(files):
			# os.path.abspath() 的参数不是绝对路径的话，其返回的路径可能不存在
			f.write(f"{i + 1}*file*{os.path.join(root, album, file)}\n")
	print(f"create playlist {dpl_name}. ")