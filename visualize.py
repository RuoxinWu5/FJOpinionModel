import matplotlib.pyplot as plt


def plot_convergence(history, title="Convergence of FJ Model"):
    """
    绘制观点最大变化的收敛曲线
    """
    plt.figure(figsize=(8, 5))
    plt.plot(history, marker='o', linestyle='--', color='#2c7bb6')
    plt.xlabel("Iteration Step")
    plt.ylabel("Maximum Opinion Change")
    plt.title(title)
    plt.grid(True, alpha=0.3)
    plt.show()


def plot_opinion_distribution(z, title="Final Opinion Distribution"):
    """
    绘制最终观点分布的直方图
    """
    plt.figure(figsize=(8, 5))
    plt.hist(z, bins=10, color='#d7191c', edgecolor='black')
    plt.xlabel("Opinion Value")
    plt.ylabel("Number of Nodes")
    plt.title(title)
    plt.show()
