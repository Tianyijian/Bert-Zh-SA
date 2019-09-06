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
- res/: 格式化测试集输出结果
- img/: 存放README中使用的图片
- 其它文件均来自于bert 源代码，并未做任何改动

## 参数调优

- max_seq_length=256

  对数据集进行了统计，结果如下。句子长度小于256的占据96%，因此该参数设置为256

  ![data_state](C:\Users\26241\Desktop\Bert-Zh-SA\img\data_state.jpg)

- train_batch_size=16

  参照Bert out-of-memory issues，seq_length=256时，设置batch_size为16

- num_train_epochs

  根据train loss的变化情况设置了不同值

  num_train_epochs = 2 ：

  ![loss_1](C:\Users\26241\Desktop\Bert-Zh-SA\img\loss_1.png)

  num_train_epochs = 3 ：

  ![loss_2](C:\Users\26241\Desktop\Bert-Zh-SA\img\loss_2.jpg)

## 实验结果

不同的训练参数下验证集的结果（bert eval的输出）

|       训练参数       | eval_accuracy | eval_loss  |
| :------------------: | :-----------: | :--------: |
| num_train_epochs=2.0 |    0.7845     | 0.4686022  |
| num_train_epochs=3.0 |    0.8105     | 0.45026487 |

不同的训练参数下测试集的结果

|       训练参数       |   P    |   R    |   F1   | Accuracy |
| :------------------: | :----: | :----: | :----: | :------: |
| num_train_epochs=2.0 | 0.7567 | 0.8288 | 0.7911 |  0.7812  |
| num_train_epochs=3.0 | 0.7773 | 0.824  | 0.7999 |  0.794   |

