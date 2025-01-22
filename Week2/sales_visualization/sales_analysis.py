import pandas as pd  # For reading CSV files
import matplotlib.pyplot as plt  # For creating plots

# Load the sales data from the CSV file
data = pd.read_csv("company_sales_data.csv")  
# Plot 1: Line Plot for Total Profit
def plot_total_profit():
    months = data["month_number"]  # Get the months
    total_profit = data["total_profit"]  # Get the total profit

    # Create a line plot
    plt.figure(figsize=(8, 5))
    plt.plot(months, total_profit, marker="o", color="blue", label="Total Profit")
    plt.title("Total Profit Over Months")
    plt.xlabel("Month")
    plt.ylabel("Total Profit")
    plt.legend()
    plt.grid()
    plt.show()  # Display the plot

# Plot 2: Subplots for Bathing Soap and Facewash Sales
def plot_soap_and_facewash_sales():
    months = data["month_number"]  # Get the months
    bathing_soap = data["bathingsoap"]  # Get bathing soap sales
    facewash = data["facewash"]  # Get facewash sales

    # Create subplots
    plt.figure(figsize=(8, 6))

    # Bathing soap sales
    plt.subplot(2, 1, 1)  # First plot in a 2x1 grid
    plt.plot(months, bathing_soap, marker="o", color="green", label="Bathing Soap")
    plt.title("Bathing Soap Sales")
    plt.ylabel("Units Sold")
    plt.legend()

    # Facewash sales
    plt.subplot(2, 1, 2)  # Second plot in a 2x1 grid
    plt.plot(months, facewash, marker="o", color="purple", label="Facewash")
    plt.title("Facewash Sales")
    plt.xlabel("Month")
    plt.ylabel("Units Sold")
    plt.legend()
    plt.tight_layout()  
    plt.show()  # Display the plots

def main():
    print("1. Plot Total Profit Over Months")
    print("2. Plot Bathing Soap and Facewash Sales")
    choice = input("Enter 1 or 2 to select a plot: ")

    if choice == "1":
        plot_total_profit()
    elif choice == "2":
        plot_soap_and_facewash_sales()
    else:
        print("Invalid choice. Please enter 1 or 2.")

# Run the main function
if __name__ == "__main__":
    main()
