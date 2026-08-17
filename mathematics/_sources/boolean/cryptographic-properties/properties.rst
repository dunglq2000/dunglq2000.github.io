Các tính chất mật mã của hàm boolean
====================================

Bậc đại số cao
--------------

Tham số :math:`\deg f` phải cao. Điều này đặc biệt quan trọng trong các stream cipher sử dụng LFSR.

Nonlinearity cao
----------------

Nonlinearity cực kì quan trọng trong việc chống phá mã tuyến tính (linear cryptanalysis). Nonlinearity càng cao, dấu vết tuyến tính càng thấp.

Hàm boolean có nonlinearity cực đại được gọi là **hàm bent** (hay **bent function**).

Theo phần đại số boolean ở trước thì

.. math:: N_f \leqslant 2^{n-1} - \dfrac{1}{2} \cdot 2^{n / 2 - 1}

khi :math:`n` chẵn.

Điều kiện cần và đủ để tồn tại hàm bent :math:`n` biến là :math:`n` chẵn.

Nếu :math:`n` lẻ thì không tồn tại hàm bent :math:`n` biến. Tuy nhiên chúng ta vẫn có thể xem xét các hàm có nonlinearity :math:`N_f` lớn nhất và gọi chúng là **Almost Bent (AB)**.

Khi đó

.. math:: N_f \leqslant 2^{n-1} - 2^{(n-1) / 2}.

Balanced
--------

Hàm Boolean được gọi là **balanced** (hay **cân bằng**, **сбалансированный**) nếu nhận giá trị :math:`0` và :math:`1` nhiều như nhau. Như vậy nếu hàm boolean :math:`f` trên :math:`n` biến cân bằng khi và chỉ khi

.. math:: \mathrm{wt}(f) = 2^{n-1}.

**Bài tập:** Xác định số lượng hàm boolean cân bằng có :math:`n` biến.

:math:`r`-resillient
--------------------

Đặt :math:`r` là số nguyên không âm nhỏ hơn :math:`n`. Hàm boolean :math:`f` với :math:`n` biến được gọi là :math:`r`-resillient (hay :math:`r`-устойчивой) nếu với mọi hàm con mà nhận được từ việc cố định :math:`r` biến thì đều là hàm cân bằng.

Hàm boolean này có độ an toàn cao hơn so với hàm cân bằng, giúp chống lại cách tấn công correlation cryptanalysis.

Correlation immune
------------------

Hàm boolean :math:`f` với :math:`n` biến được gọi là **correlation immune of order** :math:`r` (**корреляционно-иммунной порядка** :math:`r`, tạm dịch là *kháng tương quan bậc* :math:`r`) với :math:`1 \leqslant r \leqslant n` nếu với mọi hàm con :math:`f^{a_1, \ldots, a_r}_{i_1, \ldots, i_r}` nhận được từ việc cố định :math:`r` biến thì đều thỏa đẳng thức

.. math:: \mathrm{wt} (f^{a_1, \ldots, a_r}_{i_1, \ldots, i_r}) = \frac{\mathrm{wt}(f)}{2^r}.

Algebraic immune
----------------

Tính chất này được giới thiệu vào năm 2004.

**Algebraic immune** (tạm dịch là *kháng đại số*) của hàm boolean :math:`f` là số :math:`d` nhỏ nhất sao cho tồn tại hàm boolean :math:`g` bậc :math:`d`, không đồng nhất với :math:`0`, thỏa mãn :math:`f g = 0` hoặc :math:`(f \oplus \bm{1}) g = 0`.

Algebraic immune của hàm :math:`f` được kí hiệu là :math:`\mathsf{AI}(f)`.

Ví dụ algebraic immune hàm :math:`f(\bm{x}) = x_1 x_2 x_3 \oplus x_1` bằng :math:`1`, vì ta có thể chọn :math:`g(\bm{x}) = x_1 \oplus 1`. Khi đó :math:`f g = (x_1 x_2 x_3 \oplus x_1) (x_1 \oplus 1) = 1`.

Differentially :math:`\delta`-uniform
--------------------------------------

Differential :math:`\delta`-uniform
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Khái niệm này lần đầu được định nghĩa trong :cite:`eurocrypt-1993-2628`.

