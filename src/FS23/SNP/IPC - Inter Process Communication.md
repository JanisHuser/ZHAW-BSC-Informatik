Kommunikation zwischen zwei Prozessen

# POSIX Signale
Diese Signale können jedem Prozess gesendet werden. Somit sind die nachfolgenden Signale universal Anwendbar.

Mit htop können alle Prozesse unter Linux angesehen werden. Dieser dient als zudem als Task-Manager und erlaubt es Prozessen ein bestimmtes POSIX Signal zu senden.
```shell
htop
```

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

# POSIX PIPE
- Dient als FIFO (First In First Out) Buffer von fixer Maximalgrösse.
- Unidirektional, von einer zu der anderen Seite.


Mit dem Pipe befehl wird eine Unidirektionale Verbindung erstellt.
```c

int fd[2];

pipe(fd);

// Lese Seite der Pipe
fd[0];

// Schreibseite der Pipe
fd[1];

// schliessen der Read Pipe
close(fd[0]);

// Daten auf Schreib Pipe senden
// 12: länge des zu sendenden strings
write(fd[1], "Hello world\n", 12);


// Lesen von Read Pipe
// Geschieht erst, nachdem alle Kopien
// Des Write Buffers geschlossen worden sind
// Somit ist dies: BLOCKING
read(fd[0], buffer, BUFFER_SIZE);
```

## Anonymous Pipe
```c

#include <sys/types.h>
#includne <unistd.h>

const int BUFFER_SIZE = 100;

void main (void)
{
	int fd[2];
	char buffer[BUFFER_SIZE];
	ssize_t nBytes;

	status = pipe(fd);
	if (status == -1)
	{
		perror("Pipe konnte nicht erstellt werden");
		exit(EXIT_FAILURE);
	}

	pid_t child_id = fork();

	if (child_id == -1)
	{
		perror("Child Prozess konnte nicht erstellt werden");
		exit(EXIT_FAILURE);
	}

	if (child_id == 0)
	{
		// Wir sind in Child Prozess

		// Da wir nichts mit der Schreibpipe zu tun haben, 
		// können wir diese schliessen
		close(fd[1]);

		// Lese Daten von readpipe in buffer
		// Maximale Länge BUFFER_SIZE
		nbytes = read(fd[0], buffer, BUFFER_SIZE);

		// Wir haben unser Zeugs mit der readpipe gemacht,
		// jetzt können wir die pipe schliessen
		close(fd[0]);

		exit(EXIT_SUCESS);
	}

	if (child_id != 0)
	{
		// Sind in Parent Prozess
		// Dieses if ist eigentlich nicht mehr notwendig

		// Wir wollen nichts lesen,
		// daher können wir in diesem Prozess die Pipe zumachen
		close(fd[0]);

		// Jetzt schreiben wir unsere Daten auf
		// die Lesepipe
		write (fd[1], "Hello world\n", 12);

		// Schliessen der Pipe
		close(fd[1]);

		exit(EXIT_SUCCESS);
	}
}

```

## Non Blocking Version
In machen Fällen ist es notwendig, dass wir die Lesevorgänge der Pipe nicht blockierend machen. 

```c
void set_nonblocking(int fd)
{
	// Lese alle bisher gesetzten Flags
	// Wir wollen nur das nonblocking flag setzen
	int flags = fcntl (fd, F_GETFL, 0);

	if (flags == -1)
	{
		perror("Pipe Attribute konnten nicht gelesen werden");
		exit(EXIT_FAILURE);
	}

	int result = fcntl(fd, F_SETFL, flags | O_NONBLOCK);
	if (result == -1)
	{
		perror("Pipe Attribute konnten nicht gesetzt werden");
		exit(EXIT_FAILURE);
	}
}


int fd[2];

if (pipe(fd))
{
	perror("Pipe konnte nicht erstellt werden");
	exit(EXIT_FAILURE);
}

// pipe auf non blocking setzen
set_nonblocking(fd[0]);


// HOWTO LESEN
int reading = 1;
while (reading)
{
	int n = read(fd[0], buffer, BUFFER_SIZE);
	
	if (n == 0)
	{
		// polling aufhören
		// da pipe geschlossen worden ist
		close(fd[0]);
		reading = 0;
		continue;
	}

	if (n > 0)
	{
		// gelesene Daten verwenden
	}
	else if (errno = EAGAIN)
	{
		// poll interval abwarten
		// Es kann passieren, dass wir den Intervall so kurz halten
		// dass wir das Lock der pipe nicht wirklich frei lassen
		// dies wird als spin-lock bezeichnet 
	}
	else
	{
		// Da haben wir verkackt
		// Ernsthafter fehler
	}
}
```


