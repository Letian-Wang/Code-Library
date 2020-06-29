import matplotlib.pyplot as plt
import numpy as np
''' plt.axes 手绘子图 '''
# 1. Bacis
# ax1 = plt.axes()    # standard axes
# ax2 = plt.axes([0.65, 0.65, 0.2, 0.2])
# plt.show()

# 2. Object oriented
# fig = plt.figure()
# ax1 = fig.add_axes([0.1, 0.5, 0.8, 0.4], xticklabels=[], ylim=(-1.2, 1.2))
# ax2 = fig.add_axes([0.1, 0.1, 0.8, 0.4], xticklabels=[], ylim=(-1.2, 1.2))

# x = np.linspace(0, 10)
# ax1.plot(np.sin(x))
# ax2.plot(np.cos(x))
# plt.show()

''' plt.subplot 子图的简单网格 '''
# 1. Basic
# for i in range(1, 7):
#     ax = plt.subplot(2, 3, i)
#     ax.text(0.5, 0.5, str((2, 3, i)), fontsize=18, ha='center')
# plt.subplots_adjust(hspace=0.4, wspace=0.4)
# plt.show()

# 2. Object oriented
# fig = plt.figure()
# fig.subplots_adjust(hspace=0.4, wspace=0.4)
# for i in range(1, 7):
#     ax = fig.add_subplot(2, 3, i)
#     ax.text(0.5, 0.5, str((2, 3, i)), fontsize=18, ha='center')
# plt.show()

''' plt.subplots: 一次性整个网格，共享坐标轴 '''
# fig, ax = plt.subplots(2, 3, sharex='col', sharey='row')
# for i in range(2):
#     for j in range(3):
#         ax[i, j].text(0.5, 0.5, str((i,j)), fontsize=18, ha='center')
# plt.show()


''' plt.GridSpec: 更复杂的安排 '''
# grid = plt.GridSpec(2, 3, hspace=0.5)
# plt.subplot(grid[0, 0])
# plt.subplot(grid[0, 1:3])
# plt.subplot(grid[1, 0:2])
# plt.subplot(grid[1,2])
# plt.show()

''' example '''
# mean = [0, 0]
# cov = [[1, 1], [1, 4]]
# x, y = np.random.multivariate_normal(mean, cov, 3000).T

# plt.figure(figsize=(6, 6))
# grid = plt.GridSpec(4, 4, wspace=0.5, hspace=0.5)

# main_ax = plt.subplot(grid[0:3, 1:4])
# main_ax.plot(x, y, 'ok', markersize=3, alpha=0.2)

# y_hist = plt.subplot(grid[0:3, 0], xticklabels=[], sharey=main_ax)
# y_hist.hist(y, 60, orientation='horizontal', color='gray')
# y_hist.invert_xaxis()

# x_hist = plt.subplot(grid[3, 1:4], yticklabels=[], sharex=main_ax)
# x_hist.hist(x, 60, orientation='vertical', color='gray')
# x_hist.invert_yaxis()

# plt.show()