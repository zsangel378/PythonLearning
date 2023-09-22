from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# 定义一个处理新文件事件的处理程序
class NewAudioFileHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory and event.src_path.endswith(".mp3"):  # 检查文件扩展名
            print(f"New audio file created: {event.src_path}")
        if not event.is_directory and event.src_path.endswith(".txt"):  # 检查文件扩展名
            print(f"New txt file created: {event.src_path}")

# 设置要监测的目录
watch_directory = "./"

# 创建一个Observer来监测目录
observer = Observer()
observer.schedule(NewAudioFileHandler(), path=watch_directory, recursive=False)

# 启动监测
observer.start()

try:
    observer.join()
except KeyboardInterrupt:
    observer.stop()

observer.join()