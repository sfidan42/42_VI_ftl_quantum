import matplotlib.pyplot as plt

def qplot(counts):
    probabilities = [v / 500.0 for v in counts.values()]
    plt.bar(counts.keys(), probabilities)
    plt.xlabel("Measurement Outcome")
    plt.ylabel("Probabilities")
    plt.title("Qubit Probabilities")
    plt.show()
