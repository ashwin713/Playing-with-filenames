import os

def rename_files():
	curr_directory = os.getcwd()
	file_list = os.listdir(curr_directory+'/prank')
	print "The original filenames : "
	print file_list

	os.chdir(curr_directory+'/prank')
	for file_name in file_list:
		os.rename(file_name,file_name.translate(None,"0123456789"))
	print "The altered filenames : "
	print os.listdir(os.getcwd())
	os.chdir(curr_directory)
	
rename_files()