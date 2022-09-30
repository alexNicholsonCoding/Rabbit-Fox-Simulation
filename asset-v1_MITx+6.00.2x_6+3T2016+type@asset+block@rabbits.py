import random
import pylab
import numpy as np

# Global Variables
MAXRABBITPOP = 1000
CURRENTRABBITPOP = 50
CURRENTFOXPOP = 300

def rabbitGrowth():
    """ 
    rabbitGrowth is called once at the beginning of each time step.

    It makes use of the global variables: CURRENTRABBITPOP and MAXRABBITPOP.

    The global variable CURRENTRABBITPOP is modified by this procedure.

    For each rabbit, based on the probabilities in the problem set write-up, 
      a new rabbit may be born.
    Nothing is returned.
    """
    # you need this line for modifying global variables
    global CURRENTRABBITPOP
    NEWRABBITPOP = CURRENTRABBITPOP

    for rabbit in range(CURRENTRABBITPOP):
        if random.random() < 1-(CURRENTRABBITPOP/MAXRABBITPOP):
            NEWRABBITPOP += 1
    CURRENTRABBITPOP = NEWRABBITPOP
    return
            
def foxGrowth():
    """ 
    foxGrowth is called once at the end of each time step.

    It makes use of the global variables: CURRENTFOXPOP and CURRENTRABBITPOP,
        and both may be modified by this procedure.

    Each fox, based on the probabilities in the problem statement, may eat 
      one rabbit (but only if there are more than 10 rabbits).

    If it eats a rabbit, then with a 1/3 prob it gives birth to a new fox.

    If it does not eat a rabbit, then with a 1/10 prob it dies.

    Nothing is returned.
    """
    # you need these lines for modifying global variables
    global CURRENTRABBITPOP
    global CURRENTFOXPOP
    NEWFOXPOP = CURRENTFOXPOP

    for fox in range(CURRENTFOXPOP):
        if random.random() < CURRENTRABBITPOP/MAXRABBITPOP:
            if CURRENTRABBITPOP > 10:
                CURRENTRABBITPOP -= 1
            if random.random() < 1/3:
                NEWFOXPOP += 1


        else:
            if random.random() > 1/10:
                if NEWFOXPOP > 10:
                    NEWFOXPOP -= 1
    CURRENTFOXPOP = NEWFOXPOP

    return
    
            
def runSimulation(numSteps):
    """
    Runs the simulation for `numSteps` time steps.

    Returns a tuple of two lists: (rabbit_populations, fox_populations)
      where rabbit_populations is a record of the rabbit population at the 
      END of each time step, and fox_populations is a record of the fox population
      at the END of each time step.

    Both lists should be `numSteps` items long.
    """
    rabbit_populations = []
    fox_populations = []
    for step in range(numSteps):
        rabbitGrowth()
        foxGrowth()
        rabbit_populations.append(CURRENTRABBITPOP)
        fox_populations.append(CURRENTFOXPOP)
    pops_tuple = (rabbit_populations, fox_populations)
    x_list = list(range(0, numSteps))
    y_list = list(range(0, numSteps))

    #pylab.plot(x_list, rabbit_populations)
    pylab.plot(x_list, fox_populations)
    pylab.show()

    coeff  = np.polyfit(x_list, fox_populations, 2)
    print(coeff)
    pylab.plot(pylab.polyval(coeff, range(len(fox_populations))))
    pylab.show()

    coeff2 = np.polyfit(x_list, rabbit_populations, 2)
    print(coeff2)
    pylab.plot(pylab.polyval(coeff2, range(len(rabbit_populations))))
    pylab.show()
    return pops_tuple

print(runSimulation(200))