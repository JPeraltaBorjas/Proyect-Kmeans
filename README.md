# Project: Determining Optimal Cluster Point using the Elbow Method in K-Means Clustering

## Overview:

This project aims to demonstrate the use of the Elbow Method to identify the optimal number of clusters for a K-Means clustering model. By employing this method, we can make an informed decision on the appropriate number of clusters to use in our dataset. K-Means clustering is an unsupervised machine learning algorithm used for partitioning data into clusters based on similarity.

## Dataset:

The dataset used in this project contains information about the number of debits and credits, as well as their sum, across different service channels and in various jurisdictions. It is essential to have a dataset with clear patterns or groupings that can be effectively clustered.

## Methodology:

1. **Exploratory Data Analysis (EDA):** Before applying the K-Means algorithm, conduct exploratory data analysis to understand the underlying patterns and distributions within the data.

2. **Preprocessing:** Prepare the data for clustering by handling missing values, scaling features if necessary, and encoding categorical variables.

3. **K-Means Clustering:** Implement the K-Means clustering algorithm on the preprocessed data. Iterate over a range of cluster numbers, and for each iteration, calculate the sum of squared distances (inertia) of samples to their closest cluster center.

4. **Elbow Method:** Plot the number of clusters against the corresponding inertia values. The "elbow" point on the plot represents the optimal number of clusters, where adding more clusters does not significantly decrease the inertia.

5. **Model Evaluation:** Assess the performance of the K-Means clustering model using the optimal number of clusters determined by the Elbow Method. Visualize the clusters and analyze their characteristics.

## Usage:

1. **Dependencies:**
   - Python 3
   - Libraries: NumPy, Pandas, Matplotlib, Scikit-learn

2. **Installation:**
   - Install the required dependencies using pip:
     ```
     pip install numpy pandas matplotlib scikit-learn
     ```

3. **Execution:**
   - Run the Jupyter notebook or Python script provided in the repository.
   - Follow the instructions within the notebook/script to load the dataset, preprocess the data, and apply the K-Means clustering algorithm.
   - Interpret the Elbow Method plot to determine the optimal number of clusters.
   - Analyze the clustering results and evaluate the model's performance.

## Results:

The main outcome of this project is the identification of the optimal number of clusters for the given dataset using the Elbow Method. Additionally, insights into the structure of the clusters and the characteristics of the data points within each cluster will be provided.

## Repository Structure:

- `README.md`: Overview of the project, usage instructions, and results.
- `Metodo del codo.ipynb` (or `Metodo del codo.py`): Jupyter notebook or Python script containing the code implementation.
- `CANAL.xlsx, JURISDICCION.xlsx` (or relevant data format): Sample dataset used for clustering.

## Contact:

For any inquiries or suggestions regarding this project, please contact Jay Peralta Borjas at jmw.peralta@gmail.com.
