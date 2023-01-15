## Internal Sorting
Data can be sorted in memory **at once**.

## External Sorting
Data needs to be stored first on external storage devices.

# Sorting algorithms

## Merge Sort
$$
O(n \log(n))
$$
Spliting an array into two halves of comparable sizes. Each half is then sorted and merged back together by using the merge function

![[Pasted image 20230105120917.png]]

## Selection Sort
$$
O(n^2)
$$
Smallest element is sent to the first position position of the array. Next smallest is sent after

## Bubble Sort
$$
O(n^2)
$$
Starting from the beginning, two elements are compared. Moving one element forward. Moves large values to the end.

## Insertion Sort
$$
O(n^2)
$$
Der aktuelle Wert wird bei der richtigen Position eingefügt. Der rechte Teil wird verschoben. Linked List löst dieses Problem.

## Quick Sort

$$
O(n \log(n))
$$
Das Array wird nun so umsortiert, dass 

-   die Elemente, die kleiner als das Pivot-Element sind, im linken Bereich landen,
-   die Elemente, die größer als das Pivot-Element sind, im rechten Bereich landen,
-   und dass das Pivot-Element zwischen den zwei Bereichen positioniert wird - und damit automatisch an seiner endgültigen Position.

## Distribution-Sort
Creating buckets of data, sorting these independently and writing the sorted values to an output array.

## TUH - Teile und Hersche
- Problem in kleinere, einfacher zu lösende Teile zerlegen

# Optimisierung

## Parallelisierung
**Es kommt ein Overhead der Steuerung dazu**
$p$: Möglicher anteil des Programms, der parallelisiert werden kann
$s$: Anzahl der Prozessoren
$$
Speedup = \frac{1}{1-p + \frac{p}{s}}
$$
## Hardware-Memory-Architektur
- Je weiter der Memory entfernt ist, desto länger dauert es
- 