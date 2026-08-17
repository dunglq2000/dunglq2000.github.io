========================
Tính đơn điệu và cực trị
========================

Đầu tiên chúng ta cần một định lý về tính đơn điệu của hàm số khả vi.

.. prf:theorem:: 
    :label: thm-der-monotone

    Xét hàm số :math:`f(x)` khả vi trên khoảng :math:`(a; b)`. Nếu :math:`f'(x) > 0` với mọi :math:`x \in (a; b)` thì :math:`f(x)` đồng biến trên :math:`(a; b)`.

.. admonition:: Chứng minh
    :class: danger, dropdown

    Theo định nghĩa đạo hàm thì

    .. math:: f'(x) = \lim_{\Delta x \to 0}\dfrac{f(x + \Delta x) - f(x)}{\Delta x} > 0.

    Như vậy, nếu :math:`\Delta x > 0` thì :math:`f(x + \Delta x) - f(x) > 0`. Ta cũng có :math:`x + \Delta x > x` nên từ đây suy ra :math:`f(x)` đồng biến trên :math:`(a; b)`.

Tương tự:

1. Nếu :math:`f'(x) < 0` với mọi :math:`x \in (a; b)` thì :math:`f(x)` nghịch biến trên :math:`(a; b)`.
2. Nếu :math:`f'(x) = 0` với mọi :math:`x \in (a; b)` thì :math:`f(x)` có giá trị không đổi trên :math:`(a; b)`.

.. prf:definition:: Cực tiểu của hàm số
    :label: def-minimum

    Xét hàm số :math:`f(x)` liên tục trên khoảng :math:`(a; b)`. Điểm :math:`(x_0, f(x_0))` được gọi là **cực tiểu** của hàm số :math:`f(x)` nếu tồn tại một lân cận :math:`U` chứa :math:`x_0` nằm trong khoảng :math:`(a; b)` sao cho với mọi :math:`x \in U` thì :math:`f(x) \geqslant f(x_0)`.

.. prf:definition:: Cực đại của hàm số
    :label: maximum

    Xét hàm số :math:`f(x)` liên tục trên khoảng :math:`(a; b)`. Điểm :math:`(x_0, f(x_0))` được gọi là **cực đại** của hàm số :math:`f(x)` nếu tồn tại một lân cận :math:`U` chứa :math:`x_0` nằm trong khoảng :math:`(a; b)` sao cho với mọi :math:`x \in U` thì :math:`f(x) \leqslant f(x_0)`.

Theo định nghĩa cực tiểu thì chỉ cần tồn tại lân cận chứa :math:`x_0` mà :math:`f(x) \geqslant f(x_0)` thì điểm đó là cực tiểu. Như vậy một hàm số có thể có nhiều cực tiểu, tương tự cũng có thể có nhiều cực đại.

Lưu ý rằng cực đại và cực tiểu không phải điểm chỉ giá trị lớn nhất hay giá trị nhỏ nhất của hàm số. Nó chỉ lớn nhất hoặc nhỏ nhất trong vùng lân cận đó theo định nghĩa, nên người ta còn gọi là cực trị địa phương.

Từ đó chúng ta có tính chất của cực trị.

.. prf:remark:: 
    :label: rmk-der-extremum

    Xét hàm số :math:`f(x)` khả vi trên khoảng :math:`(a; b)` và một điểm :math:`x_0 \in (a; b)`. Gọi :math:`f'(x)` là đạo hàm của :math:`f(x)` trên :math:`(a; b)`. Khi đó điểm :math:`x_0 \in (a; b)` được gọi là

    1. Nếu :math:`f'(x)` đổi chiều từ âm sang dương khi đi qua :math:`x_0` thì :math:`(x_0, f(x_0))` là điểm cực tiểu.
    2. Nếu :math:`f'(x)` đổi chiều từ dương sang âm khi đi qua :math:`x_0` thì :math:`(x_0, f(x_0))` là điểm cực đại.

.. prf:definition:: Dãy Cauchy
    :label: def-cauchy-list

    Dãy :math:`\{ x_n \}` được gọi là dãy Cauchy nếu với mọi :math:`\varepsilon > 0`, tồn tại :math:`N_0 \in \mathbb{N}` sao cho, với mọi :math:`m, n > N_0` thì :math:`\lvert x_m - x_n \rvert < \varepsilon`.

.. prf:theorem:: Tiêu chuẩn Cauchy
    :label: thm-cauchy-criteria

    Dãy số :math:`\{ x_n \}` có giới hạn hữu hạn khi và chỉ khi nó là dãy Cauchy.
