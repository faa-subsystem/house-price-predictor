import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

df = pd.read_csv('data\melb_df.csv')
# df

y = df['Price']
X = df[['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']]
train_X, val_X, train_y, val_y = train_test_split(X, y)

rf = RandomForestRegressor(n_estimators=280,
                           max_depth=50,
                           min_samples_split=10,
                           min_samples_leaf=2,
                           max_features='sqrt',
                           max_leaf_nodes=5555)
rf.fit(train_X, train_y)


def rf_predictor(rooms, bathroom, landsize, lattitude, longtitude):
    out = rf.predict([[rooms, bathroom, landsize, lattitude, longtitude]])
    return round(out[0], 2)
