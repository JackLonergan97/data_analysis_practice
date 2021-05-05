import library
import argparse

parser = argparse.ArgumentParser(description = 'Choose number of MCMC runs')
parser.add_argument('runs', type = int, help = 'Number of iterations in the MCMC algorithm')
args = parser.parse_args()

ID = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
x = [201, 244, 47, 287, 203, 58, 210, 202, 198, 158, 165, 201, 157, 131, 166, 160, 186, 125, 218, 146]
y = [592, 401, 583, 402, 495, 173, 479, 504, 510, 416, 393, 442, 317, 311, 400, 337, 423, 334, 533, 344]
sigma_y = [61, 25, 38, 15, 21, 15, 27, 14, 30, 16, 14, 25, 52, 16, 34, 31, 42, 26, 16, 22]
sigma_x = [9, 4, 11, 7, 5, 9, 4, 4, 11, 7, 5, 5, 5, 6, 6, 5, 9, 8, 6, 5]
rho_xy = [-0.84, 0.31, 0.64, -0.27-0.33, 0.67, -0.02, -0.05, -0.84, -0.69, 0.30, -0.46, -0.03, 0.50, 0.73, -0.52, 0.90, 0.40, -0.78, -0.56]
data = [ ID, x, y, sigma_x, sigma_y, rho_xy]

L, params = library.MCMC(0.5, 200, 0.1, 1, 1, data, n = args.runs)
library.Figures(params)

