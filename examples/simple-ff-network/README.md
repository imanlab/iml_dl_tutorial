# Simple feed forward network

This is a simple Deep Learning example based on [this tutorial](https://machinelearningmastery.com/tutorial-first-neural-network-python-keras/) and some extensions suggested in the article itself.

## Prerequisites

You can run this example on your laptop without any major issues: no big CPU nor any GPU is required.  
The only requisites are some Python packages which will be listed later on.

## Environment setup

If you do not have `conda` installed follow [these](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html#regular-installation) instructions to install Anaconda.

When you are done create a new `conda` environment:

```bash
conda create --name simple-ff-network
```

Then activate it and navigate to the folder containing these files.

```bash
conda activate simple-ff-network
cd /path/to/the/files/examples/simple-ff-networks
```

If everything went well you should see the name of the environment in your prompt from now on.  
Something along the lines of:

```bash
(simple-ff-network) user@computer: /path/to/the/files/examples/simple-ff-networks $ 
```

Now let's install all the necessary packages.

```bash
conda install python=3.8 keras numpy matplotlib scikit-learn
```

## Running the script

Now, have a look at the Python files (they are full of comments with external links to deepen your knowledge on various topics).  
When you are ready just run:

```bash
python3 main.py
```

## Considerations

This is a very simple deep learning example with a small dataset, but it introduces various useful concepts, such as:

- data generators
- train/test split
- keras models
- losses, optimizers and metrics
- training and evaluation

Don't take this code as a "best practice" example, just use it to understand the most important steps to build and use a deep learning model.