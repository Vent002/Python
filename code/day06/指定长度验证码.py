'''
@Date: 2020-03-01 16:32:04
@LastEditors: gxm
@LastEditTime: 2020-03-01 16:42:03
@FilePath: \Python workplace\code\day06\指定长度验证码.py
'''
import random
def generate_code(code_len = 4):
  all_chars = '0123456789asdfghjklpoiuytrewqzxcvbnmABCDEFGHIJKLMNOPQRSTUVWXYZ'
  last_pos = len(all_chars) - 1
  code = ''
  for _ in range(0,code_len):
    index = random.randint(0,last_pos)
    code += all_chars[index]
  return code

print(generate_code(6))