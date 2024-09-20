import sys
import pickle
import numpy as np

# usage warning
if len(sys.argv) != 3:
    print('Usage: python compress_trajectory.py <input_file> <output_file>')
    sys.exit()

# Load the trajectory data
with open(sys.argv[1], 'rb') as f:
    data = pickle.load(f)

# Compress the trajectory data
for i in range(len(data['recorded_img_feedback_flag'])):
    if not data['recorded_img_feedback_flag'][i]:
        data['recorded_img'][i] = np.empty(0)


with open(sys.argv[2], 'wb') as f:
    pickle.dump(data, f)



