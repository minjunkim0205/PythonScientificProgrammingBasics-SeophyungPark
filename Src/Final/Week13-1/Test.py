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
img1 = np.full((rows, cols, 3), 0, np.uint8)
# Upper part of line AB
slopeAB = (A-B)[1] / (A-B)[0]
AB = (c_idx > (slopeAB * (r_idx - A[0]) + A[1]))
# Lower part of line BC
slopeBC = (C-B)[1] / (C-B)[0]
BC = c_idx < (slopeBC * (r_idx - B[0]) + B[1])
# Right part of line CD
CD = r_idx > C[0]
# DE
slopeDE = (E-D)[1] / (E-D)[0]
DE = c_idx > (slopeDE * (r_idx - D[0]) + D[1])
# EA
slopeEA = (A-E)[1] / (A-E)[0]
EA = c_idx < (slopeEA * (r_idx - E[0]) + E[1])
'''==========================================================================='''
idxABCD = AB & BC & CD
idxBCDE = BC & CD & DE
img1[idxBCDE] = vertex_colors[0]
plt.imshow(img1)
plt.show()