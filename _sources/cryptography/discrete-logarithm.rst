Logarithm rời rạc
*****************

Các thuật toán tính logarithm rời rạc
=====================================

Thuật toán Baby-Step-Giant-Step
-------------------------------

Thuật toán Baby-Step-Giant-Step (BSGS) giúp tính discrete logarithm trên nhóm cyclic với order là số nguyên tố.

.. prf:algorithm:: Thuật toán Baby-Step-Giant-Step
   :label: alg-bsgs
   
   **Input:** Nhóm vòng :math:`G` có order :math:`n`, phần tử sinh :math:`g` và phần tử :math:`h \in G`.

   **Output:** Số :math:`x` duy nhất thuộc :math:`\{ 0, 1, \ldots, n-1 \}` thỏa :math:`g^x = h`.

   1. Đặt :math:`m = \lfloor \sqrt{n} \rfloor`
   2. For :math:`j = 0` to :math:`m-1`

      1. Tính :math:`g^j`. Lưu :math:`(j, g^j)` vào bảng
   
   3. Tính :math:`g^{-m}`
   4. :math:`\gamma = h`
   5. For :math:`i = 0` to :math:`m-1`
   
      1. Kiểm tra điều kiện :math:`\gamma \stackrel{?}{=} g^j` với :math:`j = 0, 1, \ldots, m-1`
      2. Nếu điều kiện thỏa, trả về :math:`im + j`
      3. Nếu không, đặt :math:`\gamma = \gamma \cdot g^{-m}`

Thuật toán Pohlig-Hellman cho order là lũy thừa nguyên tố
---------------------------------------------------------

Khi order của nhóm vòng là lũy thừa một số nguyên tố thì ta dùng thuật toán Pohlig-Hellman.

.. prf:algorithm:: Thuật toán Pohlig-Hellman
   :label: alg-pohlig-hellman-prime-order

   **Input:** Nhóm vòng :math:`G` có order :math:`n=p^e`, phần tử sinh :math:`g` và phần tử :math:`h \in G`.

   **Output:** Số :math:`x` duy nhất thuộc :math:`\{ 0, 1, \ldots, n-1 \}` thỏa :math:`g^x = h`.

   1. Khởi tạo :math:`x_0 = 0`
   2. Tính :math:`\gamma = g^{p^{e-1}}`. Theo định lý Lagrange, :math:`\gamma` có order là :math:`p`
   3. For :math:`k = 0` to :math:`e-1`

      1. Tính :math:`h_k = (g^{-x_k} \cdot h)^{e-1-k}`
      2. Sử dụng thuật toán BSGS (:prf:ref:`alg-bsgs`), tìm :math:`d_k \in \{ 0, 1, \ldots, p-1 \}` sao cho :math:`\gamma^{d_k} = h_k`. Bước này có độ phức tạp :math:`O(\sqrt{p})`
      3. Tính :math:`x_{k+1} = x_k + p^k d_k`
   
   4. Trả về :math:`x_e` là kết quả cần tìm.

Thuật toán Pohlig-Hellman tổng quát
-----------------------------------

.. prf:algorithm:: Thuật toán Pohlig-Hellman tổng quát
   :label: alg-pohlig-hellman-general

   **Input:** Nhóm vòng :math:`G` có order :math:`n`, phần tử sinh :math:`g`, phần tử :math:`h \in G`, và phân tích nhân tử :math:`n = \prod\limits_{i=1}^r p_i^{e_i}`

   **Output:** Số :math:`x` duy nhất thuộc :math:`\{ 0, 1, \ldots, n-1 \}` thỏa :math:`g^x = h`.

   1. For :math:`i = 1` to :math:`r`

      1. Tính :math:`g_i = g^{n / p_i^{e_i}}`. Theo định lí Lagrange thì :math:`g_i` có order là :math:`p_i^{e_i}`
      2. Tính :math:`h_i = h^{n / p_i^{e_i}}`. Khi đó :math:`h_i \in \langle g_i \rangle`
      3. Sử dụng thuật toán Pohlig-Hellman cho nhóm vòng :math:`\langle g_i \rangle` (:prf:ref:`alg-pohlig-hellman-prime-order`) để tính :math:`x_i \in \{ 0, \ldots, p_i^{e_i} - 1 \}` sao cho :math:`g_i^{x_i} = h_i`

   2. Giải hệ phương trình đồng dư

      .. math:: x \equiv x_i \pmod{p_i^{e_i}}

      với mọi :math:`i \in \{ 1, \ldots, r \}`

   3. Return :math:`x`
