driving = input('請問你有沒有開過車？')
if driving != '有' and driving != '沒有':
	print('請輸入有或沒有')
	raise SystemExit

age = input('請問你的年齡？')
age = int(age)
if driving == '有':
	if age >= 18:
		print('開車小心')
	else:
		print('你母湯開車唷')
elif driving == '沒有':
	if age >= 18:
		print('可以去考駕照囉')
	else:
		print('快可以考駕照囉')
else:
	print('請輸入有或沒有')
