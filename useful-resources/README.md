# Useful resources

- [Useful resources](#useful-resources)
  - [MIT - 6.S191 - Intro to deep learning](#mit---6s191---intro-to-deep-learning)
    - [Tools](#tools)
    - [Material](#material)
    - [Topics](#topics)
  - [Washington University - T81 558 - Applications of Deep Neural Networks](#washington-university---t81-558---applications-of-deep-neural-networks)
    - [Tools](#tools-1)
    - [Material](#material-1)
    - [Topics](#topics-1)
  - [Cheatsheets (AI, ML, DL)](#cheatsheets-ai-ml-dl)
    - [Material](#material-2)
    - [Topics](#topics-2)
  - [Machine Learning Mastery](#machine-learning-mastery)
    - [Material](#material-3)
  - [StatQuest](#statquest)
    - [Material](#material-4)
    - [Topics](#topics-3)

This is a curated collection of useful resources to start with deep learning.

If you have zero previous experience in this field our suggestion is to follow this order:

- general Python tutorial
- theoretical course on DL (e.g. MIT 6.S191 or Coursera)
- practical course on DL, tutorials and hands-on examples (i.e. WU T81 558 or Machine Learning Mastery)

## MIT - 6.S191 - Intro to deep learning

This is a really high quality course from MIT which covers the basics of deep learning without delving too much into the math. It's really good to get a first overall view of the field, understanding the basic concepts and the most used structures.

The first 6 lessons are the most useful ones: the other ones are more focused on specific topics which might not be as helpful for a general introduction.

The labs are somewhat helpful, but are quite difficult as a first hands-on approach: you can safely skip them.

### Tools

**Language**: Python  
**Deep learning**: Tensorflow and Keras (some quick mentions)  
**Other tools**: Google Colab (not explained)

### Material

**Website**

http://introtodeeplearning.com/  
A summary of all the course contents. Links to lectures, material and labs.

**YouTube playlist of past lectures**

https://www.youtube.com/playlist?list=PLtBw6njQRU-rwp5__7C0oIVt26ZgjG9NI  
A playlist, updated year by year, containing all the lectures of the past editions of the course. It's recommended to follow the most recent one.

### Topics

**Intro**  
Perceptrons, activation functions, loss, feedforward networks (FFN), backpropagation, batching, Stochastic Gradient Descent (SGD)

**Recurrence**  
recurrence, recurrent neural networks (RNN), Backpropagation Through Time (BPTT), variable length sequences, vanishing and exploding gradient, LSTM, attention

**Convoloution**  
computer vision, filters, convolution, Convolutional Neural Networks (CNN), pooling, object detection, RCNN, fully convolutional NN

**Deep generative modeling**  
supervised and unsupervised learning, generative modeling, latent variables, autoencoders, Variable Auto Encoders (VAE), regularization, stochastic sampling reparametrization, Generative Adversarial Networks (GAN)

**Reinforcement learning**  
reinforcement learning, Q-learning, policy gradient, training, troubles with simulations

## Washington University - T81 558 - Applications of Deep Neural Networks

This course is heavily focused on programming and a hands-on approach, which can be very useful to start. It has almost no prerequisites since the first modules cover both the basics of Python and of deep learning, however deep learning concepts are only summarily presented and some previous theoretical knowledge is advised.

The great advantage of this course is the constant reference to complete and working implementation in Python/Keras. Also, it gives a complete introduction to Google Colab.  
Colab is a tool by Google which provides you with direct access through a web page to a Python environment pre-configured for machine learning: all the main libraries are already installed and configured, nothing has to be installed on your device and you also have access to Google's GPU which usually are much more powerful than the average laptop.

The assignments (one for each module) are really helpful to recap the content of each module and to have some hands-on experience (note: assignment **cannot** be submitted and corrected/evaluated).

### Tools

**Language**: Python  
**Deep learning libraries**: Tensorflow and Keras  
**Other tools**: Colab (with complete introduction)

### Material

**Website**  

https://github.com/jeffheaton/t81_558_deep_learning  
This is the github repository were all course material is stored, mainly the syllabus which consists of multiple Jupiter/Colab notebooks which can be used to follow along the video lessons.

**Videos**

https://www.youtube.com/playlist?list=PLjy4p-07OYzulelvJ5KVaT2pDlxivl_BN  
This is the YouTube playlist of the 2021 edition of the course.


### Topics

**Introduction**  
Basic python concepts (lists, dictionaries, files, functions...), python for machine learning (pandas, tensorflow, keras), saving and loading tensorflow models, early stopping

**Machine learning**  
Feature vectors, classification, regression, backpropagation, ADAM optimizer, losses

**General deep learning**  
Regularization, K-fold validation, dropout, hyperparameters

**Advanced deep learning**  
Image processing, CNN, ResNet, DarkNet, time series, LSTM, temporal CNN, natural language processing (NLP), reinforcement learning, Q-learning

## Cheatsheets (AI, ML, DL)

These documents are collections of quick concepts, examples and brief explanations related to Artificial Intelligence, Machine learning and Deep Learning.

They are not as useful for learning those concepts (since the content is really synthetic), but they can be used to explore new concepts or revise old ones.

The first module of AI and all the modules of ML and DL are the most useful for ML and DL.

### Material

**AI cheatsheet**  
https://stanford.edu/~shervine/teaching/cs-221/

**ML cheatsheet**  
https://stanford.edu/~shervine/teaching/cs-229/

**DL cheatsheet**  
https://stanford.edu/~shervine/teaching/cs-230/

### Topics

**Artificial intelligence**  
Predictions, models, losses, optimization, states, dynamic programming, graphs, costs, cost relaxation, Markov decision process, logic

**Machine learning**  
Supervised and unsupervised learning, losses, gradient descent, deep learning, deep architectures, convolution, normalization, LSTM

**Deep learning**  
Convolution, layers, hyperparameters, object detection, transfer learning, recurrence, vanishing and exploding gradient, GRU, LSTM, language models, data augmentation, normalization, overfit

## Machine Learning Mastery

Machine learning mastery is a great website containing tons of articles and tutorials covering almost any basic aspect of neural networks and deep learning, with great examples and code implementations.

The best way to use this resource is to find an article related to a specific topic, follow the tutorial and the expand outwards following the suggested related arguments and possible improvements.

### Material

**Website**  
https://machinelearningmastery.com/start-here/#deeplearning

**Tutorial: simple feedforward network with keras**  
https://machinelearningmastery.com/tutorial-first-neural-network-python-keras/

It's a complete tutorial, good for beginners, touching the following topics: Sequential deep model, compile, fit, evaluate, predict

Useful extensions:
- [Saving the model](https://machinelearningmastery.com/save-load-keras-deep-learning-models/)
- [Model summary](https://machinelearningmastery.com/visualize-deep-learning-neural-network-model-keras/)
- [Train and test datasets - Display learning curves](https://machinelearningmastery.com/display-deep-learning-model-training-history-in-keras/)
- [Keras Functional API](https://machinelearningmastery.com/keras-functional-api-deep-learning/)
- [Hyperparameters search](https://machinelearningmastery.com/grid-search-hyperparameters-deep-learning-models-python-keras/)

**Tutorial: CNN for image classification**  
https://machinelearningmastery.com/how-to-develop-a-cnn-from-scratch-for-cifar-10-photo-classification/

It's a good medium-advanced tutorial, helping you build a simple CNN from scratch. Topics: CIFAR-10 dataset, normalization, convolution, pooling, dropout, weight decay, data augmentation, batch normalization

Useful extensions:
- [Dropout](https://machinelearningmastery.com/dropout-for-regularizing-deep-neural-networks/)
- [Weight regularization](https://machinelearningmastery.com/weight-regularization-to-reduce-overfitting-of-deep-learning-models/)
- [Data augmentation](https://machinelearningmastery.com/how-to-configure-image-data-augmentation-when-training-deep-learning-neural-networks/)
- [Batch normalization](https://machinelearningmastery.com/how-to-configure-image-data-augmentation-when-training-deep-learning-neural-networks/)

## StatQuest

StatQuest is a YouTube channel providing almost 200 videos on various topics regarding statistics, machine learning and deep learning.  
The videos have a very slow pace, introducing all necessary content or linking to previous videos where prerequisites have already been presented in more detail. The maths are presented in detail although without many formalisms (the concepts are presented in order to require only very basic math prerequisites).

In general this channel is really good to get a good, clear and intuitive explanation on any given topic, with a particular focus on statistics and machine learning in general, although there is a playlist devoted to deep learning.

### Material

**Video index**
https://statquest.org/video-index/

This webpage collects all the videos of the channel, including the playlists (which are great if you want to cover some macro-topic, following the videos in order) and even some livestreams. The best way to access content is to look for keywords here and find the most useful videos.

### Topics

These are the main playlists available on the channel, each covering a macro-topic.

**Statistic fundamentals**: https://www.youtube.com/playlist?list=PLblh5JKOoLUK0FLuzwntyYI10UQFUhsY9

**Linear regression and linear models**: https://www.youtube.com/playlist?list=PLblh5JKOoLUIzaEkCLIUxQFjPIlapw8nU

**Logistic regression**: https://www.youtube.com/playlist?list=PLblh5JKOoLUKxzEP5HA2d-Li7IJkHfXSe

**Machine learning**: https://www.youtube.com/playlist?list=PLblh5JKOoLUICTaGLRoHQDuF_7q2GfuJF

**Neural networks**: https://www.youtube.com/playlist?list=PLblh5JKOoLUIxGDQs4LFFD--41Vzf-ME1

