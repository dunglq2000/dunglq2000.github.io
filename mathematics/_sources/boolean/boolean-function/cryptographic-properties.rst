Các tính chất mật mã của hàm Boolean
====================================

Hàm Boolean là thành phần trung tâm của nhiều stream cipher, còn hàm Boolean vectorial xuất hiện tự nhiên dưới dạng S-box trong block cipher. Các tính chất dưới đây đo khả năng chống lại những lớp tấn công khác nhau; trong thực tế thường phải cân bằng nhiều tiêu chí thay vì tối ưu riêng một tiêu chí.

Bậc đại số
-----------

Bậc đại số :math:`\deg(f)` nên đủ cao để cản trở việc biểu diễn hệ mật bằng các phương trình bậc thấp. Điều này đặc biệt quan trọng trong stream cipher sử dụng LFSR và trong các tấn công đại số.

Nonlinearity
------------

Nonlinearity đo khoảng cách từ hàm Boolean tới tập hàm affine và là một chỉ báo quan trọng đối với khả năng chống phân tích tuyến tính. Công thức qua phổ Walsh, bound cực đại và hàm Bent được trình bày tại :prf:ref:`rmk-bent`.

Với :math:`n` chẵn,

.. math:: N_f \leqslant 2^{n-1} - 2^{n/2-1}.

Dấu bằng xảy ra đúng với các hàm Bent. Hàm Bent không cân bằng, nên không thể đồng thời đạt nonlinearity cực đại và tính cân bằng.

Tính cân bằng
-------------

Theo :prf:ref:`def-balanced-bool`, hàm :math:`f : \mathbb{F}_2^n \to \mathbb{F}_2` cân bằng khi :math:`\mathrm{wt}(f)=2^{n-1}`. Điều kiện này tránh thiên lệch thống kê trực tiếp ở đầu ra. Theo tính chất của phổ Walsh, nó tương đương với :math:`W_f(\bm{0})=0`.

**Bài tập.** Xác định số lượng hàm Boolean cân bằng có :math:`n` biến. Lời giải
được trình bày trong phần đáp án bài tập sách của notebook *Contests*.

Kháng tương quan và resiliency
------------------------------

.. prf:definition:: Kháng tương quan bậc :math:`r`
   :label: def-correlation-immunity

   Hàm Boolean :math:`f` là **correlation-immune bậc** :math:`r` nếu đầu ra của nó độc lập thống kê với mọi tập gồm không quá :math:`r` biến đầu vào.

   Tương đương, với mọi :math:`I \subseteq [n]`, :math:`|I| \leqslant r`, và mọi phép gán :math:`\bm{a} \in \mathbb{F}_2^{|I|}`, restriction :math:`f_I^{\bm{a}}` thỏa

   .. math::

      \mathrm{wt}(f_I^{\bm{a}})
      = \frac{\mathrm{wt}(f)}{2^{|I|}}.

.. prf:definition:: Hàm :math:`r`-resilient
   :label: def-resilient-boolean

   Hàm :math:`f` được gọi là **:math:`r`-resilient** nếu nó vừa cân bằng vừa correlation-immune bậc :math:`r`. Tương đương, mọi hàm con thu được bằng cách cố định không quá :math:`r` biến đều cân bằng.

Resiliency là tiêu chí quan trọng đối với hàm kết hợp trong stream cipher vì giúp chống correlation attack.

Kháng đại số
------------

.. prf:definition:: Algebraic immunity
   :label: def-algebraic-immunity

   **Algebraic immunity** của :math:`f`, kí hiệu :math:`\mathsf{AI}(f)`, là số nguyên nhỏ nhất :math:`d` sao cho tồn tại hàm Boolean :math:`g \neq 0` với :math:`\deg(g)=d` và

   .. math:: fg=0

   hoặc

   .. math:: (f \oplus 1)g=0.

