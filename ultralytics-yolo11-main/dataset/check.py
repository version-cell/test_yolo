# import os
# from pathlib import Path

# def check_cache():
#     cache_dir = Path('D:/REsourece/pythonProject/ultralytics-yolo11-main/dataset/labels')
#     cache_files = list(cache_dir.glob('*.cache'))
    
#     if cache_files:
#         print("发现缓存文件：")
#         for cache in cache_files:
#             print(f"- {cache.name}: {cache.stat().st_size / 1024:.2f} KB")
#             os.remove(cache)  # 删除旧缓存
#         print("已清理所有缓存文件")
#     else:
#         print("未发现缓存文件")

# if __name__ == '__main__':
#     check_cache()