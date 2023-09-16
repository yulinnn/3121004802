import jieba  # 中文分词
import difflib  # difflib计算文本相似度
from thefuzz import fuzz  # fuzz计算文本相似度
import sys
import os
import time

# 记录运行时间
start = time.time()

# 停用词
stopwords = {}.fromkeys(['，', '。', '；', '：', '！', '？', '‘', '’', '“', '”', '（', '）', '-', '\n', '、', ' '])


# 读取文本并分词
def ReadTextAndSplit(textPath):
    if not os.path.exists(textPath):  # 检查文件路径
        print("ERROR:Invalid File Path")
        return

    with open(textPath, 'r', encoding='utf-8') as file:  # 读取文本
        rawText = file.read()

    splitWords = [i for i in jieba.cut(rawText, cut_all=False) if i not in stopwords]  # 对文本进行分词，并去除停用词
    return splitWords


# 计算文本相似度
def GetSimularityRatio(text1, text2):
    # difflib计算相似度
    difflibRatio = round(difflib.SequenceMatcher(None, text1, text2).ratio(), 2)
    # fuzz计算相似度
    fuzzRatio = round(fuzz.ratio(text1, text2) * 0.01, 2)
    print(f"difflib计算相似度：{difflibRatio}\nfuzz计算相似度：{fuzzRatio}")
    return difflibRatio, fuzzRatio


# 将结果存入文件
def WriteToFile(resultPath, output):
    with open(resultPath, 'a', encoding='utf-8') as file:
        file.write(output + "\n")


if __name__ == "__main__":
    # 从命令行参数读取文本并分词
    originText = ReadTextAndSplit(sys.argv[1])  # 原文本
    testText = ReadTextAndSplit(sys.argv[2])  # 待查重文本
    # 计算文本相似度
    difflibRatio, fuzzRatio = GetSimularityRatio(originText, testText)
    # 将结果存入指定文件sys.argv[3]
    WriteToFile(sys.argv[3], f"difflib计算相似度：{difflibRatio}")
    WriteToFile(sys.argv[3], f"fuzz计算相似度：{fuzzRatio}")
    WriteToFile(sys.argv[3], f"原文本分词结果：\n{originText}")
    WriteToFile(sys.argv[3], f"待查重文本分词结果：\n{testText}")
    print(f"文本相似度与分词结果已存入：{sys.argv[3]}")

    # 显示程序运行时间
    end = time.time()
    escape = round(end - start, 2)
    print(f"程序运行时间：{escape} seconds")


