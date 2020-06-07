from mpi4py import MPI
import numpy

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

data = numpy.arange(100, dtype=float)
#buffer = numpy.empty(10, dtype=float)

#print(rank, hex(id(data)))
if rank == 0:
	#data = {'a' : 7, 'b': 2.35}
	data[:] = numpy.arange(100, dtype=float)
	#print(hex(id(data)))
	#print("Sending data from ", rank)
	#comm.Send(data, dest=1) #send: flexible, all-purpose routine;
							#Send: use for contiguous memory buffers!
	#tgt, src = 1, 1
	comm.Send([data, 100, MPI.DOUBLE], dest=1)

elif rank==1:
	#data = numpy.empty(100, dtype=float)
	#print("Receiving data in ", rank)
	#comm.Recv(data, source=0)
	#print(hex(id(data)))
	#tgt, src = 0, 0
	comm.Recv([data, 100, MPI.DOUBLE], source=0)

#comm.Sendrecv(data, dest=tgt, recvbuf=buffer, source=src)
print(rank, "data id:", hex(id(data)))
#print(rank, "buffer id:", hex(id(buffer)))
