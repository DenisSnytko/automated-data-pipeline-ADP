/*
Zum Ausführen: 
- markieren und im Kontextmenü "Run selected Query" wählen
- STRG + SHIFT +Q drücken
*/

/*Umsatz pro Jahr*/
SELECT substr(orderdate,1,4) as "Year", SUM(ordertotal) as "Total Sales"
FROM sales
GROUP BY substr(orderdate,1,4);

/*Top Produkte*/
SELECT productid, category, subcategory,  SUM(ordertotal) as "Total Sales"
FROM sales
GROUP BY productid, category, subcategory
ORDER BY SUM(ordertotal) DESC
LIMIT 10;

/*Umsatz pro Staat*/
SELECT state, SUM(ordertotal) as "Total Sales"
FROM sales
GROUP BY state;
