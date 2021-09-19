import os
import shutil
import time

def main():

	no_of_folders_deleted = 0
	no_of_files_deleted = 0

	path = "/PATH_TO_DELETE"

	days = 30

	seconds = time.time() - (days * 24 * 60 * 60)

	if os.path.exists(path):

		for base_folder, folders, files in os.walk(path):

			if seconds >= get_file_or_folder_age(base_folder):

				remove_the_folder(base_folder)
				no_of_folders_deleted += 1 

				break

			else:

				for folder in folders:

					folder_path = os.path.join(base_folder, folder)

					if seconds >= get_file_or_folder_age(folder_path):

						remove_the_folder(folder_path)
						no_of_folders_deleted += 1 

				for file in files:

					file_path = os.path.join(base_folder, file)

					if seconds >= get_file_or_folder_age(file_path):

						remove_file(file_path)
						no_of_files_deleted += 1 

		else:

			if seconds >= get_file_or_folder_age(path):

				remove_file(path)
				no_of_files_deleted += 1

	else:

		print(f'"{path}" is not found')
		no_of_files_deleted += 1

	print(f"Total folders deleted: {no_of_folders_deleted}")
	print(f"Total files deleted: {no_of_files_deleted}")


def remove_the_folder(path):

	if not shutil.rmtree(path):

		print(f"{path} is removed successfully")

	else:

		print(f"Unable to delete the "+path)



def remove_file(path):

	if not os.remove(path):

		print(f"{path} is removed successfully")

	else:

		print("Unable to delete the "+path)


def get_file_or_folder_age(path):

	ctime = os.stat(path).st_ctime

	return ctime


if __name__ == '__main__':
	main()
