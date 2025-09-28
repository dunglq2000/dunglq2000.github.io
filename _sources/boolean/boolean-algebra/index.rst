Đại số Boolean
**************

Boolean (hay luận lý) chỉ giá trị đúng hoặc sai của mệnh đề nào đó. 

Theo cách hiểu cơ bản, boolean gồm hai giá trị :math:`0` hoặc :math:`1` (sai hoặc đúng). Chương này tham khảo chính từ :cite:`Tokareva1`, :cite:`Tokareva2` và :cite:`Pank14`.

Một số kí hiệu hay dùng:

1. Để chỉ tập hợp tất cả hàm boolean :math:`n` biến ta dùng :math:`\mathcal{F}_n`.
2. Để chỉ tập hợp tất cả hàm boolean affine :math:`n` biến ta dùng :math:`\mathcal{A}_n`.
3. Để chỉ tập hợp tất cả hàm boolean tuyến tính :math:`n` biến ta dùng :math:`\mathcal{L}_n`.

Hàm boolean :math:`f` đối với các biến :math:`x_1`, :math:`x_2`, ..., :math:`x_n` là hàm số nhận giá trị trong :math:`\mathbb{F}_2^n` và trả về giá trị thuộc :math:`\mathbb{F}_2`.

Nói cách khác :math:`f` là ánh xạ từ :math:`\mathbb{F}_2^n` tới :math:`\mathbb{F}_2`.

Ta kí hiệu hàm boolean :math:`n` biến là :math:`f(x_1, x_2, \ldots, x_n)`.

Do :math:`x_i \in \mathbb{F}_2` nên ta có :math:`2^n` vector (bộ số) :math:`(x_1, x_2, \ldots, x_n)`. Giá trị của hàm :math:`f` lại nằm trong tập :math:`\{ 0, 1 \}` nên ứng với mỗi vector có thể có :math:`2` giá trị của hàm boolean, và ta có :math:`2^n` vector nên số lượng hàm boolean có thể có là :math:`2^{2^n}`.

Một số toán tử boolean hay dùng: đối, AND, OR, XOR, NAND, NOR, kéo theo, tương đương.

Để biểu diễn hàm boolean chúng ta dùng bảng chân trị. Bảng chân
trị tương ứng với các toán tử boolean trên là:

+-------------+-------------+-----------------------+----------------------+------------------------+-----------------------+----------------------------+
|             |             | AND                   | OR                   | XOR                    | NAND                  | NOR                        |
+=============+=============+=======================+======================+========================+=======================+============================+
| :math:`x_1` | :math:`x_2` | :math:`x_1 \cdot x_2` | :math:`x_1 \vee x_2` | :math:`x_1 \oplus x_2` | :math:`x_1 \vert x_2` | :math:`x_1 \downarrow x_2` |
+-------------+-------------+-----------------------+----------------------+------------------------+-----------------------+----------------------------+
| :math:`0`   | :math:`0`   | :math:`0`             | :math:`0`            | :math:`0`              | :math:`1`             | :math:`1`                  |
+-------------+-------------+-----------------------+----------------------+------------------------+-----------------------+----------------------------+
| :math:`0`   | :math:`1`   | :math:`0`             | :math:`1`            | :math:`1`              | :math:`1`             | :math:`0`                  |
+-------------+-------------+-----------------------+----------------------+------------------------+-----------------------+----------------------------+
| :math:`1`   | :math:`0`   | :math:`0`             | :math:`1`            | :math:`1`              | :math:`1`             | :math:`0`                  |
+-------------+-------------+-----------------------+----------------------+------------------------+-----------------------+----------------------------+
| :math:`1`   | :math:`1`   | :math:`1`             | :math:`1`            | :math:`0`              | :math:`0`             | :math:`0`                  |
+-------------+-------------+-----------------------+----------------------+------------------------+-----------------------+----------------------------+

Toán tử đối làm đổi giá trị của hàm bool (:math:`0` thành :math:`1` và :math:`1` thành :math:`0`), kí hiệu :math:`\overline{x}`.

.. table:: Toán tử đối

    +-----------+----------------------+
    | :math:`x` | :math:`\overline{x}` |
    +===========+======================+
    | :math:`0` | :math:`1`            |
    +-----------+----------------------+
    | :math:`1` | :math:`0`            |
    +-----------+----------------------+

.. table:: Toán tử kéo theo và tương đương

    +-------------+-------------+-----------------------------+----------------------+
    | :math:`x_1` | :math:`x_2` | :math:`x_1 \rightarrow x_2` | :math:`x_1 \sim x_2` |
    +=============+=============+=============================+======================+
    | :math:`0`   | :math:`0`   | :math:`1`                   | :math:`1`            |
    +-------------+-------------+-----------------------------+----------------------+
    | :math:`0`   | :math:`1`   | :math:`1`                   | :math:`0`            |
    +-------------+-------------+-----------------------------+----------------------+
    | :math:`1`   | :math:`0`   | :math:`0`                   | :math:`0`            |
    +-------------+-------------+-----------------------------+----------------------+
    | :math:`1`   | :math:`1`   | :math:`1`                   | :math:`1`            |
    +-------------+-------------+-----------------------------+----------------------+

Toán tử tương đương còn chỉ sự tương đương của hai mệnh đề logic.

Khi hai biểu thức logic có cùng bảng chân trị thì hai mệnh đề đó tương đương nhau. Do đó ta có thể viết một số kết quả như sau (từ các bảng chân trị cơ bản trên):

- :math:`x_1 \vert x_2 \sim \overline{x_1 \cdot x_2}`. Ở đây ta đổi dấu từng giá trị hàm boolean :math:`x_1 \cdot x_2`;
- :math:`x_1 \downarrow x_2 \sim \overline{x_1 \vee x_2}`. Tương tự ta đổi dấu từng giá trị hàm boolean :math:`x_1 \vee x_2`.

.. toctree:: 
    :maxdepth: 2
    
    boolean-function
    boolean-affine
    boolean-monotone
    boolean-dnf-cnf
    boolean-weight
    walsh-hadamard-spectre
