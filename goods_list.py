import os #載入operatin system程式

#讀取檔案
def read_file(filename):
	goods = []
	with open(filename, 'r', encoding='utf-8', errors='ignore') as f:
		for line in f:
			if '品名,價格\n' in line:
				continue
			name, price = line.strip().split(',')
			goods.append([name, price])
	return goods
#讓使用者輸入
def user_input(goods):
	while True:
		name = input('請輸入商品名稱: ')
		if name == 'q':
			break
		price = input('請輸入商品價格: ')
		goods.append([name, price])
	print(goods)
	return goods
#印出所有購買紀錄
def print_goods(goods):
	for g in goods:
		print(g[0], '的價格是', g[1])
#寫入檔案
def write_file(filename, goods):
		with open(filename, 'w', encoding='utf-8') as f:
			f.write('品名,價格\n')
			for g in goods:
				f.write(g[0] + ',' + str(g[1]) + '\n')

def main():
	filename = 'goods_list.txt'
	if os.path.isfile(filename):
		print('yeah! 找到檔案了')
		goods = read_file(filename)
	else:
		print('找不到檔案')
	
	goods = user_input(goods)
	print_goods(goods)
	write_file(filename, goods)

main()