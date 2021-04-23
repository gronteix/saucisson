import math
import numpy as np
import os

def image_cutter(
    original_image,
    max_image_size = 300,
    cut_in_z_direction = False):
    
    multi_matrix = []
    codex = []
        
    if not cut_in_z_direction:
        
        for n_x in range(math.ceil(original_image.shape[1]/max_image_size)):
            
            for n_y in range(math.ceil(original_image.shape[2]/max_image_size)):
                
                multi_matrix.append(original_image[:,n_x*max_image_size:(n_x+1)*max_image_size, n_y*max_image_size:(n_y+1)*max_image_size])
                                
                codex.append((n_x, n_y))

        return multi_matrix, codex
    
    else:
        
        for n_z in range(math.ceil(original_image.shape[0]/max_image_size)):
        
            for n_x in range(math.ceil(original_image.shape[1]/max_image_size)):

                for n_y in range(math.ceil(original_image.shape[2]/max_image_size)):

                    multi_matrix.append(original_image[n_z*max_image_size:(n_z+1)*max_image_size, n_x*max_image_size:(n_x+1)*max_image_size, n_y*max_image_size:(n_y+1)*max_image_size])
                    codex.append((n_z, n_x, n_y))
    
    return multi_matrix, codex

def image_recompose(
    multi_segmented_matrix,
    original_image,
    max_image_size,
    codex,
    cut_in_z_direction = False):
    
    reconstructed_image = np.zeros(np.shape(original_image))
        
    if not cut_in_z_direction:

        for plane, n in zip(multi_segmented_matrix, codex):
            
            n_x, n_y = n

            reconstructed_image[:, n_x*max_image_size:(n_x+1)*max_image_size, n_y*max_image_size:(n_y+1)*max_image_size] = plane
            
    else:

        for plane, n in zip(multi_segmented_matrix, codex):

            n_z, n_x, n_y = n

            reconstructed_image[n_z*max_image_size:(n_z+1)*max_image_size, n_x*max_image_size:(n_x+1)*max_image_size, n_y*max_image_size:(n_y+1)*max_image_size] = plane

    return reconstructed_image