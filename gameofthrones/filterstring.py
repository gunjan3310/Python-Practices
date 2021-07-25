import re

# file1 = "/home/gunjan/Downloads/Game of Thrones - all seasons-480p/7/Game of Thrones_7x06_1080p.HDTV.en.zip/Game of Thrones_7x06_1080p.HDTV.en.zip"
# file2 = "/home/gunjan/Downloads/Game of Thrones - all seasons-480p/7/Game of Thrones_7x07_HDTV.en.zip/Game of Thrones_7x07_HDTV.en.zip"
# file3 = "/home/gunjan/Downloads/Game of Thrones - all seasons-480p/8/Game of Thrones (2019) - S08 EP01.mkv"
# files = [file1,file2,file3]
def filterMKV(str):
    mo = re.match(r"^.*\.(mkv)$",str)
    try:
        return mo.group(0)
    except:
        print(f"This path throws error: {str}")
def main(files):
    for s in files:
        path = filterMKV(s)
        if path is not None:
            print(path)



