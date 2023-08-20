import os
import py


# 获取当前目录下的所有txt文件名
def get_txt_files():
    txt_files = []
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith('.txt'):
                txt_files.append(os.path.join(root, file))
    return txt_files


def generate_directory(txt_files):

    for t in txt_files:
        file_name = os.path.basename(t)
        print( file_name)


import chardet

def openTxt(input):
    with open(input, 'rb') as file:
        content = file.read()
        encoding = chardet.detect(content)['encoding']
        file = open(input, 'r', encoding=encoding)
        content = file.read()
        # print(content)
        return content

if __name__ == '__main__':
    txt_files = get_txt_files()
    generate_directory(txt_files)
    # name=input()
    # openTxt(input())
    py.play_string(openTxt(input()))