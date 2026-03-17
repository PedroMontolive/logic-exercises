# logic-exercises — Pedro Emanuel

## Python, PHP e Java

> Percebi que tava travando em coisas que não deveria, então resolvi voltar ao básico.

---

## 📁 Estrutura do repositório

```
logic-exercises/
├── level-1-basics/
│   ├── 01-fizzbuzz/
│   │   ├── solution.py
│   │   └── README.md
│   ├── 02-reverse-string/
│   │   ├── solution.py
│   │   └── README.md
│   └── ...
├── level-2-strings/
├── level-3-arrays/
├── level-4-recursion/
├── level-5-sorting/
├── level-6-data-structures/
└── README.md   ← este arquivo
```

Cada pasta de exercício tem esta estrutura:

```
01-fizzbuzz/
├── README.md      ← enunciado
├── solution.py    ← resolvo aqui primeiro
├── solution.php   ← reescrevo depois sem olhar o .py
└── test.py        ← pelo menos 3 casos de teste
```

---

## 🟢 Nível 1 — Básico

---

**01. `fizzbuzz`**
Para números de 1 a N: imprime "Fizz" se divisível por 3, "Buzz" se por 5,
"FizzBuzz" se por ambos, e o número caso contrário.
Conceitos: loop, módulo, condicionais.

---

**02. `reverse-string`**
Inverte uma string sem usar função de reversão nativa.
Conceitos: loop, indexação, acumulador.

---

**03. `count-vowels`**
Conta o número de vogais em uma string (case-insensitive).
Conceitos: loop em string, comparação, contador.

---

**04. `palindrome-check`**
Verifica se uma string é um palíndromo (ex: "racecar", "madam").
Conceitos: comparação de string, inversão, limpeza de input.

---

**05. `sum-digits`**
Dado um número inteiro, retorna a soma dos seus dígitos.
Ex: 1234 → 10.
Conceitos: conversão de tipos, loop, acumulador.

---

**06. `min-max-array`**
Encontra o maior e o menor valor de uma lista sem usar `min()` / `max()`.
Conceitos: loop, comparação, variáveis de controle.

---

**07. `celsius-to-fahrenheit`**
Converte uma lista de temperaturas de Celsius para Fahrenheit.
Conceitos: loop, fórmula matemática, lista.

---

**08. `count-duplicates`**
Dado um array de inteiros, retorna quantos valores aparecem mais de uma vez.
Conceitos: dicionário/hash, contagem, iteração.

---

## 🟡 Nível 2 — Strings

---

**09. `anagram-check`**
Verifica se duas strings são anagramas (mesmas letras, ordem diferente).
Ex: "listen" e "silent".
Conceitos: ordenação, normalização de string, comparação.

---

**10. `word-frequency`**
Conta quantas vezes cada palavra aparece em um texto.
Retorna um dicionário ordenado por frequência decrescente.
Conceitos: split, dicionário, ordenação por valor.

---

**11. `caesar-cipher`**
Implementa a cifra de César: desloca cada letra N posições no alfabeto.
Ex: "abc" com shift 2 → "cde".
Conceitos: ASCII/ord/chr, módulo, loop.

---

**12. `title-case`**
Converte uma string para Title Case sem usar `.title()` nativo.
Ex: "the quick brown fox" → "The Quick Brown Fox".
Conceitos: split, capitalização manual, join.

---

**13. `compress-string`**
Comprime uma string contando caracteres consecutivos iguais.
Ex: "aaabbc" → "a3b2c1".
Conceitos: loop, agrupamento, acumulador.

---

**14. `longest-word`**
Retorna a palavra mais longa de uma frase.
Em caso de empate, retorna a primeira encontrada.
Conceitos: split, loop, comparação de tamanho.

---

## 🟠 Nível 3 — Arrays e listas

---

**15. `two-sum`**
Dado um array de inteiros e um target, retorna os índices de dois números
que somam ao target. Ex: [2, 7, 11, 15], target=9 → [0, 1].
Conceitos: hash map, loop único, complexidade O(n).

---

**16. `remove-duplicates`**
Remove duplicatas de uma lista mantendo a ordem de aparição original.
Sem usar `set()` diretamente.
Conceitos: loop, dicionário como "visitados", acumulador.

---

