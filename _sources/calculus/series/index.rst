********
Chuỗi số
********

Xét dãy số :math:`\{a_n\}`. Đặt

.. math:: 
    
    S_n = a_1 + a_2 + \ldots + a_n.

Khi đó :math:`\{S_n\}` là chuỗi số. Tương tự như sự hội tụ hoặc phân kỳ của dãy số, ta cũng quan tâm đến sự hội tụ và phân kỳ của chuỗi số.

.. prf:definition:: Chuỗi số hội tụ
    :label: def-chuoi-hoi-tu
    
    Chuỗi số :math:`\{S_n\}` được gọi là **hội tụ** nếu tồn tại giới hạn hữu hạn :math:`\displaystyle{L = \lim_{n \to \infty} S_n}`.

Ngược lại ta gọi là chuỗi phân kỳ, nghĩa là :math:`\displaystyle{\lim_{n \to \infty} S_n = \infty}` hoặc không tồn tại :math:`\lim\limits_{n \to \infty} S_n`.

.. prf:example:: 
    :label: exp-chuoi-hoi-tu

    Xét dãy số :math:`a_n = \dfrac{1}{2^n}` với :math:`n = 1, 2, \ldots`

    Khi đó

    .. math:: 
        
        S_n & = \frac{1}{2} + \frac{1}{2^2} + \ldots + \frac{1}{2^n} \\
        & = \frac{1}{2} \cdot \dfrac{1 - \dfrac{1}{2^n}}{1 - \dfrac{1}{2}} \longrightarrow \frac{1}{2} \cdot \dfrac{1}{1 - \dfrac{1}{2}} = 1 

    khi :math:`n \to \infty`. Như vậy :math:`S_n` là chuỗi hội tụ.

=================
Tiêu chuẩn Cauchy
=================

Theo định nghĩa, chuỗi số hội tụ khi tồn tại giới hạn hữu hạn. Do đó ta có thể viết theo ngôn ngữ :math:`\delta - \varepsilon` như đối với dãy số.

.. prf:theorem:: Tiêu chuẩn Cauchy
    :label: thm-cauchy-criteria-chuoi

    Chuỗi số :math:`\displaystyle{\sum_{i=1}^{\infty} a_i}` hội tụ nếu với mọi :math:`\varepsilon > 0`, tồn tại :math:`N \in \mathbb{N}`, sao cho với mọi :math:`n \geqslant m \geqslant N`, ta có 

    .. math:: 
        
        \left\lvert \sum_{i=n}^{m} a_i \right\rvert < \varepsilon.

.. admonition:: Chứng minh
    :class: danger, dropdown
    
    Do :math:`\displaystyle{\sum_{i=m}^n a_i = \sum_{i=1}^n a_i - \sum_{i=1}^{m-1} a_i}` nên chuỗi số hội tụ từ một điểm :math:`m` nào đó trở đi thì chuỗi hội tụ. Tương tự cho phân kỳ.

.. prf:corollary:: 
    :label: cor-hoi-tu-lim
    
    Nếu chuỗi số :math:`\displaystyle{\sum_{n=1}^\infty a_i}` hội tụ thì :math:`\displaystyle{\lim_{n \to \infty} a_n = 1}`.

.. admonition:: Chứng minh
    :class: danger, dropdown

    Theo tiêu chuẩn Cauchy, với mọi :math:`\varepsilon > 0`, do chuỗi hội tụ nên tồn tại :math:`N \in \mathbb{N}` sao cho với mọi :math:`n \geqslant m \geqslant N` ta có :math:`\left\lvert \sum\limits_{i=m}^{n} a_i \right\rvert < \varepsilon`.

    Nếu ta chọn :math:`m = n` thì điều kiện trở thành với mọi :math:`\varepsilon > 0`, tồn tại :math:`N \in \mathbb{N}` sao cho với mọi :math:`n \geqslant N` ta có :math:`\lvert a_n \rvert < \varepsilon`. Nói cách khác :math:`\displaystyle{\lim_{n \to \infty} a_n = 0}` (định nghĩa giới hạn dãy số).

