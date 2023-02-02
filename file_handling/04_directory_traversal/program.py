from os import listdir, path


def traverse_dir(curr_path, files_extensions):
    for file in listdir(curr_path):
        if path.isdir(path.join(curr_path, file)):
            traverse_dir(path.join(curr_path, file), files_extensions)
        else:
            extension = file.split('.')[-1]
            if extension not in files_extensions:
                files_extensions[extension] = []
            files_extensions[extension].append(file)


files_extensions = {}
traverse_dir('.', files_extensions)

for ext, files in sorted(files_extensions.items(), key=lambda x: x[0]):
    report = open('report.txt', 'a')
    report.write(f'.{ext}\n')
    print(f'.{ext}')
    for file in sorted(files):
        report.write(f'--- {file}\n')
        print(f'--- {file}')
    report.close()