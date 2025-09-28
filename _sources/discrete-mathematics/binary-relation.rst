Quan hệ hai ngôi
****************


Quan hệ hai ngôi
================

.. prf:definition:: Quan hệ hai ngôi
    :label: def-binary-relation
    
    Xét hai tập hợp :math:`A` và :math:`B`. Ta gọi :math:`\mathcal{R}` là một quan hệ hai ngôi trên :math:`A` và :math:`B` nếu :math:`\mathcal{R} \subset A \times B`, trong đó :math:`A \times B` là tích Descartes của hai tập hợp.

Nếu phần tử :math:`(a, b) \in \mathcal{R}` với :math:`a \in A` và :math:`b \in B` thì ta nói :math:`a` **có quan hệ với** :math:`b` và kí hiệu :math:`a \mathcal{R} b`.

Khi :math:`A \equiv B` thì ta nói :math:`\mathcal{R}` là quan hệ hai ngôi trên :math:`A`. Đây cũng là yếu tố quan trọng cho các khái niệm về sau.

.. prf:example:: 
    :label: exp-binary-relation

    Xét hai tập hợp :math:`A = \{1, 2, 3, 4\}` và :math:`B = \{a, b, c\}`. Khi đó tích Descartes 

    .. math:: 
        
        A \times B = \{
        & (1, a), (1, b), (1, c), (2, a), (2, b), (2, c), \\
        & (3, a), (3, b), (3, c), (4, a), (4, b), (4, c) \}
        
    Giả sử :math:`\mathcal{R} = \{(1, a), (3, b), (4, c)\}`.
    
    Khi đó :math:`1` quan hệ với :math:`a` do :math:`(1, a) \in \mathcal{R}`, hay :math:`1 R a`.
    
    Tuy nhiên :math:`1` không có quan hệ với :math:`b` do :math:`(1, b) \not\in \mathcal{R}`.

Sau đây ta định nghĩa các loại quan hệ hai ngôi.

.. prf:definition:: 
    :label: def-types-relation

    Cho :math:`R` là quan hệ hai ngôi trên tập :math:`A`. Ta nói:

    1. :math:`\mathcal{R}` **phản xạ** (hay **reflexive**) nếu với mọi :math:`x \in A` thì :math:`(x, x) \in \mathcal{R}`.
    2. :math:`\mathcal{R}` **đối xứng** (hay **symmetric**) nếu :math:`(x, y) \in \mathcal{R}` thì :math:`(y, x) \in \mathcal{R}`.
    3. :math:`\mathcal{R}` **phản xứng** (hay **antisymmetric**) nếu :math:`(x, y) \in \mathcal{R}` thì :math:`(y, x) \not\in \mathcal{R}`. Nói cách khác nếu :math:`(x, y) \in \mathcal{R}` và :math:`(y, x) \in \mathcal{R}` thì :math:`x = y`.
    4. :math:`\mathcal{R}` **bắc cầu** (hay **transitive**) nếu :math:`(x, y) \in \mathcal{R}` và :math:`(y, z) \in \mathcal{R}` thì :math:`(x, z) \in \mathcal{R}`.


Quan hệ tương đương
-------------------

Quan hệ tương đương giúp ta chia (phân hoạch) một tập hợp rời rạc thành các tập con mà chỉ cần một phần tử đại diện cho tập con đó là đủ để tính toán.

.. prf:definition:: Quan hệ tương đương
    :label: def-equiv-relation

    Cho :math:`\mathcal{R}` là quan hệ trên tập :math:`A`. Khi đó :math:`\mathcal{R}` được gọi là **quan hệ tương đương** (hay **equivalence relation**, **отношение эквивалентности**) nếu :math:`\mathcal{R}` phản xạ, đối xứng và bắc cầu.

    Ta có thể kí hiệu :math:`x \mathcal{R} y`, với :math:`\mathcal{R}` là quan hệ tương đương, là :math:`x \sim y` hoặc :math:`x \widetilde{\mathcal{R}} y`.

Tiếp theo ta định nghĩa lớp tương đương chứa phần tử :math:`x` và tập thương.

.. prf:definition:: Lớp tương đương
    :label: def-equiv-class

    Cho :math:`\mathcal{R}` là quan hệ tương đương trên tập :math:`A`. Khi đó với :math:`x \in A`, ta định nghĩa lớp tương đương chứa phần tử :math:`x` là tập các phần tử của :math:`A` có quan hệ với :math:`x`:

    .. math:: \bar{x} = \{ y \in A, \, y \mathcal{R} x \}.

.. prf:definition:: Tập thương
    :label: def-quot-set

    Tập hợp các lớp tương đương như trên tạo thành tập thương.

    .. math:: A / \mathcal{R} = \{ \bar{x}, \, x \in A \}.

