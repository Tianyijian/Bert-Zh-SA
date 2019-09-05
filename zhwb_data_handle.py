from html.parser import HTMLParser

import codecs
import csv
import numpy as np

positive_train_data = "./data/train_data/sample.positive.txt"
negative_train_data = "./data/train_data/sample.negative.txt"
test_data = "./data/test_data/test.txt"
test_data_with_label = './data/test_data/test.label.cn.xml'
data_list = []
label_list = []


class MyHTMLParser(HTMLParser):
    """parse html data file"""

    def handle_starttag(self, tag, attrs):
        # print("Start tag:", tag)
        # for attr in attrs:
        #     print("     attr:", attr)
        if len(attrs) > 1:
            label_list.append(int(attrs[1][1]))

    #
    # def handle_endtag(self, tag):
    #     print("End tag  :", tag)

    def handle_data(self, data):
        # print("Data     :", data.replace('\n', '')[0:50])
        content = data.replace('\n', '').replace('\r', '')
        if not content == '':
            data_list.append(content)


def data_parse():
    """HTMLParser parse the data, and shuffle data"""
    print("Loading train data...")
    parser = MyHTMLParser()
    parser.feed(codecs.open(positive_train_data, "r", "utf-8").read())
    pos_list = data_list[1:]
    data_list.clear()
    parser.feed(codecs.open(negative_train_data, "r", "utf-8").read())
    neg_list = data_list[1:]
    data_list.clear()
    # merge data and get label
    train_data = pos_list + neg_list
    label_list = [1] * len(pos_list) + [0] * len(neg_list)
    data_analysis(train_data, 'train')
    # Randomly shuffle data
    np.random.seed(10)
    shuffle_indices = np.random.permutation(np.arange(len(train_data)))
    return train_data, label_list, shuffle_indices


def data_analysis(data_list, tag):
    """data analysis"""
    total_length = sum(len(x) for x in data_list)
    max_length = max(len(x) for x in data_list)
    print("{:s}_data: sent_num: {:d}, max_word_length: {:d}, aver_word_length: {:f}".format(tag, len(data_list),
                                                                                            max_length,
                                                                                            total_length / len(
                                                                                                data_list)))
    count = 0
    for x in data_list:
        if len(x) < 256:
            count += 1
    print("word < 256's sent: {:d}".format(count))



def load_test_data_raw():
    """load test data and label, no segment"""
    print("Loading test data...")
    data_list.clear()
    label_list.clear()
    parser = MyHTMLParser()
    parser.feed(codecs.open(test_data_with_label, "r", "utf-8").read())
    test_list = data_list[1:]
    data_analysis(test_list, 'test')
    return test_list, label_list


def load_test_label():
    """load test data label"""
    label_list.clear()
    parser = MyHTMLParser()
    parser.feed(codecs.open(test_data_with_label, "r", "utf-8").read())
    return np.array(label_list)


def eval(file):
    """"calculate P,R,F1,Accuracy"""
    with open(file, "r", encoding="utf-8") as f:
        pre_label = np.array([int(line[1]) for line in csv.reader(f)])
    label = load_test_label()
    tp = len([i for i in range(len(label)) if label[i] == 1 and pre_label[i] == 1])
    fp = len([i for i in range(len(label)) if label[i] == 0 and pre_label[i] == 1])
    fn = len([i for i in range(len(label)) if label[i] == 1 and pre_label[i] == 0])
    tn = len([i for i in range(len(label)) if label[i] == 0 and pre_label[i] == 0])
    p = float(tp) / (tp + fp)
    r = float(tp) / (tp + fn)
    f1 = 2 * p * r / (p + r)
    acc = float(tp + tn) / len(label)
    print("TP:{}, FP:{}, FN:{}, TN:{}, P:{}, R:{}, F1:{}, Acc:{}".format(tp, fp, fn, tn, p, r, f1, acc))


# just test
if __name__ == '__main__':
    data_parse()
    load_test_data_raw()