## Named Pipes
Named pipes erlauben es, dass zwei unterschiedliche (sich nicht kennende) Prozesse eine Pipeverbindung aufbauen.

```shell
mkfifo pfad -m Mode
```

```c
#include <sys/types.h>
#include <sys/stat.h>


int fd = mkfifo("Pfad", mode_t modus);

// Jetzt kannst du diesen Buffer
// wie in FileIO mit 
// - fread
// - fwrite
// - fclose
// verwenden
```

# POSIX Message Queue

Maximale Kapazität von NxM Bytes
	- **N**: Maximale Anzahl Messages
	- **M**: Maximale Grösse einer Message (Bytes)

Mehrere Leser und Schreiber
- Jede Meldung wird beim lesen aus der Queue entfernt

Der name der Queue zeigt auf eine Datei im Filesystem. Daher sollte diese auch mit einem „/„ anfangen, um immer die gleiche Queue zu verwenden.



```c

// Öffnen einer Queue
// soll diese für alle gleich sein, dann / vorne anfügen,
// ansonsten ist die pipe relativ dem aktuellen Verzeichniss

mqd_t mqdes = mq_open ("/sideshow-bob", O_RDWR | O_CREAT, 
                   0664, NULL);


// Öffnen einer Queue mit Attributen

```

[Nachfolgendes Beispiel ist von hier](https://github.com/tisnik/message-queues-examples/blob/master/unix-messages/posix/example1/publisher.c)


### Publisher
```c
/*
 * Example used in following article:
 *
 * Implementace front zpráv podle normy POSIX
 * https://www.root.cz/clanky/implementace-front-zprav-podle-normy-posix/
 */

#include <stdio.h>
#include <string.h>

#include <mqueue.h>

#define QUEUE_NAME "/queue1"

int main(void)
{
    mqd_t message_queue_id;
    unsigned int priority = 0;
    char message_text[100];
    int status;

    message_queue_id = mq_open(QUEUE_NAME, O_RDWR | O_CREAT | O_EXCL, S_IRWXU | S_IRWXG, NULL);
    if (message_queue_id == -1) {
        perror("Unable to create queue");
        return 2;
    }

    strcpy(message_text, "Hello world!");

    status = mq_send(message_queue_id, message_text, strlen(message_text)+1, priority);
    if (status == -1) {
        perror("Unable to send message");
        return 2;
    }

    status = mq_close(message_queue_id);
    if (status == -1) {
        perror("Unable to close message queue");
        return 2;
    }

    return 0;
}
```

### Subscriber
```c
/*
 * Example used in following article:
 *
 * Implementace front zpráv podle normy POSIX
 * https://www.root.cz/clanky/implementace-front-zprav-podle-normy-posix/
 */

#include <stdio.h>
#include <string.h>

#include <mqueue.h>

#define QUEUE_NAME "/queue1"

int main(void)
{
    mqd_t message_queue_id;
    char message_text[10000];
    unsigned int sender;
    int status;

    message_queue_id = mq_open(QUEUE_NAME, O_RDWR);
    if (message_queue_id == -1) {
        perror("Unable to open queue");
        return 2;
    }

    status = mq_receive(message_queue_id, message_text, sizeof(message_text), &sender);
    if (status == -1) {
        perror("Unable to receive message");
        return 2;
    }
    printf("Received message (%d bytes) from %d: %s\n", status, sender, message_text);

    status = mq_close(message_queue_id);
    if (status == -1) {
        perror("Unable to close message queue");
        return 2;
    }

    return 0;
}
```

# POSIX Socket
Erlaubt Kommunikation über Netzwerk, oder über virtuelles LAN in einem System.

## Verbindungsorientiert

### Client
```c
#include <sys/types.h>
#include <sys/socket.h>
#include <sys/un.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <netdb.h>
#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#define RECEIVE_TIMEOUT 0
#define SEND_TIMEOUT 0

int sockfd;

void connect_server (void)
{
	struct addrinfo hints, *server_info, *p;
	
	// alles auf 0 setzen
	memset(&hints, 0, sizeof(hints)); 
	hints.ai_familiy = AF_INET;
	hints.ai_socktype = SOCK_STREAM;

	// Hole Infos zu Socket auf
	// localhost und port 80
	int status = getaddrinfo("localhost", "80", &hints, &server_info);
	if (status != 0) {
	    perror("getaddrinfo konnte nicht ausgeführt werden");
	    exit(EXIT_FAILURE);
	}

	for (p = server_info; p != NULL; p = p->ai_next) {
		if ((sockfd = socket(p->ai_family, p->ai_socktype, p->ai_protocol)) == -1)
		{
			perror ("socket error");
			exit(EXIT_FAILURE);
		}

		if (connect(sockfd, p->ai_addr, p->ai_addrlen) == -1) {
			close(sockfd);
			perror ("Es konnte keine Verbinung hergestellt werden");
			exit(EXIT_FAILURE);
		}

		// wenn erfolgreich verbunden, aus der Schleife ausbrechen
		break;
   }

    if (p == NULL) {
        perror ("Es konnte keine Verbinung hergestellt werden");
		exit(EXIT_FAILURE);
    }


	// SOCKET VERBUNDEN
}

void write(char * buffer, int len)
{
	int totalSent = 0;

	while (totalSent < len) {
		int bytesSent = send(
			communicationSocket,
			buffer + totalSent,
			len - totalSent,
			SEND_TIMEOUT);

		if (bytesSent == -1) {
			perror ("Error in send");
			exit(EXIT_FAILURE);
		}
		totalSent += bytesSent;
   }
}

int read(char *buffer, int len)
{
	int totalReceived = 0;

	while (totalReceived < len) {
		int bytesReceived = recv(
			communicationSocket,
			buffer + totalReceived,
			len - totalReceived, 
			RECEIVE_TIMEOUT);
			
		if (bytesReceived == -1) {
			perror("Error in Receive");
			exit(EXIT_FAILURE);
		}

		totalReceived += bytesReceived;
	}

	return totalReceived;
}

void main (void)
{
	connect_server();

	write ("Hello World", 11);

	char bufffer[1000];
	int read = read(buffer, 1000);

	close(sockf);
}
```

### Server

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include <sys/types.h>
#include <sys/socket.h>

#include <netdb.h>
#include <unistd.h>


#define RECEIVE_TIMEOUT 0
#define SEND_TIMEOUT 0
#define MAX_QUEUE 1

void server_init(){
   // BEGIN-STUDENTS-TO-ADD-CODE

   struct addrinfo hints, *server_info, *p;

   memset(&hints, 0, sizeof(hints));

   hints.ai_family = AF_INET;
   hints.ai_socktype = SOCK_STREAM;

   int status = getaddrinfo(NULL,"80" , &hints, &server_info);
   if(status != 0){
      ExitOnError(status, "getaddrinfo");
   }

   int sockfd;
   for (p = server_info; p != NULL; p = p->ai_next) {
      if ((sockfd = socket(p->ai_family, p->ai_socktype, p->ai_protocol)) == -1) {
         perror("socket error");
         exit(EXIT_FAILURE);
      }

      if (bind(sockfd, p->ai_addr, p->ai_addrlen) == -1) {
         close(sockfd);
         perror("connect error");
         exit(EXIT_FAILURE);
      }

      break; // wenn erfolgreich verbunden, aus der Schleife ausbrechen
   }

   ListeningSocket = sockfd;

   listen(ListeningSocket, MAX_QUEUE);

   // END-STUDENTS-TO-ADD-CODE
}

int getRequest(char* requestBuffer, int max_len)
{
   // BEGIN-STUDENTS-TO-ADD-CODE
   int bytesReceived = recv(
      connectedSocket,
      requestBuffer,
      max_len -1,
      RECEIVE_TIMEOUT);
   requestBuffer[bytesReceived] = '\0';
   return bytesReceived;
   // END-STUDENTS-TO-ADD-CODE
}

void sendResponse(char* response, int resp_len)
{
   // BEGIN-STUDENTS-TO-ADD-CODE
   send(connectedSocket, response, resp_len, 0);
   // END-STUDENTS-TO-ADD-CODE
}

void server_close_connection(void)
{
   // BEGIN-STUDENTS-TO-ADD-CODE
   close(connectedSocket);
   // END-STUDENTS-TO-ADD-CODE
}


int wait_client(void) {
   connectedSocket = accept(ListeningSocket, 0, 0);
   return connectedSocket;
}

void main (void)
{
	server_init();
	wait_client();

	char buffer[1000];

	getRequest(buffer, 1000);
	sendResponse("Hello World", 11);
	server_close_connection();
}


```

## Verbindungslos
Client/Server Architektur
• Client
- Socketdefinition (getaddrinfo(), socket())
- keine Verbindungsanfrage
- bidirektionales Lesen/Schreiben (recfrom(), sendto())
- danach Socket schliessen (close())
• Server
- Socketdefinition (getaddrinfo(), socket(), bind())
- kein Abwarten und Akzeptieren von Verbindungsanfragen
- bidirektionales Lesen/Schreiben (recfrom(), sendto())
- danach eventuell Socket schliessen (close())