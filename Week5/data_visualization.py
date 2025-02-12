import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Set random seed 
np.random.seed(42)

# Generate sample data
data = pd.DataFrame({
    'x': np.arange(1, 31),  # Simple range from 1 to 30
    'y': np.random.randint(10, 100, 30),  # 30 random numbers between 10 and 100
    'category': np.random.choice(['A', 'B'], 30)  # Randomly assign 'A' or 'B'
})

# ---- Line Plot ----
plt.figure(figsize=(8, 5))
plt.plot(data['x'], data['y'], marker='d', linestyle='-', color='blue', label='Line Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Line Plot')
plt.legend()
plt.grid(True)
plt.show()

# ---- Scatter Plot ----
plt.figure(figsize=(8, 5))
plt.scatter(data['x'], data['y'], color='green', label='Scatter Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Scatter Plot')
plt.legend()
plt.grid(True)
plt.show()

# ---- Histogram using seaborn ----
plt.figure(figsize=(8, 5))
sns.histplot(data['y'], bins=8, kde=True, color='orange')
plt.xlabel('Y-axis Values')
plt.ylabel('Frequency')
plt.title('Histogram')
plt.show()

# ---- Box Plot using seaborn ----
plt.figure(figsize=(6, 4))
sns.boxplot(x='category', y='y', data=data, color='purple')
plt.xlabel('Category')
plt.ylabel('Y-axis')
plt.title('Box Plot')
plt.show()
