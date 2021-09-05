import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from celluloid import Camera
import ffmpeg # will not be used directly, but is needed for .mp4 animation


def show(matrix, name=''):
    # Define colormap
    cmapmine = ListedColormap(['w','k'], N=2)

    fig, ax = plt.subplots(1, 1)
    ax.imshow(matrix, cmap=cmapmine, vmin=0, vmax=1)
    ax.set_yticklabels([])
    ax.set_xticklabels([])
    ax.set_title(name)
    plt.show()


def animate(states, name='sample'):
    cmapmine = ListedColormap(['w','k'], N=2)

    fig, ax = plt.subplots(1, 1)
    ax.set_yticklabels([])
    ax.set_xticklabels([])
    ax.set_title(name)
    camera = Camera(fig)

    for state in states:
        ax.imshow(state, cmap=cmapmine, vmin=0, vmax=1)
        camera.snap()
    
    animation = camera.animate()
    file_name = name + '.gif' 
    animation.save(file_name)
    



if __name__ == "__main__":
    import seeds
    #seed = seeds.library['blinker']
    seed = seeds.random(8,8)
    #print(seed)
    show(seed)