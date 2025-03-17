# Dream Homes Price Estimator
[Download Here](https://sites.google.com/view/faurys-portfolio/software) 

The real estate market had always been dynamic, presenting significant challenges in accurately estimating property prices. Clients often faced uncertainty and delays, which led to missed opportunities and decreased satisfaction. They lacked reliable tools to guide their decision-making effectively regarding property pricing.
The standalone Windows application was developed to address these challenges. It incorporated a house price prediction model that utilized the Melbourne Housing dataset and machine learning techniques, specifically the Random Forest Regressor algorithm. The application predicted property prices based on key features such as location, square footage, and historical real estate data. Additionally, it included visualizations, such as histograms, scatter plots, and a correlation heatmap, to make complex data insights easily interpretable.
## Visualizations
The application features an intuitive and user-friendly design where all the key visualizations are prominently displayed on the main screen upon launch. These include the histogram of house prices, the correlation heatmap, and the scatter plot of square footage versus price. By placing these visualizations at the forefront, users are immediately provided with a clear, graphical overview of critical market trends and data insights. This design ensures that users, whether clients or agents, can quickly grasp the distribution of prices, the relationships between property attributes, and how property size impacts pricing.
## Data Entry
 After specifying the number of rooms,, bathrooms, land size, and the location by latitude and longitude, the machine learning model delivers a property price estimation.
## Data Source and Collection
The raw data for this project was sourced from the publicly available Melbourne Housing dataset, which was hosted on Kaggle. The dataset contained detailed information on property features such as location, square footage, the number of rooms, and historical sale prices. This dataset was collected through real estate transactions in Melbourne, Australia, and was curated to provide insights into housing trends and pricing in the region. Since it was publicly shared on Kaggle, the data adhered to the platform's terms of use, making it ethical and legal for analysis and modeling purposes. Exploratory Data Analysis (EDA) was conducted to identify trends, correlations, and potential anomalies, such as missing values or extreme outliers. A data cleaning plan was developed to ensure the dataset met the requirements for predictive modeling. Feature Engineering were applyed, relevant features were selected, and categorical variables were encoded for compatibility with the Random Forest Regressor model. The data was also scaled or normalized where necessary.
## Machine Learning
The algorithm applyied in this porject was the Random Forest Regression. the Random Forest Regression is a supervised machine learning method used for predicting continuous values. In this project, it was implemented to work by constructing multiple decision trees during training and averaging their predictions to deliver more accurate and reliable results. During the training phase, the algorithm’s arguments were tested to identify the most prolific values to obtain a reliable output.
During training, the Random Forest method randomly selected subsets of the dataset and trained individual decision trees on these subsets. This process was known as "bootstrap aggregating" or "bagging." At each split in a decision tree, only a random subset of features was considered, which reduced correlation among trees and strengthened the ensemble model. After training, the predictions of all decision trees were measured to produce a final regression output. This reduced the noise from individual trees and ensured more stable and accurate predictions.
## Validation 
The validation of the Random Forest Regression model was performed using the Mean Absolute Error (MAE) as the primary performance metric. MAE measured the average of the absolute differences between the predicted house prices and the actual house prices. This method provided an intuitive and straightforward way to assess the model’s accuracy, as it directly represented the average prediction error in the same units as the target variable (house prices).

## MAE Results:
After the model was trained and tested, it achieved an MAE of 17000.0 on the testing dataset, which indicated that the model’s predictions were closely aligned with actual house prices.
