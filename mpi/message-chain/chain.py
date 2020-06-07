import numpy as np
from mpi4py import MPI

comm = MPI.COMM_WORLD
myid = comm.Get_rank()
ntasks = comm.Get_size()

N = 1250
data = np.full(N, myid, dtype=int) 
buff = np.empty(N, dtype=int)

if myid < ntasks-1:
	comm.Send(data, dest=myid+1)
	print("Rank %d sent %d elements to %d." % (myid, N, myid+1))
if myid > 0:
	comm.Recv(buff, source=myid-1)
	print("Rank %d received a bunch of %ds." % (myid, buff[0]))
