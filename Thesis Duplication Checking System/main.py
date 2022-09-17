import re
import jieba
import gensim


# 读取文件内容
def getpath(path):
    """
    :param path:
    :return:
    """
    symbol = ''
    fopen1 = open(path, 'r', encoding='UTF-8')
    flag = fopen1.readline()
    while flag:
        symbol += flag
        flag = fopen1.readline()
    fopen1.close()
    return symbol


# jieba分词，过滤标点
def filterpunctuation(fil):
    """
    :param fil:
    :return:
    """
    fil = jieba.lcut(fil)
    final = []
    for tags in fil:
        if re.match(u"[a-zA-Z0-9\u4e00-\u9fa5]", tags):
            final.append(tags)
        else:
            pass
    return final


# 计算余弦相似度
def cosinesimilarity(textone, texttwo):
    """
    :param textone: 
    :param texttwo:
    :return: 
    """
    text = [textone, texttwo]
    word = gensim.corpora.Dictionary(text)
    warehouse = [word.doc2bow(text) for text in text]
    same = gensim.similarities.Similarity('-Similarity-index', warehouse, num_features=len(word))
    testwarehouse = word.doc2bow(textone)
    cosinesim = same[testwarehouse][1]
    return cosinesim


if __name__ == '__main__':
    print('依次输入论文原文文件、抄袭版论文文件、输出的答案文件的绝对路径')
    path1 = input()
    path2 = input()
    finalpath = input()
    # path1 = ".\paper.txt"  # 论文原文的文件的绝对路径
    # path2 = ".\paper-add.txt"  # 抄袭版论文的文件的绝对路径
    # finalpath = ".\save.txt"  # 输出的答案文件的绝对路径
    str1 = getpath(path1)
    str2 = getpath(path2)
    text1 = filterpunctuation(str1)
    text2 = filterpunctuation(str2)
    similarity = cosinesimilarity(text1, text2)
    print("两篇论文的相似度： %.4f" % similarity)  # 将相似度结果写入指定文件
    fopen2 = open(finalpath, 'w', encoding="utf-8")
    fopen2.write("两篇论文的相似度： %.4f" % similarity)
    fopen2.close()
