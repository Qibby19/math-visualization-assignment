#TASK 1
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 200)

y1 = x
y2 = x ** 2
y3 = np.sin(x)
y4 = np.exp(-0.1 * x) * np.cos(x)

plt.plot(x, y1, label='x', linestyle = "dashed")
plt.plot(x, y2, label='x^2', marker = "o")
plt.plot(x, y3, label='sin(x)', color = "black")
plt.plot(x, y4, label='e^(-0.1x) * cos(x)', color = "red")
plt.title('Functions')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()
plt.savefig('math_functions.png')

#TASK 2

x = np.linspace(-10, 10, 200)

y = 5*x**3 + 7 * x #This is a cubic equation

plt.plot(x, y, label='x')
plt.title('Graph of y = 5x^3 + 7x')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()
plt.savefig('own_equation.png')

#TASK 3

students = ["S1", "S2", "S3", "S4", "S5", "S6", "S7", "S8", "S9", "S10"]

midterm = np.array([85, 72, 90, 66, 78, 92, 60, 74, 88, 95])
final = np.array([80, 70, 94, 68, 75, 90, 65, 72, 84, 96])

total = 0.4 * midterm + 0.6 * final

plt.scatter(midterm, final, label='Scatter Plot')
plt.title('Midterm vs Final Scores')
plt.xlabel('Midterm Score')
plt.ylabel('Final Score')
plt.grid(True)
plt.show()
plt.savefig('score_scatter.png')

plt.hist(total, bins=5, edgecolor='black')
plt.title('Distribution of Total Scores')
plt.xlabel('Total Score')
plt.ylabel('Number of Students')
plt.grid(axis='y', alpha=0.75)
plt.show()
plt.savefig('score_histogram.png')

plt.bar(students, total, label='Bar Plot')
plt.title('Student Scores')
plt.xlabel('Student')
plt.ylabel('Total Score')
plt.grid(True)
plt.show()
plt.savefig('score_bar_chart.png')

#TASK 4

students = ["S1", "S2", "S3", "S4", "S5", "S6", "S7", "S8", "S9", "S10"]
midterm = np.array([85, 72, 90, 66, 78, 92, 60, 74, 88, 95])
final = np.array([80, 70, 94, 68, 75, 90, 65, 72, 84, 96])

slope, intercept = np.polyfit(midterm, final, 1)

midterm_for_line = np.linspace(min(midterm), max(midterm), 100)
predicted_final_for_line = slope * midterm_for_line + intercept

plt.figure(figsize=(8, 6))
plt.scatter(midterm, final, label='Original Data Points')
plt.plot(midterm_for_line, predicted_final_for_line, color='red', label=f'Best-Fit Line (y = {slope:.2f}x + {intercept:.2f})')

plt.title('Midterm vs Final Scores with Best-Fit Line')
plt.xlabel('Midterm Score')
plt.ylabel('Final Score')
plt.legend()
plt.grid(True)
plt.show()
plt.savefig('score_prediction.png')

print("\n--- Prediction Examples ---")
prediction_midterms = [50, 75, 100]
for m in prediction_midterms:
    predicted_final = slope * m + intercept
    print(f"For a midterm score of {m}, the predicted final score is: {predicted_final:.2f}")