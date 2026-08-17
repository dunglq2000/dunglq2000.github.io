Biểu diễn hàm Boolean vectorial
===============================

Hàm tọa độ và ANF
-----------------

Một hàm :math:`(n,m)` là ánh xạ

.. math::

   F : \mathbb{F}_2^n \longrightarrow \mathbb{F}_2^m,
   \qquad
   F = (f_1, \ldots, f_m),

trong đó :math:`f_1, \ldots, f_m` là các hàm Boolean tọa độ.

Bảng chân trị của :math:`F` thu được bằng cách ghép các cột bảng chân trị của những hàm tọa độ:

.. list-table::
   :header-rows: 1
   :class: centered-table

   * - :math:`\bm{x}`
     - :math:`f_1(\bm{x})`
     - :math:`f_2(\bm{x})`
     - :math:`\cdots`
     - :math:`f_m(\bm{x})`
   * - :math:`(0,\ldots,0)`
     - :math:`f_1(0,\ldots,0)`
     - :math:`f_2(0,\ldots,0)`
     - :math:`\cdots`
     - :math:`f_m(0,\ldots,0)`
   * - :math:`\vdots`
     - :math:`\vdots`
     - :math:`\vdots`
     - :math:`\ddots`
     - :math:`\vdots`
   * - :math:`(1,\ldots,1)`
     - :math:`f_1(1,\ldots,1)`
     - :math:`f_2(1,\ldots,1)`
     - :math:`\cdots`
     - :math:`f_m(1,\ldots,1)`

Các quan hệ :math:`x_i^2=x_i` cho phép đồng nhất vành hàm Boolean với vành thương

.. math::

   \mathcal{B}_n
   = \frac{\mathbb{F}_2[x_1,\ldots,x_n]}
     {\langle x_1^2+x_1,\ldots,x_n^2+x_n\rangle}.

Vì thế mỗi lớp có duy nhất một đại diện multilinear, tức mỗi biến xuất hiện với số mũ không quá :math:`1`.

.. prf:definition:: ANF của hàm vectorial
   :label: def-anf-vectorial

   Algebraic normal form của :math:`F` là biểu diễn duy nhất

   .. math::

      F(\bm{x})
      = \sum_{I \subseteq [n]} \bm{a}_I \prod_{i \in I} x_i
      = \sum_{I \subseteq [n]} \bm{a}_I \bm{x}^I,

   trong đó :math:`\bm{a}_I \in \mathbb{F}_2^m` và tổng được tính theo từng tọa độ trong :math:`\mathbb{F}_2^m`.

Với :math:`\bm{u} \in \mathbb{F}_2^n`, đặt

.. math::

   \bm{x}^{\bm{u}} = \prod_{j \in [n]} x_j^{u_j},
   \qquad
   \operatorname{supp}(\bm{u}) = \{j \in [n] : u_j = 1\}.

Khi đó cũng có thể viết

.. math:: F(\bm{x}) = \sum_{\bm{u} \in \mathbb{F}_2^n} \bm{a}_{\bm{u}} \bm{x}^{\bm{u}}.

Nếu :math:`\bm{u} \lor \bm{v}` là phép OR theo từng tọa độ thì, trong vành các hàm Boolean,

.. math::

   \bm{x}^{\bm{u}} \bm{x}^{\bm{v}} = \bm{x}^{\bm{u} \lor \bm{v}},
   \qquad
   \operatorname{supp}(\bm{u} \lor \bm{v})
   = \operatorname{supp}(\bm{u}) \cup \operatorname{supp}(\bm{v}).

Từ công thức ANF suy ra

.. math:: F(\bm{x}) = \sum_{I \subseteq \operatorname{supp}(\bm{x})} \bm{a}_I.

Phép đảo Möbius cho hệ số
-------------------------

.. prf:theorem:: Công thức hệ số ANF
   :label: thm-vectorial-anf-coefficient

   Với mọi :math:`I \subseteq [n]`, hệ số ANF của :math:`F` là

   .. math::

      \bm{a}_I
      = \sum_{\substack{\bm{x} \in \mathbb{F}_2^n \\ \operatorname{supp}(\bm{x}) \subseteq I}}
        F(\bm{x}).

   Tổng được tính trong :math:`\mathbb{F}_2^m`. Với :math:`m=1`, đây chính là công thức biến đổi Möbius của hàm Boolean.

