import time
from threading import Thread as thr
def get_thread(thread_name, i):
	time.sleep(3)
	print(f'Привет, {thread_name}')
	if(i == 4):
		print(f'Got with {time.time()-start} seconds')
threads = []
for i in range(5):
	name = input(f'Введите название {i+1} потока: ')
	threads.append(thr(target=get_thread, args=(name,i,)))
start = time.time()
for t in threads:
	t.start()

names = []
for i in range(5):
	name = input(f'Введите название {i+1} потока: ')
	names.append(name)
start = time.time()
for name in names:
	time.sleep(3)
	print(f'Привет, {name}')
	if(names.index(name) == 4):
		print(f'Got with {time.time()-start} seconds')