Ecco un esempio di regex che può essere utilizzato per identificare i numeri compresi tra due caratteri di underscore (_):

```
_([0-9]+)_
```

Questa regex cercherà un underscore seguito da uno o più numeri (0-9) e un altro underscore successivo. Ad esempio, se hai un testo come questo:

```
Questo è un esempio di numero _123_ all'interno di underscore.
```

La regex identificherà il numero "123". Si noti che la regex utilizzerà le parentesi tonde per catturare il numero trovato, in modo da poterlo utilizzare in seguito nel codice.