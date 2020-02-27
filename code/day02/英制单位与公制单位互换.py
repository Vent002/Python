'''
@Date: 2020-02-27 18:54:51
@LastEditors: gxm
@LastEditTime: 2020-02-27 19:00:19
@FilePath: \Python workplace\code\day02\英制单位与公制单位互换.py
'''
value = float(input('输入长度：'))
unit = input('输入单位(in/cm/英寸/厘米：')
if unit == 'in' or unit == '英寸':
  print('%.1f 英寸 = %.1f 厘米' % (value,value * 2.54))
elif unit == 'cm' or unit == '厘米':
  print('%.1f 厘米 = %.1f 英寸 ' % (value,value / 2.54))
else:
  print('输入有误')