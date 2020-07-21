# Machine Learning Project : Iris-flower-classification
This program applies basic machine learning (classification) concepts on *Fisher's Iris Data* to predict the species of a new sample of Iris flower.

**Software and Libraries**
- Python
- Anaconda (64 bit)
- scikit-learn

**Introduction**  
The dataset for this project originates from the [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Iris). The Iris flower data set or Fisher's Iris data set is a multivariate data set introduced by the British statistician and biologist Ronald Fisher in his 1936 paper The use of multiple measurements in taxonomic problems as an example of linear discriminant analysis.
- The data set consists of 50 samples from each of three species of Iris (Iris setosa, Iris virginica and Iris versicolor).
- Four features were measured from each sample (in centimetres): 
  - Length of the sepals
  - Width of the sepals
  - Length of the petals
  - Width of the petals
  
 **Working of the project**
- The program takes data from the `load_iris()` function available in `sklearn` module.
- The program then divides the dataset into training and testing samples in 80:20 ratio randomly using `train_test_learn()` function available in `sklearn` module.
- The training sample space is used to train the program and predictions are made on the testing sample space.
- Accuracy score is then calculated by comparing with the correct results of the training dataset.

**There are 3 species of iris flowers**

These are
1. Iris-Setosa
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/56/Kosaciec_szczecinkowaty_Iris_setosa.jpg/220px-Kosaciec_szczecinkowaty_Iris_setosa.jpg" title="iris-setosa" height=300px width=300px>

2. Iris-Versicolor
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/4/41/Iris_versicolor_3.jpg/220px-Iris_versicolor_3.jpg" title="iris-versicolor" height=300px width=300px>

3. Iris-Virginica
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9f/Iris_virginica.jpg/220px-Iris_virginica.jpg" title="iris-virginica" height=300px width=300px>
