import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("../data/co2_emissions_by_sector_sample.csv")

# Plotting
plt.figure(figsize=(10, 6))
plt.stackplot(
    df["Year"],
    df["Energy"],
    df["Transport"],
    df["Industry"],
    labels=["Energy", "Transport", "Industry"]
)
plt.title("Global CO₂ Emissions by Sector (2010–2024) – Sample Data")
plt.xlabel("Year")
plt.ylabel("CO₂ Emissions (Gt)")
plt.legend(loc="upper left")
plt.tight_layout()
plt.savefig("../images/co2_emissions_area_chart.png")
plt.show()
