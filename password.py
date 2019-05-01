password = 'a123456'
x = 3
y = 3
while x > 0:
	ps = input('請輸入密碼: ') 
	if ps == password:
		print('登入成功!')
		break
	else:
		y = y - 1
		print('密碼錯誤!還有' ,y ,'次機會')
	x = x - 1
if y == 0:
	print('帳戶已遭封鎖!')