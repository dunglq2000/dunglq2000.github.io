Giới thiệu
==========

Trung tâm của stream cipher và block cipher là các hàm Boolean. Ở những bài viết tiếp theo mình sẽ mô tả các đặc trưng khi xây dựng các hệ mật mã dạng dòng (stream cipher) và khối (block cipher) từ các hàm Boolean.

Nhắc lại, hàm Boolean :math:`n` biến là ánh xạ :math:`f` từ :math:`\{ 0, 1 \}^n` tới :math:`\{ 0, 1 \}`. Ở phần này mình sẽ sử dụng kí hiệu trường :math:`\mathbb{F}_2`. Như vậy hàm Boolean trên :math:`n` biến là ánh xạ

.. math:: f: \mathbb{F}_2^n \to \mathbb{F}_2, \quad f(x_1, x_2, \ldots, x_n) = y.

Tiếp theo, khi "ghép" các hàm Boolean lại ta có **hàm Boolean vector** (hay **vectorial Boolean function**). Như vậy hàm Boolean vector là ánh xạ

.. math:: F: \mathbb{F}_2^n \to \mathbb{F}_2^m, \quad f(x_1, x_2, \ldots, x_n) = (y_1, y_2, \ldots, y_m) \in \mathbb{F}_2^m.

Chúng ta có thể coi mỗi hàm :math:`y_i = f_i(x_1, \ldots, x_n)` là một hàm Boolean nên khi ghép cạnh nhau chúng ta có hàm Boolean vector.

.. only:: html

   .. table:: 
      :class: centered-table

      .. include:: tab-boolean.rst.inc

.. only:: latex

   .. tabularcolumns:: |c|c|c|c|c|c|c|c|

   .. include:: tab-boolean.rst.inc

Ở đây :math:`\bm{x} = (x_1, \ldots, x_n) \in \mathbb{F}_2^n`.

