# CMPS 2200  Recitation 02

**Name (Team Member 1):** Viv heurtevant vheurtevant@tulane.edu

note: apologies for the lengthy answers on Q4. I wanted to get used to solving the recurrences individually before using brick method. I also do not know how to format the summations, so apologies for that too.

In this recitation, we will investigate recurrences. 
To complete this recitation, follow the instructions in this document. Some of your answers will go in this file, and others will require you to edit `main.py`.



## Running and testing your code
- To run tests, from the command-line shell, you can run
  + `pytest test_main.py` will run all tests
  + `pytest test_main.py::test_one` will just run `test_one`
  + We recommend running one test at a time as you are debugging.

## Turning in your work

- Once complete, click on the "Git" icon in the left pane on repl.it.
- Enter a commit message in the "what did you change?" text box
- Click "commit and push." This will push your code to your github repository.
- Although you are working as a team, please have each team member submit the same code to their repository. One person can copy the code to their repl.it and submit it from there.

## Recurrences

In class, we've started looking at recurrences and how to we can establish asymptotic bounds on their values as a function of $n$. In this lab, we'll write some code to generate recursion trees (via a recursive function) for certain kinds of recurrences. By summing up nodes in the recurrence tree (that represent contributions to the recurrence) we can compare their total cost against the corresponding asymptotic bounds. We'll focus on  recurrences of the form:

$$ W(n) = aW(n/b) + f(n) $$

where $W(1) = 1$.

- [ ] 1. (2 point) In `main.py`, you have stub code which includes a function `simple_work_calc`. Implement this function to return the value of $W(n)$ for arbitrary values of $a$ and $b$ with $f(n)=n$.

- [ ] 2. (2 point) Test that your function is correct by calling from the command-line `pytest test_main.py::test_simple_work` by completing the test cases and adding 3 additional ones.

- [ ] 3. (2 point) Now implement `work_calc`, which generalizes the above so that we can now input $a$, $b$ and a *function* $f(n)$ as arguments. Test this code by completing the test cases in `test_work` and adding 3 more cases.

- [ ] 4. (2 point) Now, derive the asymptotic behavior of $W(n)$ using $f(n) = 1$, $f(n) = \log n$ and $f(n) = n$. Then, generate actual values for $W(n)$ for your code and confirm that the trends match your derivations.
 

For deriving the asymptoptic behavior of W(n) = aW(n/b) + 1, observe there are a^i nodes per level and the cost per level is c*a^i . Because the merge cost per node is f(n)=1, the total cost per level is c^1 a^i. The max tree depth is log_b(n). Therefore, we have c multiplied by the sum from i = 0 to log_bn with summand a^i. Because a>= 1 and the sum is finite, we use the property of geometric series to bound the result above by a/a-1 * c * a^log_bn. By change of base properties of log, we can rewrite a^logbn as b^(log_bn * log_ba) = n^(log_b(a)) and conclude that W(n) is O(n^log_b(a)) when f(n)=1. When a = b this simplifies to O(n).

When f(n) = log_b(n), cost per node is log_b(n/b^i) so the cost per level is a^i * c * log_b(n/b^i). As before, we sum these results up and take c out of the sum as it is constant. Using properties of log, we further seperate the equation into two summands. Let the bounds for both sums be from i = 0 to log_b(n): c* log_b(n) *sum(a^i) - c * log_b(b) * sum(a^i * i ) . From the previous problem, we know sum(a^i) can be bounded above by a/a-1 * n ^ log_b(a) * log_b(n) . Observe that the second term's summand is increasing- therefore,its highest cost level will be its leaves: log_b(n) * n^log_b(a). Observe that because this is subtracted, it cancels out with the log_b(n) * n^log_b(a) term in the first summand, giving O(n^log_b(a)) instead. When a = b this simplifies to O(n).

When f(n)= n, the cost per node becomes c(n/b^i), making the total cost per level (a^i/b^i)= (a/b)^i. Note that the behavior of W(n) from this point on depends on the relationship between a & b, which will be discussed more in the next question. For now, let a=b and observe that the cost per level collapses to cn*1^i. Evaluating the summation, we have cn * sum from i=0 to logb_n with summand 1. Observe this can be bounded above by c * nlog(n), meaning W(n) is O(nlog(n)) when f(n)=O(n) and a=b.