**17. `flatten-array`**
Transforma uma lista aninhada em uma lista plana.
Ex: [1, [2, [3, 4]], 5] → [1, 2, 3, 4, 5].
Conceitos: recursão ou stack, verificação de tipo.

---

**18. `rotate-array`**
Rotaciona um array N posições para a direita sem usar slice nativo.
Ex: [1,2,3,4,5], n=2 → [4,5,1,2,3].
Conceitos: módulo, loop, índice calculado.

---

**19. `chunk-array`**
Divide uma lista em sublistas de tamanho N.
Ex: [1,2,3,4,5], n=2 → [[1,2],[3,4],[5]].
Conceitos: loop com step, slice, acumulador.

---

**20. `intersection`**
Retorna os elementos que aparecem em duas listas, sem duplicatas.
Sem usar operadores de set nativos.
Conceitos: loop, hash, filtragem.

---

**21. `group-by`**
Agrupa uma lista de dicionários por um campo chave.
Ex: lista de produtos agrupada por "category".
Conceitos: dicionário de listas, loop, acumulador.

---

## 🔵 Nível 4 — Recursão

> O conceito que mais me trava. Regra pra mim mesmo: cada exercício tem que ter
> solução recursiva E iterativa — implementar os dois e comparar.

---

**22. `factorial`**
Calcula o fatorial de N de forma recursiva.
Depois implementa de forma iterativa e compara.
Conceitos: caso base, chamada recursiva, stack de chamadas.

---

**23. `fibonacci`**
Retorna o N-ésimo número de Fibonacci de forma recursiva.
Depois otimiza com memoização e compara a performance.
Conceitos: recursão dupla, memoização, cache.

---

**24. `sum-nested`**
Soma todos os números em uma lista aninhada de profundidade arbitrária.
Ex: [1, [2, [3, [4]]]] → 10.
Conceitos: recursão com tipo dinâmico, caso base múltiplo.

---

**25. `power`**
Calcula base^expoente de forma recursiva sem usar `**` ou `pow()`.
Depois implementa a versão eficiente com exponentiation by squaring.
Conceitos: recursão, divisão do problema, complexidade O(log n).

---

**26. `binary-search-recursive`**
Implementa busca binária de forma recursiva em um array ordenado.
Conceitos: divisão do espaço de busca, índices, caso base.

---

## 🔴 Nível 5 — Ordenação

---

**27. `bubble-sort`**
Implementa Bubble Sort. Depois mede quantas comparações foram feitas
pra entender por que é O(n²).
Conceitos: loop duplo, swap, flag de otimização.

---

**28. `selection-sort`**
Implementa Selection Sort. Compara com Bubble Sort em número de swaps.
Conceitos: loop duplo, índice do mínimo, swap.

---

**29. `insertion-sort`**
Implementa Insertion Sort. Testa com listas quase ordenadas e vê
por que ele é eficiente nesses casos.
Conceitos: loop, deslocamento, inserção na posição correta.

---

**30. `merge-sort`**
Implementa Merge Sort recursivo. O primeiro algoritmo O(n log n) da lista.
Conceitos: divisão, merge de listas ordenadas, recursão.

---

**31. `counting-sort`**
Implementa Counting Sort para inteiros não-negativos.
Conceitos: array de contagem, offset, reconstrução.

---

## ⚫ Nível 6 — Estruturas de dados

---

**32. `stack`**
Implementa uma pilha (Stack) com push, pop, peek e is_empty.
Usa pra resolver: verificar se parênteses estão balanceados.
Ex: "({[]})" → válido. "({[})" → inválido.
Conceitos: LIFO, classe, encapsulamento.

---

**33. `queue`**
Implementa uma fila (Queue) com enqueue, dequeue, peek e is_empty.
Usa pra simular uma fila de atendimento com prioridade.
Conceitos: FIFO, classe, encapsulamento.

---

**34. `linked-list`**
Implementa uma lista ligada simples com append, prepend, delete e search.
Conceitos: nó, ponteiro para próximo, travessia.

---

**35. `binary-search-tree`**
Implementa uma BST com insert, search e in-order traversal.
O in-order traversal de uma BST retorna os elementos em ordem crescente — implementa e verifica.
Conceitos: nó com filho esquerdo/direito, recursão, propriedade da BST.

---

