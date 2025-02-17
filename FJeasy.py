"""
Friedkin-Johnsen模型的一个简单版本，用于模拟一个小型有向图中节点观点的演变过程。
主要步骤包括：
1.定义图结构（邻接矩阵）
2.生成内部观点
3.初始化表达观点
4.通过迭代更新表达观点，直到达到平衡状态或达到最大迭代次数。
"""
import numpy as np
from FJmodel import FJModel

# Step1: 手动定义小型网络邻接矩阵（有向、类型为浮点数） 0->1->2
A = np.array([
    [0, 1, 0],  # 节点0连接节点1
    [0, 0, 1],  # 节点1连接节点2
    [0, 0, 0]  # 节点2无出边
], dtype=float)

# Step2: 生成内部观点向量s
n = 3  # 节点数量
np.random.seed(42)  # 固定随机种子，便于复现
s = np.random.rand(n)  # 生成3个[0,1)的随机数
print("internal opinion s:", s)

# Step3: 初始化表达观点z
z = s.copy()  # 初始时表达观点=内部观点
print("expressed opinion z:", z)
print()

# Step4: 迭代更新表达观点
max_iter = 5  # 迭代次数
for step in range(max_iter):
    # 建立一个与初始观点一样大小的全0向量
    z_new = np.zeros_like(z)
    # 更新一轮
    for i in range(n):
        neighbors = np.where(A[i] > 0)[0]  # 节点i的邻居（即A[0]中非零的位置）
        new_z_up = z[i] + A[i, neighbors] @ z[neighbors]
        new_z_down = 1 + A[i, neighbors].sum()
        z_new[i] = new_z_up / new_z_down
    z = z_new
    print("new z", step, "=", z_new)
    # 如果有收敛条件，将迭代次数max_iter设置稍大一点
    # 在此处检查是否收敛，若收敛就break
    # print(f"在第 {step + 1} 步收敛")

print()
"""
此处尝试调用 FJModel 类及其 iterate() 方法
"""
model = FJModel(A, s)
z_history = model.iterate(max_iter)
print("z_history", z_history)
