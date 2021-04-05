import h5py
from nntrainer import arguments, maths, utils
import numpy as np
import os
from pathlib import Path

"""
Converts the file into a h5 file by joinig the data that are in .npy format
"""

parser = utils.ArgParser(description=__doc__)
arguments.add_path_args(parser)
args = parser.parse_args()
#path_data = args.data_path
path_data='/scratch-shared/ActiveNet'
path_to_folder = Path(path_data)/ "fc6_feat_100rois"  # Multiple npy files in one folder,
#txtpath=‘/CNN/txtpath'
namelist=[x for x in os.listdir(path_to_folder)]
#namelist.sort(key=lambda x:int(x[:-4]))   #npy file name in order

with h5py.File("mytestfile.h5", "w") as hf:
    #print len(namelist)#1674
    for i in range( len(namelist) ):
        datapath=os.path.join(path_to_folder,namelist[i]) #specific address
        data = np.load(datapath)  
        #np.savetxt('%s/%d.txt'%(txtpath,i),data)
        hf.create_dataset("numpy_db", data=data)
    
    print ('over')
hf.close()
#npfiles = glob.glob("*.npy")
# for npfile in npfiles:
#     all_arrays.append(np.load(os.path.join(path_to_folder, npfile)))
# all_arrays = np.array(all_arrays)
# np.save(f_handle, all_array)