.. admonition:: Chứng minh
   :class: danger, dropdown

   Đặt vế phải là :math:`\bm{b}_I` và xét :math:`G(\bm{x}) = \sum_I \bm{b}_I \bm{x}^I`. Khi đổi thứ tự hai tổng, hệ số của :math:`F(\bm{y})` trong :math:`G(\bm{x})` là số tập :math:`I` thỏa

   .. math::

      \operatorname{supp}(\bm{y})
      \subseteq I
      \subseteq \operatorname{supp}(\bm{x}).

   Nếu :math:`\bm{y} \npreccurlyeq \bm{x}` thì không có tập nào. Nếu :math:`\bm{y} \preccurlyeq \bm{x}`, số tập như vậy là

   .. math:: 2^{\mathrm{wt}(\bm{x}) - \mathrm{wt}(\bm{y})}.

   Số này lẻ khi và chỉ khi :math:`\bm{x}=\bm{y}`. Vì tổng được tính trong đặc số :math:`2`, suy ra :math:`G(\bm{x})=F(\bm{x})`; tính duy nhất của ANF cho :math:`\bm{a}_I=\bm{b}_I`.

Indicator của đồ thị
--------------------

Với đồ thị

.. math:: \mathcal{G}_F = \{(\bm{x},F(\bm{x})) : \bm{x} \in \mathbb{F}_2^n\},

đặt :math:`\mathbf{1}_{\mathcal{G}_F}` là hàm Boolean trên :math:`\mathbb{F}_2^{n+m}` nhận giá trị :math:`1` đúng tại các điểm thuộc :math:`\mathcal{G}_F`.

.. prf:property:: ANF của graph indicator
   :label: prop-graph-indicator-anf

   Nếu :math:`F=(f_1,\ldots,f_m)` thì

   .. math::

      \mathbf{1}_{\mathcal{G}_F}(\bm{x},\bm{y})
      = \prod_{j \in [m]} (y_j \oplus f_j(\bm{x}) \oplus 1)

   và do đó

   .. math::

      \mathbf{1}_{\mathcal{G}_F}(\bm{x},\bm{y})
      = \bigoplus_{J \subseteq [m]}
        \bm{y}^J
        \prod_{j \in [m] \setminus J} (f_j(\bm{x}) \oplus 1).

Thật vậy, với hai vector :math:`\bm{y},\bm{y}' \in \mathbb{F}_2^m`, ta có

