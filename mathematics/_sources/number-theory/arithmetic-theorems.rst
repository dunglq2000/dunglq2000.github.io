Các định lí số học quan trọng
=============================

Ta nhắc lại một số tính chất của ước chung lớn nhất và bội chung nhỏ nhất.

Gọi :math:`\gcd(a, b)` là ước chung lớn nhất của hai số nguyên :math:`a` và :math:`b`.

#. Với mọi số nguyên dương :math:`a`, :math:`\gcd(a, a) = a`.
#. Với mọi số nguyên :math:`a` và :math:`b` thì :math:`\gcd(a, b) = \gcd(b, a)`. Đây là tính giao hoán của ước chung lớn nhất.
#. Mọi ước chung của :math:`a` và :math:`b` sẽ chia hết :math:`\gcd(a, b)`.
#. Với mọi số nguyên :math:`m` thì :math:`\gcd(a + m b, b) = \gcd(a, b)`. Tương tự, :math:`\gcd(a \bmod b, b) = \gcd(a, b)`.
#. Với mọi số nguyên :math:`m` thì :math:`\gcd(m a, m b) = m\gcd(a, b)`.
#. Nếu :math:`\gcd(a, b) = d` thì :math:`\gcd(a/d, b/d) = 1`.

.. prf:theorem:: 
   :label: thm-m-n-gcd

   Với mọi số nguyên dương :math:`a`, :math:`m`, :math:`n` ta có

   .. math:: \gcd(a^m - 1, a^n - 1) = a^{\gcd(m, n)} - 1.

.. admonition:: Chứng minh
   :class: danger, dropdown

   Không mất tính tổng quát, giả sử :math:`m \geqslant n`. Ta có

   .. math:: 

      \gcd(a^m - 1, a^n - 1) & = \gcd(a^m - 1 - (a^n - 1), a^n - 1) \quad (\text{tính chất} \ \gcd(a, b) = \gcd(a + mb, b)) \\ 
      & = \gcd(a^{n}(a^{m-n} - 1) + a^n - 1, a^n - 1),

   mà :math:`\gcd(a^n, a^n - 1) = 1` nên

   .. math:: 

      \gcd(a^n(a^{m-n} - 1), a^n - 1) = \gcd(a^{m-n} - 1, a^n - 1).

   Thực hiện tương tự, cuối cùng ta có

   .. math:: \gcd(a^m - 1, a^n - 1) = \gcd(a^{m \bmod n} - 1, a^n - 1).

   Đặt :math:`m_1 = m \bmod n`, lúc này :math:`m_1 < n`. Thực hiện tương tự nhưng với chiều ngược lại

   .. math:: \gcd(a^{m_1} - 1, a^n - 1) = \gcd(a^{m_1} - 1, a^{n - m_1} - 1) = \cdots = \gcd(a^{m_1} - 1, a^{n \bmod m_1} - 1).

   Đây chính là thuật toán Euclid nhằm tìm ước chung lớn nhất (ở đây thực hiện trên số mũ). Do đó số mũ cuối cùng sẽ là ước chung lớn nhất giữa :math:`m` và :math:`n`.