Hàm :math:`g` được gọi là một annihilator của :math:`f` hoặc :math:`f \oplus 1`. Algebraic immunity càng cao thì càng khó dựng quan hệ đại số bậc thấp phục vụ fast algebraic attack.

.. prf:example::
   :label: exp-algebraic-immunity

   Với

   .. math:: f(\bm{x}) = x_1x_2x_3 \oplus x_1,

   chọn :math:`g(\bm{x})=x_1\oplus1`. Khi đó

   .. math:: fg=x_1(x_2x_3\oplus1)(x_1\oplus1)=0,

   nên :math:`\mathsf{AI}(f)=1`.

Differential uniformity
-----------------------

.. prf:definition:: Differential :math:`\delta`-uniformity
   :label: def-delta-uniform

   Hàm :math:`F : \mathbb{F}_p^n \to \mathbb{F}_p^m` được gọi là **differentially :math:`\delta`-uniform** nếu, với mọi :math:`\bm{a} \in \mathbb{F}_p^n \setminus \{\bm{0}\}` và :math:`\bm{b} \in \mathbb{F}_p^m`, phương trình

   .. math:: F(\bm{x}+\bm{a})-F(\bm{x})=\bm{b}

   có không quá :math:`\delta` nghiệm :math:`\bm{x}`.

Số :math:`\delta` càng nhỏ thì phân phối sai khác đầu ra càng đều và S-box càng ít để lộ đặc trưng cho phân tích vi sai. Trong trường hợp nhị phân,

.. math:: F(\bm{x}+\bm{a})-F(\bm{x})
          =F(\bm{x}\oplus\bm{a})\oplus F(\bm{x}).

Nếu :math:`\bm{x}` là nghiệm thì :math:`\bm{x}\oplus\bm{a}` cũng là nghiệm, nên differential uniformity của một hàm nhị phân không hằng theo đạo hàm luôn là số chẵn.

Perfect nonlinear và almost perfect nonlinear
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. prf:definition:: Hàm perfect nonlinear
   :label: def-PN

   Hàm :math:`F : \mathbb{F}_p^n \to \mathbb{F}_p^m` được gọi là **perfect nonlinear** (PN) nếu, với mọi :math:`\bm{a}\neq\bm{0}` và mọi :math:`\bm{b}`, phương trình sai khác có đúng :math:`p^{n-m}` nghiệm.

Khi :math:`n=m`, điều này tương đương differential :math:`1`-uniformity. Vì nghiệm trong trường hợp nhị phân nghiệm đi thành cặp, không tồn tại hàm PN từ :math:`\mathbb{F}_2^n` tới chính nó.

.. prf:definition:: Hàm almost perfect nonlinear
   :label: def-APN

   Hàm nhị phân vectorial :math:`F : \mathbb{F}_2^n \to \mathbb{F}_2^m` được gọi là **almost perfect nonlinear** (APN) nếu nó differentially :math:`2`-uniform, tức mỗi phương trình

   .. math:: F(\bm{x}\oplus\bm{a})\oplus F(\bm{x})=\bm{b}

   có không quá hai nghiệm khi :math:`\bm{a}\neq\bm{0}`.

Việc xây dựng các hoán vị APN trong số biến chẵn là một bài toán quan trọng, đặc biệt đối với kích thước S-box là lũy thừa của :math:`2`.

Almost Bent
^^^^^^^^^^^

Với :math:`n` lẻ, một hàm vectorial :math:`F : \mathbb{F}_2^n \to \mathbb{F}_2^n` được gọi là **Almost Bent** (AB) nếu mọi component :math:`\langle\bm{b},F\rangle`, :math:`\bm{b}\neq\bm{0}`, có phổ Walsh thuộc

.. math:: \{0,\,\pm 2^{(n+1)/2}\}.

Khi đó nonlinearity vectorial đạt

.. math:: N_F=2^{n-1}-2^{(n-1)/2}.
