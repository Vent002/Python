'''
@Date: 2020-02-29 18:05:15
@LastEditors: gxm
@LastEditTime: 2020-02-29 18:06:56
@FilePath: \Python workplace\code\day06\跑马灯.py
'''
import os
import time
def main():
  content = '四川欢迎你'
  while True:
    os.system('cls')
    print(content)
    time.sleep(0.2)
    content = content[1:] + content[0]

if __name__ == '__main__':
  main()