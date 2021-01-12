import os
import matplotlib.pyplot as plt
import matplotlib.image as img
from matplotlib import animation
fig = plt.figure(figsize=(5,5))


def animate(i):
    img1 = os.path.join(os.getcwd(), 'draw_image', '{}.png'.format(i))
    im1 = img.imread(img1)
    ax1 = plt.axes([0.5,0.5,0.25, 0.25])
    a = ax1.imshow(im1)
    ax1.set_xticks([])
    ax1.set_yticks([])
    ax1.set_ylabel('lalalallaa')
    
    ax2 = plt.axes([0,0,0.25, 0.25])
    b = ax2.imshow(im1)
    
    imgs = []
    imgs.append(a)
    imgs.append(b)
    # return dynamic items
    return imgs

anim = animation.FuncAnimation(fig, animate, frames=20, interval=500, blit=True)
anim.save('draw_image.mp4', writer = 'ffmpeg', fps = 30) 
plt.show()