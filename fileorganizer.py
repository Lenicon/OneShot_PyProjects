
from os import path, listdir, startfile, mkdir
import re
import shutil

def extension_filter(list, exts):
    pattern = r"\." + r"|".join(re.escape(ext) for ext in exts) + r"$"
    return [item for item in list if not re.search(pattern, item, flags=re.IGNORECASE)]

def main(filetypes):
    homedir = path.expanduser('~')

    input_dir = input(f"\nOrganize Files at {homedir}\\")
    
    dir = path.realpath(path.join(homedir, input_dir))

    if input_dir.split():
        if path.isdir(dir):
            filelist = [f for f in listdir(dir) if path.isfile(path.join(dir, f))]
            
            filtered_extensions = ['ini','xml','log1','dat','blf']
            filelist = extension_filter(filelist, filtered_extensions)

            for i in filelist:
                if path.isfile(path.join(dir, i)):
                    folder = filetypes.get(str.lower(path.splitext(i)[1]))

                    newpath = path.join(dir, folder)
                    if not path.isdir(newpath):
                        mkdir(newpath)
                    
                    shutil.move(path.join(dir, i), path.join(newpath, i))

                else:
                    main()
            
            print("\nSuccessfuly organized files at", dir)
            main()
            
        else:
            print("\nFile path unavailable, please retry.")
            main()
    else:
        print("\nI don't think I should touch this place.")
        main()


if __name__ == "__main__":
    print("File Organizer 2000 by Len.icon\n")
    filetypes = {
        ".mp4" : "Videos",
        ".mov" : "Videos",
        ".avi" : "Videos",
        ".wmv" : "Videos",
        ".webm": "Videos",
        ".mp3" : "Audio",
        ".wav" : "Audio",
        ".ogg" : "Audio",
        ".wma" : "Audio",
        ".jpg" : "Images",
        ".png" : "Images",
        ".gif" : "Images",
        ".jpeg": "Images",
        ".bmp" : "Images",
        ".pdf" : "Documents",
        ".doc" : "Documents",
        ".docx": "Documents",
        ".odt" : "Documents",
        ".txt" : "Documents",
        ".odp" : "Presentations",
        ".ppt" : "Presentations",
        ".pptx": "Presentations",
        ".ods" : "Spreadsheets",
        ".xlsx": "Spreadsheets",
        ".xls": "Spreadsheets",
        ".zip": "Compressed",
        ".rar": "Compressed",
        ".tar": "Compressed",
        ".gz" : "Compressed",
        ".7z" : "Compressed",
        ".iso": "Compressed",
        ".exe": "Executables",
        ".bin": "Executables",
        ".apk": "Executables"
    }
    main(filetypes)