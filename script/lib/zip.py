from genericpath import isdir
from os import getcwd, listdir, path as osPath, walk
from zipfile import ZipFile, ZIP_DEFLATED

def zip_file(include: list[str] = listdir(), name: str = osPath.basename(getcwd()), exclude: list[str] = []):
	if not name.endswith(".zip"): name += ".zip"
	zip_file = ZipFile(name, "x", compression=ZIP_DEFLATED, compresslevel=9)
	for i in include:
		if isdir(i):
			base_path = i.removesuffix(osPath.basename(i)) if len(include) > 1 else i
			for (path, dir, files) in walk(i):
				if not (path in exclude or osPath.basename(path) in exclude):
					for file in files:
						file_path = osPath.join(path, file)
						if not (file in exclude or file_path in exclude):
							zip_file.write(file_path,file_path.removeprefix(base_path))
		else:
			zip_file.write(i)
