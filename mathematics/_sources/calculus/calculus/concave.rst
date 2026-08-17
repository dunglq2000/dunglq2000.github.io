====================================
Tính lồi, lõm và điểm uốn của đồ thị
====================================

.. prf:definition:: Hàm lồi, lõm
    :label: def-concave-func
    
    Giả sử :math:`\mathbb{I}` là một khoảng trong :math:`\mathbb{R}`. Hàm số :math:`f` được gọi là **lõm** trên :math:`\mathbb{I}` nếu và chỉ nếu với mọi :math:`\alpha, \beta \geqslant 0` mà :math:`\alpha + \beta = 1`, ta đều có

    .. math:: f(\alpha x + \beta y) \leqslant \alpha f(x) + \beta f(y)

    với mọi :math:`x, y \geqslant 0`.

    Trong trường hợp ngược lại (đổi chiều bất đẳng thức) thì ta nói :math:`f` là hàm **lồi** trên :math:`\mathbb{I}`.

Trong một số sách toán ở nước ngoài thì khái niệm lồi, lõm của hàm số được hiểu ngược lại. Khi đó hàm lõm ở định nghĩa trên được gọi là hàm *lồi* (*lồi dưới*) và hàm lồi ở định nghĩa trên gọi là hàm *lõm* (*lồi trên*).

Ví dụ ở bài viết `Выпуклость и точки перегиба <http://nuclphys.sinp.msu.ru/mathan/p1/m1503.html>`_ (Tính lồi và điểm uốn) của Moscow State University (MSU) mang tên Lomonosov thì định nghĩa hàm lồi bên trên được MSU gọi là *lồi trên* (*выпуклая вверх*), còn định nghĩa hàm lõm bên trên được MSU gọi là *lồi dưới* (*выпуклая вниз*).

Ví dụ ở trang wikipedia `Concave function <https://en.wikipedia.org/wiki/Concave_function>`_ thì định nghĩa hàm lồi bên trên (dấu :math:`\geqslant`) được wikipedia định nghĩa là hàm lõm (concave). Tương tự, ở trang wikipedia `Convex function <https://en.wikipedia.org/wiki/Convex_function>`_ thì định nghĩa hàm lõm bên trên (dấu :math:`\leqslant`) được wikipedia định nghĩa là hàm lồi (convex).

Về mặt hình học, các bạn có thể xem :math:`y = x^2` là một ví dụ của hàm lõm và :math:`y = -x^2` là một ví dụ của hàm lồi. Sau đây chúng ta sẽ phân tích một số tính chất từ định nghĩa hàm lồi, lõm để đưa ra khía cạnh hình học này.

.. prf:theorem:: 
    :label: thm-concave
    
    Giả sử :math:`f(x)` có đạo hàm trên :math:`\mathbb{I}`. Khi đó :math:`f(x)` lõm trên :math:`\mathbb{I}` khi và chỉ khi :math:`f'(x)` là hàm tăng không nghiêm ngặt (knn) trên :math:`\mathbb{I}`.

