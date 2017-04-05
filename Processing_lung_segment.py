import numpy as np

much_data_1 = np.load('./preprocessing_model/muchdata_1.npy')
much_data_2 = np.load('./preprocessing_model/muchdata_2.npy')
much_data = much_data_1 + much_data_2

np.save('./preprocessing_model/muchdata.npy', much_data)
