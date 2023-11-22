import numpy as np
import matplotlib.pyplot as plt
'''==========================================================================='''
radius = 150
center = (200,200)
theta = np.linspace(0, np.pi*4, 6) + np.pi
x = radius*np.cos(theta) + center[0]
y = radius*np.sin(theta) + center[1]
x = np.round(x, 0).astype(np.int32)
y = np.round(y, 0).astype(np.int32)
A, B, C, D, E = (np.array([x[n], y[n]]) for n in range(5))
'''==========================================================================='''
cols = rows = 401
img = np.full((rows, cols, 3), 0, np.uint8)
'''==========================================================================='''
v_rad = 20
V = (A, B, C, D, E)
vertex_colors = np.array([[255,0,0],
                          [0,255,0],
                          [0,0,255],
                          [0,255,255],
                          [255,0,255]])
r_idx = np.arange(rows).reshape(-1,1)
c_idx = np.arange(cols).reshape(1,-1)
'''==========================================================================='''
img = np.full((rows, cols, 3), 0, np.uint8)
# Upper,Lower part of line AB
slopeAB = (A-B)[1] / (A-B)[0]
idxUpperAB = (c_idx > (slopeAB * (r_idx - A[0]) + A[1]))
idxLowerAB = (c_idx < (slopeAB * (r_idx - A[0]) + A[1]))
# Upper,Lower part of line BC
slopeBC = (B-C)[1] / (B-C)[0]
idxUpperBC = c_idx > (slopeBC * (r_idx - B[0]) + B[1])
idxLowerBC = c_idx < (slopeBC * (r_idx - B[0]) + B[1])
# Upper,Lower part of line CD
idxUpperCD = r_idx > C[0]
idxLowerCD = r_idx < C[0]
# Upper,Lower part of line DE
slopeDE = (D-E)[1] / (D-E)[0]
idxUpperDE = c_idx > (slopeDE * (r_idx - D[0]) + D[1])
idxLowerDE = c_idx < (slopeDE * (r_idx - D[0]) + D[1])
# Upper,Lower part of line EA
slopeEA = (E-A)[1] / (E-A)[0]
idxUpperEA = c_idx > (slopeEA * (r_idx - E[0]) + E[1])
idxLowerEA = c_idx < (slopeEA * (r_idx - E[0]) + E[1])
'''==========================================================================='''
idxABCDE = idxUpperAB & idxLowerBC & idxUpperCD & idxUpperDE & idxLowerEA
img[idxABCDE] = vertex_colors[4]
plt.imshow(img)
plt.show()