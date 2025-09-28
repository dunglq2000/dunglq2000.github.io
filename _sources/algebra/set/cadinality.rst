Lực lượng của tập hợp
=====================

Để chỉ số lượng phần tử của một tập hợp ta dùng khái niệm lực lượng của tập hợp.

Kí hiệu lực lượng của tập hợp :math:`A` là :math:`\lvert A \rvert` hoặc :math:`\# A`.

Khi một tập hợp có vô số phần tử, ta gọi đó là tập vô hạn. Ngược lại ta gọi là tập hữu hạn.

.. prf:example:: 
    :label: exp-cadinality

    Các tập hợp số thông dụng :math:`\mathbb{N}`, :math:`\mathbb{Z}`, :math:`\mathbb{Q}`, :math:`\mathbb{R}` là các tập vô hạn.

    Tập hợp :math:`A = \{ 1, 2, 3, 4, 5 \}` là tập hữu hạn có :math:`5` phần tử. Kí hiệu :math:`\lvert A \rvert = 5`.

Từ biểu đồ Venn chúng ta cũng có thể tìm được công thức tính lực lượng của tập :math:`A \cup B`.

.. _set4:

.. figure:: ../../figures/set/venn_diagram-4.*

    Nguyên lý bù trừ cho hai tập hợp

Dựa vào hình ta có thể suy ra công thức sau:

.. math:: \lvert A \cup B \rvert = \lvert A \rvert + \lvert B \rvert - \lvert A \cap B \rvert.
