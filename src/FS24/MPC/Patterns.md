# Patterns

## Dependency Analysis

### Group Tasks Pattern

- Tasks share the **same** constraints and data

### Order Tasks Pattern

- Following tasks may not start until previous tasks have completed

### Data Sharing Pattern

Data can be
- Read-only
- Effectively-local
- Read write
	- accumulate
	- multiple read single-write


## Task Parallelism Pattern

- At least as many tasks as unit of execution (UEs), preferably more
- Computation effort enough to offset management overhead

- Order dependencies must be enforced
- Data dependencies
	- **Removable dependencies**: can be removed by code/loop transformation
	- **Seperable dependencies**: data structures could be replicated

### Schedule

- **Static Schedule**: defined a priori, low management effort but low number of tasks
- **Dynamic schedule**: higher management effort but unknown or unpredictable task load
	- Define a task queue and when UE completes its current task it gets a new one from the queue (UEs with tasks completed faster will take more from the queue)
- **Work-Stealing**: if UE has nothign to do, it looks to the queue of other UEs and takes a task to do 
	- Adds <span style="text-decoration: underline">significant</span> complexity

### Fork Join

- An implementation mechanism
- Implies the cloning of a section of code into another (structurally - but necessarily in terms of data) independent task
- is **NOT** an abstraction of the POSIX fork.

#### USe-Cases

- Recursive structures, such as trees
- Irregular sets of connected taks
- Where different functions are mapped onto different tasks


## Loop Parallelization

### Independent

When data is not shared across multiple indexes. This allows that each iteration could be parallelized

```c
for (int i = 0; i < N; i++) {
    a[i] = b[i] + c[i];
}
```


### Dependent

Each loop needs to wait for the previous index to finish
```c
for (int i = 1; i < N; i++) {
    a[i] = a[i-1] + b[i];
}
```


## Distributed Array Pattern

