import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as mpimage

# Matplotlib Basics
x = np.linspace(0,5,11)
print(x)

y = x**2
print(y)

# creating a line graph
# plt.plot(x,y)
# plt.title('Squares of a Number')
# plt.xlabel('Numbers')
# plt.ylabel('Squares')
# plt.show()

# learn about subploting
# plt.subplot(2,2,1)
# plt.plot(x**2,y**2)
# plt.subplot(2,2,2)
# plt.plot(x,x)
# plt.subplot(2,2,3)
# plt.plot(y,x)
# plt.subplot(2,2,4)
# plt.plot(x,y)
# plt.show()

# Object Oriented way

# fig = plt.figure(figsize=(20,8), dpi=100)
# axis1 = fig.add_axes([0.1, 0.1, 1, 1])
# axis1.plot(x,y)
# # plt.show()
# axis2 = fig.add_axes([0.3, 0.1, 0.6, 0.6])
# axis2.plot(x,y)
# plt.show()

# -------------------------------------------------
# Types of Plots
# plt.scatter(x,y)
# plt.show()

# plt.hist(x)
# plt.show()

# plt.boxplot(x)
# plt.show()

# --------------------------------------------------
# here is how we save the plots
# fig = plt.figure()
# ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
# ax.plot(x,y)
# plt.show()
# plt.savefig('BasicPlot.png')

# -------------------------------------------------
# Working with images
img = mpimage.imread('images.jpeg')
# print(img)
plt.imshow(img)
plt.axis('off')
plt.show()
cropped_img = img[50:200, 100:300] # crop [rows, columns]
plt.imshow(cropped_img)
plt.axis('off')
plt.show()

# -----------------------------------------------------
plt.plot(x,y,color='pink')
plt.show()


















