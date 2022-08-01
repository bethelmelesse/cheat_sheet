'''to check if cpu or gpu available'''

import torch
device = 'cuda' if torch.cuda.is_available() else 'cpu'
print('Using {} device'.format(device))