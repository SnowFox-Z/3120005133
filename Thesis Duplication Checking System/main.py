import os
import re
import jieba
import gensim


# 读取文件内容
def getpath(path: object) -> object:
    """
    :param path:
    :return:
    """
    symbol = ''
    fopen1 = open(path, 'r', encoding='UTF-8')  # 编码方式使用UTF-8
    flag = fopen1.readline()
    while flag:
        symbol += flag
        flag = fopen1.readline()
    fopen1.close()
    return symbol


# jieba分词处理，过滤标点
def filtration(fil):
    """
    :param fil:
    :return:
    """
    fil = jieba.lcut(fil)
    final = []
    for tags in fil:
        if re.match(u"[a-zA-Z0-9\u4e00-\u9fa5]", tags):  # 寻找标点位置，并过滤
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
    pattern = [word.doc2bow(text) for text in text]
    testpattern = word.doc2bow(textone)
    cosine = gensim.similarities.Similarity('-Similarity-index', pattern, num_features=len(word))
    coefficient = cosine[testpattern][1]
    return coefficient


# # 实现命令行输入文件路径，文件路径以空格隔开
# if __name__ == '__main__':
#     print('依次输入论文原文文件、抄袭版论文文件、输出的答案文件的绝对路径,参数之间使用空格隔开')
#     path1, path2, finalpath = map(str, input().split())
#     if not os.path.exists(path1):
#         print("论文原文文件不存在！")
#         exit()
#     if not os.path.exists(path2):
#         print("抄袭版论文文件不存在！")
#         exit()
#     str1 = getpath(path1)
#     str2 = getpath(path2)
#     text1 = filtration(str1)
#     text2 = filtration(str2)
#     similarity = cosinesimilarity(text1, text2)
#     print("两篇论文的相似度： %.4f" % similarity)  # 将相似度结果写入指定文件
#     fopen2 = open(finalpath, 'w', encoding="utf-8")  # 编码方式使用UTF-8
#     fopen2.write("两篇论文的相似度： %.4f" % similarity)
#     fopen2.close()

# 单元测试代码
if __name__ == '__main__':
    i = {"./test1/text-add1.txt",
         "./test1/text-add2.txt",
         "./test1/text-add3.txt",
         "./test1/text-add4.txt",
         "./test1/text-add5.txt"}
    path1 = './test1/text.txt'
    for x in i:
        path2 = x
        str1 = getpath(path1)
        str2 = getpath(path2)
        text1 = filtration(str1)
        text2 = filtration(str2)
        similarity = cosinesimilarity(text1, text2)
        print("论文原文text.txt与抄袭版论文", end=x)
        print("的相似度： %.4f" % similarity)
