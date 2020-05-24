import os
import shutil

location = input('Specify the folder path to be sorted:')
os.chdir(location)
folders = ['Pictures', 'Videos', 'Applications', 'Compressed', 'Documents']
for folder in folders:
    try:
        os.mkdir(folder)
    except FileExistsError:
        print('Folder ' + folder + ' already exists!')
extensions = {
    'Pictures': ['.jpg', 'jpeg', '.jpe', '.jif', '.jfif', '.jfi', '.png', '.gif', '.webp', '.tiff', '.tif', '.raw',
                 '.arw', '.cr2', '.nrw', '.k25', '.bmp', '.dib', '.heif', '.heic', '.indd', '.ind', '.indt', '.jp2',
                 '.j2k', '.jpf', '.jpx', '.jpm', '.mj2'],
    'Videos': ['.webm', '.mkv', '.flv', '.vob', '.ogv', '.ogg', '.drc', '.gifv', '.mng', '.avi', '.wmv', '.yuv', '.rm',
               '.rmvb', '.asf', '.amv', '.mp4', '.m4p', '.m4v', '.mpv', '.mpe', '.mpeg', '.mp2', '.mpg', '.svi', '.3gp',
               '.3g2', '.mxf', '.roq', '.nsv', '.f4b', '.f4a', '.f4p', '.f4v', '.flv', '.mov', '.qt', '.TS', '.M2TS',
               '.MTS'],
    'Applications': ['.exe', '.apk', '.bat', '.bin', '.cgi', '.pl', '.com', '.gadget', '.jar', '.msi', '.py', '.wsf'],
    'Documents': ['.txt', '.doc', '.docx', '.pdf', '.ppt', '.pptx', '.html', '.rtf', '.odt'],
    'Compressed': ['.zip', '.z', '.rar', '.7z', '.arj', '.deb', '.pkg', '.rpm', '.tar.gz']
}

arr = os.listdir()
print(arr)
for file in arr:
    source = location + '\\' + file
    dst = location + '\\' + 'Documents'
    for ext in extensions['Documents']:
        if ext in file:
            shutil.move(source, dst)

arr = os.listdir()
print(arr)
for file in arr:
    source = location + '\\' + file
    dst = location + '\\' + 'Pictures'
    for ext in extensions['Pictures']:
        if ext in file:
            shutil.move(source, dst)

arr = os.listdir()
print(arr)
for file in arr:
    source = location + '\\' + file
    dst = location + '\\' + 'Videos'
    for ext in extensions['Videos']:
        if ext in file:
            shutil.move(source, dst)

arr = os.listdir()
print(arr)
for file in arr:
    source = location + '\\' + file
    dst = location + '\\' + 'Compressed'
    for ext in extensions['Compressed']:
        if ext in file:
            shutil.move(source, dst)

arr = os.listdir()
print(arr)
for file in arr:
    source = location + '\\' + file
    dst = location + '\\' + 'Applications'
    if '.exe' in file:
            shutil.move(source, dst)









