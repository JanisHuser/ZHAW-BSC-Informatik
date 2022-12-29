# Suchen nach Mustern

## Regex: Reguläre Ausdrücke

- Zum Suchen von definierten Mustern in Texten
    - Bestimmter String: "ZHAW"
	- Unschafte Muster: "IT20a, IT19a, IT20c"
	- Wiederholende (Teil-)Muster: 170.12.34.12

- Die meisten heutigen Programmiersprachen unterstützen die Suche nacm Muster in Form von regulären Ausdrücken.

```java
import java.util.regex.*;

Pattern pat = Pattern.compile("ZHAW");
Matcher matcher = pat.matcher("Willkommen an der ZHAW");
while (matcher.find()) {
	String group = matcher.group();
	int start = matcher.start();
	int end = matcher.end();
	// do something
}
```

[Regex Standard](https://en.wikipedia.org/wiki/Regular_expression)