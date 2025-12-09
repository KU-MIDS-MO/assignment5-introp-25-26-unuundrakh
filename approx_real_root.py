import numpy as np
def approx_real_root(coeffs, interval):
   a, b = interval
   
   roots = np.roots(coeffs[::-1])
   
   real_roots = np.real(roots[np.isclose(roots.imag, 0, atol=1e-12)])
   
   for r in real_roots:
       if a < r < b:
           return float(r)
       
   
   
   

