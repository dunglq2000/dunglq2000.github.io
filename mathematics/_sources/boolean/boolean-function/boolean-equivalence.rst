Các quan hệ tương đương của hàm vectorial
=========================================

Một hàm :math:`(n,m)` là ánh xạ

.. math:: F : \mathbb{F}_2^n \longrightarrow \mathbb{F}_2^m.

Các quan hệ tương đương dưới đây cho phép phân loại những hàm chỉ khác nhau bởi phép đổi tọa độ hoặc đổi biểu diễn. Ta kí hiệu :math:`\mathfrak{S}_n` là nhóm hoán vị trên :math:`[n]`.

Tương đương hoán vị, tuyến tính và affine
-----------------------------------------

.. prf:definition:: Tương đương hoán vị
   :label: def-permutation-equivalence

   Một hoán vị :math:`\sigma \in \mathfrak{S}_n` tác động lên :math:`\mathbb{F}_2^n` bởi

   .. math::

      \sigma(x_1, \ldots, x_n)
      = (x_{\sigma(1)}, \ldots, x_{\sigma(n)}).

   Hai hàm :math:`(n,m)` là :math:`F` và :math:`G` được gọi là **tương đương hoán vị** nếu tồn tại :math:`\sigma \in \mathfrak{S}_n` và :math:`\tau \in \mathfrak{S}_m` sao cho

   .. math:: G = \tau \circ F \circ \sigma.

.. prf:definition:: Tương đương tuyến tính
   :label: def-linear-equivalence-vectorial

   Hai hàm :math:`F` và :math:`G` được gọi là **tương đương tuyến tính** nếu

   .. math:: G = L' \circ F \circ L,

   trong đó :math:`L` và :math:`L'` lần lượt là các tự đẳng cấu tuyến tính của :math:`\mathbb{F}_2^n` và :math:`\mathbb{F}_2^m`.

   Viết vector dưới dạng hàng, mọi :math:`L` như vậy có dạng

   .. math:: L(\bm{x}) = \bm{x} M,

   với :math:`M \in \operatorname{GL}(n,2)`.

.. prf:definition:: Tương đương affine
   :label: def-affine-equivalence-vectorial

   Hai hàm :math:`F` và :math:`G` được gọi là **tương đương affine** nếu

   .. math:: G = A' \circ F \circ A,

   trong đó :math:`A` và :math:`A'` là các hoán vị affine. Chẳng hạn,

   .. math:: A(\bm{x}) = \bm{x} M + \bm{a}, \qquad M \in \operatorname{GL}(n,2).

Tương đương EA
--------------

.. prf:definition:: Tương đương affine mở rộng
   :label: def-ea-equivalence

   Hai hàm :math:`(n,m)` là :math:`F` và :math:`G` được gọi là **tương đương affine mở rộng** (extended-affine equivalent, hay **EA-equivalent**) nếu

   .. math:: G = A' \circ F \circ A + A'',

   trong đó :math:`A` và :math:`A'` là các hoán vị affine tương ứng trên miền xác định và miền giá trị, còn :math:`A'' : \mathbb{F}_2^n \to \mathbb{F}_2^m` là một hàm affine tùy ý:

   .. math:: A''(\bm{x}) = \bm{x} M'' + \bm{b},

   với :math:`M''` là ma trận :math:`n \times m` trên :math:`\mathbb{F}_2`.

Tương đương CCZ
---------------

.. prf:definition:: Đồ thị của hàm vectorial
   :label: def-graph-vectorial

   Đồ thị của :math:`F : \mathbb{F}_2^n \to \mathbb{F}_2^m` là tập

   .. math:: \mathcal{G}_F = \{(\bm{x}, F(\bm{x})) : \bm{x} \in \mathbb{F}_2^n\}.

.. prf:definition:: Tương đương CCZ
   :label: def-ccz-equivalence

   Hai hàm :math:`F, G : \mathbb{F}_2^n \to \mathbb{F}_2^m` được gọi là **tương đương CCZ** (Carlet--Charpin--Zinoviev equivalent) nếu tồn tại một hoán vị affine :math:`\mathcal{L}` của :math:`\mathbb{F}_2^{n+m}` sao cho

   .. math:: \mathcal{G}_G = \mathcal{L}(\mathcal{G}_F).

Giả sử viết

.. math::

   \mathcal{L}(\bm{x}, \bm{y})
   = \bigl(L_1(\bm{x}, \bm{y}), L_2(\bm{x}, \bm{y})\bigr),

trong đó :math:`L_1` nhận giá trị trong :math:`\mathbb{F}_2^n` và :math:`L_2` nhận giá trị trong :math:`\mathbb{F}_2^m`. Đặt

.. math::

   F_1(\bm{x}) = L_1(\bm{x}, F(\bm{x})), \qquad
   F_2(\bm{x}) = L_2(\bm{x}, F(\bm{x})).

Ảnh :math:`\mathcal{L}(\mathcal{G}_F)` là đồ thị của một hàm khi và chỉ khi :math:`F_1` là hoán vị của :math:`\mathbb{F}_2^n`. Khi đó hàm tương ứng là

.. math:: G = F_2 \circ F_1^{-1}.

Vì thế, tìm các hàm CCZ-equivalent với :math:`F` tương đương với tìm các hoán vị affine :math:`\mathcal{L} = (L_1,L_2)` sao cho :math:`F_1` là song ánh.

Nếu hai phép biến đổi CCZ của cùng :math:`F` có chung thành phần :math:`L_1` nhưng khác thành phần :math:`L_2`, hai hàm thu được là EA-equivalent. Đặc biệt, một hàm CCZ-equivalent với :math:`F` là EA-equivalent với :math:`F` hoặc :math:`F^{-1}` (khi :math:`F^{-1}` tồn tại) chính trong trường hợp có thể chọn :math:`L_1` chỉ phụ thuộc vào một trong hai biến :math:`\bm{x}` hoặc :math:`\bm{y}`.

Quan hệ giữa các dạng tương đương
---------------------------------

Mỗi quan hệ trong chuỗi sau kéo theo quan hệ đứng sau nó:

.. math::

   \text{hoán vị}
   \Longrightarrow \text{tuyến tính}
   \Longrightarrow \text{affine}
   \Longrightarrow \text{EA}
   \Longrightarrow \text{CCZ}.

Nhìn chung các chiều đảo lại không đúng. Riêng với một hoán vị :math:`F`, phép đổi chỗ hai thành phần của đồ thị cho thấy :math:`F` và :math:`F^{-1}` luôn CCZ-equivalent.

.. prf:definition:: Bất biến theo một quan hệ tương đương
   :label: def-equivalence-invariant

   Một tính chất hoặc tham số được gọi là **bất biến** đối với một quan hệ tương đương nếu nó có cùng giá trị trên mọi hàm thuộc cùng một lớp tương đương. Ta lần lượt có các khái niệm bất biến hoán vị, tuyến tính, affine, EA và CCZ.
