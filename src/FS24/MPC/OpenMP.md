# OpenMP - Open Multi-Processing

- Operates on top of an OS
- Supports a shared memory model
- Opens – per directive - a team of threads to parallelise code sections - Operates according to the Fork-Join pattern
master thread

## omp_get_thread_num()

- retreive the unique integer of the currently executing thread within the parallel region
- starting from 0


## Run with as many threads as possible

```c
#pragma omp parallel
{
    // Code to be executed in parallel
    printf("Hello, world! I'm thread %d\n", omp_get_thread_num());
}
```

## Run multiple sections in parallel


```c
#pragma omp parallel sections
{
    #pragma omp section
    {
        for (i = 0; i <= maxval; i++) {
            do_some_work_here
        }
    }

    #pragma omp section
    {
        for (i = 0; i <= maxval; i++) {
            do_some_other_work_here
        }
    }
}
```

## Statememts

### Run for loop 

```c
#include <stdio.h>
#include <omp.h>

int main() {
    #pragma omp parallel
    {
        #pragma omp for
        for (int i = 0; i < 10; i++) {
            printf("Thread %d is processing iteration %d\n", omp_get_thread_num(), i);
        }
    }
    return 0;
}
```

### Lock

A lock is used, whenever a critical section **must not** be run with multiple threads in parallel

```c
#include <stdio.h>
#include <omp.h>

int main() {
    // Parallel region
    #pragma omp parallel
    {
        // Each thread will execute this block
        // Only one thread at a time will be allowed to execute the critical section
        #pragma omp critical
        {
            // Critical section
            printf("Thread %d is inside the critical section\n", omp_get_thread_num());
        }
    }

    return 0;
}
```

### Syncing threads

```c
#include <stdio.h>
#include <omp.h>

int main() {
    // Parallel region
    #pragma omp parallel
    {
        // Some work done by each thread
        printf("Thread %d is doing some work before the barrier\n", omp_get_thread_num());

        // Synchronize all threads at this point
        #pragma omp barrier

        // After the barrier, all threads will execute this
        printf("Thread %d passed the barrier\n", omp_get_thread_num());
    }

    return 0;
}
```

### Run on only master thread

```c
#include <stdio.h>
#include <omp.h>

int main() {
    // Parallel region
    #pragma omp parallel
    {
        // This block of code is executed by all threads
        printf("This is executed by all threads\n");

        // The following block of code is executed only by the master thread
        #pragma omp master
        {
            printf("This is executed only by the master thread\n");
        }

        // This block of code is executed by all threads
        printf("This is executed by all threads again\n");
    }

    return 0;
}
```

### Execute by one thread only

```c
{
    #pragma omp parallel
    {
        #pragma omp single
        {
            // This block of code will be executed by only one thread
            printf("This is executed by only one thread\n");
        }

        // Code executed by all threads
    }
}
```

## Task paralellism

```c
#pragma omp parallel
{
    // Code executed by all threads
    
    #pragma omp task
    {
        // creates a task that can be executed asynchronously by any available thread in the team.
        // Code inside the task
    }
}
```