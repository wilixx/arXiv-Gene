# Outlines a method for solving the convex optimization problem in
# shaparenko and joachims 07.
# Derivied and modified from the scopt example demb781.py from mosek
#
#
########## len pi = |S| #############################
# pi = [Real_1,...Real_|S|]
#
########## m log terms ##############################
# max over pi [tfn_1 * (pi dot x^1) + ... + tfn_m * (pi dot x^m)]
# 
########## |S| + 1 varaible constraints #############
# pi_1 >= 0
# .
# .
# .
# pi_|s|
# sum over elements of pi = 1
#

from __future__ import with_statement

import sys

import mosek

def streamprinter(text):
    sys.stdout.write(text)
    sys.stdout.flush()

def main ():

  try:
    with mosek.Env() as env:
      env.set_Stream (mosek.streamtype.log, streamprinter)
      with env.Task(0,0) as task:
        task.set_Stream (mosek.streamtype.log, streamprinter)
        
        # numvar = 6
        # numcon = 5
      

        # bkc = [ mosek.boundkey.up, 
        #         mosek.boundkey.fx, 
        #         mosek.boundkey.fx, 
        #         mosek.boundkey.fx, 
        #         mosek.boundkey.fx ]
        # blc = [ 1.0, 0.0, 0.0, 1.3862944, 0.0 ]
        # buc = [ 0.0, 0.0, 0.0, 1.3862944, 0.0 ]

        # bkx = [ mosek.boundkey.fr ] * numvar
        # blx = [ 0.0 ] * numvar
        # bux = [ 0.0 ] * numvar

        # aptrb = [ 0, 0, 3, 6, 8 ]
        # aptre = [ 0, 3, 6, 8, 10 ]
        # asubi = [ 0, 1, 2, 3, 4 ]
        # asubj = [ 0, 1, 2,
        #           0, 1, 3,
        #           0, 4,
        #           1, 5 ] 
        # aval  = [  1.0,  1.0, -1.0,
        #           -1.0, -1.0, -1.0,
        #            0.5, -1.0,
        #            1.0, -1.0 ]
        
        # task.appendvars(numvar)
        # task.appendcons(numcon)

        # task.putobjsense(mosek.objsense.maximize)

        # task.putboundslice(mosek.accmode.var, 0, numvar, bkx, blx, bux)
        # task.putboundslice(mosek.accmode.con, 0, numcon, bkc, blc, buc)

        # task.putarowlist(asubi, aptrb, aptre, asubj, aval )

        # opro  = [ mosek.scopr.pow, mosek.scopr.pow ]
        # oprjo = [ 2, 3 ]
        # oprfo = [ 1.0, 1.0 ]
        # oprgo = [ 1.0, 1.0 ]
        # oprho = [ 0.0, 0.0 ]


        # oprc  = [ mosek.scopr.pow, mosek.scopr.pow ]
        # opric = [ 0, 0 ]
        # oprjc = [ 4, 5 ]
        # oprfc = [ 1.0, 1.0 ]
        # oprgc = [ 1.0, 1.0 ]
        oprhc = [ 0.0, 0.0 ]

        task.putSCeval(opro, oprjo, oprfo, oprgo, oprho,
                       oprc, opric, oprjc, oprfc, oprgc, oprhc)

        task.optimize()

        res = [ 0.0 ] * numvar
        task.getsolutionslice(
          mosek.soltype.itr,
          mosek.solitem.xx,
          0, numvar,
          res)

        print ( "Solution is: %s" % res )
  except NameError, e:
    print(e)
      
main()

