import time
import keyboard
import random

pai = 120
print(type(pai))

# 定义按下每个按键的持续时间（单位为秒）
key_duration = 60 / pai / 4

# 定义空格连续出现时的停顿时间（单位为秒）
space_duration = 60 / pai

duration_sec = 0.1

def play_string(string1):
    time.sleep(1)
    i = 0

    pai_str = ''
    while i < len(string1) and string1[i] != ':':
        pai_str += string1[i]
        i += 1

    if pai_str:
        pai = int(pai_str)

    # 定义按下每个按键的持续时间（单位为秒）
    key_duration = 60 / pai / 4

    # 定义空格连续出现时的停顿时间（单位为秒）
    space_duration = 60 / pai

    duration_sec = 0.1
    pause_flag = False

    while i < len(string1):
        char = string1[i]

        if char.isdigit():
            duration_str = ''
            while i < len(string1) and string1[i].isdigit():
                duration_str += string1[i]
                i += 1
            duration_sec = int(key_duration) / int(duration_str) + 1
        
        elif char == ' ':
            time.sleep(key_duration)
            i += 1
            pause_flag = True

        elif char == '[':
            end_index = string1.index(']', i)
            sub_string = string1[i+1:end_index]
            for single_key in sub_string:
                keyboard.press(single_key)
            time.sleep(0.001)  # 使用更合理的时间间隔
            for single_key in sub_string:
                keyboard.release(single_key)
            i = end_index + 1
            time.sleep(key_duration if key_duration != duration_sec else duration_sec)
            pause_flag = False
        elif char == '\n':
            i += 1
        else:
            if i > 0 and char == string1[i-1]:
                time.sleep(random.uniform(0.01, 0.02))
            
            try:
                keyboard.press(char)
    
            
                time.sleep(0.001)  # 使用更合理的时间间隔
                print(key_duration if key_duration != duration_sec else duration_sec)

                keyboard.release(char)
                time.sleep(key_duration if key_duration != duration_sec else duration_sec)
                i += 1
            except:
                print('按键错误')
                i += 1
