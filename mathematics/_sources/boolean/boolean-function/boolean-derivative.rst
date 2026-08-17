Đạo hàm của hàm Boolean
=======================

Đạo hàm theo một hướng
----------------------

.. prf:definition:: Đạo hàm Boolean
   :label: def-boolean-derivative

   Với :math:`f : \mathbb{F}_2^n \to \mathbb{F}_2` và :math:`\bm{a} \in \mathbb{F}_2^n`, **đạo hàm của** :math:`f` **theo hướng** :math:`\bm{a}` là

   .. math:: D_{\bm{a}} f(\bm{x}) = f(\bm{x} + \bm{a}) \oplus f(\bm{x}).

Do làm việc trong đặc số :math:`2`, ta có

.. math:: D_{\bm{a}} D_{\bm{a}} f = 0.

.. prf:property:: Bậc của đạo hàm
   :label: prop-degree-boolean-derivative

   Nếu :math:`f` không hằng và :math:`\bm{a} \neq \bm{0}` thì

   .. math:: \deg(D_{\bm{a}} f) \leqslant \deg(f) - 1

   mỗi khi :math:`D_{\bm{a}}f` khác không. Hơn nữa, luôn tồn tại một hướng :math:`\bm{a}` sao cho

   .. math:: \deg(D_{\bm{a}} f) = \deg(f) - 1.

   Thật vậy, nếu một đơn thức bậc cao nhất chứa :math:`x_i`, đạo hàm theo vector đơn vị :math:`\bm{e}_i` loại :math:`x_i` khỏi đơn thức đó.

Đạo hàm cấp cao
---------------

.. prf:definition:: Đạo hàm cấp :math:`k`
   :label: def-higher-order-boolean-derivative

   Với :math:`\bm{a}_1, \ldots, \bm{a}_k \in \mathbb{F}_2^n`, đạo hàm cấp :math:`k` của :math:`f` theo các hướng này là

   .. math:: D_{\bm{a}_1} \cdots D_{\bm{a}_k} f.

Nếu :math:`\bm{a}_1, \ldots, \bm{a}_k` độc lập tuyến tính và :math:`E = \operatorname{span}(\bm{a}_1, \ldots, \bm{a}_k)` thì

.. math::

   D_{\bm{a}_1} \cdots D_{\bm{a}_k} f(\bm{x})
   = \bigoplus_{\bm{a} \in E} f(\bm{x} + \bm{a}).

Nếu các hướng phụ thuộc tuyến tính thì đạo hàm lặp trên bằng :math:`0`.

.. prf:corollary::
   :label: cor-degree-higher-derivative

   Nếu :math:`\deg(f) \geqslant k` thì mọi đạo hàm cấp :math:`k` thỏa

   .. math:: \deg(D_{\bm{a}_1} \cdots D_{\bm{a}_k}f) \leqslant \deg(f) - k,

   nếu đạo hàm ở vế trái khác :math:`0`; trường hợp nó bằng :math:`0` là hiển nhiên.

Đặc trưng bậc bằng affine flat
------------------------------

Một **affine flat** chiều :math:`k` là một tập :math:`A = \bm{a} + E`, trong đó :math:`E` là không gian con tuyến tính chiều :math:`k` của :math:`\mathbb{F}_2^n`. Ràng buộc :math:`f|_A` có thể xem như một hàm Boolean :math:`k` biến.

.. prf:property:: Tiêu chuẩn affine flat cho bậc đại số
   :label: prop-degree-affine-flat

   Hàm Boolean :math:`f` có bậc không quá :math:`d` khi và chỉ khi ràng buộc của nó trên mọi affine flat chiều :math:`d+1` có trọng số chẵn.

   Tương đương,

   .. math:: \bigoplus_{\bm{x} \in A} f(\bm{x}) = 0

   với mọi affine flat :math:`A` chiều :math:`d+1`.

Để có :math:`\deg(f) = d`, ngoài điều kiện trên phải tồn tại ít nhất một affine flat chiều :math:`d` mà ràng buộc của :math:`f` trên đó có trọng số lẻ.

Biến đổi Möbius và bậc
----------------------

Nếu :math:`\mu(f)` là biến đổi Möbius nhị phân của hàm Boolean khác hằng :math:`0`, ta có bất đẳng thức Pieprzyk--Zhang

.. math:: \deg(f) + \deg(\mu(f)) \geqslant n.

Các hàm thỏa :math:`\mu(f) = f` được gọi là **hàm coincident**.
