### README: Spotify Track Genre Predictor

#### i. Dataset Description
The dataset used for this project is the Spotify Tracks Dataset, which contains audio features and metadata for over a range of 125 different genres. Key columns include numerical features like danceability, energy, tempo, loudness, and key, as well as categorical variables such as track name, artist, and genre. After preprocessing, genres were grouped into 10 broader categories for better classification performance. The dataset was cleaned by removing rows with missing values and duplicate entries, ensuring high-quality data for training and evaluation.

#### ii. Problem Overview
The objective of this project was to classify Spotify tracks into their respective genres based on their numerical and audio-based features. Genre prediction is a challenging multi-class classification problem due to the overlapping characteristics of certain genres and the variability within each genre. Grouping similar genres into broader categories was a key preprocessing step to simplify the classification task and enhance model performance.

#### iii. Key Methodology
The primary methodology involved using a fully connected feedforward neural network for genre classification. 
The neural network was selected for its ability to model complex feature interactions, which are essential for multi-class problems like genre classification.

The network consisted of:
- An input layer with 15 neurons corresponding to the input features.
- Two hidden layers with 16 and 32 neurons, respectively, using ReLU activation for non-linearity.
- An output layer with 10 neurons representing the 10 genre categories, optimized using the CrossEntropyLoss function.

The dataset was preprocessed by normalizing numerical features and encoding genres into numerical labels. It was then split into training (70%), validation (15%), and test (15%) sets to evaluate the model's performance. The Adam optimizer was used with a learning rate of 0.0005 to adjust weights during training. Batch processing with a size of 64 enabled efficient updates to the model.

The neural network’s architecture was chosen for its ability to learn non-linear relationships in the data, making it well-suited for the multi-class genre prediction task. Training was conducted over 50 epochs, with both training and validation losses monitored to detect overfitting or convergence issues.

#### iv. Results and Evaluation
The model achieved a validation accuracy of approximately 27% on the test set. Evaluation metrics included:
- **Cross-Entropy Loss**: Monitored during training and validation to assess convergence.
- **Accuracy**: Used as the primary metric to evaluate the classification performance.

Cross-validation was indirectly used by splitting the dataset into train, validation, and test sets to ensure robust evaluation. While the model performed better than random guessing for a 10-class problem, the accuracy was relatively low due to the inherent challenges of genre classification, including overlapping features and noise in the data.

Its limitations include sensitivity to hyperparameter choices and the need for large amounts of training data. Future work could address these by exploring data augmentation or advanced architectures such as convolutional or recurrent neural networks.

#### v. Usage Instructions
To use this code for genre prediction, follow these steps:

1. **Install Required Libraries**:
   Ensure the following libraries are installed:
   ```bash
   pip install numpy pandas torch matplotlib scikit-learn
   ```
2. **Run the Code**:
   To execute the project, run the following Jupyter notebook: 
   ```
   genre_predictor.ipynb
   ```
