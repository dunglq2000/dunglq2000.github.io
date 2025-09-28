==========================
Thuật toán rút gọn lattice
==========================

--------------------------------
Thuật toán rút gọn lattice Gauss
--------------------------------

Gọi :math:`L \subset \mathbb{R}^2` là lattice :math:`2` chiều với các vector cơ sở là :math:`\bm{v}_1` và :math:`\bm{v}_2`. Thuật toán rút gọn lattice Gauss (Gaussian Lattice Reduction) hoạt động như sau.

.. prf:algorithm:: Thuật toán rút gọn lattice Gauss
    :label: algo-gaussian-lattice-reduction
    
    1. Loop

       1. Nếu :math:`\lVert \bm{v}_2 \rVert < \lVert \bm{v}_1 \rVert` thì đổi chỗ :math:`\bm{v}_1` và :math:`\bm{v}_2` (swap).
       2. Tính :math:`m = \left\lfloor\dfrac{\bm{v}_1 \cdot \bm{v}_2}{\lVert \bm{v}_1 \rVert^2}\right\rceil`.
       3. Nếu :math:`m = 0` thì trả về cơ sở mới gồm các vector :math:`\bm{v}_1` và :math:`\bm{v}_2`.
       4. Thay :math:`\bm{v}_2` thành :math:`\bm{v}_2 - m \bm{v}_1`.
    
    2. Tiếp tục loop :)))

Sau khi thuật toán kết thúc thì :math:`\bm{v}_1` là vector khác không ngắn nhất trong :math:`L`, và do đó bài toán :math:`\texttt{SVP}` được giải quyết. Hơn nữa góc :math:`\theta` giữa :math:`\bm{v}_1` và :math:`\bm{v}_2` thỏa mãn

.. math:: \lvert\cos\theta\rvert \leqslant \lVert\bm{v}_1\rVert / 2\lVert\bm{v}_2\rVert,

cụ thể là :math:`\dfrac{\pi}{3} \leqslant \theta \leqslant \dfrac{2\pi}{3}`.

