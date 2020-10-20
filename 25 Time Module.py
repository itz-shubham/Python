import time
#
# initial = time.time()
#
# k = 0
# while k < 10:
#     print("Hello World")
#     k += 1
#
# print("While loop ran in", time.time() - initial, "seconds")
#
# initial2 = time.time()
#
# for i in range(10):
#     print("Hello World")
#
# print("For loop ran in", time.time() - initial2, "seconds")
#

localtime = time.asctime(time.localtime(time.time()))
print(localtime)

print(time.localtime(time.time()))

count = 1

while count <= 10:
    print(count)
    count += 1
    time.sleep(1)
