# Myntra-image-search
Deep Learning

<img align="left" alt="Visual Studio Code" height="520px" width="820px" src="https://github.com/harshithvh/Myntra-image-search/blob/main/images/img1.jpg" />

# About

---

**Myntra was originally a B2B platform for personalized gifts.**

Founded in 2007 by 3 IIT Kanpur alumni; Vineet Saxena, Ashutosh Lawania, and Mukesh Bansal; the platform allowed customers to personalize t-shirts, mousepads, mugs,etc.

**Becoming the launch platform for brands like Being Human & Fastrack**

By 2011, Myntra had moved away from personalization and focused on selling fashion and lifestyle products exclusively. 
Its eclectic collections from over 1000 local and international lifestyle brands made it the preferred choice for the fashion-conscious consumer. 

**Myntra has only grown in scale since then**

30,000+ Orders delivered per day, 1.5 L+ Fashion Products Listed, 18 M Monthly Active Users 

<img align="left" alt="Visual Studio Code" height="600px" width="820px" src="https://github.com/harshithvh/Myntra-image-search/blob/main/images/img2.png" />

# Image Search

---

Myntra’s Image Search feature on its mobile app lets the users search for similar products simply by uploading an image. So now, whenever we find something interesting and fashionable like a shirt, jeans or footwear, click the photo of it, and search it on Myntra using its image search option.

<img align="left" alt="Visual Studio Code" width="820px" src="https://github.com/harshithvh/Myntra-image-search/blob/main/images/img3.png" />

Most of the fashion purchases are done when we see someone using the product and then look for a similar product or sometimes maybe the exact one. This thing cannot be achieved by the simple text search and to overcome it, Myntra introduced the image search. Myntra's Image Search feature on its mobile app lets the users search for similar products simply by uploading an image.
**From clicked image to similar product recommendation**

<img align="left" alt="Visual Studio Code" width="820px" src="https://github.com/harshithvh/Myntra-image-search/blob/main/images/img4.png" />

# Techonology used by Myntra

# Deep Learning

---

Deep learning is a subset of Machine Learning which is, in turn, a subset of AI. It is based on artificial neural networks and representation learning. It has a wide range of applications in areas like computer vision, bioinformatics, and board game programs, where the results are comparable to human expert performance, and in some cases even surpassed it. 

<img align="left" alt="Visual Studio Code" height="620px" width="820px" src="https://github.com/harshithvh/Myntra-image-search/blob/main/images/img5.png" />

# Image Search Implementation : INTUITION

---

We will be performing the following three steps:

1. Generate product attributes (features) using an algorithm
2. Using the same algorithm, find attributes of clicked image
3. Find images with attributes similar to clicked image attributes 

<img align="left" alt="Visual Studio Code" width="256px" src="https://github.com/harshithvh/Myntra-image-search/blob/main/images/img6.png" />
<img align="left" alt="Visual Studio Code" width="256px" src="https://github.com/harshithvh/Myntra-image-search/blob/main/images/img7.png" />
<img align="left" alt="Visual Studio Code" height="380px" width="256px" src="https://github.com/harshithvh/Myntra-image-search/blob/main/images/img8.png" />

<img align="left" alt="Visual Studio Code" width="820px" src="https://github.com/harshithvh/Myntra-image-search/blob/main/images/img9.png" />

<img align="left" alt="Visual Studio Code" width="820px" src="https://github.com/harshithvh/Myntra-image-search/blob/main/images/img10.png" />

# Neural Networks

---

Neural networks, also known as artificial neural networks or simulated neural networks, are a subset of machine learning and are at the heart of deep learning algorithms. Their name and structure are inspired by the human brain, mimicking the way that biological neurons signal to one another.

Neural networks are comprised of node layers, containing an input layer, one or more hidden layers, and an output layer.

<img align="left" alt="Visual Studio Code" width="820px" src="https://github.com/harshithvh/Myntra-image-search/blob/main/images/img11.png" />

We divide our dataset into two categories:

Train Dataset: Used to fit the machine learning model.

Test Dataset: Used to evaluate the fit machine learning model.

<img align="left" alt="Visual Studio Code" width="820px" src="https://github.com/harshithvh/Myntra-image-search/blob/main/images/img12.png" />

# Convolutional Neural Network

---

A CNN is a Deep Learning algorithm that can take in a bi-dimensional input and be able to differentiate it from another by learning filters that extract complex features from the inputs automatically. Basic modelling of a CNN is represented in Figure.

<img align="left" alt="Visual Studio Code" width="820px" src="https://github.com/harshithvh/Myntra-image-search/blob/main/images/img13.png" />

During the training step, each convolution layer learns the filter weights to then produce a feature map. The filter or kernel is sliding over the input and the sum of the convolution generates the feature map. After a convolution layer, it is common to add a pooling layer. These kinds of layers are used to decrease the number of parameters in the network. This reduces the computational cost and controls overfitting. The most frequent type of pooling is Max-pooling, which takes the maximum value in each window. In order to carry out a classification or a regression problem with the features generated by the convolutional layers, it is necessary to add dense layers at the end of the network.

# K- Nearest Neighbors

---

The k-nearest neighbors (KNN) algorithm is a simple machine learning algorithm that can be used to find the nearest neighbors. It compares the distance between all product features and clicked product features. K refers to a number of neighbors we want to find.

<img align="left" alt="Visual Studio Code" width="820px" src="https://github.com/harshithvh/Myntra-image-search/blob/main/images/img15.png" />
<img align="left" alt="Visual Studio Code" width="820px" src="https://github.com/harshithvh/Myntra-image-search/blob/main/images/img16.png" />
<img align="left" alt="Visual Studio Code" width="820px" src="https://github.com/harshithvh/Myntra-image-search/blob/main/images/img17.png" />
