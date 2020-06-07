from mpi4py import MPI
import numpy
from sys import stdout

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

assert size == 4, 'Number of MPI tasks has to be 4.'

#if rank == 0:
#    print('First collective:')

if rank == 0:
    data = numpy.arange(0,8,1)
else:
    data = numpy.empty(8, int)    
comm.Bcast(data, 0) 
#print('  Task {0}: {1}'.format(rank, data))


# Prepare data vectors ..
data += rank*8  
buff = numpy.full(8, -1, int)

# ... wait for every rank to finish ...
#stdout.flush
#comm.barrier()
if rank == 0:
    print('')
    print('-' * 32)
    print('')
    print('Start:')
    print('  Task {0}: {1}'.format(rank, data))
#comm.barrier()
##if rank == 0:
##    print('')
##    print('Gather')
##comm.Gather(data[0:2], buff, root=1)
##
##print('  Task {0}: {1}'.format(rank, buff))

# ... wait for every rank to finish ...
buff[:] = -1
stdout.flush()
comm.barrier()
if rank == 0:
    print('')
    print('Reduce:')

# Calculate partial sums using two communicators
color = rank // 2
sub_comm = comm.Split(color)
sub_comm.Reduce(data, buff, op=MPI.SUM, root=0)
print('  Task {0}: {1}'.format(rank, buff))

###
#### ... wait for every rank to finish ...
###buff[:] = -1
###comm.barrier()
##if rank == 0:
###    print('')
###    print('d)')
###
#### TODO: how to get the desired receive buffer using a single collective
####       communication routine?
###
###...
###print('  Task {0}: {1}'.format(rank, buff))
###
#### ... wait for every rank to finish ...
###buff[:] = -1
###comm.barrier()
###if rank == 0:
###    print('')
###    print('e)')
###
#### TODO: how to get the desired receive buffer using a single collective
####       communication routine?
###...
###print('  Task {0}: {1}'.format(rank, buff))
###
