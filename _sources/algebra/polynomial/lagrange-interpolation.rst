Đa thức nội suy Lagrange
=========================

Trong đại số, công thức nội suy Lagrange cho phép chúng 
ta tìm được một đa thức :math:`f(x)` trên trường 
:math:`\mathbb{F}` bất kì khi biết được một số cặp 
:math:`(x_i, f(x_i))` nhất định với :math:`x_i, f(x_i) \in \mathbb{F}`.

Để tìm đa thức :math:`f(x)` có bậc :math:`n` ta cần ít 
nhất :math:`n+1` cặp :math:`(x_i, f(x_i) = y_i)` với 
:math:`0 \leqslant i \leqslant n` và :math:`x_i \neq x_j` 
với mọi :math:`i \neq j`.

Khi đó, ta có **công thức nội suy Lagrange** như sau:

.. math:: f(x) = \sum_{i=0}^{n} \left(y_i \cdot \prod_{j \neq i} \frac{x - x_j}{x_i - x_j}\right).

.. prf:example:: 
    :label: exp-lagrange-interpolation

    Giả sử chúng ta có hàm :math:`f(x) = x^2 + x + 1`. 
    Khi đó :math:`f(1) = 3`, :math:`f(-1) = 1`, :math:`f(0) = 1`.

    Từ ba cặp :math:`(x_i, f(x_i))` trên mình sẽ tìm 
    ngược lại :math:`f(x)` ban đầu.

    Theo công thức thì

    .. math::

        f(x) = & y_0 \cdot \frac{(x - x_1) (x - x_1)}{(x_0 - x_1) (x_0 - x_2)} + y_1 \cdot \frac{(x - x_0) (x - x_2)}{(x_1 - x_0) (x_1 - x_2)} \\
        + & y_2 \cdot \frac{(x - x_0) (x - x_1)}{(x_2 - x_0) (x_2 - x_1)}

    Thay số vào thì ta có

    .. math:: f(x) = 3 \cdot \frac{(x - (-1)) (x - 0)}{(1 - (-1)) (1 - 0)} + 1 \cdot \frac{(x - 1) (x - 0)}{(-1 - 1) (-1 - 0)} + 1 \cdot \frac{(x - 1) (x - (-1))}{(0 - 1) (0 - (-1))}

    Thu gọn lại ta có :math:`f(x) = x^2 + x + 1` (đúng với hàm cần tìm).

Phần tiếp theo sẽ liên quan đến phương pháp tính đa thức nội suy Lagrange được tham khảo ở :cite:`Kuntzmann1979` (bản dịch tiếng Nga, chương 4).
Nếu đặt

.. math:: L_i(x) = \prod_{j \neq i} \frac{x - x_j}{x_i - x_j} = \frac{(x - x_0) \cdots (x - x_{i-1}) (x - x_{i+1}) \cdots (x - x_n)}{(x_i - x_0) \cdots (x_i - x_{i-1}) (x_i - x_{i+1}) \cdots (x_i - x_n)}

thì đa thức :math:`L_i(x)` được gọi là **hệ số Lagrange**. Đa thức này có tính chất:

* đều có bậc là :math:`n`;
* :math:`L_i(x_i) = 1`;
* :math:`L_i(x_j) = 0` với :math:`j \neq i`.

Như vậy, nội suy Lagrange có thể biểu diễn dưới dạng

.. math:: f(x) = \sum_{i=0}^n y_i L_i(x)

thỏa mãn các điều kiện:

* :math:`f(x)` có bậc không quá :math:`n`;
* :math:`f(x_i) = y_i`.

Ta sẽ gọi biểu diễn này là **dạng Lagrange** (hay **форма Лагранжа**).

Dễ thấy rằng biểu diễn của :math:`L_i` chứa rất nhiều phép nhân và việc tính toán sẽ khó khăn khi :math:`n` lớn. Do đó ta sẽ xem xét **công thức tỉ cự** (hay **барицентрическая формула**).

Nếu ta chọn :math:`y_i = 1` với mọi :math:`x_i` thì ta có :math:`g(x) = 1` thỏa :math:`g(x_i) = y_i`. Khi đó

.. math:: 1 = \sum_{i=0}^n L_i(x),

.. math:: f(x) = \frac{f(x)}{1} = \frac{y_0 L_0(x) + y_1 L_1(x) + \cdots + y_n L_n(x)}{L_0(x) + L_1(x) + \cdots + L_n(x)}.

nếu ta chia cả tử và mẫu của :math:`f(x)` cho

.. math:: (x - x_0) (x - x_1) \cdots (x - x_n)

thì nhận được

.. math:: f(x) = \dfrac{\sum\limits_{i=0}^n \dfrac{y_i X_i}{x - x_i}}{\sum\limits_{i=0}^n \dfrac{X_i}{x - x_i}}

với

.. math:: X_i = \dfrac{1}{(x_i - x_0) \cdots (x_i - x_{i-1}) (x_i - x_{i+1}) \cdots (x_i - x_n)}.

Biểu thức :math:`X_i` có dạng phức tạp nhưng chỉ phụ thuộc vào :math:`x_i`. Do đó ta chỉ cần tính một lần cho mọi cặp điểm. Công thức đó được gọi là **công thức tỉ cự** (hay **барицентрическая формула**).
