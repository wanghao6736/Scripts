import imageio.v2 as imageio
import os

def create_gif(image_list, gif_name, duration = 1.0):
    '''
    可修改变量
    :1. image_list: 这个列表用于存放生成动图的图片
    :2. gif_name: 字符串，所生成gif文件名，带.gif后缀
    :3. duration: 图像间隔时间
    :4. 在IDLE 运行的时候，将 .py 文件保存在图片存在的文件夹中
    '''
    frames = []
    for image_name in image_list:
        print(image_name)
        frames.append(imageio.imread(os.path.join(imgs_path, image_name)))

    imageio.mimsave(gif_name, frames, 'GIF', duration=duration)
    return

def main():
    gif_name = os.path.split(imgs_path)[-1] + ".gif"
    gif_name = os.path.join(imgs_path, gif_name)
    if os.path.exists(gif_name):
        os.remove(gif_name)
    
    duration = 0.15 # 在这里修改图像间隔的时间
    image_list = os.listdir(imgs_path)
    create_gif(image_list, gif_name, duration)


imgs_path = r"file_path"
main()
