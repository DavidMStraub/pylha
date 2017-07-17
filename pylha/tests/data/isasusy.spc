#  SUSY parameters in Les Houches accord format
#  SPS point 1a
Block MODSEL               # Model selection
    1    1                 #  Minimal supergravity (mSUGRA) model              
Block SMINPUTS             # SM Input parameters
    3    1.188191697E-01   #  alpha_s(M_Z)
    6    1.743000031E+02   #  M_{top}
Block MINPAR               #  Model parameters
    1    1.000000000E+02   #  m_0
    2    2.500000000E+02   #  m_{1/2}
    3    1.000000000E+01   #  tan(beta)
    4    1.000000000E+00   #  sign(mu)
    5   -1.000000000E+02   #  A_0
#  
Block MASS   # Scalar and gaugino mass spectrum
#  PDG code   mass                 particle
         6    1.743000031E+02   #  top            
        25    1.135365829E+02   #  h^0            
        35    3.964976807E+02   #  H^0            
        36    3.936475220E+02   #  A^0            
        37    4.041576538E+02   #  H^+            
   1000001    5.706302490E+02   #  dnl            
   1000002    5.646319580E+02   #  upl            
   1000003    5.706303101E+02   #  stl            
   1000004    5.646336060E+02   #  chl            
   1000005    5.148857422E+02   #  b1             
   1000006    4.018119202E+02   #  t1             
   1000011    2.048680573E+02   #  el-            
   1000012    1.859734192E+02   #  nuel           
   1000013    2.048680573E+02   #  mul-           
   1000014    1.859734192E+02   #  numl           
   1000015    1.345723572E+02   #  tau1           
   1000016    1.850830841E+02   #  nutl           
   1000021    6.117097168E+02   #  glss           
   1000022    9.543494415E+01   #  z1ss           
   1000023    1.816832733E+02   #  z2ss           
   1000024    1.817783661E+02   #  w1ss           
   1000025   -3.563564148E+02   #  z3ss           
   1000035    3.756089478E+02   #  z4ss           
   1000037    3.737724304E+02   #  w2ss           
   2000001    5.479114380E+02   #  dnr            
   2000002    5.482348633E+02   #  upr            
   2000003    5.479114990E+02   #  str            
   2000004    5.482366943E+02   #  chr            
   2000005    5.390317383E+02   #  b2             
   2000006    5.782148438E+02   #  t2             
   2000011    1.431091919E+02   #  er-            
   2000013    1.431092072E+02   #  mur-           
   2000015    2.077922211E+02   #  tau2           
Block ALPHA                     # Alpha
    -1.107271686E-01        
Block HMIX Q= 4.567678528E+02   # Higgs parameters
    1    3.499483948E+02        # mu
Block STOPMIX                   # stop mixing matrix
  1  1    5.378097296E-01
  1  2   -8.430662751E-01
  2  1    8.430662751E-01
  2  2    5.378097296E-01
Block SBOTMIX                   # sbottom mixing matrix
  1  1    9.297426939E-01
  1  2   -3.682098687E-01
  2  1    3.682098687E-01
  2  2    9.297426939E-01
Block STAUMIX                   # stau mixing matrix
  1  1    2.526287735E-01
  1  2   -9.675632715E-01
  2  1    9.675632715E-01
  2  2    2.526287735E-01
Block NMIX                      # neutralino mixing matrix
  1  1    9.867345095E-01
  1  2   -5.358754843E-02
  1  3    1.438069195E-01
  1  4   -5.294487253E-02
  2  1   -9.951802343E-02
  2  2   -9.437011480E-01
  2  3    2.729507387E-01
  2  4   -1.581837982E-01
  3  1   -5.851639062E-02
  3  2    8.841120452E-02
  3  3    6.959396601E-01
  3  4    7.102304697E-01
  4  1   -1.141367853E-01
  4  2    3.142290115E-01
  4  3    6.484485269E-01
  4  4   -6.839206219E-01
Block UMIX                      # chargino U mixing matrix
  1  1   -9.101191759E-01
  1  2    4.143465161E-01
  2  1   -4.143465161E-01
  2  2   -9.101191759E-01
Block VMIX                      # chargino V mixing matrix
  1  1   -9.709569812E-01
  1  2    2.392542213E-01
  2  1   -2.392542213E-01
  2  2   -9.709569812E-01
Block GAUGE Q= 4.567678528E+02  # DRbar gauge couplings
    1    3.575287759E-01   # g`
    2    6.526660323E-01   # g_2
    3    1.221935272E+00   # g_3
Block YU Q= 4.567678528E+02 
  3  3    8.864250779E-01   # y_t
Block YD Q= 4.567678528E+02
  3  3    1.354373097E-01   # y_b
Block YE Q= 4.567678528E+02 
  3  3    1.003626511E-01   # y_tau
Block AU Q= 4.567678528E+02
  3  3   -4.996444397E+02   # A_t
Block AD Q= 4.567678528E+02 
  3  3   -7.677929688E+02   # A_b
Block AE Q= 4.567678528E+02 
  3  3   -2.533071442E+02   # A_tau
Block SPINFO   # Program information
    1                                ISASUGRA   # Spectrum Calculator
    2    ISAJET     V7.67p  30-MAY-2003 19:26   # Version number
