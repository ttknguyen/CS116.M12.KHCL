from typing import FrozenSet, Sized
import matplotlib.pyplot as plt
import numpy as np

def draw_plot(t, s):
    plt.plot(t, s)
    plt.plot(t, s + 1, 'r^')
    plt.plot(t, s - 1, 'go')

    plt.title('Biểu đồ sóng dạng hình sin', fontsize = 15)
    plt.xlabel('Trục thời gian (t)')
    plt.ylabel('Trục biên độ (s)')
    plt.xlim(-0.5, 2.5)
    plt.ylim(-2.5, 2.5)
    plt.text(1.55, -0.4, r'$s=\mathrm{sin}(2 \pi t)$')
    plt.text(1.58, 0.9, r'$s=\mathrm{sin}(2 \pi t) + 1$')
    plt.text(1.55, -1.2, r'$s=\mathrm{sin}(2 \pi t) - 1$')

    plt.show()

def draw_plot_2(t, s):
    plt.subplot(231)
    plt.scatter(t, s, marker=">")

    plt.subplot(232)
    plt.plot(t, s)

    plt.subplot(233)
    x = np.arange(3)
    money = [1.5e5, 2.5e6, 5.5e6]
    plt.bar(x, money)
    plt.xticks(x, ('Cty A', 'Cty C', 'Cty C'))


    plt.subplot(234)
    labels = 'Others', 'China', 'USA'
    sizes = [25, 35, 40]
    plt.pie(sizes, labels=labels, autopct='%1.0f%%',shadow=True, startangle=90)

    plt.subplot(235)
    x = [1, 2, 3, 4, 5]
    y1 = [1, 1, 2, 3, 5]
    y2 = [0, 4, 2, 6, 8]
    y3 = [1, 3, 5, 7, 9]
    y = np.vstack([y1, y2, y3])
    plt.stackplot(x, y1, y2, y3, labels=labels)

    plt.subplot(236)
    image =plt.imread('logo-uit.png')
    plt.imshow(image)
    plt.axis('off')

    plt.show()



def main():
    t = np.arange(0.0, 2.0, 0.05)
    s = np.sin(2 * np.pi * t)
    #draw_plot(t, s)
    draw_plot_2(t, s)

if __name__ == '__main__':
    main()
