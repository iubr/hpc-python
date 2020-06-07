from mpi4py import MPI
import mpi4py

#print(mpi4py.get_config())
comm = MPI.COMM_WORLD

size = comm.Get_size()
rank = comm.Get_rank()

print("I am rank %d in group of %d processes" % (rank, size))