.. admonition:: Chứng minh
    :class: danger, dropdown

    Đầu tiên ta chứng minh :math:`\bm{v}_1` là vector khác không ngắn nhất trong :math:`L`.

    Giả sử thuật toán kết thúc và trả về hai vector :math:`\bm{v}_1` và :math:`\bm{v}_2`. Bước 1 của vòng lặp đảm bảo rằng :math:`\lVert \bm{v}_2 \rVert \geqslant \lVert \bm{v}_1 \rVert` và

    .. math::
        :label: v1:2:v2

        \frac{\lvert \bm{v}_1 \cdot \bm{v}_2 \rvert}{\lVert \bm{v}_1\rVert^2} \leqslant \frac{1}{2}

    vì đây là điều kiện để làm tròn :math:`\dfrac{\bm{v}_1 \cdot \bm{v}_2}{\lVert \bm{v}_1 \rVert^2}` thành :math:`0` và thỏa bước 3.

    Mỗi vector :math:`\bm{v}` khác không trong :math:`L` đều biểu diễn được dưới dạng

    .. math:: \bm{v} = a_1 \bm{v}_1 + a_2 \bm{v}_2, \quad a_1, a_2 \in \mathbb{Z}.

    Sử dụng :eq:`v1:2:v2` và bất đẳng thức quen thuộc :math:`\lvert x \rvert \geqslant -x` với mọi :math:`x \in \mathbb{R}` ta có

    .. math::
        
        \lVert \bm{v} \rVert^2 & = \lVert a_1 \bm{v}_1 + a_2 \bm{v}_2 \rVert^2 \\
        & = a_1^2 \lVert\bm{v}_1\rVert^2 + 2 a_1 a_2 \cdot \bm{v}_1 \cdot \bm{v}_2 + a_2^2 \lVert\bm{v}_2\rVert^2 \\
        & \geqslant a_1^2\lVert\bm{v}_1\rVert^2 - 2 \lvert a_1 a_2 \rvert \cdot \bm{v}_1 \cdot \bm{v}_2 + a_2^2 \lVert\bm{v}_2\rVert^2 \\
        & \geqslant a_1^2\lVert\bm{v}_1\rVert^2 - 2\lvert a_1 a_2 \rvert \cdot \lVert\bm{v}_1\rVert^2 + a_2^2\lVert\bm{v}_2\rVert^2 \\
        & \geqslant a_1^2\lVert\bm{v}_1\rVert^2 - 2\lvert a_1 a_2\rVert \cdot \lVert\bm{v}_1\rVert^2 + a_2^2 \lVert\bm{v}_1\rVert^2 \quad (\text{vì} \ \lVert\bm{v}_2\rVert \geqslant \lVert\bm{v}_1\rVert)  \\
        & = (a_1^2 - 2\lvert a_1 \rvert \cdot \lvert a_2\rvert + a_2^2) \lVert\bm{v}_1\rVert^2.
        

    Ta sử dụng bất đẳng thức quen thuộc: với mọi :math:`t_1, t_2 \in \mathbb{R}` thì

    .. math:: t_1^2 - 2 t_1 t_2 + t_2^2 = \left(t_1 - \frac{t_2}{2}\right)^2 + \frac{3}{4} \cdot t_2^2 = \frac{3}{4} \cdot t_1^2 + \left(\frac{t_1}{2} - t_2\right)^2 \geqslant 0.

    Biểu thức bằng :math:`0` khi và chỉ khi :math:`t_1 = t_2 = 0`. Vì :math:`a_1` và :math:`a_2` là các số nguyên không đồng thời bằng :math:`0` nên có thể suy ra :math:`\lVert\bm{v}\rVert^2 \geqslant \lVert\bm{v}_1\rVert^2` với mọi vector :math:`\bm{v}` khác không trong :math:`L`. Nói cách khác, :math:`\bm{v}_1` là vector khác không ngắn nhất trong :math:`L` và bài toán :math:`\texttt{SVP}` được giải xong.

    Tiếp theo, với :math:`\cos\theta`, ta có

    .. math:: \lvert\cos\theta\rvert = \left|\frac{\bm{v}_1 \cdot \bm{v}_2}{\lVert\bm{v}_1\rVert \cdot \lVert\bm{v}_2\rvert}\right| = \frac{\bm{v}_1 \cdot \bm{v}_2}{\lVert\bm{v}_1\rVert^2} \cdot \frac{\lVert\bm{v}_1\rVert}{\lVert\bm{v}_2\rVert} \leqslant \frac{1}{2} \cdot \frac{\lVert\bm{v}_1\rVert}{\lVert\bm{v}_2\rVert}.

    Hơn nữa :math:`\lVert \bm{v}_2 \rVert \geqslant \lVert \bm{v}_1 \rVert` nên suy ra

    .. math:: \lvert\cos\theta\rvert \leqslant \frac{1}{2} \cdot \frac{\lVert\bm{v}_1\rVert}{\lVert\bm{v}_2\rVert} \leqslant \frac{1}{2} \Longleftrightarrow -\frac{1}{2} \leqslant \cos\theta \leqslant \frac{1}{2} \Longleftrightarrow \frac{\pi}{3} \leqslant \theta \leqslant \frac{2\pi}{3}.

Mình sẽ ví dụ thuật toán trên qua việc phá mã congruential public key cryptosystem với số liệu đã trình bày trong bài viết.

Số nguyên tố :math:`q = 3973659461` là public parameter.

Ta đã chọn :math:`f = 36624` và :math:`g = 33577` làm private key. Ở đây :math:`f` và :math:`g` điều kiện

.. math:: f < \sqrt{q/2}, \quad \sqrt{q/4} < g < \sqrt{q/2}, \quad \gcd(f, qg) = 1.

Lúc này public key là

.. math:: h \equiv f^{-1} g \equiv 3540857813 \pmod q.

Để ý rằng :math:`h = f^{-1} g \pmod q`, tương đương :math:`fh + kq = g` với :math:`k \in \mathbb{Z}`.

Ta thấy rằng :math:`f \cdot (h, 1) + k \cdot (q, 0) = (g, f)`. Như vậy cơ sở của lattice gồm hai vector

