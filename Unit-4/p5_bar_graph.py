import matplotlib.pyplot as plt

companies = []
sizes = []

for i in range(5):
    company = input(f"Enter Company {i+1} Name: ")
    size = int(input(f"Enter Employee Size for {company}: "))
    companies.append(company)
    sizes.append(size)

plt.bar(companies, sizes, color='green')
plt.title("Company vs Employee Size")
plt.xlabel("Company")
plt.ylabel("Number of Employees")
plt.tight_layout()
plt.savefig("company_bar_graph.png")
plt.show()
print("Bar graph saved as company_bar_graph.png")
