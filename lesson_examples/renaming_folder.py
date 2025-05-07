## Imported modules ##
import os


## Create variable ##
source_folder = r"C:\Users\chari plus\Downloads\Telegram Desktop\Familiars"


## Rename file ##
for item in os.listdir(source_folder):
	# Check if an item is file or not
	if os.path.isfile(os.path.join(source_folder, item)):
		if item.endswith(".jpg"):
			try:
				# Renaming a file
				os.rename(
					os.path.join(source_folder, item),
					os.path.join(source_folder, "Waifu" + item)
					)

			except PermissionError:
				continue

			except Exception as e:
				raise Exception(e)