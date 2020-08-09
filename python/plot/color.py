import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

def value_to_rgb(val, cmap_name):
    """ 
        Input：cmap_name, val range: [0,1]
        Rerutn: rgb on that cmap

        >>> value_to_rgb('YlOrBr', 1)
        (0.4, 0.1450980392156863, 0.02352941176470588)
    """
    RGB_Index = int(val * 299)
    x = np.linspace(0.0, 1.0, 300)
    rgb = tuple(cm.get_cmap(cmap_name)(x)[np.newaxis, :, :3][0][RGB_Index])
    return rgb

num = [i for i in range(10)]
    
cmap = 'YlGn'
color = value_to_rgb(0.5, cmap)     # Green
print(cmap, ": ", color)

cmap = 'Purples'
color = value_to_rgb(0.5, cmap)     # Purples
print(cmap, ": ", color)

cmap = 'Blues'
color = value_to_rgb(0.5, cmap)     # Blues
print(cmap, ": ", color)

cmap = 'Reds'
color = value_to_rgb(0.5, cmap)     # Reds
print(cmap, ": ", color)

cmap = 'YlOrBr'
color = value_to_rgb(0.5, cmap)     # Orange
print(cmap, ": ", color)

cmap = 'gray'
color = value_to_rgb(0.5, cmap)     # gray
print(cmap, ": ", color)
plt.plot(num, num, color = color,linewidth=20)

plt.show()


# Green - YlGn :  (0.4738485198000769, 0.7778854286812764, 0.4758016147635525)
# Purples - Purples :  (0.6214532871972318, 0.606074586697424, 0.7855440215301807)
# Blues - Blues :  (0.42274509803921567, 0.684075355632449, 0.8398923490965013)
# Reds - Reds :  (0.9843752402921953, 0.4181468665897732, 0.2926566705113418)
# Orange - YlOrBr :  (0.996078431372549, 0.602645136485967, 0.16312187620146099)
# gray - gray :  (0.4980392156862745, 0.4980392156862745, 0.4980392156862745)
