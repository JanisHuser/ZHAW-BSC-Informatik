## Datei öffnen

Eine Datei kann in unterschiedliche Modis geöffnet werden.

| Modus | Beschreibung | Datei nicht vorhanden |
|-|-|-|
| r | ASCII lesen | NULL |
| rb | Binär lesen | NULL |
| w | ASCII schreiben | Erstellt Datei |
| wb | Binäres schreiben | Erstellt Datei |
| a | Anfügen | Erstellt Datei |
| ab| Binäres Anfügen | Erstellt Datei |
| r+ | Lesen und schreiben | NULL |
| rb+ | Lesen und schreiben in binär | NULL |
| w+| lesen und schreiben | Erstellt Datei |
| wb+ | Lesen und schreiben in binär | Erstellt Datei |
| ab+ | Anfügen und lesen in binär | Erstellt Datei |



```c
#include <stdio.h>
#include <stdlib.h>

FILE *f = fopen("Pfad", "mode");
```

## Datei lesen (line by line)
```c

#include <stdio.h>
#include <stdlib.h>

int main(void)
{
	char * line = NULL;
	size_t len = 0;
	ssize_t read;
	FILE *f = fopen("Pfad", "r");
	
	if (f == NULL) { // das gleiche wie if (!f)
		perror("Datei konnte nicht geöffnet werden!");
		exit(-1);
	}
	
	while ((read = getline(&line, &len, f)) != -1) {
		printf("Retrieved line of length %zu:\n", read);
		printf("%s", line);
	}
	
	// Datei wieder schliessen
	fclose(f);
	
	if (line)
	{
		free (line);
	}
	return EXIT_STATUS;
}

```

## Datei schreiben (by Charater)
```c

#include <stdio.h>
#include <stdlib.h>


int main(void)
{
	char * line = NULL;
	size_t len = 0;
	ssize_t read;
	FILE *f = fopen("Pfad", "w");
	
	if (f == NULL) { // das gleiche wie if (!f)
		perror("Datei konnte nicht geöffnet werden!");
		exit(-1);
	}
	
	fprintf(f, "format\n", arg1);
	
	
	// Datei wieder schliessen
	fclose(f);
	
	if (line)
	{
		free (line);
	}
	return EXIT_STATUS;

}
```


## Datei anfügen
```c

int main(void)
{
	

	#include <stdio.h>
	#include <stdlib.h>
	
	char * line = NULL;
	size_t len = 0;
	ssize_t read;
	FILE *f = fopen("Pfad", "a
					");
	
	if (f == NULL) { // das gleiche wie if (!f)
		perror("Datei konnte nicht geöffnet werden!");
		exit(-1);
	}
	
	fprintf(f, "format\n", arg1);
	
	
	// Datei wieder schliessen
	fclose(f);
	
	if (line)
	{
		free (line);
	}
 	return EXIT_STATUS;
 }

```