To test the values, a and b are fixed at 2, So the theoretical run time of W(n) is O(n) when f(n)=1, O(n) when f(n)=log(n), and O(nlogn) when f(n)=n. The results are as follows:
|     n |   W_1 |   W_2 |    W_3 |
|-------|-------|-------|--------|
|    10 |    15 |    19 |     36 |
|    20 |    31 |    42 |     92 |
|    50 |    63 |    89 |    276 |
|   100 |   127 |   184 |    652 |
|  1000 |  1023 |  1525 |   9120 |
|  5000 |  8191 | 12274 |  61728 |
| 10000 | 16383 | 24561 | 133456 |

Where W_1 has f(n)=1, W_2 has f(n)= log(n), and W_3 has f(n) = n. The results match well- it is interesting to observe that although W_1 and W_2 are both O(N), W_2 has consistently higher work.

- [ ] 5. (4 points) Now that you have a nice way to empirically generate valuess of $W(n)$, we can look at the relationship between $a$, $b$, and $f(n)$. Suppose that $f(n) = n^c$. What is the asypmptotic behavior of $W(n)$ if $c < \log_b a$? What about $c > \log_b a$? And if they are equal? Modify `test_compare_work` to compare empirical values for different work functions (at several different values of $n$) to justify your answer. 

Given f(n)= n^c and from our previous results, we can write the cost of W(n) as the sum from i = 0 to log_b(n) n^c *summand(a/b^c)^i. Observe this is the geometric series where r= (a/b^c).Rewriting this as an equation, we have a = b^c -> log_b(a) = c .
 So when c > log_b(a), r < 1 Which bounds the summation by 1/1-a * n^c, meaning W1(n) is O(n^c) and root dominated.
 When c = log_b(a), r = 1. Then, the problem collapses as seen in question four and W2(n) is O(n^c log_b(n)) and balanced.
 Finally, c < log_b(a) implies r > 1, Which bounds the equation above by a/a-1 * n^c * n^-c * n^log_b(a), which means W3 is O(n^log_b(a)) and leaf dominated.

 Let W_1 have c > log_b(a): c=2, b=2, a=1, Meaning W_1 is O(n^2)
 Let W_2 have c = log_b(a): c=2, b=2, a=4, Meaning W_2 is O(n^2log_2(n))
 Let W_3 have c < log_b(a): c=2, b=2, a=8 , Meaning W_3 is O(n^3).
 |     n |       W_1 |        W_2 |           W_3 |
|-------|-----------|------------|---------------|
|    10 |       130 |        328 |          1068 |
|    20 |       530 |       1712 |          8944 |
|    50 |      3315 |      12936 |        104780 |
|   100 |     13315 |      61744 |        848240 |
|  1000 |   1333214 |    8544512 |     509190592 |
|  5000 |  33332873 |  294904064 |  143543110592 |
| 10000 | 133332873 | 1279616256 | 1148444884736 |

The empirical results match the theoretical predictions. 
 
- [ ] 6. (3 points) $W(n)$ is meant to represent the running time of some recursive algorithm. Suppose we always had $a$ processors available to us and we wanted to compute the span of the same algorithm. Implement the function `span_calc` to compute the empirical span, where the work of the algorithm is given by $W(n)$. Implement `test_compare_span` to create a new comparison function for comparing span functions. Derive the asymptotic expressions for the span of the recurrences you used in problem 4 above. Confirm that everything matches up as it should. 

To keep results consistent with problem 4, let b=2. The value of "a" will always be 1 as the recursive calls are able to be ran in parallel and thus do not contribute to the span.

For a theoretical span S(n)= S(n/b)+1 where b=2,a=1, observe f(n)= n^0 = 1 meaning c=0. Therefore, we have 0 = log_2(1) = 0, meaning the recursion is balanced. Therefore, S is O(n^c log_b(n)), which in this case simplifies to O(log_2(n)). 

For the theoretical span S(n)=S(n/b)+log_b(n), observe the cost per level decreases: log_b(n/b^i), where i is the level. Therefore, we can conclude the recursion is root dominated- meaning we only need to look at the initial cost, in this case O(log_2(n)). 

For the theoretical span S(n)=S(n/b)+O(n), The cost per level is also decreasing, so the cost will be O(n).

|     n |   S_1 |   S_2 |   S_3 |
|-------|-------|-------|-------|
|    10 |     4 |     7 |    18 |
|    20 |     5 |    11 |    38 |
|    50 |     6 |    16 |    97 |
|   100 |     7 |    22 |   197 |
|  1000 |    10 |    46 |  1994 |
|  5000 |    13 |    79 |  9995 |
| 10000 |    14 |    92 | 19995 |

The results match expectations- observe that although S_1 and S_2 are both O(logn), S_2 grows faster (and takes longer).