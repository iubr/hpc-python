import numpy as np
from mpi4py import MPI

comm = MPI.COMM_WORLD
myid = comm.Get_rank()
ntasks = comm.Get_size()

N = 1267
data = np.full(N, myid, dtype=int)
buff = np.empty(N, dtype=int)

tgt = myid + 1
src = myid - 1

if tgt >= ntasks:
	tgt = MPI.PROC_NULL
if src < 0:
	src = MPI.PROC_NULL

req = []
req.append(comm.Isend(data, dest=tgt))
req.append(comm.Irecv(buff, source=src))
if src != MPI.PROC_NULL:
	print(" Rank %d received a bunch of %ds from %d." % (myid, buff[0], src))
if tgt != MPI.PROC_NULL:
	print(" Rank %d sent %d elements to %d." % (myid, N, tgt))

MPI.Request.waitall(req)
