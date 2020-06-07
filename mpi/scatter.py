from mpi4py import MPI
from numpy import arange, empty

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()
if rank == 0:
    py_data = range(size)
    data = arange(size**2, dtype=float)
    print("Original data", data)
else:
    py_data = None
    data = None

new_data = comm.scatter(py_data, root=0)  # returns the value

buffer = empty(size, float)         # prepare a receive buffer
comm.Scatter(data, buffer, root=0)  # in-place modification

print(rank, buffer)
new = 0.5*buffer
newbuffer = empty(size**2, dtype=float)

comm.Gather(new, newbuffer, root=0)
if rank==0:
    print("Modified data:")
    print(newbuffer)