.. admonition:: Chứng minh chiều thuận
    :class: danger, dropdown

    Ta có :math:`f(x)` là hàm lõm trên :math:`\mathbb{I}` và ta cần chứng minh :math:`f'(x)` tăng knn trên :math:`\mathbb{I}`, nghĩa là

    .. math:: 
        f'(x_1) \leqslant f'(x_2)

    với mọi :math:`x_1, x_2 \in \mathbb{I}` mà :math:`x_1 < x_2`.

    Từ định nghĩa hàm lồi, ta chọn :math:`\alpha = \dfrac{x_2 - x}{x_2 - x_1}` và :math:`\beta = \dfrac{x - x_1}{x_2 - x_1}` với :math:`x_1 < x < x_2` thì khi đó :math:`\alpha, \beta > 0` và :math:`\alpha + \beta = 1`. Ta có

    .. math:: 
        f(x) = f\left(\dfrac{x_2 - x}{x_2 - x_1} x_1 + \dfrac{x - x_1}{x_2 - x_2} x_2\right) \leqslant \dfrac{x_2 - x}{x_2 - x_1} f(x_1) + \dfrac{x - x_1}{x_2 - x_1} f(x_2).

    Ta biến đổi bất đẳng thức như sau

    .. math:: 
        :label: eq-concave
        
        & (x_2 - x_1) f(x) \leqslant (x_2 - x) f(x_1) + (x - x_1) f(x_2) \\
        \Longleftrightarrow \ & (x_2 - x + x - x_1) f(x) \leqslant (x_2 - x) f(x_1) + (x - x_1) f(x_2) \\
        \Longleftrightarrow \ & (x_2 - x) \left[f(x) - f(x_1)\right] \leqslant (x - x_1) \left[f(x_2) - f(x)\right] \\
        \Longleftrightarrow \ & \dfrac{f(x) - f(x_1)}{x - x_1} \leqslant \dfrac{f(x_2) - f(x)}{x_2 - x}.  

    Cho :math:`x \to x_1^{+}` thì vế phải BĐT là đạo hàm phải tại :math:`x_1`, nghĩa là

    .. math:: f'(x_1) \leqslant \dfrac{f(x_2) - f(x_1)}{x_2 - x_1}.

    Tương tự, cho :math:`x \to x_2^{-}` thì vế trái BĐT là đạo hàm trái tại :math:`x_2`, nghĩa là

    .. math:: \dfrac{f(x_2) - f(x_1)}{x_2 - x_1} \leqslant f'(x_2).

    Từ hai BĐT vừa rồi suy ra :math:`f'(x_1) \leqslant f'(x_2)`. Ta có điều phải chứng minh.

.. admonition:: Chứng minh chiều ngược
    :class: danger, dropdown
    
    Ở phần trên ta dùng biến đổi tương đương để có :eq:`eq-concave`. Như vậy nếu chứng minh được :eq:`eq-concave` thì cũng đồng nghĩa :math:`f(x)` là hàm lõm.

    Theo định lí Lagrange tồn tại các số :math:`x_3` và :math:`x_4` sao cho :math:`x_1 < x_3 < x < x_4 < x_2` và

    .. math:: \dfrac{f(x) - f(x_1)}{x - x_1} = f'(x_3), \ \dfrac{f(x_2) - f(x)}{x_2 - x} = f'(x_4).

    Vì :math:`x_3 < x_4` và :math:`f'(x)` tăng knn trên :math:`\mathbb{I}` nên ta có :math:`f'(x_3) \leqslant f'(x_4)`, suy ra

    .. math:: \dfrac{f(x) - f(x_1)}{x - x_1} \leqslant \dfrac{f(x_2) - f(x)}{x_2 - x}.

    Như vậy :eq:`eq-concave` được chứng minh.

Một hệ quả quan trọng hay được sử dụng của định lí này như sau.

.. prf:corollary:: 
    :label: cor-thm-concave
    
    Nếu :math:`f(x)` liên tục trên :math:`\mathbb{I}` và có đạo hàm cấp hai trên :math:`\mathbb{I}` thì :math:`f(x)` lõm trên :math:`\mathbb{I}` khi và chỉ khi :math:`f''(x) \geqslant 0` với mọi :math:`x \in \mathbb{I}`.

Một số tính chất của hàm lồi và hàm lõm là:

1. Nếu :math:`f(x)` có đạo hàm và lõm trên khoảng :math:`\mathbb{I}` thì tiếp tuyến tại mọi điểm thuộc :math:`\mathbb{I}` của nó đều nằm phía dưới đồ thị của hàm :math:`f(x)`.
2. Nếu :math:`f(x)` có đạo hàm và lồi trên khoảng :math:`\mathbb{I}` thì tiếp tuyến tại mọi điểm thuộc :math:`\mathbb{I}` của nó đều nằm phía trên đồ thị của hàm :math:`f(x)`.
3. Nếu  :math:`f(x)` là hàm lõm trên đoạn :math:`[a; b]` thì ta có :math:`f(x) \leqslant \max\{f(a), f(b)\}` với mọi :math:`x \in [a; b]`. Nói cách khác, giá trị lớn nhất của :math:`f(x)` trên :math:`[a; b]` đạt được tại đầu mút của đoạn :math:`[a; b]`.
4. Tương tự, nếu :math:`f(x)` là hàm lồi trên đoạn :math:`[a; b]` thì giá trị nhỏ nhất của nó trên đoạn này đạt được tại đầu mút của đoạn :math:`[a; b]`.

