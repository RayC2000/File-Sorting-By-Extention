import os
import shutil

# folders to scan
fol_to_scan = ["Downloads/", "Documents/", "Pictures/", "Videos/"]

# constant path
main_path = "C:/Users/" + os.getlogin() + "/"

# list of specified extensions
documents = [".doc", ".docx", ".pdf", ".pptx", ".ppt", ".txt", ".docm", ".odt", ".rtf", ".html", ".xlsx", ".xlsm", ".xlsb", ".xltx"]
downloads = [".exe", ".mp3", ".wav", ".iso", ".bat", ".com", ".cmd", ".inf", ".run"]
pictures = [".png", ".jpg", ".jpeg", ".bmp", ".gif", ".jfif", ".ico"]
videos = [".mp4", ".wmv", ".avi", ".mkv"]

for current in range(len(fol_to_scan)):
    fol = os.listdir(main_path + fol_to_scan[current])
    # scan
    for file in range(len(fol)):
        for ext in downloads:
            if fol[file].endswith(ext):
                shutil.move(main_path + fol_to_scan[current] + fol[file], main_path + "Downloads/" + fol[file])
        for ext in documents:
            if fol[file].endswith(ext):
                shutil.move(main_path + fol_to_scan[current] + fol[file], main_path + "Documents/" + fol[file])
        for ext in videos:
            if fol[file].endswith(ext):
                shutil.move(main_path + fol_to_scan[current] + fol[file], main_path + "Videos/" + fol[file])
        for ext in pictures:
            if fol[file].endswith(ext):
                shutil.move(main_path + fol_to_scan[current] + fol[file], main_path + "Pictures/" + fol[file])

