# Praktyczny_python_M08

1. Stwórz dla domu maklerskiego graficzny dashboard, który pozwoli na podejmowanie decyzji o zakupie lub sprzedaży akcji Facebooka lub innych spółek. W tym celu wyświetl ceny akcji razem z średnią kroczącą z ostatnich 14 dni. Gdy aktualna cena spadnie poniżej średniej, to znak, że jesteśmy na górce i trzeba sprzedawać. Dodatkowo w dashboardzie umieść informacje o wolumenie sprzedaży, aby móc wykrywać nietypowe zdarzenia. Użyj w tym celu drugiej osi Y.

2. Notowania Facebooka ściągniesz stąd: https://www.nasdaq.com/market-activity/stocks/fb/historical Możesz także pobrać notowania innych interesujących Cię spółek. Te same dane znajdziesz także w pliku M08/data/fb.csv.

3. Zauważysz, że dane są posortowane od najnowszych do najstarszych. Jak odwrócisz tę kolejność? Poszukaj!

4. Wyceny akcji są poprzedzone znakiem dolara, np. `$80.20`. Napisz funkcję, która przyjmuje pojedynczy string, usuwa znak dolara i zwraca float'a. Użyj metody `.map()` na pojedynczej kolumnie, aby wyzwolić tę funkcję na każdym wierszu danych.