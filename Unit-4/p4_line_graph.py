import matplotlib.pyplot as plt

years = []
profits = []

for i in range(5):
    year = int(input(f"Enter Year {i+1}: "))
    profit = float(input(f"Enter Profit for {year}: "))
    years.append(year)
    profits.append(profit)

plt.plot(years, profits, marker='o', color='blue', linestyle='-')
plt.title("Profit Over 5 Years")
plt.xlabel("Year")
plt.ylabel("Profit")
plt.grid(True)
plt.tight_layout()
plt.savefig("profit_line_graph.png")
plt.show()
print("Line graph saved as profit_line_graph.png")
