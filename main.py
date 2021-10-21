from linkbudget import LinkBudget


def printAll(case):
    print("\nAll variables in dB:\n")
    print(f"P={case.P}")
    print(f"L_l={case.L_l}")
    print(f"G_t={case.G_t}")
    print(f"L_a={case.L_a}")
    print(f"G_r={case.G_r}")
    print(f"L_s={case.L_s}")
    print(f"L_pr={case.L_pr}")
    print(f"L_r={case.L_r}")
    print(f"1/R={case.R_inv}")
    print(f"1/T_s={case.T_s_inv}")


# samplecase = LinkBudget(True, 2, 0, 0.8, 0.8, 2.5, 1, 0.5, 10, 570, 0, 0.25, 0,
#                         6371e3, 5.972e24, 149597871e3, 0, 0, 0, 50, 2, 1e-6)

case1down = LinkBudget(True, 150, 400, 0.8, 0.7, 2.2, 221 / 240, 1, 15, 820, 0, 0.12, 1e8,
                       6371e3, 5972e21, 149597871e3, 45, 0.01, 32, 100, 0.5, 1e-6)
case1up = LinkBudget(False, 150, 400, 0.8, 0.7, 2.2, 221 / 240, 1, 15, 820, 0, 0.12, 1e8,
                       6371e3, 5972e21, 149597871e3, 45, 0.01, 32, 100, 0.5, 1e-6)

case = case1down

if __name__ == '__main__':
    print(f"The received SNR is {case.SNR} dB")
    print(f"The margin is {case.margin} dB")
    if case.margin > 3:
        print("The budget link closes!")
    else:
        print("The link budget doesn't close.")

    # printAll(case)

