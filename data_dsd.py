#These are from http://www.helsinki.fi/~mleskine/sateet/RD69.html
disdro_D = array([0.3671, 0.4643, 0.5611, 0.6667, 0.7822, 0.9245, 1.1275, 
                  1.3424, 1.5171, 1.6759, 1.9227, 2.2695, 2.5945, 2.8797, 
                  3.2091, 3.5557, 3.9284, 4.3634, 4.8738, 5.3892])
disdro_dD = array([0.0932, 0.1010, 0.0917, 0.1196, 0.1123, 0.1722, 0.2329,
                   0.1968, 0.1528, 0.1658, 0.3287, 0.3639, 0.2861, 0.2843,
                   0.3745, 0.3196, 0.4239, 0.4471, 0.5735, 0.4563])
disdro_V = array([1.4702, 1.9005, 2.3074, 2.7331, 3.1948, 3.7564, 4.4181,
                  5.0182, 5.4520, 5.8193, 6.3375, 7.0271, 7.5608, 7.9154,
                  8.2681, 8.5640, 8.7901, 8.9693, 9.0791, 9.1400])
                   
disdro_min = disdro_D - 0.5*disdro_dD

rho_0 = 1.225 #sea level air density, from http://www.aviation.ch/tools-atmosphere.asp
rho_h = 1.218 #density at 56 m, same source
rho_w = 1000.0

#Disdrometer sampling area, from 
#"RAINDROP SIZE DISTRIBUTION OVER NORTHEASTERN COAST OF BRAZIL"
disdro_A = 0.0050 

dT = 60.0 #disdrometer sampling time, seconds
