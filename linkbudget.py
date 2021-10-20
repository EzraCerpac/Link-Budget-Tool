from math import *

class DownlinkBudget():
    def __init__(self, P_sc, P_gs, L_l, L_r, f_d, turnaround_ratio, D_sc, D_gs, h, theta_ES, e_t_sc, DR_u,
                 r_plan, M_plan, d_S,
                 swath_width_angle, pixel_size, B_p, D_C, T_DL, BER_req):
        # Assumptions
        self.eta = 0.55  # if parabolic
        d_E = 149597871000  # m (Earth-Sun distance)

        # Down specific
        self.f = f_d  # GHz
        D_t = D_sc
        D_r = D_gs
        e_t_t = e_t_sc
        e_t_r = 0

        # Transmitter Power
        self.P = 10 * log10(P_sc)  # dBW

        # System Noise Temperature
        self.T_s = 135  # K
        self.T_s_inv = 10 * log10(1 / self.T_s)  # dBK^-1

        # Transmission Path Loss
        self.L_a = 4e-2  # dB

        # Downlink Data Rate
        S_W = 2 * tan(swath_width_angle / 2) * h  # m
        P_S = 2 * tan(pixel_size / 60 / 2) * h  # m
        V = sqrt(6.673e-11 * M_plan / (r_plan + h))  # m/s
        self.R_G = B_p * S_W * V / P_S ** 2  # b/s
        self.R = self.R_G * D_C / T_DL  # b/s
        self.R_inv = 10 * log10(1 / self.R)  # dB(b/s)^-1

        # Distance spacecraft-ground station (worst-case, zero elevation)
        if abs(d_S - d_E) > 5:
            print("not around Earth")
            self.S = sqrt(d_E ** 2 + d_S ** 2 - 2 * d_E * d_S * cos(theta_ES))
        else:
            print("around Earth")
            self.S = sqrt((r_plan + h) ** 2 - r_plan ** 2)

        # Signal wavelength and space loss
        self.wavelength = 299792458 / (self.f * 1e9)  # m
        self.L_s = 10 * log10((self.wavelength / (4 * pi * self.S)) ** 2)  # dB

        # Transmitting/receiving antenna gains
        self.G_t = 20 * log10(D_t) + 20 * log10(self.f) + 17.8  # dB
        self.G_r = (pi * D_r / self.wavelength) ** 2 * self.eta  # dB

        # Transmitting/receiving antenna half-power angles
        alpha_half_t = 21 / (self.f * D_t)  # deg
        alpha_half_r = 21 / (self.f * D_r)  # deg

        # Transmitting/receiving antenna pointing losses
        self.L_pr_t = -12 * (e_t_t / alpha_half_t) ** 2  # dB
        self.L_pr_r = -12 * (e_t_r / alpha_half_r) ** 2  # dB
        self.L_pr = self.L_pr_t + self.L_pr_r  # dB

        # Budget
        self.E_b_over_N_0 = self.P + 10 * log10(L_l) + self.G_t + self.L_a + self.G_r + self.L_s + self.L_pr \
                            + 10 * log10(L_r) + 228.6 + self.R_inv + self.T_s_inv
        # self.BER =

    def reveivedSNR(self):
        return


class UplinkBudget():
    def __init__(self, P_sc, P_gs, L_l, L_r, f_d, turnaround_ratio, D_sc, D_gs, h, e_t_sc, e_t_gs, DR_u,
                 swath_width_angle, pixel_size, bits_per_pixel, D_c, T_DL, BER_req):
        self.P = 10 * log10(P_gs)  # dBW
        self.T_s = 614  # K

    def reveivedSNR(self):
        return
