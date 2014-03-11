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
  inf = 0.0
  try:
    with mosek.Env() as env:
      env.set_Stream (mosek.streamtype.log, streamprinter)
      with env.Task(0,0) as task:
        task.set_Stream (mosek.streamtype.log, streamprinter)


        # Given - to include as paramters to this function once it is abstracted
        m = 2 
        tf = [ 1,2 ]
        theta = [ 0.5,0.5,0.5,0.5 ]
        s = { 1,2 }

        
        # numvar = 6
        numvar = len(s)

        # numcon = 5
        numcon = 1
      

        # bkc = [ mosek.boundkey.up, 
        #         mosek.boundkey.fx, 
        #         mosek.boundkey.fx, 
        #         mosek.boundkey.fx, 
        #         mosek.boundkey.fx ]
        # blc = [ 1.0, 0.0, 0.0, 1.3862944, 0.0 ]
        # buc = [ 0.0, 0.0, 0.0, 1.3862944, 0.0 ]

        bkc = [ mosek.boundkey.ra]
        blc = [ 1.0]
        buc = [ 1.0]

        # bkx = [ mosek.boundkey.fr ] * numvar
        # blx = [ 0.0 ] * numvar
        # bux = [ 0.0 ] * numvar

        bkx = [ mosek.boundkey.lo ] * numvar
        blx = [ 0.0 ] * numvar
        bux = [ +inf ] * numvar


        # Below is the sparse representation of the A 
        # matrix stored by column.  
        # asub = [ array([0, 1]), 
        #          array([0, 1, 2]), 
        #          array([0, 1]), 
        #          array([1, 2])] 
        # aval = [ array([3.0, 2.0]), 
        #          array([1.0, 1.0, 2.0]), 
        #          array([2.0, 3.0]), 
        #          array([1.0, 3.0]) ] 

        # A matrix as one constraint over numvar variables
        asub = range(numvar)
        aval = [1.0] * numvar
        
        # task.appendvars(numvar)
        # task.appendcons(numcon)

        task.appendvars(numvar)
        task.appendcons(numcon)

        # task.putobjsense(mosek.objsense.maximize)

        task.putobjsense(mosek.objsense.maximize)

        # task.putboundslice(mosek.accmode.var, 0, numvar, bkx, blx, bux)
        # task.putboundslice(mosek.accmode.con, 0, numcon, bkc, blc, buc)

        task.putboundslice(mosek.accmode.var, 0, numvar, bkx, blx, bux)
        task.putboundslice(mosek.accmode.con, 0, numcon, bkc, blc, buc)

        # task.putarowlist(asubi, aptrb, aptre, asubj, aval )

        task.putarow(0,asub,aval)

        # opro  = [ mosek.scopr.pow, mosek.scopr.pow ]
        # oprjo = [ 2, 3 ]
        # oprfo = [ 1.0, 1.0 ]
        # oprgo = [ 1.0, 1.0 ]
        # oprho = [ 0.0, 0.0 ]

        opro  = [ mosek.scopr.log ] * (m * len(s))
        oprjo = range(len(s)) * m
        oprfo = [ tf[i] for i in sorted(range(m) * len(s)) ]
        oprgo = theta
        oprho = [ 0.0 ] * (m * len(s))

        # oprc  = [ mosek.scopr.pow, mosek.scopr.pow ]
        # opric = [ 0, 0 ]
        # oprjc = [ 4, 5 ]
        # oprfc = [ 1.0, 1.0 ]
        # oprgc = [ 1.0, 1.0 ]
        # oprhc = [ 0.0, 0.0 ]

        oprc  = []
        opric = []
        oprjc = []
        oprfc = []
        oprgc = []
        oprhc = []

        task.putSCeval(opro, oprjo, oprfo, oprgo, oprho,
                       oprc, opric, oprjc, oprfc, oprgc, oprhc)

        task.optimize()

        res = [ 0.0 ] * numvar
        task.getsolutionslice( mosek.soltype.itr, mosek.solitem.xx, 0, numvar, res)

        print ( "Solution is: %s" % res )
  except NameError, e:
    print(e)
      
main()

