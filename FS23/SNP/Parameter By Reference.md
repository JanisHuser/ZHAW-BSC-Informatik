
**POINTER WIRD ÜBERGEBEN**

```c

void swap (int *a, int *b)
{
	int saved_a = *a; // Wert von a zwischenspeichern
	*a = *b;
	*b = saved_a; // WIHCTIG: Wert anpassen, und nicht Adresse
}
```

## Read only

```c
void print_array(const int *a, int n)
{
	// const verhindert die Modifikation von a
}
```

## Arrays übergeben
```c
void print_array(int *a, int n)
{ }
```
ist gleich wie
```c
void print_array(int a[], int n)
{ }
```

## Structs übergeben
```c
void do_something(struct *s)
{ }
```

```c
void do_something(const struct *s)
{
	// struct kann nicht überschrieben werden
}
```