.. math:: \{ (h, 1), (q, 0) \}.

Điều kiện của :math:`f` và :math:`g` cho ta tính chất quan trọng: vector :math:`(g, f)` ngắn trong lattice. Do đó thuật toán rút gọn lattice Gauss sẽ hoạt động trong trường hợp này (số chiều bằng :math:`2`).

Đặt :math:`\bm{v}_1 = (h, 1) = (3540857813, 1)` và :math:`\bm{v}_2 = (q, 0) = (3973659461, 0)`.

Bước 1, ta có

.. math:: \lVert\bm{v}_1\rVert = \sqrt{12537674051883142970} > \lVert\bm{v}_2\rVert = 3973659461

nên ta giữ nguyên :math:`\bm{v}_1` và :math:`\bm{v}_2`.

Tiếp theo ta tính

.. math:: m = \left\lfloor\frac{\bm{v}_1 \cdot \bm{v}_2}{\lVert\bm{v}_1\rVert^2}\right\rceil = \left\lfloor\frac{14070163148683218793}{12537674051883142970}\right\rceil = 1 \neq 0

nên ta thay :math:`\bm{v}_2` bởi :math:`\bm{v}_2 - m \bm{v}_1` thì

.. math:: \bm{v}_2 = (432801648, -1).

Bước 2, hiện tại

.. math:: \bm{v}_1 = (3540857813, 1), \ \bm{v}_2 = (432801648, -1)

nên

.. math:: \lVert\bm{v}_1\rVert < \lVert\bm{v}_2\rVert,

đổi chỗ :math:`\bm{v}_1` và :math:`\bm{v}_2` ta được

.. math:: \bm{v}_1 = (432801648, -1), \bm{v}_2 = (3540857813, 1).

Tiếp theo ta tính

.. math:: m = \left\lfloor\frac{\bm{v}_1 \cdot \bm{v}_2}{\lVert\bm{v}_1\rVert^2}\right\rceil = \left\lfloor\frac{1532489096800075823}{187317266511515905}\right\rceil = 8 \neq 0

nên ta thay :math:`\bm{v}_2` bởi :math:`\bm{v}_2 - m \bm{v}_1` thì

.. math:: \bm{v}_2 = (78444629, 9).


Cứ tiếp tục như vậy, vector :math:`\bm{v}_1`, :math:`\bm{v}_2` và giá trị :math:`m` sau bước 3 ở mỗi vòng lặp sẽ được thể hiện ở bảng sau.

+------+--------------------------+--------------------------+-------------+
| Loop | :math:`\bm{v}_1`         | :math:`\bm{v}_2`         | :math:`m`   |
+======+==========================+==========================+=============+
| 1    | :math:`(3540857813, 1)`  | :math:`(3973659461, 0)`  | :math:`1`   |
+------+--------------------------+--------------------------+-------------+
| 2    | :math:`(432801648, -1)`  | :math:`(3540857813, 1)`  | :math:`8`   |
+------+--------------------------+--------------------------+-------------+
| 3    | :math:`(78444629, 9)`    | :math:`(432801648, -1)`  | :math:`6`   |
+------+--------------------------+--------------------------+-------------+
| 4    | :math:`(-37866126, -55)` | :math:`(78444629, 9)`    | :math:`-2`  |
+------+--------------------------+--------------------------+-------------+
| 5    | :math:`(2712377, -101)`  | :math:`(-37866126, -55)` | :math:`-14` |
+------+--------------------------+--------------------------+-------------+
| 6    | :math:`(107152, -1469)`  | :math:`(2712377, -101)`  | :math:`25`  |
+------+--------------------------+--------------------------+-------------+
| 7    | :math:`(33577, 36624)`   | :math:`(107152, -1469)`  | :math:`1`   |
+------+--------------------------+--------------------------+-------------+
| 8    | :math:`(33577, 36624)`   | :math:`(73575, -38093)`  | :math:`0`   |
+------+--------------------------+--------------------------+-------------+

Vector :math:`\bm{v}_1` ở bước cuối chính xác là :math:`(g, f)` bên trên.