.. prf:example:: 
    :label: exp-quot-set

    Xét số nguyên dương :math:`n`. Với số nguyên :math:`x` và :math:`y`, ta nói :math:`x` có quan hệ với :math:`y` nếu :math:`n \mid (x - y)`, hay :math:`x \equiv y \bmod n`. Ta kí hiệu quan hệ này là :math:`n \mathbb{Z}`.

    Quan hệ trên là quan hệ tương đương vì

    1. :math:`n \mid 0 = x - x` với mọi :math:`x \in \mathbb{Z}` nên có tính phản xạ.
    2. :math:`n \mid (x - y)` suy ra :math:`n \mid -(x-y) = y-x` với mọi :math:`x, y \in \mathbb{Z}` nên có tính đối xứng.
    3. :math:`n \mid (x - y)` và :math:`n \mid (y - z)` suy ra :math:`n \mid (x - y + y - z) = (x - z)` nên có tính bắc cầu.

    Từ đó ta có thể phân tập :math:`\mathbb{Z}` thành các lớp tương đương

    .. math:: 
        
        \begin{array}{ccl}
            \overline{0} & = & \{ \ldots, -2n, -n, 0, n, 2n, \ldots \}, \\
            \overline{1} & = & \{ \ldots, -2n+1, -n+1, 1, n+1, 2n+1, \ldots \}, \\
            \vdots \\
            \overline{n-1} & = & \{ \ldots, -n-1, -1, n-1, 2n-1, 3n-1, \ldots \}.
        \end{array}

    Tập thương của chúng ta là
    
    .. math:: \mathbb{Z} / n\mathbb{Z} = \{ \overline{0}, \overline{1}, \ldots, \overline{n-1} \}.


Quan hệ thứ tự
--------------

.. prf:definition:: Quan hệ thứ tự
    :label: def-ordered-relation
    
    Cho quan hệ :math:`\mathcal{R}` trên tập :math:`A`. Ta nói :math:`\mathcal{R}` là **quan hệ thứ tự** (hay **order relation**, **отношение порядка**) nếu :math:`\mathcal{R}` phản xạ, phản xứng và bắc cầu.

.. prf:definition:: 
    :label: def-ordered-set

    Cho tập hợp :math:`A` và quan hệ :math:`\mathcal{R}` trên :math:`A` là quan hệ thứ tự. Nếu :math:`x \mathcal{R} y` thì ta kí hiệu :math:`x \prec y`. Khi đó :math:`(A, \prec)` được gọi là **tập có thứ tự** (hay **ordered set**).

Tiếp theo là một số định nghĩa quan trọng về tập hợp có thứ tự.

.. prf:definition:: 
    :label: def-prec

    Với :math:`(A, \prec)` và :math:`x, y \in A`.

    1. Nếu :math:`x \prec y`, ta nói :math:`y` là **trội** của :math:`x`, hay là :math:`x` **được trội** bởi :math:`y`.
    2. :math:`y` là **trội trực tiếp** của :math:`x` nếu không tồn tại :math:`z` sao cho :math:`x \prec z` và :math:`z \prec y`.

.. prf:definition:: 
    :label: def-types-ordered-relation

    Xét :math:`(A, \prec)`.

    1. :math:`x` và :math:`y` thuộc :math:`A` được gọi là **so sánh được** nếu :math:`x \prec y` hoặc :math:`y \prec x`.
    2. Nếu với mọi :math:`x, y \in A`, :math:`x` và :math:`y` so sánh được thì :math:`(A, \prec)` được gọi là **quan hệ thứ tự toàn phần**. Ngược lại thì gọi là **quan hệ thứ tự bán phần**.

Để biểu diễn sự so sánh trong một tập hợp, ta sử dụng biểu đồ Hasse.

.. prf:definition:: 
    :label: def-hasse-diagram

    Biểu đồ Hasse của :math:`(A, \prec)` với :math:`A` là tập hữu hạn bao gồm

    1. Tập điểm - mỗi điểm biểu diễn một phần tử của :math:`A`.
    2. Tập cung - vẽ một cung từ :math:`x` tới :math:`y` nếu :math:`y` là trội trực tiếp của :math:`x`.

.. prf:example:: 
    :label: exp-hasse-diagram

    Xét tập :math:`U_{12} = \{ 1, 2, 3, 4, 6, 12 \}` với quan hệ :math:`x \mathcal{R} y` được định nghĩa bởi :math:`x` là ước của :math:`y`.

    Theo đó, biểu đồ Hasse của quan hệ trên là :numref:`hasse-1`.

.. _hasse-1:

.. figure:: ../figures/hasse/hasse.*

    Biểu đồ Hasse của :math:`U_{12}`

.. prf:definition:: 
    :label: def-min-max

    Xét quan hệ thứ tự :math:`(A, \prec)`.

    1. Phần tử :math:`M \in A` được gọi là
        
       1. **Tối đại** nếu :math:`M \prec x` thì :math:`x = M`.
       2. **Cực đại** (hay **lớn nhất**) nếu với mọi :math:`x \in A` thì :math:`x \prec M`.
    
    2. Phần tử :math:`m \in A` được gọi là
        
       1. **Tối tiểu** nếu :math:`x \prec m` thì :math:`x = m`.
       2. **Cực tiểu** (hay **nhỏ nhất**) nếu với mọi :math:`x \in A` thì :math:`m \prec x`.

.. prf:remark:: 
    :label: rmk-min-max

    1. Phần tử cực đại nếu có là duy nhất. Tương tự cho cực tiểu.
    2. Nếu :math:`n` là phần tử tối đại duy nhất thì nó cũng là cực đại. Tương tự cho tối tiểu.

Trong ví dụ :math:`U_{12}` ở trên thì :math:`1` là tối tiểu và cũng là cực tiểu, và :math:`12` là tối đại và cũng là cực đại.