**36. `lru-cache`**
Implementa um cache LRU (Least Recently Used) com capacidade N.
Get em O(1) e Put em O(1).
Conceitos: dicionário + lista duplamente ligada (ou OrderedDict), eviction policy.
O mais difícil da lista — deixa por último.

---

## 📋 Cronograma

> Início: 17/03/2025. Ritmo de 1 exercício por dia — pode pular um dia ou dois sem culpa,
> só retoma de onde parou. O prazo é flexível, o progresso não precisa ser linear.

---

### Semana 1 — Básico absoluto `(17/03 → 24/03)`

```
17/03 (seg)  →  01. fizzbuzz
18/03 (ter)  →  02. reverse-string
19/03 (qua)  →  03. count-vowels
20/03 (qui)  →  04. palindrome-check
21/03 (sex)  →  05. sum-digits
22/03 (sáb)  →  06. min-max-array
23/03 (dom)  →  07. celsius-to-fahrenheit
24/03 (seg)  →  08. count-duplicates
```

- [ ]   1. fizzbuzz
- [ ]   2. reverse-string
- [ ]   3. count-vowels
- [ ]   4. palindrome-check
- [ ]   5. sum-digits
- [ ]   6. min-max-array
- [ ]   7. celsius-to-fahrenheit
- [ ]   8. count-duplicates

---

### Semana 2 — Strings `(25/03 → 31/03)`

```
25/03 (ter)  →  09. anagram-check
26/03 (qua)  →  10. word-frequency
27/03 (qui)  →  11. caesar-cipher
28/03 (sex)  →  12. title-case
29/03 (sáb)  →  13. compress-string
30/03 (dom)  →  14. longest-word
```

- [ ]   9. anagram-check
- [ ]   10. word-frequency
- [ ]   11. caesar-cipher
- [ ]   12. title-case
- [ ]   13. compress-string
- [ ]   14. longest-word

---

### Semana 3 — Arrays e listas `(01/04 → 08/04)`

```
01/04 (ter)  →  15. two-sum
02/04 (qua)  →  16. remove-duplicates
03/04 (qui)  →  17. flatten-array
04/04 (sex)  →  18. rotate-array
05/04 (sáb)  →  19. chunk-array
06/04 (dom)  →  20. intersection
07/04 (seg)  →  21. group-by
```

- [ ]   15. two-sum
- [ ]   16. remove-duplicates
- [ ]   17. flatten-array
- [ ]   18. rotate-array
- [ ]   19. chunk-array
- [ ]   20. intersection
- [ ]   21. group-by

---

### Semana 4 — Recursão `(08/04 → 13/04)`

```
08/04 (ter)  →  22. factorial
09/04 (qua)  →  23. fibonacci
10/04 (qui)  →  24. sum-nested
11/04 (sex)  →  25. power
12/04 (sáb)  →  26. binary-search-recursive
```

- [ ]   22. factorial
- [ ]   23. fibonacci
- [ ]   24. sum-nested
- [ ]   25. power
- [ ]   26. binary-search-recursive

---

### Semana 5 — Ordenação `(14/04 → 19/04)`

```
14/04 (seg)  →  27. bubble-sort
15/04 (ter)  →  28. selection-sort
16/04 (qua)  →  29. insertion-sort
17/04 (qui)  →  30. merge-sort
18/04 (sex)  →  31. counting-sort
```

- [ ]   27. bubble-sort
- [ ]   28. selection-sort
- [ ]   29. insertion-sort
- [ ]   30. merge-sort
- [ ]   31. counting-sort

---

### Semana 6 — Estruturas de dados `(21/04 → 27/04)`

```
21/04 (seg)  →  32. stack
22/04 (ter)  →  33. queue
23/04 (qua)  →  34. linked-list
24/04 (qui)  →  35. binary-search-tree
25/04 (sex)  →  36. lru-cache  ← pode spilhar pro fim de semana
```

- [ ]   32. stack
- [ ]   33. queue
- [ ]   34. linked-list
- [ ]   35. binary-search-tree
- [ ]   36. lru-cache

---

## 📌 Regras que eu mesmo defini

- **README.md por exercício** — enunciado, exemplo de input/output, dica pra quando eu travar
- **Python primeiro** — depois reescrevo em PHP ou Java sem olhar a solução anterior
- **Sem copiar da internet** — se travar, dorme e volta.
- Preciso terminar tudo
