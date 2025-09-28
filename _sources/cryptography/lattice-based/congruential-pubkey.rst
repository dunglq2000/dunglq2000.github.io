====================================
Congruential public key cryptosystem
====================================

Thuật toán này mình lấy từ :cite:`Hoffstein2014`.

--------
Tạo khóa
--------

Trong thuật toán này, ta chọn số nguyên tố :math:`q` làm public parameter.

Sau đó chọn hai số :math:`f` và :math:`g` làm private key. Hai số này phải thỏa mãn các điều kiện

.. math:: f < \sqrt{q/2}, \quad \sqrt{q/4} < g < \sqrt{q/2}, \quad \gcd(f, qg) = 1.

Tính :math:`h \equiv f^{-1} g \pmod q`. Khi đó public key là :math:`h`.

------
Mã hóa
------

Để mã hóa thông điệp :math:`m`, ta chọn số một số ngẫu nhiên :math:`r` thỏa mãn 
 
.. math:: 0 < m < \sqrt{q/4}, \quad 0 < r < \sqrt{q/2}.

Tiếp theo, ta tính :math:`e \equiv rh + m \pmod q`.

Bản mã :math:`e` thỏa mãn :math:`0 < e < q`.

-------
Giải mã
-------

Từ bản mã :math:`e` ta giải mã bằng cách tính

.. math:: a \equiv fe \pmod q, \quad b \equiv f^{-1} a \pmod g.

Lưu ý :math:`f^{-1}` là nghịch đảo modulo :math:`g`. Khi đó :math:`b \equiv m` là message ban đầu.

.. admonition:: Chứng minh
    :class: danger, dropdown

    Để chứng minh rằng số :math:`b` sau khi tính toán bằng chính xác :math:`m` ban đầu ta cần xem xét điều kiện của private key và public key.
        
    Đầu tiên ta có 

    .. math:: a \equiv fe \equiv f(rh + m) \equiv f(r f^{-1} g + m) \equiv rg + fm \pmod q.
        
    Từ điều kiện của :math:`f`, :math:`g`, :math:`r` và :math:`m` ta có

    .. math:: rg + fm < \sqrt{\dfrac{q}{2}} \cdot \sqrt{\dfrac{q}{2}} + \sqrt{\dfrac{q}{2}} \cdot \sqrt{\dfrac{q}{4}} < q.
        
    Nói cách khác :math:`rg + fm` giữ nguyên giá trị trong phép modulo :math:`q`, hay :math:`a \equiv rg + fm`.
        
    Ta suy ra

    .. math:: b \equiv f^{-1} a \equiv f^{-1} (rg + fm) \equiv m \pmod g,

    ở đây giá trị :math:`a` không thay đổi khi chuyển từ modulo :math:`q` sang modulo :math:`g`.

    Do :math:`0 < m < \sqrt{q/4}` và :math:`\sqrt{q/4} < g < \sqrt{q/2}` nên :math:`m < g`. Nói cách khác :math:`b` bằng đúng :math:`m` ban đầu.

-----------------------
Ví dụ mã hóa và giải mã
-----------------------

Ta chọn số nguyên tố :math:`q = 3973659461` là public parameter.

Ta chọn :math:`f = 36624` và :math:`g = 33577` làm private key. Ở đây có thể kiểm tra điều kiện

.. math:: f < \sqrt{q/2}, \quad \sqrt{q/4} < g < \sqrt{q/2}, \quad \gcd(f, qg) = 1.

Lúc này public key là

.. math:: h \equiv f^{-1} g \equiv 3540857813 \pmod q.

Giả sử ta muốn mã hóa thông điệp :math:`\boxed{m = 1024}`.

Ta chọn (ngẫu nhiên) giá trị :math:`r = 21542`. Ta tính được bản mã là

.. math:: e \equiv rh + m \equiv 2765654775 \pmod{q}.

Để giải mã bản mã :math:`e = 2765654775` với private key :math:`f = 36624` và :math:`g = 33577`, đầu tiên ta tính

.. math:: a \equiv f e \equiv 760818710 \pmod q.

Tiếp theo tính

.. math:: b \equiv f^{-1} a \equiv 1024 \pmod g.

Như vậy :math:`b` bằng chính xác bản rõ :math:`m = 1024` ban đầu.

------
Phá mã
------

Để tấn công hệ mật mã này ta xây dựng lattice. Để ý rằng :math:`h = f^{-1} g \pmod q`, hay :math:`fh + kq = g` với :math:`k \in \mathbb{Z}`.

Ta thấy rằng :math:`f \cdot (h, 1) + k \cdot (q, 0) = (g, f)`. Như vậy cơ sở của lattice gồm hai vector :math:`(h, 1)` và :math:`(q, 0)`. Thuật toán rút gọn lattice Gauss sẽ hoạt động trong trường hợp này (số chiều bằng :math:`2`).
