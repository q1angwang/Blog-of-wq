import sys

def getRrgv():
    """
     通过sys模块获取命令行参数
    """

    if(sys.argv[1]):
        print(sys.argv[1])
        getFirst = sys.argv[1]
        if(getFirst == "1"):
            print('Branch 1')
        elif(getFirst == "2"):
            print('Branch 2')
        else:
            print('no match')

    return getFirst


    # print('参数个数为:', len(sys.argv), '个参数。')
    # print('参数列表:', str(sys.argv))
    # print('脚本名为：', sys.argv[0])
    # for i in range(1, len(sys.argv)):
    #     print('参数 %s 为：%s' % (i, sys.argv[i]))


if __name__ == '__main__':
    getRrgv()