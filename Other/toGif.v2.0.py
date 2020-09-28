import ffmpy
import os
import json
import math
import subprocess
import time


current_dir = os.path.dirname(__file__)
input_paths = os.path.join(current_dir, 'mp4')
output_dir = os.path.join(current_dir, 'gif')

gif_list = []
mp4_files = os.listdir(input_paths)
gif_files = os.listdir(output_dir)

for file in gif_files:
    gif_name = str(os.path.splitext(file)[0]).lower()
    gif_list.append(gif_name)

for file in mp4_files:
    file_ext = str(os.path.splitext(file)[-1]).lower()
    if file_ext != '.mp4':
        continue
    name_text = str(os.path.splitext(file)[0]).lower()
    if name_text in gif_list:
        continue
    print('开始转换MP4：%s' % file)
    file_name = os.path.join(input_paths, file)
    gif_name = name_text + '.gif'
    gif_path = os.path.join(output_dir, gif_name)
    print(file_name, gif_path)
    ff = ffmpy.FFmpeg(
    inputs={file_name: None},
    outputs={gif_path: None}
    )
    ff.run()
    time.sleep(1)
    gif_size = os.path.getsize(gif_path)
    if gif_size > 10 * 1024 * 1024:
        strCmd = 'ffprobe -v quiet -print_format json -show_format -show_streams -i %s' % file_name
        mystring = os.popen(strCmd).read()
        time.sleep(1)
        streams = json.loads(mystring)
        width = float(streams['streams'][0]['width'])
        height = float(streams['streams'][0]['height'])
        cmd = 'ffmpeg -i %s -r 15 %s -y' % (file_name, gif_path)
        subprocess.call(cmd)
        time.sleep(1)
        for i in range(9):
            gif_size = os.path.getsize(gif_path)
            if gif_size > 10 * 1024 * 1024:
                rate = math.sqrt(gif_size / ((9 - i) * 1024 * 1024))
                new_width = math.floor(width / rate)
                new_height = math.floor(height / rate)
                cmd = 'ffmpeg -i %s -r 15 -s %sx%s %s -y' % (file_name, new_width, new_height, gif_path)
                subprocess.call(cmd)
                time.sleep(1)

