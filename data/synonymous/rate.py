import numpy as np
import matplotlib.pyplot as plt

words = np.array([25, 50, 100, 200, 400])

no_persona = [
    [6, 4, 4],
    [4, 3, 5],
    [8, 9, 6],
    [11, 12, 11],
    [18, 14, 14]
]

short_persona = [
    [5, 5, 5], 
    [8, 8, 10], 
    [13, 8, 12], 
    [15, 15, 15], 
    [19, 17, 21]
]

long_persona = [
    [5, 7, 7], 
    [10, 9, 10], 
    [12, 9, 11], 
    [10, 14, 17], 
    [23, 18, 21]
]

anti_rep = [
    [7, 7, 5], 
    [7, 10, 10], 
    [10, 14, 13], 
    [17, 18, 12], 
    [24, 22, 25]
]

def get_stats(data, lengths):
    means = [np.mean(d)/l for d, l in zip(data, lengths)]
    stds = [np.std(d)/l for d, l in zip(data, lengths)]
    return np.array(means), np.array(stds)

def fit_power_law(x, y):
    log_x = np.log(x)
    log_y = np.log(y)
    alpha, log_c = np.polyfit(log_x, log_y, 1)
    c = np.exp(log_c)
    return alpha, c

plt.figure()

for data, label, marker in [
    (no_persona, "No Persona", 'o'),
    (short_persona, "Short Persona", 's'),
    (long_persona, "Long Persona", '^'),
    (anti_rep, "Persona + Anti-Rep", 'D')
]:
    means, stds = get_stats(data, words)

    # main plot
    plt.errorbar(words, means, yerr=stds, marker=marker, capsize=5, label=label)

    # power-law fit
    alpha, c = fit_power_law(words, means)
    x_fit = np.linspace(words.min(), words.max(), 200)
    y_fit = c * (x_fit ** alpha)

    plt.plot(x_fit, y_fit, linestyle='--', alpha=0.7,
             label=f"{label} fit (α={alpha:.2f})")

plt.xlabel("Response word count")
plt.ylabel("Repetition rate")
plt.title("Repetition Rate vs Response Length")
plt.legend()
plt.show()