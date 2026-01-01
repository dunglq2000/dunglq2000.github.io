Hệ phương trình tuyến tính
**************************

Hệ phương trình tuyến tính
==========================

**Hệ phương trình tuyến tính** (hay **system of linear equations**, **система линейных уравнений**) là một tập các phương trình dạng

.. math:: 
   :label: eq-slq

   \left\{
      \begin{array}{ccc}
         a_{11} x_1 + a_{12} x_2 + \cdots + a_{1n} x_n & = & b_1 \\
         a_{21} x_2 + a_{22} x_2 + \cdots + a_{2n} x_n & = & b_2 \\
         \vdots & = & \vdots \\
         a_{m1} x_1 + a_{m2} x_2 + \cdots + a_{mn} x_n & = & b_m
      \end{array}
   \right.

Cụ thể hơn, nếu ta xét hệ trên một trường số nào đó (chẳng hạn :math:`\mathbb{R}`, :math:`\mathbb{C}`) thì các hệ số :math:`a_{ij}` và :math:`b_i` sẽ thuộc vào trường đó, :math:`1 \leqslant i \leqslant m`, :math:`1 \leqslant j \leqslant n`.

Xét hệ :eq:`eq-slq` trên trường :math:`\mathbb{F}`. **Nghiệm** (hay **solution**, **решение**) của hệ là bộ :math:`(\alpha_1, \alpha_2, \ldots, \alpha_n) \in \mathbb{F}^n` thỏa mãn

.. math:: 

   \left\{
      \begin{array}{ccc}
         a_{11} \alpha_1 + a_{12} \alpha_2 + \cdots + a_{1n} \alpha_n & = & b_1 \\
         a_{21} \alpha_1 + a_{22} \alpha_2 + \cdots + a_{2n} \alpha_n & = & b_2 \\
         \vdots & = & \vdots \\
         a_{m1} \alpha_1 + a_{m2} \alpha_2 + \cdots + a_{mn} \alpha_n & = & b_n
      \end{array}
   \right.

Tập nghiệm của hệ :eq:`eq-slq` là tập hợp tất cả bộ số :math:`(\alpha_1, \alpha_2, \ldots, \alpha_n) \in \mathbb{F}^n` thỏa mãn hệ phương trình.

Hai hệ phương trình được gọi là **tương đương** (hay **equivalent**, **эквивалентны**) nếu chúng có cùng tập nghiệm.

Tiếp theo chúng ta sẽ viết ma trận hệ số trước :math:`x_i` là :math:`\bm{A}` và cột hệ số tự do là :math:`\bm{b}`:

.. math:: 

   \bm{A} = \begin{pmatrix}
      a_{11} & a_{12} & \cdots & a_{1n} \\
      a_{21} & a_{22} & \cdots & a_{2n} \\
      \vdots & \vdots & \ddots & \vdots \\
      a_{m1} & a_{m2} & \cdots & a_{mn} \\
   \end{pmatrix}, \quad \bm{b} = \begin{pmatrix}
      b_1 \\ b_2 \\ \vdots \\ b_n
   \end{pmatrix}.

Ngoài ra ta cũng định nghĩa ma trận hệ số mở rộng bằng việc ghép thêm cột hệ số tự do vào sau ma trận :math:`\bm{A}`:

.. math:: 

   \begin{pmatrix}
      a_{11} & a_{12} & \cdots & a_{1n} & b_1 \\
      a_{21} & a_{22} & \cdots & a_{2n} & b_2 \\
      \vdots & \vdots & \ddots & \ddots & \vdots \\
      a_{m1} & a_{m2} & \cdots & a_{mn} & b_m \\
   \end{pmatrix}.

Phép biến đổi dòng (row operation) biến đổi một ma trận :math:`m \times n` thành một ma trận cùng cỡ và thuộc một trong các dạng sau

1. Đổi vị trí hai dòng.
2. Nhân tất cả phần tử của một dòng bất kì với phần tử khác không.
3. Nhân một dòng với một phần tử bất kì và cộng kết quả vào dòng khác. Dòng đầu giữ nguyên, dòng sau nhận kết quả là giá trị vừa tính được.

Hai ma trận được gọi là **tương đương dòng** (hay **row-equivalent**) nếu có một dãy các phép biến đổi dòng biến ma trận này thành ma trận kia.

Nếu hai ma trận hệ số mở rộng :math:`\bm{A}` và :math:`\bm{B}` tương đương dòng với nhau (qua các phép biến đổi dòng) thì hai hệ phương trình tuyến tính tương ứng tương đương với nhau.
