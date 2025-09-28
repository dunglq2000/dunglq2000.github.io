====
NTRU
====

.. [#ntru-hrss-presentation] https://csrc.nist.gov/presentations/2018/ntru-hrss-kem

Đối với NTRU-HRSS mình sử dụng bài thuyết trình ở dự án PQC của NIST [#ntru-hrss-presentation]_.

Đối với NTRUEncrypt thì mình tham khảo :cite:`Hoffstein2014` (chương 7 về lattice). Mình sẽ sử dụng kí hiệu từ tài liệu này làm chuẩn cho cả NTRUEncrypt, NTRU-HRSS và NTRU.

----------------
Tham số cho NTRU
----------------

Các thuật toán NTRU hoạt động dựa trên các vành thương (quotient ring) sau:

.. math:: R = \frac{\mathbb{Z}[x]}{x^n - 1}, \quad R_p = \frac{(\mathbb{Z} / p\mathbb{Z})[x]}{x^n - 1}, \quad R_q = \frac{(\mathbb{Z} / q\mathbb{Z})[x]}{x^n - 1},

trong đó :math:`p`, :math:`q` và :math:`n` là các số nguyên tố khác nhau.

Ta cần định nghĩa một phép biến đổi gọi là *center-lift*. Trong các tài liệu khác thì gọi là phép *modular reduction*.

Với số nguyên :math:`n` cố định đóng vai trò modulo, ta xét phần tử

.. math:: r \in \{ 0, 1, \ldots, n - 1 \}.

Khi đó center-lift của :math:`r` là số :math:`r' \in \mathbb{Z}` sao cho :math:`-\dfrac{n}{2} < r' \leqslant \dfrac{n}{2}` và :math:`r \equiv r' \pmod{n}`.

Ví dụ, khi :math:`n = 8`:

- với :math:`r = 3` thì :math:`r' = 3`;
- với :math:`r = 6` thì :math:`r' = -2`.

Ta cần thêm tập

.. math:: 

    \mathcal{T}(d_1, d_2) = \left\{\begin{array}{cl}
    & : a(x) \ \text{có đúng} \ d_1 \ \text{hệ số bằng} \ 1 \\
    a(x) \in R & : a(x) \ \text{có đúng} \ d_2 \ \text{hệ số bằng} \ -1 \\
    & : a(x) \ \text{có các hệ số còn lại là} \ 0.
    \end{array}\right\}.

-----------
NTRUEncrypt
-----------

^^^^^^^^
Tạo khóa
^^^^^^^^

Chọn :math:`f(x) \in \mathcal{T}(d+1, d)` và :math:`g(x) \in \mathcal{T}(d, d)` ngẫu nhiên.

Ta tính

.. math:: 
    
    
        F_q(x) = f(x)^{-1} \in R_q, \\
        F_p(x) = f(x)^{-1} \in R_p.
    

Tiếp theo, tính

.. math:: h(x) = F_q(x) \cdot g(x) \in R_q.

Khi đó, private key là cặp :math:`(f(x), F_p(x))` và public key là :math:`h(x)`.

^^^^^^
Mã hóa
^^^^^^

Giả sử bản rõ là đa thức :math:`m(x) \in R` sao cho hệ số :math:`m_i` thỏa :math:`-\dfrac{p}{2} < m_i \leqslant \dfrac{p}{2}` (center-lift hệ số).

Chọn ngẫu nhiên đa thức :math:`r(x) \in \mathcal{T}(d, d)` và tính

.. math:: e(x) = p \cdot h(x) \cdot r(x) + m(x) \pmod{q}.

Khi đó bản mã là :math:`e(x) \in R_q`.

^^^^^^^
Giải mã
^^^^^^^

Để giải mã, ta tính

.. math:: a(x) = f(x) \cdot e(x) \pmod{q}.

Sau đó ta center-lift các hệ số của :math:`a(x)` thành đa thức thuộc :math:`R` rồi tính trong modulo :math:`p`:

.. math:: b(x) = F_p(x) \cdot a(x) \pmod{p}.

Khi đó :math:`b(x)` chính là bản rõ :math:`m(x)` ban đầu.

Ở đây, điều kiện của các tham số :math:`n`, :math:`p`, :math:`q` và :math:`d` để NTRUEncrypt hoạt động đúng là

.. math:: \boxed{q > (6d + 1) p.}

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Tính đúng đắn của quá trình giải mã
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Ta có

.. math:: 
    
    
        a(x) & \equiv f(x) \cdot e(x) \pmod{q} \\
        & \equiv f(x) \left(p \cdot h(x) \cdot r(x) + m(x)\right) \pmod{q} \\
        & \equiv p \cdot f(x) \cdot h(x) \cdot r(x) + f(x) \cdot m(x) \pmod{q} \\
        & \equiv p \cdot f(x) \cdot r(x) \cdot F_q(x) \cdot g(x) + f(x) \cdot m(x) \pmod{q} \\
        & \equiv p \cdot g(x) \cdot r(x) + f(x) \cdot m(x) \pmod{p}
    

vì :math:`f(x) \cdot F_q(x) \equiv 1 \pmod{q}`.

Xét đa thức :math:`p \cdot g(x) \cdot r(x) + f(x) \cdot m(x)` trong :math:`R` (center-lift). Ta có

.. math:: 
    
    
        b(x) & \equiv F_p(x) \cdot a(x) \pmod{p} \\
        & \equiv \underbrace{F_p(x) \cdot p \cdot g(x) \cdot r(x)}_{0} + \underbrace{F_p(x) \cdot f(x)}_{1} \cdot m(x) \pmod{p} \\
        & \equiv m(x) \pmod{p}.
    

^^^^^^^^^^^^
NTRU lattice
^^^^^^^^^^^^

Đặt public key

.. math:: h(x) = h_0 + h_1(x) + \cdots + h_{n-1} x^{n-1},

các hệ số đa thức tương ứng với vector

.. math:: \bm{h} = (h_0, h_1, \ldots, h_{n-1}).

Đặt

.. math:: 
    
    M^{\text{NTRU}}_{\bm{h}} = \left(\begin{array}{cccc|cccc}
        1 & 0 & \cdots & 0 & h_0 & h_1 & \cdots & h_{n-1} \\
        0 & 1 & \cdots & 0 & h_{n-1} & h_0 & \cdots & h_{n-2} \\
        \vdots & \vdots & \ddots & \vdots & \vdots & \vdots & \ddots & \vdots \\
        0 & 0 & \cdots & 1 & h_1 & h_2 & \cdots & h_0 \\ \hline
        0 & 0 & \cdots & 0 &  q & 0 & \cdots & 0 \\
        0 & 0 & \cdots & 0 & 0 & q & \cdots & 0 \\
        \vdots & \vdots & \ddots & \vdots & \vdots & \vdots & \ddots & \vdots \\
        0 & 0 & \cdots & 0 & 0 & 0 & \cdots & q
    \end{array}\right) = \left(\begin{array}{c|c}
        \bm{I}_n & \bm{h} \\ \hline \bm{O}_n & q \bm{I}_n
    \end{array}\right),

ở đây :math:`\bm{I}_n` là ma trận đơ đơn vị cấp :math:`n`, :math:`\bm{O}_n` là ma trận không cấp :math:`n`.

Giả sử

.. math:: 
    
    
        a(x) & = a_0 + a_1 x + \cdots + a_{n-1} x^{n-1}, \\
        b(x) & = b_0 + b_1 x + \cdots + b_{n-1} x^{n-1},
    

tương ứng với các vector

.. math:: \bm{a} = (a_0, a_1, \ldots, a_{n-1}), \quad \bm{b} = (b_0, b_1, \ldots, b_{n-1}).

Ta kí hiệu

.. math:: (\bm{a}, \bm{b}) = (a_0, a_1, \ldots, a_{n-1}, b_0, b_1, \ldots, b_{n-1}) \in \mathbb{Z}^{2n}.

Giả sử :math:`f(x) \cdot h(x) \equiv g(x) \pmod{q}`, đặt :math:`u(x) \in R` là đa thức thỏa

.. math:: f(x) \cdot g(x) = g(x) + q \cdot u(x).

Khi đó

.. math:: (\bm{f}, -\bm{u}) \cdot M^{\text{NTRU}}_{\bm{h}} = (\bm{f}, \bm{g})

nên vector :math:`(\bm{f}, \bm{g})` thuộc lattice :math:`L^{\text{NTRU}}_{\bm{h}}`.

---------
NTRU-HRSS
---------

Hệ mật mã NTRU-HRSS được nộp vòng 1 của dự án NIST PQC. Ở vòng 2, NTRU-HRSS hợp nhất với NTRUEncrypt trở thành NTRU.

^^^^^^^^
Tạo khóa
^^^^^^^^

Đối với NTRU-HRSS cần thêm các vành con của :math:`R_p` và :math:`R_q` xác định bằng đa thức cyclotomic. Ta kí hiệu đa thức cyclotomic thứ :math:`d` là :math:`\Phi_d`. Nhận xét bên trên:

- :math:`\Phi_1(x) = x - 1`;
- nếu :math:`d` là số nguyên tố thì

.. math:: \Phi_d(x) = 1 + x + \ldots + x^{d-1}.

Đặt :math:`S_p = \dfrac{(\mathbb{Z} / p\mathbb{Z})[x]}{\Phi_n(x)}` và :math:`S_q = \dfrac{(\mathbb{Z} / q\mathbb{Z})[x]}{\Phi_n(x)}` với :math:`p`, :math:`q` và :math:`n` là các số nguyên tố như trên.

Hơn nữa, Khi :math:`n` là số nguyên tố thì $x^n - 1 = \Phi_1(x) \Phi_n(x)$ và do đó

.. math:: R_p \cong \dfrac{(\mathbb{Z} / p\mathbb{Z})[x]}{\Phi_1(x)} \times S_p, \quad R_q \cong \dfrac{(\mathbb{Z} / q\mathbb{Z})[x]}{\Phi_1(x)} \times \mathcal{S}_q.

Thông thường ta chọn :math:`p = 3` và :math:`n = 701`. Việc chọn :math:`n` như vậy được (nhiều) người khẳng định là an toàn.

Đối với NTRU-HRSS-PKE, private key là một phần tử khác không :math:`f \in S_p`.

Từ :math:`f` ta tính public key :math:`h = \Phi_1(x) \cdot g \cdot f^{-1} \in R_q` với một phần tử :math:`g \in S_p`. Điều này đòi hỏi :math:`f` khả nghịch trong :math:`R_q`.

Để hỗ trợ giải mã ta cần nghịch đảo của :math:`f` trong :math:`S_p`. Ta viết nghịch đảo của :math:`f` trong :math:`R_q` và :math:`S_p` tương ứng là là :math:`f^{-1}_q` và :math:`f^{-1}_p`.

Theo cấu trúc thì :math:`f` khả nghịch trong cả :math:`S_p` và :math:`\mathcal{S}_q`.

Thay vì lấy :math:`f` và :math:`g` trực tiếp từ :math:`S_p` thì ta lấy từ tập con:

.. math:: \mathcal{T}^+ = \{ v \in S_p : \langle xv, v \rangle \geqslant 0 \}.

Thuật toán sinh khóa gồm các bước:

1. :math:`f \gets \mathcal{T}^+`.
2. :math:`f^{-1}_p \gets f^{-1} \in S_p`.
3. :math:`f^{-1}_q \gets f^{-1} \in \mathcal{S}_q`.
4. :math:`g \gets \mathcal{T}^+`.
5. :math:`h = \Phi_1(x) \cdot g \cdot f^{-1} \in R_q`.
6. Trả về public key là :math:`\text{pk} = h` và private key là :math:`\text{sk} = (f, f^{-1}_p)`.

^^^^^^
Mã hóa
^^^^^^

Gọi :math:`m \in S_p` là encode của bản rõ và :math:`r \in S_p` được chọn ngẫu nhiên.

Bản rõ :math:`e` được tính:

.. math:: e \gets p \cdot r \cdot h + [m]_3 \in R_q

Ở đây :math:`p = 3` là số nguyên tố bên trên.

^^^^^^^
Giải mã
^^^^^^^

Input: :math:`(e, (f, f^{-1}_3))` và hai vành :math:`(R_q, S_p)`.

Output: plaintext :math:`m'`:

.. math:: m' \gets [e \cdot f]_q \cdot f^{-1}_3 \in S_p.

Ở đây kí hiệu :math:`[e \cdot f]_q` nghĩa là phép tính diễn ra trong vành :math:`R_q`. Tương tự ở trên :math:`[m]_3` là encode của thông điệp :math:`m` trong :math:`S_p`.
