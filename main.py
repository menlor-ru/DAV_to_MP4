import os
import subprocess
from time import sleep

try:
    os.makedirs('mp4')
    print('New directory created <mp4>')
except FileExistsError:
    pass


def dav_to_mp4():
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    for file in files:
        ext = file.split(".")[-1]
        if ext.lower() == "dav":
            mp4_name = file.replace(ext, "mp4")
            print(f"Converting to mp4: {file}", end=' >>> ')

            command = f"ffmpeg -y -i {file} -c copy ./mp4/{mp4_name} -preset ultrafast"

            output = subprocess.Popen(command, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
            while output.poll() is None:
                sleep(0.5)

            if output.poll() == 0:
                print('Done.')
            else:
                print('Error!')


if __name__ == '__main__':
    dav_to_mp4()
