import numpy as np
import matplotlib.pyplot as plt

def main():
    # Domain
    x = np.linspace(-10, 10, 800)

    # Functions
    y_sq = x**2
    y_sin = np.sin(x)
    y_cos = np.cos(x)
    y_exp = np.exp(x)

    fig, ax = plt.subplots(2, 1, figsize=(9, 8), sharex=True)

    # First subplot
    ax[0].plot(x, y_sq, label='x^2')
    ax[0].plot(x, y_sin, label='sin(x)')
    ax[0].plot(x, y_cos, label='cos(x)')
    ax[0].set_title('Basic Functions')
    ax[0].legend()
    ax[0].grid(True)

    # Second subplot
    ax[1].plot(x, y_exp, label='exp(x)', color='red')
    ax[1].set_title('Exponential Function')
    ax[1].legend()
    ax[1].grid(True)

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()