class Solution(object):
    def subsetXORSum(self, nums):
        """
        The XOR total of an array is defined as the bitwise XOR of all its elements,
        or 0 if the array is empty.
        For example, the XOR total of the array [2,5,6] is 2 XOR 5 XOR 6 = 1.
        Given an array nums, return the sum of all XOR totals for every subset of nums.
        Note: Subsets with the same elements should be counted multiple times.
        An array a is a subset of an array b if a can be obtained
        from b by deleting some (possibly zero) elements of b.

        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        total_sum = 0

        for i in range(1 << n):
            xor = 0
            for j in range(n):
                if i & (1 << j):
                    xor ^= nums[j]
            total_sum += xor
        return total_sum


"""
1 << n erzeugt die Zahl 
2 hoch n, also die Anzahl der möglichen Teilmengen für ein Array der Länge n.
Jede Zahl von 0 bis 2^n - 1 repräsentiert eine eindeutige Kombination von Elementen aus nums,
d.h., eine eindeutige Teilmenge.
Das äußere for-Loop (for i in range(1 << n)) durchläuft jede mögliche Teilmenge von nums, 
wobei i die Teilmenge in Form einer Bitmaske darstellt.
Bitmaske: Wie i die Teilmenge repräsentiert
Eine Zahl i zwischen 0 und 2^n - 1 wird in ihrer Binärform verwendet, um die Teilmenge zu repräsentieren.
Jedes Bit in i steht dabei für ein bestimmtes Element in nums:

Bit ist 1: Das Element ist in der Teilmenge enthalten.
Bit ist 0: Das Element ist nicht in der Teilmenge enthalten.
Beispiel für nums = [a, b, c] (also n = 3)

Wenn i = 5, dann ist i in Binär 101. Das bedeutet:

Das erste Bit (rechts) ist 1: Das erste Element a ist in der Teilmenge enthalten.
Das zweite Bit ist 0: Das zweite Element b ist nicht in der Teilmenge enthalten.
Das dritte Bit ist 1: Das dritte Element c ist in der Teilmenge enthalten.
In diesem Fall steht i = 5 für die Teilmenge [a, c].

Inneres for-Loop: Prüfung mit Bitweise AND
Im inneren for-Loop durchlaufen wir jedes Bit von i, um festzustellen,
ob das j-te Element in der Teilmenge enthalten ist.
Dies wird durch die Anweisung if i & (1 << j) erreicht:

1 << j: Erzeugt eine Zahl, die nur das j-te Bit als 1 hat. Zum Beispiel:
1 << 0 ergibt 0001 (entspricht 1 in Dezimal).
1 << 1 ergibt 0010 (entspricht 2 in Dezimal).
1 << 2 ergibt 0100 (entspricht 4 in Dezimal).
i & (1 << j): Vergleicht die j-te Position von i mit dem j-ten Bit von 1 << j:
Wenn das j-te Bit von i 1 ist, ergibt der Ausdruck i & (1 << j) einen Wert ungleich 0, 
was bedeutet, dass das j-te Element in der Teilmenge enthalten ist.
Wenn das j-te Bit von i 0 ist, ergibt i & (1 << j) 0,
was bedeutet, dass das j-te Element nicht in der Teilmenge enthalten ist.
Beispiel zur Bedingung if i & (1 << j)

Nehmen wir an, i = 5 (also 101 in Binär) und j = 0, j = 1, und j = 2:

Für j = 0:
1 << 0 ergibt 001.
i & (1 << 0) vergleicht 101 & 001, was 1 ergibt.
Da das Ergebnis ungleich 0 ist, ist das Element nums[0] in der Teilmenge enthalten.
Für j = 1:
1 << 1 ergibt 010.
i & (1 << 1) vergleicht 101 & 010, was 0 ergibt.
Das Ergebnis ist 0, daher ist das Element nums[1] nicht in der Teilmenge enthalten.
Für j = 2:
1 << 2 ergibt 100.
i & (1 << 2) vergleicht 101 & 100, was 4 ergibt.
Da das Ergebnis ungleich 0 ist, ist das Element nums[2] in der Teilmenge enthalten.
XOR-Operation für die Teilmenge
Für jede Teilmenge, die durch i repräsentiert wird:

Die Elemente, bei denen if i & (1 << j) wahr ist,
werden per XOR (xor_total ^= nums[j]) miteinander verknüpft, 
um die XOR-Summe dieser spezifischen Teilmenge zu berechnen.
Am Ende der Schleife
Nachdem alle Teilmengen durchlaufen wurden, 
enthält total_sum die Summe der XOR-Ergebnisse jeder einzelnen Teilmenge von nums, 
was die gewünschte Lösung darstellt.
"""