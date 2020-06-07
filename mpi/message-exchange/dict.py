from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

#data = {'My_rank' : rank}

n=100000
arr = np.full(n, rank, dtype=float)
buff = np.empty(n, dtype=float)

if rank == 0:
	#comm.send(data, dest=1)
	#msg = comm.recv(source=1)
	comm.Send(arr, dest=1)
	comm.Recv(buff, source=1)
elif rank == 1:
	#comm.send(data, dest=0)
	#msg=comm.recv(source=0)
	comm.Recv(buff, source=0) #The ORDER Matters!!
	comm.Send(arr, dest=0)
else:
	errtxt = "You have run this program with more "
	errtxt += "with more than 2 parallel processes."
	errtxt += "Use -np 2 in mpirun. "
	errtxt += "Aborting..."
	raise ValueError(errtxt)

#comm.sendrecv(data, dest=tgt, source=src)
#print("Rank %d received a message from rank %d." % (rank, msg['My_rank']))
print("Rank %d received an array filled with %d %ds." % (rank, len(buff), buff[0]))