----------------------------
Ý nghĩa hình học của hàm lõm
----------------------------

Giả sử hàm :math:`f(x)` lõm trên :math:`\mathbb{I}`. Lấy bất kì :math:`x_1, x_2 \in \mathbb{I}` với :math:`x_1 < x_2`.

Gọi :math:`M_1(x_1, f(x_1))` và :math:`M_2(x_2, f(x_2))` là hai điểm trên đồ thị hàm số :math:`y = f(x)`.

Khi đó điểm :math:`M'(x, y)` nằm trên đoạn thẳng :math:`M_1 M_2` khi và chỉ khi có số :math:`\alpha \in [0, 1]` sao cho :math:`\overrightarrow{M_2 M'} = \alpha \overrightarrow{M_2 M_1}` như trên hình vẽ sau.

.. figure:: ../../figures/calculus/concave_func.*

Điều kiện này tương đương với

.. math:: 

    \begin{cases}
        x - x_2 = \alpha(x_1 - x_2), \\ 
        y - f(x_2) = \alpha \left[f(x_1) - f(x_2)\right].
    \end{cases}

hay

.. math:: 

    \begin{cases}
        x = \alpha x_1 + (1 - \alpha) x_2, \\ 
        y = \alpha f(x_1) + (1 - \alpha) f(x_2).
    \end{cases}

Vì :math:`f(x)` lõm trên :math:`\mathbb{I}` nên ta có

.. math:: y_M = f(\alpha x_1 + (1-\alpha) x_2) \leqslant \alpha f(x_1) + (1 - \alpha) f(x_2) = y_M'.

Kết quả này cho chúng ta kết quả:

    Hàm số :math:`f(x)` lõm trên :math:`\mathbb{I}` khi và chỉ khi với mọi cặp điểm :math:`M_1`, :math:`M_2` thuộc đồ thị hàm số :math:`y = f(x)`, cung :math:`M_1 M_2` của đồ thị luôn nằm phía dưới đoạn thẳng :math:`M_1 M_2`.

-------------------
Điểm uốn của đồ thị
-------------------

.. prf:definition:: Điểm uốn của đồ thị
    :label: def-inflection
    
    Giả sử hàm số :math:`f(x)` có đạo hàm trên khoảng :math:`(a; b)` chứa :math:`x_0`. Nếu đồ thị :math:`(C)` của hàm số :math:`y = f(x)` lõm trên một trong hai khoảng :math:`(a, x_0)`, :math:`(x_0, b)` và lồi trên khoảng còn lại thì :math:`U(x_0, f(x_0))` được gọi là **điểm uốn** (hay **inflection point**, **точка перегиба**) của đồ thị :math:`(C)`.

    Nói cách khác, qua điểm uốn lồi thành lõm hoặc lõm thành lồi.

.. prf:remark:: 
    :label: rmk-inflection-tangent
    
    Tiếp tuyến tại điểm uốn đi xuyên qua đồ thị.

Điều này có nghĩa là trên một trong hai khoảng :math:`(a; x_0)`, :math:`(x_0; b)` thì tiếp tuyến tại :math:`x_0` nằm phía dưới đồ thị và trên khoảng còn lại thì tiếp tuyến đó nằm phía trên đồ thị.

Từ kết quả trên về tính lồi, lõm chúng ta có định lí sau là công cụ hữu ích để xác định điểm uốn của đồ thị.

.. prf:theorem:: 
    :label: thm-inflection
    
    Giả sử hàm số :math:`f(x)` có đạo hàm cấp hai trên khoảng :math:`\mathbb{I}` chứa điểm :math:`x_0`. Nếu :math:`f''(x_0) = 0` và :math:`f''(x)` đổi dấu khi :math:`x` đi qua điểm :math:`x_0` thì :math:`U(x_0, f(x_0))` là một điểm uốn của đồ thị hàm số :math:`y = f(x)`.
