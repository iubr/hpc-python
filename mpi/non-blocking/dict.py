from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

#data = {'My_rank' : rank}

N=1267
arr = np.full(N, rank, dtype=float)
buff = np.empty(N, dtype=float)

if rank == 0:
	req = comm.Isend(arr, dest=1)
	#comm.Irecv(buff, source=1)
	S = 0
	for i in range(N):
		S += arr[i]
	req.wait()
elif rank == 1:
	req=comm.Irecv(buff, source=0)
	S = 0
	for i in range(N):
		S += arr[i]
	req.wait()
else:
	errtxt = "You have run this program with more "
	errtxt += "with more than 2 parallel processes."
	errtxt += "Use -np 2 in mpirun. "
	errtxt += "Aborting..."
	raise ValueError(errtxt)

#comm.sendrecv(data, dest=tgt, source=src)
#print("Rank %d received a message from rank %d." % (rank, msg['My_rank']))
print("Rank %d received an array filled with %d %ds." % (rank, len(buff), buff[0]))
