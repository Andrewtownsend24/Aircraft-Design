# weight transport
'''
def get_wing_weight_transport(Sw, Wfw, AR_w,sweep, q, taper_ratio, t_c, W0):
    W_w=0.036*(Sw**.758)*(Wfw**.0035) * \
        ((AR_w / (np.cos(sweep*(180/np.pi)**2)))**2) * \
        (q**.006) * (taper_ratio**.04) * (((100 * t_c) / (np.cos(sweep * (180 / np.pi))))**-0.3) * \
        (Nz * WO)**0.49
'''