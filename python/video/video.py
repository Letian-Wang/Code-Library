# install ffmpeg: https://medium.com/@suryadayn/error-requested-moviewriter-ffmpeg-not-available-easy-fix-9d1890a487d3
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np
ims = []
fig = plt.figure()
for i in range(1,10):
    im = plt.plot(np.linspace(0, i,10), np.linspace(0, np.random.randint(i),10))
    # 绘制散点图时，比较特殊需要调用findobj：im = plt.scatter(1,1).findobj()
    ims.append(im)
ani = animation.ArtistAnimation(fig, ims, interval=500, repeat_delay=1000)
# ani.save("test.gif", writer='pillow')

Writer = animation.writers['ffmpeg']  # 需安装ffmpeg
writer = Writer(fps=15, metadata=dict(artist='Me'), bitrate=1800)
plt.show()
ani.save("movie.mp4",writer=writer)