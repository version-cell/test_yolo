import warnings, os
# os.environ["CUDA_VISIBLE_DEVICES"]="-1"    # 代表用cpu训练 不推荐！没意义！ 而且有些模块不能在cpu上跑
# os.environ["CUDA_VISIBLE_DEVICES"]="0"     # 代表用第一张卡进行训练  0：第一张卡 1：第二张卡
# 多卡训练参考<YOLOV11配置文件.md>下方常见错误和解决方案
warnings.filterwarnings('ignore')
from ultralytics import YOLO

# 训练参数官方详解链接：https://docs.ultralytics.com/modes/train/#resuming-interrupted-trainings:~:text=a%20training%20run.-,Train%20Settings,-The%20training%20settings

# 训练过程中loss出现nan，可以尝试关闭AMP，就是把下方amp=False的注释去掉。
# 训练时候输出的AMP Check使用的YOLO11n的权重不是代表载入了预训练权重的意思，只是用于测试AMP，正常的不需要理会。



if __name__ == '__main__':
    model = YOLO('ultralytics/cfg/models/11/yolo11.yaml')
    
    model.train(
        task='detect',
        data='dataset/data.yaml',
        cache=True,
        imgsz=640,
        epochs=100,
        batch=16,  # 由于模型较轻量，可以适当增加batch size
        workers=4,
        optimizer='SGD',
        lr0=0.01,
        lrf=0.01,
        momentum=0.937,
        project='runs/arc_detect',
        name='test',
        exist_ok=True,
        amp=True
    )