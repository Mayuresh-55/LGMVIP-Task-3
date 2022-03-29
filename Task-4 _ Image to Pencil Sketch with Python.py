#!/usr/bin/env python
# coding: utf-8

# ## Lets Grow More
# ## Name : Mayuresh Kumbhar
# ## Internship : Data Science
# 
# ### Task-4 : Image to Pencil Sketch with Python
# 
# ### Description : 
# 
# We need to read the image in RBG format and then convert it to a grayscale image. This will turn an image into a classic black and white photo. Then the next thing to do is invert the grayscale image also called negative image, this will be our inverted grayscale image. Inversion can be used to enhance details. Then we can finally create the pencil sketch by mixing the grayscale image with the inverted blurry image. This can be done by dividing the grayscale image by the inverted blurry image. Since images are just arrays, we can easily do this programmatically using the divide function from the cv2 library in Python.
# 
# ### Reference link : https://thecleverprogrammer.com/2020/09/30/pencil-sketch-with-python/
# 
# # Installing OpenCV library

# In[2]:


# Used for image processing and performing computer vision tasks
pip install opencv-python


# # Importing library

# In[8]:


import cv2
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# # Changing image directory

# In[9]:


import os


# In[10]:


os.getcwd()


# In[11]:


os.chdir("C:\\Users\\Admin\\Downloads\\geo project\\2")


# In[12]:


os.getcwd()


# # Reading and processing image

# In[13]:


# reading image
image = cv2.imread("cat.jpg")
image


# In[14]:


# displaying image
cv2.imshow("Cat", image)
cv2.waitKey(0)
plt.imshow(image)


# In[15]:


# converting image to grayscale image
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("New Cat", gray_image)
cv2.waitKey(0)
plt.imshow(gray_image)
gray_image


# In[16]:


# inverting grayscale image
inverted_image = 255 - gray_image
cv2.imshow("Inverted", inverted_image)
cv2.waitKey()
plt.imshow(inverted_image)
inverted_image


# In[17]:


# blurring image using Gaussian function in OpenCV
blurred = cv2.GaussianBlur(inverted_image, (21, 21), 0)
plt.imshow(blurred)
blurred


# In[18]:


# inverting the blurred image 
# displaying final sketch
inverted_blurred = 255 - blurred
pencil_sketch = cv2.divide(gray_image, inverted_blurred, scale=256.0)
cv2.imshow("Sketch", pencil_sketch)
cv2.waitKey(0)
plt.imshow(pencil_sketch)
pencil_sketch


# # Comparison between original image and pencil sketch

# In[19]:


# display original image alongside pencil sketch
cv2.imshow("original image", image)
cv2.imshow("pencil sketch", pencil_sketch)
cv2.waitKey(0)


# In[ ]:




