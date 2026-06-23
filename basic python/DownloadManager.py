import time


class DownloadManager:
    def __init__(self):
        self.downloads = []

    def add_download(self, filename):
        for i in range(0, 110, 10):
            time.sleep(1)
            print(f"\n{i}%")
        self.downloads.append(filename)
        with open("downloads.txt", "a", encoding="utf-8") as file:
            for idx, item in enumerate(self.downloads):
                print(f"{idx + 1}. {item}", file=file)

    def show_downloads(self):
        print("Downloaded Files")

    def save(self):
        pass

    def load(self):
        pass

    def load_downloads(self):
        with open("downloads.txt", "r", encoding="utf-8") as file:
            print(file.readlines())


options = ["Download File", "Show Downloads", "Exit"]
for index, value in enumerate(options):
    print(f"{index + 1}. {value}")
choice = input("Enter choice:")
print(options[int(choice) - 1])

download_manager = DownloadManager()

if int(choice) == 1:
    filename = input("Enter filename:")
    download_manager.add_download(filename)
if int(choice) == 2:
    download_manager.load_downloads()


