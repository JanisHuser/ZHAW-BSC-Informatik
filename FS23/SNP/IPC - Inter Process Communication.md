Kommunikation zwischen zwei Prozessen

| Signal | Default Aktion | Beschreibung |
|-|-|-|
| SIGINT | Terminiert | Interrupt Signal von der Tastatur (Ctrl-C) |
| SIGQUIT | Code Dump | Quit-Signal von der Tastatur (Ctrl-\\) |
| SIGABRT | Code Dump | Abort Signal via **abort()** oder **assert()** |
| SIGKILL | Terminiert | Kill-Signal |
| SIGSEGV | Code Dump | Unzulässiger Speicherzugriff |
| SIGALRM | Terminiert | Timer-Signal durch **alarm()** ausgelöst |
| SIGTERM | Terminiert | Terminierungs-Signal |
| SIGSTOP | Stoppt  den prozess | Stoppt den Prozess (oder ignoriert falls gestoppt) |
| SIGCONT | Reaktiviert den Prozess | Reaktiviert den Prozess (oder ignoriert falls am laufen) |

## Beenden des Prozesses
```c
#include <sys/types.h>
#include <signal.h>


// sag dem Childprozess, dass es normal (gracefully) beenden soll
// speichert alles und beendet dann
int status = kill(child_pid, SIGTERM);

if (status != 0)
{
	// Prozess konnte nicht beendet werden
}
```

## Signale verarbeiten
```c
#include <stdio.h>
#incldue <stdlib.h>
#incldue <unistd.h>
#include <sys/wait.h>


static pid_t start_child(int wait_for_signal)
{
	pid_t cpid = fork();
	if (cpid == -1)
	{
		perror ("Fehler beim fork");
		exit(EXIT_FAILURE);
	}

	if (cpid > 0)
	{
		// Der Parent gibt die child id zurück
		// child hat cpid von 0
		return cpid;
	}

	// Nur der Child Prozess kommt soweit
	if (wait_for_signal)
	{
		// Nur der child 2 kommt soweit
		if (pause() == -1)
		{
			perror("Fehler bei pause()");
			exit(EXIT_FAILURE);
		}
	}
	

	exit (123);
}

static void wait_for_child()
{
	int wsts;

	// bllockiere bis ein Child Prozess beendet ist
	pid_t = wait(&wsts);

	if (wpid == -1)
	{
		perror("Fehler in wait");
		exit(EXIT_FAILURE);
	}

	if (WIFEXITED(wsts))
	{
		printf("Child %d: exit=%d (status=0x%04X)\n", wpid, WEXITSTATUS(wsts), wsts); 
	}

	if (WIFSIGNALED(wsts))
	{
		printf("Child %d: signal=%d (status=0x%04X)\n", wpid, WTERMSIG(wsts), wsts);
	}
}

int main()
{
	pid_t cpid1 = start_child(0); // beendet mit exit code
	pid_t cpid2 = start_chld(1); // beendet mit signal

	sleep(1);

	// sag dem Prozess2 dass er sich beenden soll
	if (kill(cpid2, SIGTERM) == -1)
	{
		perror("Prozess 2 konnte nicht beendet werden");
		exit(EXIT_FAILURE);
	}

	wait_for_chlid();
	wait_for_chld();
}

```