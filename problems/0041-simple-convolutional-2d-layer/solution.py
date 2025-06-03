import numpy as np

def simple_conv2d(input_matrix: np.ndarray, kernel: np.ndarray, padding: int, stride: int):
  input_height, input_width = input_matrix.shape
  kernel_height, kernel_width = kernel.shape
  if padding > 0:
    input_matrix = np.pad(input_matrix, ((padding, padding), (padding, padding)), 'constant', constant_values=0)
    # input_height, input_width = input_matrix.shape
  output_height = (input_height - kernel_height + 2 * padding) // stride + 1
  output_width = (input_width - kernel_width + 2 * padding) // stride + 1

  output_matrix = np.zeros((output_height, output_width))
  padded_height, padded_width = input_matrix.shape
  for i in range(output_height):
      if i*stride + kernel_height > padded_height:
          continue
      for j in range(output_width):
          if j*stride + kernel_width > padded_width:
              continue
          output_matrix[i, j] = np.sum(input_matrix[i*stride:i*stride+kernel_height, j*stride:j*stride+kernel_width