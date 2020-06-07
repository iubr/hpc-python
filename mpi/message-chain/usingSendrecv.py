import numpy as np
from mpi4py import MPI

comm = MPI.COMM_WORLD
myid = comm.Get_rank()
ntasks = 5

N = 1267
data = np.full(N, myid, dtype=int)
buff = np.empty(N, dtype=int)

tgt = myid + 1
src = myid - 1

if myid == 0:
	comm.Send(data, dest=tgt)
	print(" Rank %d sent %d elements to %d." % (myid, N, tgt))
elif myid == ntasks-1:
	comm.Recv(buff, source=src)
	print(" Rank %d received a bunch of %ds from %d." % (myid, buff[0], src))
else:
	comm.Sendrecv(data, dest=tgt, recvbuf=buff, source=src)
	print(" Rank %d sent %d elements to %d." % (myid, N, tgt))
	print(" Rank %d received a bunch of %ds from %d." % (myid, buff[0], src))
