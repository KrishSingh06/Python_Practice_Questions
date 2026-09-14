# consider the following  linear eq and solve using scipy 
# i) 2x + 3y = 8 ,4x+ 5y = 14
import numpy as np
from scipy.linalg import solve
A = np.array([[2, 3],[4, 5]])
B = np.array([8, 14])
solution = solve(A, B)
print("x =", solution[0])
print("y =", solution[1])
# ii) consider a scenario where two car are moving from a point P to point Q
# in the same direction and meet each other after 11 hr .if they move in opposition direction
# they will meet each other after 1 hr .find out the velocity of both car 
D = 110   
A = np.array([[11, -11],[1,   1]])
B = np.array([D, D])
x, y = solve(A, B)
print("Velocity of car 1 =", x, "km/hr")
print("Velocity of car 2 =", y, "km/hr")