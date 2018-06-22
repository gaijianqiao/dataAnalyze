import numpy as np

lArray = np.arange(1,11)
# print(lArray)
bArray = lArray.reshape(2,5)
# print(bArray)
# print(lArray is bArray)
# 转置
btArray = bArray.T
# print(bArray)
# print(btArray)


mAArray = np.arange(10).reshape(2,5)
# print(mAArray)
mBArray = np.arange(10).reshape(5,2)
# print(mBArray)
# mCArray = mBArray * mAArray
# print(mCArray)
baseArray = np.arange(10)
rArray = baseArray.resize(2,10)
print(baseArray)
