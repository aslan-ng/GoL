import matplotlib.pyplot as plt


def show(matrix, name=''):
    # Define colormap
    from matplotlib.colors import ListedColormap
    cmapmine = ListedColormap(['w','k'], N=2)

    fig, ax = plt.subplots(1, 1)
    ax.imshow(matrix, cmap=cmapmine, vmin=0, vmax=1)
    ax.set_yticklabels([])
    ax.set_xticklabels([])
    ax.set_title(name)
    plt.show()


'''def animate(states):
    from matplotlib.animation import FuncAnimation 
    fig = plt.figure() 
    #axis = plt.axes(xlim =(0, 4), ylim =(-2, 2))
    axis = plt.axes()

    anim = FuncAnimation(fig, animate, init_func = init, frames = 200, interval = 20, blit = True)
  
   
    anim.save('continuousSineWave.mp4', writer = 'ffmpeg', fps = 30))'''


if __name__ == "__main__":
    import seeds
    #seed = seeds.library['blinker']
    seed = seeds.random(8,8)
    #print(seed)
    show(seed)