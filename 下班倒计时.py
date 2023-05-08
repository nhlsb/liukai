import time

def progress_bar(end_time):
    total_time = end_time - time.time()
    start_time = time.time()
    while time.time() < end_time:
        elapsed_time = time.time() - start_time
        progress = elapsed_time / total_time
        progress_bar_length = 50
        filled_length = int(progress_bar_length * progress)
        remaining_length = progress_bar_length - filled_length
        progress_bar = '#' * filled_length + '-' * remaining_length
        print(f'进度条: [{progress_bar}] {int(progress * 100)}%', end='\n')
        time.sleep(1)  # 每秒钟更新一次进度条

    print("\n下班啦！")

end_time_str = input("请输入下班时间（格式为HH:MM）：")
end_time_str = time.strftime("%Y-%m-%d") + " " + end_time_str
end_time = time.strptime(end_time_str, "%Y-%m-%d %H:%M")
end_time = time.mktime(end_time)

progress_bar(end_time)
