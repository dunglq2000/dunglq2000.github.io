Симметричная криптография
*************************

Lời giải cho quyển sách :cite:`Tokareva1` của Н.Н. Токарева.

Глава 3. Булевы функции. Комбинаторный подход
=============================================

Bài 16. Chứng minh rằng, hàm Boolean :math:`f` tuyến tính khi và chỉ khi :math:`f(\bm{x} \oplus \bm{y}) = f(\bm{x}) \oplus f(\bm{y})` với mọi :math:`\bm{x}`, :math:`\bm{y}`. Tương tự kiểm tra hàm Boolean là affine khi và chỉ khi :math:`f(\bm{x} \oplus \bm{y}) = f(\bm{x}) \oplus f(\bm{y}) \oplus f(\bm{0})`.

.. admonition:: Chứng minh cho hàm tuyến tính
    :class: danger, dropdown

    **Chiều thuận.** Nếu :math:`f` là hàm tuyến tính thì nó có dạng

    .. math:: f(x_1, \ldots, x_n) = a_n x_n \oplus \cdots \oplus a_1 x_1

    nên ta tính :math:`f(\bm{x} \oplus \bm{y})` như sau

    .. math:: 

        f(\bm{x} \oplus \bm{y}) & = a_n (x_n \oplus y_n) \oplus \cdots \oplus a_1 (x_1 \oplus y_1) \\
        & = (a_n x_n \oplus \cdots \oplus a_1 x_1) \oplus (a_n y_n \oplus \cdots \oplus a_1 y_1) \\
        & = f(\bm{x}) \oplus f(\bm{y}).

    **Chiều nghịch.** Với :math:`f(\bm{x} \oplus \bm{y}) = f(\bm{x}) \oplus f(\bm{y})`, đặt dạng ANF của :math:`f` là

    .. math:: f(x_1, \ldots, x_n) = \left(\bigoplus_{k=1}^n \bigoplus_{i_1, \ldots, i_k} a_{i_1, \ldots, i_k} x_{i_1} \cdots x_{i_k}\right) \oplus a_0.

    Khi đó

    .. math:: f(\bm{x} \oplus \bm{y}) = \left(\bigoplus_{k=1}^n \bigoplus_{i_1, \ldots, i_k} a_{i_1, \ldots, i_k} (x_{i_1} \oplus y_{i_1}) \cdots (x_{i_k} \oplus y_{i_k})\right) \oplus a_0,

    và

    .. math:: 
        
        f(\bm{x}) \oplus f(\bm{y}) & = \left(\bigoplus_{k=1}^n \bigoplus_{i_1, \ldots, i_k} a_{i_1, \ldots, i_k} x_{i_1} \cdots x_{i_k}\right) \oplus a_0 \oplus \left(\bigoplus_{k=1}^n \bigoplus_{i_1, \ldots, i_k} a_{i_1, \ldots, i_k} y_{i_1} \cdots y_{i_k}.\right) \oplus a_0 \\
        & = \bigoplus_{k=1}^n \bigoplus_{i_1, \ldots, i_k} a_{i_1, \ldots, i_k} (x_{i_1} \cdots x_{i_k} \oplus y_{i_1} \cdots y_{i_k}).

    Như vậy, khi đồng nhất hệ số :math:`a_{i_1, \ldots, i_k}` của :math:`f(\bm{x} \oplus \bm{y})` và :math:`f(\bm{x}) \oplus f(\bm{y})` thì ta có

    .. math:: (x_{i_1} \oplus y_{i_1}) \cdots (x_{i_k} \oplus y_{i_k}) = x_{i_1} \cdots x_{i_k} \oplus y_{i_1} \cdots y_{i_k}.

    Ở vế trái khi khai triển ra ta sẽ nhận được các đơn thức dạng :math:`x_{i_1} y_{i_2} y_{i_3} \cdots y_{i_k}` khi :math:`k > 1`, tuy nhiên ở vế phải chỉ có đúng hai đơn thức là :math:`x_{i_1} \cdots x_{i_k}` và :math:`y_{i_1} \cdots y_{i_k}`. Do đó các hệ số :math:`a_{i_1, \ldots, i_k}` với :math:`k > 1` phải bằng :math:`0`. Hay nói cách khác bậc của ANF là :math:`1`. Ngoài ra :math:`f(\bm{x} \oplus \bm{y})` có hệ số tự do :math:`a_0` còn :math:`f(\bm{x}) \oplus f(\bm{y})` thì không có nên khi đồng nhất hệ số cũng cho ta :math:`a_0 = 0`. Như vậy :math:`f` là hàm tuyến tính.

