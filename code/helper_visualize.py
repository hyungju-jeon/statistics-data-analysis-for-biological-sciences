import functools

import ipywidgets as widgets
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# from google.colab import output
from IPython import display, get_ipython

# %%
get_ipython().run_line_magic("matplotlib", "widget")
# output.enable_custom_widget_manager()
plt.xkcd()
plt.rcParams.update({"path.effects": []})
plt.rcParams["font.family"] = "Humor Sans"
plt.rcParams["font.serif"] = ["Humor Sans"]

SMALL_SIZE = 12
MEDIUM_SIZE = 14
BIGGER_SIZE = 20

plt.rc("font", size=SMALL_SIZE)  # controls default text sizes
plt.rc("axes", titlesize=MEDIUM_SIZE)  # fontsize of the axes title
plt.rc("axes", labelsize=MEDIUM_SIZE)  # fontsize of the x and y labels
plt.rc("xtick", labelsize=SMALL_SIZE)  # fontsize of the tick labels
plt.rc("ytick", labelsize=SMALL_SIZE)  # fontsize of the tick labels
plt.rc("legend", fontsize=SMALL_SIZE)  # legend fontsize
plt.rc("figure", titlesize=BIGGER_SIZE)  # fontsize of the figure title


# %%
def visualize_simulation(func_list, xlabel, ylabel, title):
    if not isinstance(func_list, list):
        func_list = [func_list]

    X = [list() for _ in range(len(func_list))]

    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111)
    ax.set_ylim([-0.1, 1.1])
    ax.set(ylabel=ylabel, xlabel=xlabel, title=title)
    line_objs = [
        ax.plot(0, "o-", label=func_name, linewidth=2, ms=3, mfc="white")[0]
        for (func_name, _) in func_list
    ]
    L = ax.legend(loc="center right", bbox_to_anchor=(1, 0.9), ncol=1, fancybox=True, shadow=True)
    plt.show()

    def run_simulation(num_trials, X, b):
        for j, (func_name, func) in enumerate(func_list):
            for i in range(num_trials):
                X[j].append(func())
            total_trials = len(X[j])
            Y = np.cumsum(X[j]) / (np.arange(total_trials) + 1)
            line_objs[j].set_xdata(np.arange(total_trials) + 1)
            line_objs[j].set_ydata(Y)
            L.get_texts()[j].set_text(f"{func_name}: {Y[-1]:.2f}")
        ax.set_xlim([0, total_trials + 0.1])
        fig.canvas.draw()

    def reset_figure(b):
        # X = [list() for _ in range(len(func_list))]
        for j, (func_name, func) in enumerate(func_list):
            X[j].clear()
            total_trials = len(X[j])
            Y = np.cumsum(X[j]) / (np.arange(total_trials) + 1)
            line_objs[j].set_xdata(np.arange(total_trials) + 1)
            line_objs[j].set_ydata(Y)
            L.get_texts()[j].set_text(f"{func_name}")
        ax.set_xlim([0, total_trials + 0.1])
        fig.canvas.draw()

    button_one = widgets.Button(description="Run Once")
    button_one.on_click(functools.partial(run_simulation, 1, X))
    button_batch = widgets.Button(description="Run 100 times")
    button_batch.on_click(functools.partial(run_simulation, 100, X))
    button_reset = widgets.Button(description="Reset")
    button_reset.on_click(functools.partial(reset_figure))

    display.display(widgets.HBox([button_one, button_batch, button_reset]))
