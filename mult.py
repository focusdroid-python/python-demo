import os
import multiprocessing


def cpoy_file(file_name, old_folder_name, new_folder_name):

	pass


def main():
	old_folder_name = input("file name is : ")

	try:
		new_folder_name = old_folder_name + '[copy file]'
		os.mkdir(new_folder_name)
	except:
		pass

	file_name = os.listdir(old_folder_name)

	print(file_name)

	po = multiprocessing.Pool(5)

	for file_name_temp in file_name:
		po.apply_async(cpoy_file, args=(file_name_temp, old_folder_name, new_folder_name))

	po.close()
	po.join()




if __name__ == '__main__':
	main()