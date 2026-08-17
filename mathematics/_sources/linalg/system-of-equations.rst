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

Giải hệ phương trình tuyến tính
===============================

Giả sử ta giải hệ phương trình tuyến tính

.. math:: \left\{\begin{array}{ccc}a_{11} x_1 + a_{12} x_2 + \cdots + a_{1n} x_n & = & b_1 \\ a_{21} x_1 + a_{22} x_2 + \cdots + a_{2n} x_n & = & b_2 \\ \ddots & = & \\ a_{n1} x_1 + a_{n2} x_2 + \cdots + a_{nn} x_n & = & b_n\end{array}\right.

Phương pháp Gauss
-----------------

Đặt

.. math:: \bm{A} = \begin{pmatrix} a_{11} & a_{12} & \cdots & a_{1n} & b_1 \\ a_{21} & a_{22} & \cdots & a_{2n} & b_2 \\ \vdots & \vdots & \ddots & \vdots & \vdots \\ a_{n1} & a_{n2} & \cdots & a_{nn} & b_n \end{pmatrix}.

Ta biến đổi thành dạng bậc thang

.. math:: \bm{A}' = \begin{pmatrix} a_{11} & a_{12} & \cdots & a_{1n} & b_1 \\ 0 & a_{22}' & \cdots & a_{2n}' & b_2' \\ \vdots & \vdots & \ddots & \vdots & \vdots \\ 0 & 0 & \cdots & a_{nn}' & b_n' \end{pmatrix}.

Ý tưởng: thực hiện :math:`n-1` lần biến đổi.

Ở lần thứ :math:`i`, ta làm cho :math:`a_{ji} = 0` với :math:`i + 1 \leqslant j \leqslant n` bằng cách:

.. math:: \text{dòng} \ j = \text{dòng} \ i \times m,

với :math:`m = \dfrac{-a_{ji}}{a_{ij}}`.

Sau đó tìm nghiệm ngược :math:`x_n`, rồi :math:`x_{n-1}`, ..., :math:`x_1`.

Ví dụ, xét hệ

.. math:: \begin{pmatrix}1 & 2 & 3 & -1 \\ 4 & 5 & 6 & -2 \\ 7 & 8 & 10 & -3\end{pmatrix} \to \begin{pmatrix}1 & 2 & 3 & -1 \\ 0 & -3 & -6 & 2 \\ 0 & -6 & -11 & 4\end{pmatrix} \to \begin{pmatrix}1 & 2 & 3 & -1 \\ 0 & -3 & -6 & 2 \\ 0 & 0 & 1 & 0\end{pmatrix},

như vậy

.. math:: x_3 = \dfrac{0}{1} = 0 \Longrightarrow x_2 = -\dfrac{2}{3} \Longrightarrow x_1 = \dfrac{1}{3}.

Thuật toán: ma trận :math:`(a_{ij})` với :math:`1 \leqslant i \leqslant n`, :math:`1 \leqslant j \leqslant n+1`.

For :math:`j = 1` to :math:`n-1`:

1. Tìm pivot: tìm phần tử pivot có giá trị tuyệt đối max ở cột :math:`j` (phần tử :math:`a_{ij}`) trong các hàng từ :math:`j` tới :math:`n`.
2. Sway hàng :math:`j` với hàng có pivot vừa rồi.
3. Khử các phần tử phía dưới:

   - for :math:`i = j+1` to :math:`n`: // hàng

     - tính :math:`m = a_{ij} / a_{jj}`
     - for :math:`k = j` to :math:`n+1`: // cột
       
       - :math:`a_{ik} = a_{ik} - m \cdot a_{jk}`.

Ở trên là khử tiến (forward elimination).

Tiếp theo, ở giai đoạn thế lùi (backward substitution), ta dùng ma trận tam giác trên ở giai đoạn khử tiến.

1. Tìm nghiệm cuối :math:`x_n = a_{n, n+1} / a_{nn}`.
2. For :math:`i = n-1` to 1:

   - tính :math:`S = \sum\limits_{k=i+1}^n a_{ik} \cdot x_k`
   - tính nghiệm :math:`x_i = (a_{i, n+1} - S) / a_{ii}`.

Phương pháp lặp Gauss-Siedel
----------------------------

Ta biến đổi hệ phương trình tuyến tính như sau: đầu tiên biểu diễn :math:`x_i` theo các biến khác ở phần tử thứ :math:`i`:

.. math:: \left\{\begin{array}{ccl}x_1 & = & \dfrac{1}{a_{11}}(b_1 - a_{12} x_2 - a_{13} x_3 - \cdots - a_{1n} x_n) \\ x_2 & = & \dfrac{1}{a_{22}}(b_2 - a_{21} x_1 - a_{23} x_3 - \cdots - a_{2n} x_n) \\ \vdots & = & \ddots \\ x_n & = & \dfrac{1}{a_{nn}}(b_n - a_{n1} x_1 - a_{n2} x_2 - \cdots - a_{n,n-1} x_{n-1})\end{array}\right.

Lấy vector khởi đầu :math:`\bm{x}^{(0)} = (x_1^{(0)}, x_2^{(0)}, \ldots, x_n^{(0)})`.

Với mỗi lần lặp :math:`k` ta tính

.. math:: \bm{x}_i^{(k+1)} = \dfrac{1}{a_{ii}}\left(b_i - \sum_{j=1}^{i-1} a_{ij} x_j^{(k+1)} - \sum_{j=i+1}^n a_{ij} x_j^{(k)}\right).

Với độ chính xác :math:`\varepsilon` cho trước, việc lặp dừng lại khi :math:`\lvert x_i^{(k+1)} - x_i^{(k)}\rvert < \varepsilon` với mọi :math:`i = \overline{1, n}`.

Khi đó :math:`\bm{x}^{(k)} = (x_1^{(k)}, \ldots, x_n^{(k)})` là nghiệm của hệ phương trình.

Điều kiện hội tụ là một trong ba điều kiện sau:

1. :math:`\max_i \sum\limits_{j=1}^n \lvert b_{ij} \rvert < 1`
2. :math:`\max_j \sum\limits_{i=1}^n \lvert b_{ij} \rvert < 1`
3. :math:`\sum\limits_{i=1}^n \sum\limits_{j=1}^n b_{ij}^2 < 1`

với :math:`b_{ij}` là hệ số của ma trận lặp :math:`\bm{B}` (vế phải), tức là

.. math:: \underbrace{\begin{pmatrix}x_1 \\ x_2 \\ \vdots \\ x_n\end{pmatrix}}_{\bm{x}} = \underbrace{\begin{pmatrix}0 & -a_{12} / a_{11} & \cdots & -a_{1n} / a_{11} \\ -a_{21} / a_{22} & 0 & \cdots & -a_{2n} / a_{22} \\ \vdots & \vdots & \ddots & \vdots \\ -a_{n1} / a_{nn} & -a_{n2} / a_{nn} & \cdots & 0\end{pmatrix}}_{\bm{B}} \underbrace{\begin{pmatrix}x_1 \\ x_2 \\ \vdots \\ x_n\end{pmatrix}}_{\bm{x}} + \underbrace{\begin{pmatrix}b_1 / a_{11} \\ b_2 / a_{22} \\ \vdots \\ b_n / a_{nn}\end{pmatrix}}_{\bm{g}},

hay :math:`\bm{x} = \bm{B} \cdot \bm{x} + \bm{g}`.

Phương pháp lặp Jacobi
----------------------

Phương pháp này khác với phương pháp lặp Gauss-Siedel ở chỗ, mỗi :math:`x_i^{(k+1)}`, với :math:`1 \leqslant i \leqslant n`, được tính bởi toàn bộ :math:`x_i^{(k)}` chứ không phải :math:`x_j^{(k+1)}` với :math:`1 \leqslant j \leqslant i-1` và :math:`x_j^{(k)}` với :math:`i + 1 \leqslant j \leqslant n`, hay

.. math:: x_i^{(k+1)} = \dfrac{1}{a_{ii}} \left(b_i - \sum_{j \neq i} a_{ij} x_j^{(k)}\right).
