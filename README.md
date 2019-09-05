# 使用BERT 进行中文情感分类

## 环境

- tensorflow>=1.11.0
- numpy==1.17.1

## 数据集

使用中文微博数据进行情感二分类，正负情感各5000条，XML格式

<img src=".\img\datainfo.png" alt="datainfo"  />



## 文件说明

- run_c.py: 基于bert的run_classifier.py文件，添加ZhWbProcessor 

- zhwb_data_handle.py: 用于对数据进行处理
- run_zhwb.sh: 模型的训练脚本
- run_zhwb_pre.sh: 模型的预测脚本
- data/: 原始数据目录
- img/: 存放README中使用的图片
- 其它文件均来自于bert 源代码，并未做任何改动

