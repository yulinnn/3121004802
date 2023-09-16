from main import ReadTextAndSplit, GetSimularityRatio


def unittest():
    for i in range(1, 11):
        origText = ReadTextAndSplit(
            f"C:\\Users\\yullin\\PycharmProjects\\SE_PersonalProject\\unittest_samples\\test{i}_1.txt")
        testText = ReadTextAndSplit(
            f"C:\\Users\\yullin\\PycharmProjects\\SE_PersonalProject\\unittest_samples\\test{i}_2.txt")
        print(f"text1：{origText}\ntext2：{testText}")

        difflib, fuzz = GetSimularityRatio(origText, testText)


if __name__ == '__main__':
    unittest()