Dựa vào tiêu chuẩn Cauchy ta có một số tiêu chuẩn hội tụ hữu dụng như sau.

.. prf:theorem:: Tiêu chuẩn thứ nhất về sự hội tụ
    :label: thm-first-criteria-hoi-tu

    Xét hai chuỗi số :math:`\displaystyle{\sum_{n=1}^\infty a_n}` và :math:`\displaystyle{\sum_{n=1}^\infty b_n}`. Khi điều kiện :math:`0 \leqslant a_n \leqslant b_n` thỏa mãn, ta có các kết quả sau:

    1. Nếu :math:`\sum b_n` hội tụ thì :math:`\sum a_n` cũng hội tụ.
    2. Nếu :math:`\sum a_n` phân kỳ thì :math:`\sum b_n` cũng phân kỳ.

.. admonition:: Chứng minh
    :class: danger, dropdown

    Ta thấy rằng nếu :math:`\sum b_n` hội tụ thì với mọi :math:`\varepsilon > 0`, tồn tại :math:`N \in \mathbb{N}` sao cho với mọi :math:`n \geqslant m \geqslant N`, :math:`\displaystyle{\left\lvert \sum_{i=m}^n a_i \right\rvert < \varepsilon}`.

    Do :math:`0 \leqslant a_i \leqslant b_i` nên :math:`\displaystyle{\left\lvert \sum_{i=m}^{n} a_i \right\rvert < \left\lvert \sum_{i=m}^{n} b_i \right\rvert < \varepsilon}`. Như vậy chuỗi :math:`\displaystyle{\sum_{n=1}^{\infty} a_n}` cũng hội tụ.

.. prf:theorem:: Tiêu chuẩn so sánh
    :label: thm-criteria-compare

    Xét hai chuỗi số dương :math:`\displaystyle{\sum_{n=1}^\infty a_n}` và :math:`\displaystyle{\sum_{n=1}^\infty b_n}`. Nếu tồn tại giới hạn hữu hạn :math:`\displaystyle{\lim_{n \to \infty} \dfrac{a_n}{b_n} = L}` thì hai dãy số trên cùng hội tụ hoặc cùng phân kỳ.

.. admonition:: Chứng minh
    :class: danger, dropdown
    
    Do dãy số :math:`\dfrac{a_n}{b_n}` có giới hạn hữu hạn :math:`L` nên với mọi :math:`\varepsilon > 0`, tồn tại :math:`N \in \mathbb{N}` sao cho với mọi :math:`n \geqslant N`, ta có :math:`\left\lvert \dfrac{a_n}{b_n} - L \right\rvert < \varepsilon`. Tương đương với :math:`\displaystyle{b_n (-\varepsilon + L) < a_n < b_n (\varepsilon + L)}`. Từ tiêu chuẩn thứ nhất về sự hội tụ và bất đẳng thức thứ hai suy ra nếu chuỗi :math:`\sum b_n` hội tụ thì chuỗi :math:`\sum a_n` cũng hội tụ.

    Tương tự, với bất đẳng thức thứ nhất, nếu :math:`\sum b_n` phân kỳ thì :math:`\sum a_n` cũng phân kỳ.

.. prf:theorem:: Tiêu chuẩn tích phân Cauchy
    :label: thm-criteria-integral-cauchy

    Xét chuỗi số dương :math:`\displaystyle{\sum_{n=1}^{\infty} a_n}`. Nếu :math:`a_n` là dãy số có dạng :math:`a_n = f(n)`, ta chuyển qua xét hàm số :math:`f(x)`.

    Nếu hàm số :math:`f(x)` thỏa mãn:

    1. :math:`f(x)` không tăng.
    2. :math:`\displaystyle{\int\limits_{0}^{\infty} f(x)\,dx}` hữu hạn.

    Khi đó chuỗi số :math:`\displaystyle{\sum_{n=1}^{\infty} a_n}` hội tụ.