Hàm boolean vector :math:`F : \mathbb{F}_2^n \to \mathbb{F}_2^n` gọi là **differentially** :math:`\delta`- **uniform** nếu với mọi vector :math:`\bm{a}` khác không và vector :math:`\bm{b}` bất kì thì phương trình

.. math:: F(\bm{x}) \oplus F(\bm{x} \oplus \bm{a}) = \bm{b}

có không quá :math:`\delta` nghiệm với :math:`\delta` là số nguyên dương.

Để ý rằng nếu phương trình có nghiệm là :math:`\bm{x}` thì cũng có nghiệm :math:`\bm{x} \oplus \bm{a}`. Số :math:`\delta` càng nhỏ thì phép biến đổi của thuật toán mã hóa càng ít có dấu hiệu vi sai, tăng khả năng kháng phá mã vi sai.

Một cách tổng quát ta có định nghĩa sau.

.. prf:definition:: Differential :math:`\delta`-uniform
   :label: def-delta-uniform

   Hàm boolean vector từ :math:`\mathbb{F}_p^n` tới :math:`\mathbb{F}_p^m` được gọi là **differential** :math:`\delta`- **uniform** nếu với mọi :math:`\bm{a} \in \mathbb{F}_p^n` khác không và với mọi :math:`\mathbb{F}_p^m` thì phương trình

   .. math:: F(\bm{x} + \bm{a}) - F(\bm{x}) = \bm{b}

   có không quá :math:`\delta` nghiệm.

Trong mật mã học thường dùng :math:`p = 2`. Thông thường các hàm boolean tập trung vào việc xây dựng các S-box nên :math:`n` thường là :math:`4` hoặc :math:`8`.

Perfect Nonlinear và Almost Perfect Nonlinear
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. prf:definition:: Hàm Perfect Nonlinear
   :label: def-PN

   Hàm boolean vector :math:`F` từ :math:`\mathbb{F}_p^n` tới :math:`\mathbb{F}_p^m` được gọi là hàm **Perfect Nonlinear (PN)** nếu phương trình

   .. math:: F(\bm{x} + \bm{a}) - F(\bm{x}) = \bm{b}

   có đúng :math:`p^{n-m}` nghiệm với mọi vector :math:`\bm{a} \in \mathbb{F}_p^n` khác không và :math:`\bm{b} \in \mathbb{F}_p^m`.

Số lượng hàm PN rất ít. Đối với các giá trị :math:`n` và :math:`p` thường được sử dụng trong mật mã thậm chí không tồn tại hàm PN. Do đó chúng ta sẽ nới lỏng điều kiện thành hàm Almost Perfect Nonlinear (APN).

.. prf:definition:: Hàm Almost Perfect Nonlinear
   :label: def-APN

   Hàm boolean vector :math:`F` từ :math:`\mathbb{F}_p^n` tới :math:`\mathbb{F}_p^m` được gọi là hàm **Almost Perfect Nonlinear (APN)** nếu phương trình

   .. math:: F(\bm{x} + \bm{a}) - F(\bm{x}) = \bm{b}

   có không quá hai nghiệm với mọi :math:`\bm{a} \in \mathbb{F}_p^n` khác không và với mọi :math:`\bm{b} \in \mathbb{F}_p^m`.

Bài toán khó hiện nay là xây dựng hàm APN là song ánh với số biến :math:`n` chẵn. Đặc biệt là :math:`n` có dạng lũy thừa của :math:`2`.

Như vậy, theo định nghĩa có thể thấy điều tương đương sau

- APN là differential :math:`2`-uniform.
- PN là differential :math:`1`-uniform khi :math:`n = m`.

Hoán vị APN
^^^^^^^^^^^

Từ trước tới nay có ba phương pháp xây dựng hoán vị APN trên :math:`\mathbb{F}_2^n`. Tuy nhiên cả ba phương pháp chỉ hoạt động trên :math:`n` lẻ. Câu hỏi về việc xây dựng hoán vị APN tới giờ vẫn là vấn đề mở với :math:`n` chẵn, dặc biệt là :math:`n` có dạng lũy thừa của :math:`2` như đã nói ở trên.

Lời giải cho các bài tập trên ở chương :ref:`chap_symmetric_cryptography`.
