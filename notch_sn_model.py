from pysb.core import *
from pysb.integrate import *
import matplotlib.pyplot as plt
import numpy as np
from pysb.integrate import ScipyOdeSimulator as SOS
from pysb.bng import generate_equations

Model()
Monomer('NOTCH3', ['dll4', 'jag2'])
Monomer('DLL4', ['notch3'])
Monomer('JAG2', ['notch3'])
Monomer('NICD', ['rbpj'])
Monomer('RBPJ', ['nicd'])
Monomer('HES1', ['dimer'])
Monomer('DIMER', ['hes1'])
Monomer('HCM', ['e'])
Monomer('HNP', ['hes6'])
Monomer ('HES6', ['hnp'])
Monomer ('ENZM', ['m'])

Parameter('kf', 1e-2)
Parameter('kr', 1e-4)
Parameter('kc', 1)
Parameter('NOTCH3_0', 270)
Parameter('JAG2_0', 1500)
Parameter('DLL4_0', 2000)
Parameter('NICD_0', 100)
Parameter('RBPJ_0', 430)
Parameter('DIMER_0', 0)
Parameter('HES1_0', 1)
Parameter('HCM_0', 1)
Parameter('HNP_0', 130)
Parameter('HES6_0', 50)
Parameter('ENZM_0', 50)

Initial(NOTCH3(dll4 = None, jag2 = None), NOTCH3_0)
Initial(JAG2(notch3 = None), JAG2_0)
Initial(DLL4(notch3 = None),DLL4_0)
Initial(NICD(rbpj = None),NICD_0)
Initial(RBPJ(nicd = None),RBPJ_0)
Initial(HES1(dimer = None),HES1_0)
Initial(DIMER(hes1 = None),DIMER_0)
Initial(HCM(e = None),HCM_0)
Initial(HNP(hes6 = None),HNP_0)
Initial(HES6(hnp = None),HES6_0)
Initial(ENZM(m = None),ENZM_0)  

Rule('jag_binds_notch', JAG2(notch3 = None) + NOTCH3(dll4 = None, jag2 = None) |
     JAG2(notch3 = 1) % NOTCH3(dll4 = None, jag2 = 1), kf, kr)
Rule('dll_binds_notch', DLL4(notch3 = None) + NOTCH3(dll4 = None, jag2 = None) |
     DLL4(notch3 = 2) % NOTCH3(dll4 = 2, jag2 = None), kf, kr)

Rule('nicd_catalysis_j', JAG2(notch3 = 1) % NOTCH3(dll4 = None, jag2 = 1) >> NOTCH3(dll4 = None, jag2 = None) + JAG2(notch3 = None) + NICD(rbpj = None), kc)
Rule('nicd_catalysis_d', DLL4(notch3 = 2) % NOTCH3(dll4 = 2, jag2 = None) >> NOTCH3(dll4 = None, jag2 = None) + DLL4(notch3 = None) + NICD(rbpj = None), kc)

        
Rule('nicd_binds_rbpj', NICD(rbpj = None) + RBPJ(nicd = None) >> DIMER(hes1 = None) + NICD(rbpj = None) + RBPJ(nicd = None), kc)
Rule('hes1_activation', HES1(dimer = None) + DIMER(hes1 = None) |
     HES1(dimer = 1) % DIMER(hes1 = 1), kf, kr)

Rule('hcm_synth', HES1(dimer = None) >> HCM(e = None) + HES1(dimer = None), kf)
Rule('hnp_synth', HCM(e = None) >> HCM(e = None) + HNP(hes6 = None), kf)

Rule('hcm_deg_complex', HCM(e = None) + ENZM(m = None) |
     HCM(e = 3) % ENZM(m = 3), kf, kr)
Rule('hcm_deg', HCM(e = 3) % ENZM (m = 3) >> ENZM(m = None), kf)

Rule('hnp_deg_complex', HNP(hes6 = None) + HES6(hnp = None) |
     HNP(hes6 = 4) % HES6(hnp = 4), kf, kr)
Rule('hnp_deg', HNP(hes6 = 4) % HES6 (hnp = 4) >> HES6(hnp = None), kf)

Observable('NICD_obs', NICD(rbpj = None))

generate_equations(model)