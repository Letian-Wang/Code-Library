# Extract data from pkl to mat
import scipy.io
import pickle
a=pickle.load( open( 'xy_list.pkl', "rb" ) )
scipy.io.savemat('xy_list2.mat', mdict={'pickle_data': a})