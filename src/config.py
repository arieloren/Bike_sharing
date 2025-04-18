FILE_PATH = 'data/batch1.csv'


# Transofrm
drop_columns = ['weekday','hour']
prdict_colunms = ['year','month','hour_x','hour_y','temp','humidity','windspeed']

# model
model_casual = 'models/model_casual.pkl'
model_registered = 'models/model_registered.pkl'

# load
RESULT_FILE_PATH = 'data/predictions.csv'