.. admonition:: Chứng minh cho hàm affine
    :class: danger, dropdown

    **Chiều thuận.** Nếu :math:`f` là hàm tuyến tính thì nó có dạng

    .. math:: f(x_1, \ldots, x_n) = a_n x_n \oplus \cdots \oplus a_1 x_1 \oplus a_0

    và ta chứng minh tương tự cho trường hợp hàm tuyến tính với lưu ý :math:`f(\bm{0}) = a_0`.

    **Chiều nghịch.** Chứng minh tương tự cho trường hợp hàm tuyến tính.

Bài 17. Tìm số đỉnh và số cạnh của đồ thị :math:`E^n`. Có bao nhiêu vector :math:`\bm{x}, \bm{y} \in E^n` sao cho :math:`d(\bm{x}, \bm{y}) = k`?

Mỗi đỉnh của :math:`E^n` biểu diễn một vector dạng

.. math:: (z_1, \ldots, z_n), \quad z_i \in \{ 0, 1 \}

nên :math:`E^n` có :math:`2^n` đỉnh. Mỗi đỉnh nối với :math:`n` đỉnh khác (khác nhau chỉ ở vị trí :math:`z_i`) nên :math:`\deg v_i = n` với :math:`i = \overline{1, 2^n}`. Theo định lí cơ bản về số cạnh của đồ thị (:prf:ref:`thm-vertice-edges`) thì

.. math:: \text{số cạnh} = \dfrac{1}{2} \sum_{i=1}^{2^n} \deg v_i = \dfrac{1}{2} \cdot n \cdot 2^n = n \cdot 2^{n-1}.

Để :math:`d(\bm{x}, \bm{y}) = k` thì đầu tiên ta chọn :math:`k` vị trí khác nhau với :math:`C_n^k` cách. Với mỗi vị trí khác nhau ta có hai cách chọn :math:`x_i` và :math:`y_i` là

.. math:: 

    \begin{cases} x_i = 1 \\ y_i = 0 \end{cases}, \quad \text{hoặc} \ \begin{cases} x_i = 0 \\ y_i = 1 \end{cases}.

Do đó có :math:`2^k` cách chọn cho các vị trí khác nhau, còn :math:`n - k` vị trí còn lại thì chọn tùy ý nên có :math:`2^{n-k}` cách.

Đáp án là :math:`C_n^k \cdot 2^k \cdot 2^{n-k} = C_n^k \cdot 2^n`.

Bài 18. Tìm lực lượng của *mặt cầu* :math:`S_r(\bm{x}) = \{ \bm{y} : d(\bm{x}, \bm{y}) = r \}` và *hình cầu* :math:`B_r(\bm{x}) = \{ \bm{y} : d(\bm{x}, \bm{y}) \leqslant r \}`.

Đối với mặt cầu thì đáp án chính là bài 17, nghĩa là :math:`\lvert S_r(\bm{x}) \rvert = 2^r \cdot C_n^r`.

Đối với hình cầu :math:`B_r(\bm{x})` ta xét tất cả giá trị từ :math:`0` tới :math:`r`:

- khi :math:`d(\bm{x}, \bm{y}) = 0` thì có :math:`2^n \cdot C_n^0` cách chọn;
- khi :math:`d(\bm{x}, \bm{y}) = 1` thì có :math:`2^n \cdot C_n^1` cách chọn;
- tương tự, khi :math:`d(\bm{x}, \bm{y}) = i` thì có :math:`2^n \cdot C_n^i` cách chọn;
- cho tới khi :math:`d(\bm{x}, \bm{y}) = r` thì có :math:`2^n \cdot C_n^r` cách chọn.

Như vậy lực lượng của hình cầu là tổng tất cả giá trị trên:

.. math:: \lvert B_r(\bm{x}) \rvert = 2^n \cdot (C_n^0 + C_n^1 + \cdots + C_n^r).