.. math::

   \prod_{j \in [m]} (y_j \oplus y'_j \oplus 1) = 1
   \quad\Longleftrightarrow\quad
   \bm{y}=\bm{y}'.

Hệ số của đơn thức :math:`\bm{x}^I \bm{y}^J` trong graph indicator là

.. math::

   a_{I,J}
   = \left|
      \left\{\bm{x} \in \mathbb{F}_2^n :
      \operatorname{supp}(\bm{x}) \subseteq I,
      \operatorname{supp}(F(\bm{x})) \subseteq J
      \right\}
     \right| \pmod 2.

Nếu :math:`F` là một hoán vị của :math:`\mathbb{F}_2^n`, đồ thị của hàm nghịch đảo thu được bằng cách đổi chỗ hai tọa độ:

.. math::

   \mathbf{1}_{\mathcal{G}_F}(\bm{x},\bm{y})
   = \mathbf{1}_{\mathcal{G}_{F^{-1}}}(\bm{y},\bm{x}).

Graph indicator cũng biểu diễn phép hợp thành. Nếu :math:`F : \mathbb{F}_2^n \to \mathbb{F}_2^m` và :math:`G : \mathbb{F}_2^m \to \mathbb{F}_2^r` thì

.. math::

   \mathbf{1}_{\mathcal{G}_{G \circ F}}(\bm{x},\bm{z})
   = \bigoplus_{\bm{y} \in \mathbb{F}_2^m}
     \mathbf{1}_{\mathcal{G}_F}(\bm{x},\bm{y})
     \mathbf{1}_{\mathcal{G}_G}(\bm{y},\bm{z}).

Bậc đại số
-----------

.. prf:definition:: Bậc của hàm vectorial
   :label: def-degree-vectorial

   Bậc đại số của :math:`F` là

   .. math::

      \deg(F)
      = \max\{|I| : I \subseteq [n],\ \bm{a}_I \neq \bm{0}\}.

   Tương đương,

   .. math:: \deg(F) = \max_{j \in [m]} \deg(f_j).

Nếu viết

.. math::

   \mathbf{1}_{\mathcal{G}_F}(\bm{x},\bm{y})
   = \bigoplus_{J \subseteq [m]} \varphi_J(\bm{x}) \bm{y}^J,

thì hệ số ứng với :math:`|J|=m-1` chính là một hàm tọa độ của :math:`F` hoặc bù của nó. Vì vậy

.. math:: \deg(F) = \max_{|J|=m-1} \deg(\varphi_J).

Ngoài ra,

.. math::

   \deg(\mathbf{1}_{\mathcal{G}_F})
   = \max_{J \subseteq [m]}
     \left(
       \deg\!\left(\prod_{j \in [m] \setminus J}(f_j \oplus 1)\right)
       + |J|
     \right),

nên

.. math::

   \deg(\mathbf{1}_{\mathcal{G}_F})
   \geqslant \max\{m,\,m-1+\deg(F)\}.

Graph indicator còn cho các chặn bậc hữu ích đối với phép hợp thành. Với

.. math::

   F : \mathbb{F}_2^n \to \mathbb{F}_2^m,
   \qquad
   G : \mathbb{F}_2^m \to \mathbb{F}_2^r,

ta có chặn Carlet

.. math::

   \deg(G \circ F)
   \leqslant
   \deg(\mathbf{1}_{\mathcal{G}_F}) + \deg(G) - m.

Tổng quát hơn, nếu :math:`H : \mathbb{F}_2^r \to \mathbb{F}_2^s` thì

.. math::

   \deg(H \circ G \circ F)
   \leqslant
   \deg(\mathbf{1}_{\mathcal{G}_F})
   + \deg(\mathbf{1}_{\mathcal{G}_G})
   + \deg(H) - m - r.

Biểu diễn đơn biến
------------------

Sau khi đồng nhất không gian vector :math:`\mathbb{F}_2^n` với trường :math:`\mathbb{F}_{2^n}`, mọi ánh xạ :math:`F : \mathbb{F}_{2^n} \to \mathbb{F}_{2^n}` có biểu diễn đa thức duy nhất

.. math:: F(x) = \sum_{i=0}^{2^n-1} \delta_i x^i,

với :math:`\delta_i \in \mathbb{F}_{2^n}`. Đây được gọi là **biểu diễn đơn biến** của :math:`F`. Ta cũng có thể xem nó là một phần tử của

.. math:: \mathbb{F}_{2^n}[X] / (X^{2^n} + X),

vì mọi phần tử của :math:`\mathbb{F}_{2^n}` đều thỏa :math:`x^{2^n}=x`.

Trường hợp hàm Boolean
^^^^^^^^^^^^^^^^^^^^^^

Một đa thức đơn biến

.. math:: f(x)=\sum_{i=0}^{2^n-1}\delta_i x^i

nhận giá trị trong :math:`\mathbb{F}_2` khi và chỉ khi :math:`f(x)^2=f(x)` với mọi :math:`x \in \mathbb{F}_{2^n}`. Do ánh xạ :math:`x \mapsto x^2` là tự đẳng cấu Frobenius, điều kiện này tương đương với

.. math::

   \sum_{i=0}^{2^n-1}\delta_i^2 X^{2i}
   \equiv
   \sum_{i=0}^{2^n-1}\delta_i X^i
   \pmod{X^{2^n}+X}.

Suy ra

.. math::

   \delta_0,\delta_{2^n-1} \in \mathbb{F}_2,
   \qquad
   \delta_{2i \bmod (2^n-1)}=\delta_i^2

với mọi :math:`i \in \{1,\ldots,2^n-2\}`.

Các quan hệ tương đương
-----------------------

Các quan hệ tương đương cho phép phân loại những hàm vectorial chỉ khác nhau bởi phép đổi tọa độ hoặc đổi biểu diễn.

.. prf:definition:: Tương đương hoán vị
   :label: def-permutation-equivalence

   Một hoán vị :math:`\sigma\in\mathfrak{S}_n` tác động lên :math:`\mathbb{F}_2^n` bởi

   .. math::

      \sigma(x_1,\ldots,x_n)
      =(x_{\sigma(1)},\ldots,x_{\sigma(n)}).

   Hai hàm :math:`(n,m)` là :math:`F` và :math:`G` **tương đương hoán vị** nếu tồn tại :math:`\sigma\in\mathfrak{S}_n` và :math:`\tau\in\mathfrak{S}_m` sao cho

   .. math:: G=\tau\circ F\circ\sigma.

.. prf:definition:: Tương đương tuyến tính
   :label: def-linear-equivalence-vectorial

   Hai hàm :math:`F` và :math:`G` **tương đương tuyến tính** nếu

   .. math:: G=L'\circ F\circ L,

   trong đó :math:`L` và :math:`L'` là các tự đẳng cấu tuyến tính của miền xác định và miền giá trị. Viết vector dưới dạng hàng, :math:`L(\bm{x})=\bm{x}M` với :math:`M\in\operatorname{GL}(n,2)`.

.. prf:definition:: Tương đương affine
   :label: def-affine-equivalence-vectorial

   Hai hàm :math:`F` và :math:`G` **tương đương affine** nếu

   .. math:: G=A'\circ F\circ A,

   trong đó :math:`A` và :math:`A'` là các hoán vị affine. Chẳng hạn,

   .. math:: A(\bm{x})=\bm{x}M+\bm{a}, \qquad M\in\operatorname{GL}(n,2).

.. prf:definition:: Tương đương affine mở rộng
   :label: def-ea-equivalence

   Hai hàm :math:`F` và :math:`G` **tương đương affine mở rộng** (extended-affine equivalent, hay **EA-equivalent**) nếu

   .. math:: G=A'\circ F\circ A+A'',

   trong đó :math:`A,A'` là các hoán vị affine và :math:`A'' : \mathbb{F}_2^n\to\mathbb{F}_2^m` là hàm affine tùy ý,

   .. math:: A''(\bm{x})=\bm{x}M''+\bm{b}.

Tương đương CCZ
^^^^^^^^^^^^^^^

.. prf:definition:: Tương đương CCZ
   :label: def-ccz-equivalence

   Hai hàm :math:`F,G : \mathbb{F}_2^n\to\mathbb{F}_2^m` **tương đương CCZ** (Carlet--Charpin--Zinoviev equivalent) nếu tồn tại một hoán vị affine :math:`\mathcal{L}` của :math:`\mathbb{F}_2^{n+m}` sao cho

   .. math:: \mathcal{G}_G=\mathcal{L}(\mathcal{G}_F).

Viết

.. math::

   \mathcal{L}(\bm{x},\bm{y})
   =\bigl(L_1(\bm{x},\bm{y}),L_2(\bm{x},\bm{y})\bigr),

trong đó :math:`L_1` nhận giá trị trong :math:`\mathbb{F}_2^n` và :math:`L_2` nhận giá trị trong :math:`\mathbb{F}_2^m`. Đặt

.. math::

   F_1(\bm{x})=L_1(\bm{x},F(\bm{x})),
   \qquad
   F_2(\bm{x})=L_2(\bm{x},F(\bm{x})).

Ảnh :math:`\mathcal{L}(\mathcal{G}_F)` là đồ thị của một hàm khi và chỉ khi :math:`F_1` là hoán vị của :math:`\mathbb{F}_2^n`. Khi đó

.. math:: G=F_2\circ F_1^{-1}.

Nếu hai phép biến đổi CCZ của cùng :math:`F` có chung :math:`L_1` nhưng khác :math:`L_2`, hai hàm thu được là EA-equivalent. Riêng với một hoán vị :math:`F`, phép đổi chỗ hai thành phần của đồ thị cho thấy :math:`F` và :math:`F^{-1}` luôn CCZ-equivalent.

Các quan hệ tạo thành chuỗi kéo theo

.. math::

   \text{hoán vị}
   \Longrightarrow\text{tuyến tính}
   \Longrightarrow\text{affine}
   \Longrightarrow\text{EA}
   \Longrightarrow\text{CCZ}.

Nhìn chung các chiều đảo lại không đúng.

.. prf:definition:: Bất biến theo một quan hệ tương đương
   :label: def-equivalence-invariant

   Một tính chất hoặc tham số được gọi là **bất biến** đối với một quan hệ tương đương nếu nó có cùng giá trị trên mọi hàm thuộc cùng một lớp tương đương.
