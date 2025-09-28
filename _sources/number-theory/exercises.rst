Bài tập số học sưu tầm
**********************

**Câu 1** (đề kiểm tra, ITMO). Chứng minh (không dùng quy nạp) rằng với mọi :math:`n \in \mathbb{N}` thì

.. math:: 5 \cdot 2^{3n-2} + 3^{3n-1} \ \vdots \ 19.

Theo định lý Fermat nhỏ thì :math:`2^{18} \equiv 1 \pmod{19}`, hay :math:`(2^3)^6 \equiv 1 \pmod{19}`. Tương tự :math:`3^{18} \equiv 1 \pmod{19}`. Do đó mình sẽ xét các dạng của :math:`n` là :math:`6k`, :math:`6k+1`, ..., :math:`6k+5`.

**Trường hợp 1.** :math:`n = 6k`. Khi đó

.. math::   
    
    & 2^{3n-2} = 2^{3 \cdot 6k - 2} \equiv 2^{-2} = 5 \pmod{19} \\
    & 3^{3n-1} = 3^{3 \cdot 6k - 1} \equiv 3^{-1} = 13 \pmod{19} \\ 
    \Rightarrow \ & 5 \cdot 2^{3n-2} + 3^{3n-1} \equiv 5 \cdot 5 + 13 \equiv 0 \pmod{19}.
    

**Trường hợp 2.** :math:`n = 6k + 1`. Khi đó

.. math:: 
    
    & 2^{3n-2} = 2^{3 \cdot 6k + 1} \equiv 2 \pmod{19} \\
    & 3^{3n-1} = 3^{3 \cdot 6k + 2} \equiv 3^{2} = 9 \pmod{19} \\ 
    \Rightarrow \ & 5 \cdot 2^{3n-2} + 3^{3n-1} \equiv 5 \cdot 2 + 9 \equiv 0 \pmod{19}.
    

**Trường hợp 3.** :math:`n = 6k + 2`. Khi đó

.. math:: 
    
    & 2^{3n-2} = 2^{3 \cdot 6k + 4} \equiv 2^{4} = 16 \pmod{19} \\
    & 3^{3n-1} = 3^{3 \cdot 6k + 5} \equiv 3^{5} = 15 \pmod{19} \\ 
    \Rightarrow \ & 5 \cdot 2^{3n-2} + 3^{3n-1} \equiv 5 \cdot 16 + 15 \equiv 0 \pmod{19}.
    

**Trường hợp 4.** :math:`n = 6k + 3`. Khi đó

.. math:: 
    
    & 2^{3n-2} = 2^{3 \cdot 6k + 7} \equiv 2^{7} = 14 \pmod{19} \\
    & 3^{3n-1} = 3^{3 \cdot 6k + 8} \equiv 3^{8} = 6 \pmod{19} \\ 
    \Rightarrow \ & 5 \cdot 2^{3n-2} + 3^{3n-1} \equiv 5 \cdot 14 + 6 \equiv 0 \pmod{19}.
    
**Trường hợp 5.** :math:`n = 6k + 4`. Khi đó

.. math:: 
    
    & 2^{3n-2} = 2^{3 \cdot 6k + 10} \equiv 2^{10} = 17 \pmod{19} \\
    & 3^{3n-1} = 3^{3 \cdot 6k + 11} \equiv 3^{11} = 10 \pmod{19} \\ 
    \Rightarrow \ & 5 \cdot 2^{3n-2} + 3^{3n-1} \equiv 5 \cdot 17 + 10 \equiv 0 \pmod{19}.
    
**Trường hợp 6.** :math:`n = 6k + 5`. Khi đó

.. math:: 
    
    & 2^{3n-2} = 2^{3 \cdot 6k + 13} \equiv 2^{13} = 3 \pmod{19} \\
    & 3^{3n-1} = 3^{3 \cdot 6k + 14} \equiv 3^{14} = 4 \pmod{19} \\ 
    \Rightarrow \ & 5 \cdot 2^{3n-2} + 3^{3n-1} \equiv 5 \cdot 3 + 4 \equiv 0 \pmod{19}.
    
**Câu 2** (đề kiểm tra, ITMO). Tính

.. math:: 1! + 2! + \ldots + 2023! + 2024! \bmod 10.

