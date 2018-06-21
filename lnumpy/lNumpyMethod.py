import numpy as np
tArray = np.array([['a',1,'3',4],['a','2','3',4]])
print(tArray)
print(type(tArray))
print(tArray.ndim)
print(np.random.rand(10).reshape(2,5))
# 将1000个数 做成一个10*10*10的一个三维数组中
threeArray = np.random.rand(1000).reshape(10,10,10)

# print(threeArray.ndim)
linSpaceArray = np.linspace(start=10,stop=20,num=10,endpoint=True,retstep=False)
# print(linSpaceArray)


zerosThreeArray = np.zeros_like(threeArray)
# print(zerosThreeArray)


zeroByShape = np.zeros(threeArray.shape)
oneByShape = np.ones(threeArray.shape)
# print(oneByShape)
# print(zeroByShape)
# 创建一个数组，对角线为1其他的为0
eyesArray = np.eye(5,5,dtype=np.int32)
print(eyesArray)


