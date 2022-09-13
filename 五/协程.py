import time


def func():
    print("aaa")
    time.sleep(3)  #让当前的线程处于阻塞状态，cpu是不为程序工作的
    print("bbbb")

if __name__ == "__main__":
    func()

#input()程序也是出于阻塞状态
#requests.get(url)在网络请求返回数据之前，程序也是处于阻塞状态
#一般情况下，程序处于IO操作的时候，线程都会处于阻塞状态

#协程：当程序遇见了IO操作的时候，可以选择性的切换到其他任务上
# 在微观上是一个任务一个任务的进行切换，切换条件一般就是IO操作
# 在宏观上，我们能看到的是多个任务一起在执行
# 多任务的异步操作


# 上述讲的一切，都是在单线程的条件下