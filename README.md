# 3121004802
| 这个作业属于哪个课程 | [软件工程](https://edu.cnblogs.com/campus/gdgy/CSGrade21-12) |
| ----------------- | --------------- |
| 这个作业要求在哪里 | <center>[个人项目](https://edu.cnblogs.com/campus/gdgy/CSGrade21-12/homework/13014)</center> |
| 这个作业的目标 | 个人项目，实现论文查重功能 |
<font size=3>文件SE_PersonalProject包含：主程序main.py，单元测试unittest.py，依赖requirements.txt，答案文件output.txt，样例examples，单元测试用例unittest_samples。</font>

# <font color=#484891>项目需求</font>
题目：论文查重

描述如下：

设计一个论文查重算法，给出一个原文文件和一个在这份原文上经过了增删改的抄袭版论文的文件，在答案文件中输出其重复率。

- 原文示例：今天是星期天，天气晴，今天晚上我要去看电影。
- 抄袭版示例：今天是周天，天气晴朗，我晚上要去看电影。

要求输入输出采用文件输入输出，规范如下：

- 从命令行参数给出：论文原文的文件的绝对路径。
- 从命令行参数给出：抄袭版论文的文件的绝对路径。
- 从命令行参数给出：输出的答案文件的绝对路径。

我们提供一份样例，课堂上下发，上传到班级群，使用方法是：orig.txt是原文，其他orig_add.txt等均为抄袭版论文。

- 注意：答案文件中输出的答案为浮点型，精确到小数点后两位。

# <font color=#484891>PSP</font>
| PSP2.1 | Personal Software Process Stages | 预估耗时（分钟） | 实际耗时（分钟） |
| ----------------- | --------------- | --------------- | --------------- |
| Planning | 计划 | 25 | 25 |
| Estimate | 估计这个任务需要多少时间 | 10 | 10 |
| Development | 开发 | 120 | 100 |
| Analysis | 需求分析 (包括学习新技术) | 60 | 80 |
| Design Spec | 生成设计文档 | 20 | 20 |
| Design Review | 设计复审 | 20 | 20 |
| Coding Standard | 代码规范 (为目前的开发制定合适的规范) | 10 | 10 |
| Design | 具体设计 | 30 | 30 |
| Coding | 具体编码 | 90 | 80 |
| Code Review | 代码复审 | 30 | 40 |
| Test | 测试（自我测试，修改代码，提交修改） | 90 | 70 |
| Reporting | 报告 | 120 | 100 |
| Test Repor | 测试报告 | 60 | 60 |
| Size Measurement | 计算工作量 | 20 | 20 |
| Postmortem & Process Improvement Plan | 事后总结, 并提出过程改进计划 | 10 | 15 |
| overall | 合计 | 715 | 680 |

# <font color=#484891>开发环境</font>
## <font color=#6495ED>计算机配置</font>
<table border="1" width="500px" cellspacing="10">
<tr>
  <td>CPU</td>
  <td>AMD Ryzen 7 6800H</td>
</tr>
<tr>
  <td>内存大小</td>
  <td>16GB</td>
</tr>
<tr>
  <td>操作系统</td>
  <td>Windows 11, version 22H2</td>
</tr>
</table>

## <font color=#6495ED>编程语言与IDE</font>
<table border="1" width="500px" cellspacing="10">
<tr>
  <td>编程语言</td>
  <td>Python</td>
</tr>
<tr>
  <td>IDE</td>
  <td>PyCharm Community Edition 2022.2.2</td>
</tr>
</table>

## <font color=#6495ED>依赖库</font>
<font size=3>python == 3.9.13</font>
<font size=3>jieba == 0.42.1</font>
<font size=3>thefuzz == 0.20.0</font>

# <font color=#484891>模块接口的设计与实现</font>
## <font color=#6495ED>接口设计</font>
| 函数 | 功能 |
| ----------------- | --------------- |
| ReadTextAndSplit(textPath) | 参数为文本地址textPath，读取文本并对该中文文本进行分词，返回分词结果 |
| GetSimularityRatio(text1, text2) | 参数为两个分词后的中文文本，采用基于文本分配的方法，分别用difflib库和thefuzz库计算这两个文本的相似度，返回这两种相似度 |
| WriteToFile(resultPath, output) | 参数为要写入的文件路径resultPath和要写入的内容output，将output写入指定文件中，没有返回值 |
## <font color=#6495ED>具体实现</font>
&emsp;&emsp;程序按照传递命令行参数的方式提供文件的位置，具体为：python main.py [原文文件] [抄袭版论文的文件] [答案文件]。具体实现中采用sys库中的sys.argv[]传递命令行参数。
&emsp;&emsp;函数ReadTextAndSplit(textPath)中，采用中文分词库jieba实现文本的分词，并且设置停用词，如标点符号、空格、换行符等，从而提高分词结果的准确度与信息密度，使之后的文本相似度计算更为精确有效。
&emsp;&emsp;函数GetSimularityRatio(text1, text2)中，采用difflib库和thefuzz库计算两个文本的相似度，这两个库都是基于文本匹配的方法进行相似度计算。其中difflib库通过比较两个字符串之间相同字符的个数得出相似度；thefuzz库则采用Edit Distance算法，即通过比较两个字符串之间由一个转成另一个所需的最少编辑操作次数得出相似度，编辑操作一般指插入一个字符、删除一个字符或将一个字符替换成另一个字符，一般来说，编辑距离越小，两个串的相似度越高。
&emsp;&emsp;程序最终通过函数WriteToFile(resultPath, output)将两种相似度写入用户指定的答案文件中，同时还会写入原文和抄袭版论文的分词结果。

# <font color=#484891>样例运行结果</font>
&emsp;&emsp;终端运行截图如下：
<img width="900" alt="运行结果" src="https://github.com/yulinnn/3121004802/assets/88888883/3bc7266a-4e38-4656-b209-542b503275ae">
<br />&emsp;&emsp;可以看到，jieba库分词耗时0.367s，程序运行总耗时0.5s，说明处理速度较快。
<br />&emsp;&emsp;答案文件output.txt写入的部分截图如下：
<img width="900" alt="写入截图" src="https://github.com/yulinnn/3121004802/assets/88888883/eda377e1-e7da-4a77-95c3-1ed475298968">

# <font color=#484891>性能分析</font>
&emsp;&emsp;使用Python自带的性能分析模块cProfile进行性能分析。在终端中输入对应命令，并以cumtime（指定的函数及其所有子函数从调用到退出消耗的累积时间）降序排序，部分截图如下：
<img width="900" alt="cProfile性能分析（cumtime）" src="https://github.com/yulinnn/3121004802/assets/88888883/94e6ac01-2aa3-423d-91bd-7568464ec74c">
<br />&emsp;&emsp;可以看到，脚本执行耗时0.83s，并且可以看到大部分的耗时都被中文分词库jieba的执行时间占据，其中函数_call_aside耗时最多，可以说明程序本身的编码较为合理，大部分耗时都由第三方库的运行占据，程序的运行效率较高。

# <font color=#484891>单元测试和覆盖率分析</font>
## <font color=#6495ED>单元测试运行结果</font>
&emsp;&emsp;单元测试中，从样例的原文文本中抽取了十个测试用例，这些测试用例包含两种形式：
- 1、原文和待查重文本为几乎相同的字段，只有四五处对字段原意改变不大的改动或增删
- 2、原文和待查重文本分别取自完全不同的字段

&emsp;&emsp;本单元测试针对函数ReadTextAndSplit(textPath)和函数GetSimularityRatio(text1, text2)进行测试，主要检测：文件是否可以正常读取、中文分词是否准确、相似度计算是否符合测试用例实际情况。
&emsp;&emsp;单元测试程序unittest.py的运行结果部分截图如下：
<img width="900" alt="单元测试" src="https://github.com/yulinnn/3121004802/assets/88888883/b3366235-7620-4fa2-9604-c66eb163e408">
<img width="900" alt="单元测试_" src="https://github.com/yulinnn/3121004802/assets/88888883/dc2aa732-5ea2-4c65-a142-b9a6eed691ca">
<br />&emsp;&emsp;可以看到，这些测试用例都被较好地进行了分词，并且相似度的计算结果基本符合实际情况。
## <font color=#6495ED>覆盖率分析</font>
&emsp;&emsp;使用Coverage库进行代码覆盖率分析，结果如下：
<img width="900" alt="覆盖率" src="https://github.com/yulinnn/3121004802/assets/88888883/90c2ca4d-b725-410e-a706-fb8d691cbab6">
<br />&emsp;&emsp;可以看到，单元测试代码unittest.py完全覆盖。而在main.py中，由于本单元测试只针对函数ReadTextAndSplit(textPath)和函数GetSimularityRatio(text1, text2)，故只有这些部分的代码得以覆盖；其中未覆盖到的18-19行用于检查文件路径是否有效，由于在单元测试中所有文件都正常地被读取，故这部分的代码未被覆盖；而40-41行、46-60行则为与单元测试无关的代码。

# <font color=#484891>异常处理</font>
&emsp;&emsp;项目开发过程中暂未遇到异常。
