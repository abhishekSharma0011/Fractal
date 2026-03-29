import matplotlib.pyplot as plt

def plot_cantor(start, end, depth, y_offset):
    if depth == 0:
        plt.plot([start, end], [y_offset, y_offset], color='black', lw=2)
        return

    segment_length = (end - start) / 3
    # Plot the current level's segments by drilling down
    plot_cantor(start, start + segment_length, depth - 1, y_offset)
    plot_cantor(end - segment_length, end, depth - 1, y_offset)

# Setup the plot
plt.figure(figsize=(10, 4))
levels = 5
for i in range(levels):
    # We plot each level higher than the last to show the progression
    plot_cantor(0, 1, i, -i)

plt.title("Cantor Set Construction (First 5 Iterations)")
plt.yticks(range(0, -levels, -1), range(levels))
plt.ylabel("Iteration")
plt.xlabel("Interval [0, 1]")
plt.show()