Trong các giai thừa từ :math:`5!` trở đi luôn có :math:`5` và :math:`2` do đó luôn chia hết cho :math:`10`. Vì vậy chỉ cần tính

.. math:: 1! + 2! + 3! + 4! = 1 + 2 + 6 + 24 \equiv 3 \bmod 10.

**Câu 3** (đề kiểm tra, ITMO). Chứng minh số :math:`154^{20} + 139^{31}` là hợp số.

Vì

.. math:: 154^{20} \equiv (-1)^{20} \equiv 1 \pmod 5 \ \text{và} \ 139^{31} \equiv (-1)^{31} \equiv -1 \pmod 5

nên số đã cho chia hết cho :math:`5` và do đó là hợp số.

**Câu 4** (đề kiểm tra, ITMO). Chứng minh số :math:`31^{51} + 27` là hợp số.

Dễ thấy :math:`31` là số lẻ nên lũy thừa của nó cũng là số lẻ. Tổng hai số lẻ là số chẵn nên số đã cho chia hết cho :math:`2` và do đó là hợp số.

**Câu 5** (đề kiểm tra, ITMO). Chứng minh với mọi :math:`n \in \mathbb{N}` thì :math:`n^8 + 4` là hợp số.

Ta có

.. math:: n^8 + 4 = n^8 + 4n^4 + 4 - 4n^4 = (n^4 + 2) - (2n^2)^2 = (n^4 + 2 - 2n^2) (n^4 + 2 + 2n^2).

Hai biểu thức trong ngoặc luôn lớn hơn :math:`1` nên suy ra :math:`n^8 + 4` là hợp số.

**Câu 6** (đề kiểm tra, ITMO). Tìm tất cả số nguyên tố :math:`p` sao cho :math:`3p + 20` và :math:`4p + 1` là số nguyên tố.

*Chưa làm ra.*

**Câu 7** (đề kiểm tra, ITMO). Tìm tất cả số nguyên tố :math:`p` sao cho :math:`2p^2 + 5p - 2` cũng là số nguyên tố.

*Chưa làm ra.*

**Câu 8** (đề kiểm tra, ITMO). Chứng minh rằng không tồn tại đa thức :math:`P` với hệ số nguyên sao cho :math:`P(40) = 30` và :math:`P(19) = 24`.

Đặt

.. math:: P(x) = a_n x^n + a_{n-1} x^{n-1} + \ldots + a_1 x + a_0.

Khi đó

.. math:: P(40) = a_n \cdot 40^n + a_{n-1} \cdot 40^{n-1} + \ldots + a_1 \cdot 40 + a_0,

và

.. math:: P(19) = a_n \cdot 19^n + a_{n-1} \cdot 19^{n-1} + \ldots + a_1 \cdot 19 + a_0.

Vì :math:`40^k - 19^k = (40 - 19) \cdot (\ldots)` nên :math:`40^k - 19^k` chia hết cho :math:`40 - 19 = 21` với mọi :math:`k`.

Nói cách khác :math:`P(40) - P(19)` chia hết cho :math:`21`, nhưng :math:`30 - 24 = 6` không chia hết :math:`21`. Do đó không tồn tại đa thức :math:`P` thỏa mãn đề bài.

**Câu 9** (đề kiểm tra, ITMO). Tìm tập tất cả số :math:`x \in \mathbb{Z}` sao cho :math:`533 x \equiv 1 \pmod{17}`.

Vì :math:`533 \equiv 6 \pmod{17}` nên ta chỉ cần giải phương trình :math:`6 x \equiv 1 \pmod{17}` là đủ.

Sử dụng thuật toán Euclid mở rộng có thể tính được :math:`6^{-1} = 3 \pmod{17}`, suy ra nghiệm là

.. math:: x \equiv 3 \pmod{17},

nghĩa là :math:`x = 3 + 17k` với :math:`k \in \mathbb{Z}`.

**Câu 10** (đề kiểm tra, ITMO). Tìm số dư của :math:`454^{225}` khi chia cho :math:`16`.

Do :math:`454` chia hết cho :math:`2` nên :math:`454^4` chia hết cho :math:`16`.

Suy ra :math:`454^{225}` chia hết cho :math:`16`.
