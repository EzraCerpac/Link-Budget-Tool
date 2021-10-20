from math import *

class DownlinkBudget():
    def __init__(self, P_sc, P_gs, L_l, L_r, f_d, turnaround_ratio, D_sc, D_gs, h, e_t_sc, e_t_gs, DR_u,

                 swath_width_angle, pixel_size, bits_per_pixel, D_c, T_DL, BER_req):
        self.P = 10*log10(P_sc)  # dBW


    def reveivedSNR(self):
        return