# MPI

## Process spatially related data on the same UE (Units of execution)

- moving data around takes time and causes latency
- 

## MPI RUN

[https://www.open-mpi.org/doc/current/man1/mpirun.1.php](https://www.open-mpi.org/doc/current/man1/mpirun.1.php)

## run multiple programms

```shell
mpirun -np 2 a.out : -np 2 b.out
```

- Runs in total 4 processes 

- Runs 2 processes for a.out with rank 0-1
- Runs 2 processes for b.out with rank 2-3


## Test Status non blocking

```c
#include <mpi.h>
#include <stdio.h>

int main(int argc, char *argv[]) {
    MPI_Init(&argc, &argv);

    int rank, size;
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);

    int data = rank;
    MPI_Request request;
    MPI_Status status;

    if (rank == 0) {
        // Initiate a non-blocking send
        MPI_Isend(&data, 1, MPI_INT, 1, 0, MPI_COMM_WORLD, &request);

        int flag = 0;
        while (!flag) {
            // Do some work here...
            printf("Rank 0 is doing some work while waiting for send to complete\n");

            // Check if the send is complete
            MPI_Test(&request, &flag, &status);
        }

        printf("Rank 0: Send completed\n");
    } else if (rank == 1) {
        // Initiate a blocking receive
        MPI_Recv(&data, 1, MPI_INT, 0, 0, MPI_COMM_WORLD, &status);
        printf("Rank 1: Received data = %d\n", data);
    }

    MPI_Finalize();
    return 0;
}
```

## Element-wise reduction

### On the root process

```c
#include <mpi.h>

int MPI_Reduce(const void *sendbuf, void *recvbuf, int count,
               MPI_Datatype datatype, MPI_Op op, int root, MPI_Comm comm);
```

### Distributed on many systems


```c
#include <mpi.h>

int MPI_Allreduce(const void *sendbuf, void *recvbuf, int count,
                  MPI_Datatype datatype, MPI_Op op, MPI_Comm comm);
```