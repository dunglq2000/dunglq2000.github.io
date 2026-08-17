Goppa Code
==========

Goppa code được sử dụng trong thuật toán Classic McEliece, 
là một thuật toán mã hóa khóa công khai thuộc post-quantum 
cryptography. Phần này mình sử dụng slide bài giảng [#kirshanova]_.

.. [#kirshanova] https://crypto-kantiana.com/elena.kirshanova/talks/Talk_McEliece.pdf


Thiết lập Goppa Code
---------------------

Đầu tiên ta chọn số nguyên :math:`m \geqslant 1` và 
số nguyên tố :math:`q \geqslant 2` nhằm xác định 
trường :math:`\mathbb{F}_{q^m}`.

Chọn tập

.. math:: L = \{ \alpha_1, \ldots, \alpha_n \}

sao cho :math:`\alpha_i \in \mathbb{F}_{q^m}` đôi một 
khác nhau và :math:`n \leqslant q^m`.

Ta chọn đa thức :math:`g(x)` bậc không quá :math:`t` 
với hệ số trong :math:`\mathbb{F}_{q^m}`, sao cho 
:math:`g(x)` không có nghiệm bội và :math:`g(\alpha_i) \neq 0` 
với mọi :math:`i = 1, \ldots, n`.

Khi đó Goppa code :math:`\mathcal{C}` với độ dài :math:`n` là:

.. math:: 
    
    \mathcal{C} = \Gamma(L, g) = \left\{
        \bm{c} = (c_1, \ldots, c_n) \in \mathbb{F}_q^n : 
        \sum_{i=1}^n \frac{c_i}{x - \alpha_i} = 0 \bmod{g(x)}
    \right\},

nghĩa là Goppa code :math:`\mathcal{C}` gồm các vector 
:math:`\bm{c} \in \mathbb{F}_q^n` sao cho tổng

.. math:: \frac{c_1}{x - \alpha_1} + \frac{c_2}{x - \alpha_2} + \cdots + \frac{c_n}{x - \alpha_n} = 0 \bmod{g(x)}.

Dễ thấy khi biến đổi tương đương ta có

.. math:: \dfrac{1}{x - \alpha_i} = -\dfrac{g(x) - g(\alpha_i)}{x - \alpha_i} \cdot g^{-1}(\alpha_i) \bmod{g(x)}.

Trong Classic McEliece thì :math:`q = 2` 
và :math:`g(x)` là đa thức monic và tối giản.

-------------------------
Tìm ma trận parity-check
-------------------------

Giả sử

.. math:: g(x) = g_0 + g_1 x + \cdots + g_t x^t = \sum_{i=0}^t g_i x^i

với :math:`g_i \in \mathbb{F}_{q^m}`.

Ta có

.. math:: 

    \frac{g(x) - g(\alpha_i)}{x - \alpha_i} 
        & = \frac{g_t(x^t - \alpha_i^t) + \cdots + g_1(x - \alpha_i) + g_0 \cdot 0}{x - \alpha_i} \\
        & = g_t(x^{t-1} + x^{t-2} \alpha_i + x^{t-3} \alpha_i^2 + \cdots + \alpha_i^{t-1}) \\
        & \ + g_{t-1}(x^{t-2} + x^{t-3} \alpha_i + x^{t-4} \alpha_i^2 + \cdots + \alpha_i^{t-2}) \\
        & \ + \cdots + g_2(x + \alpha_i) + g_1 \\
        & = g_t x^{t-1} + (g_t \alpha_i + g_{t-1}) x^{t-2} \\
        & \ + (g_t \alpha_i^2 + g_{t-1} \alpha_i + g_{t-2}) x^{t-3} \\
        & \ + \cdots \\
        & \ + (g_t \alpha_i^{t-1} + g_{t-1} \alpha_i^{t-2} + \cdots + g_2 \alpha_i + g_1).

Như vậy, hệ số trước :math:`x^j` của codeword

.. math:: \sum_{i=1}^n c_i \cdot \frac{g(x) - g(\alpha_i)}{x - \alpha_i} \cdot g^{-1}(\alpha_i)

lần lượt là

.. math:: 
    
    \begin{array}{ccc}
        x^{t-1} & : & g_t g^{-1}(\alpha_1) c_1 + \cdots + g_t g^{-1}(\alpha_n) c_n \\
        x^{t-2} & : & (g_t \alpha_1 + g_{t-1}) g^{-1}(\alpha_1) c_1 + \cdots + (g_t \alpha_n + g_{t-1}) g^{-1}(\alpha_n) c_n \\
        \vdots \\
        x^0 & : & \substack{(g_t \alpha_1^{t-1} + g_{t-1} \alpha_1^{t-2} + \cdots + g_2 \alpha_1 + g_1) c_1 + (g_t \alpha_2^{t-1} + g_{t-1} \alpha_2^{t-2} + \cdots + g_2\alpha_2 + g_1) c_2 \\ + \cdots + (g_t \alpha_n^{t-1} + g_{t-1} \alpha_n^{t-2} + \cdots + g_2\alpha_n + g_1) c_n}
    \end{array}.

Khi đó, :math:`\bm{c} \in \Gamma(L, g)` khi và chỉ khi 
tất cả hệ số trước :math:`x^j` bằng :math:`0`. Điều này 
tương đương với :math:`\overline{\bm{H}} \bm{c}^\intercal = 0` 
với :math:`\overline{\bm{H}} \in \mathbb{F}_{q^m}^{t \times n}`.

Ở đây

.. math:: 

    \overline{H} & = \begin{pmatrix}
        g_t \cdot g^{-1}(\alpha_1) & \cdots & g_t \cdot g^{-1}(\alpha_n) \\
        (g_t \alpha_1 + g_{t-1}) \cdot g^{-1}(\alpha_1) & \cdots & (g_t \alpha_n + g_{t-1}) \cdot g^{-1}(\alpha_n) \\
        \vdots & \ddots & \vdots \\
        (g_t \alpha_1^{t-1} + g_{t-1} \alpha_1^{t-2} + \cdots + g_2 \alpha_1 + g_1) \cdot g^{-1}(\alpha_1) & \cdots & (g_t \alpha_n^{t-1} + g_{t-1} \alpha_n^{t-2} + \cdots + g_2 \alpha_n + g_1) \cdot g^{-1}(\alpha_n)
    \end{pmatrix} \\
    & = \underbrace{\begin{pmatrix}
        g_t & 0 & \cdots & 0 \\ g_{t-1} & 0 & \cdots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ g_1 & g_2 & \cdots & g_t
    \end{pmatrix}}_{\bm{G}} \cdot \underbrace{\begin{pmatrix}
        1 & 1 & \cdots & 1 \\ \alpha_1 & \alpha_2 & \cdots & \alpha_n \\ \vdots & \vdots & \ddots & \vdots \\ \alpha_1^{t-1} & \alpha_2^{t-1} & \cdots & \alpha_n^{t-1}
    \end{pmatrix}}_{\bm{X}} \cdot \underbrace{\begin{pmatrix}
        g^{-1}(\alpha_1) & 0 & \cdots & 0 \\ 0 & g^{-1}(\alpha_2) & \cdots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \cdots & g^{-1}(\alpha_n)
    \end{pmatrix}}_{\bm{Y}}.

Ma trận :math:`\bm{G}` khả nghịch, đặt

.. math:: 
    
    \bm{H} = \bm{G}^{-1} \overline{\bm{H}} = \begin{pmatrix}
        g^{-1}(\alpha_1) & \cdots & g^{-1}(\alpha_n) \\
        \alpha_1 g^{-1}(\alpha_1) & \cdots & \alpha_n g^{-1}(\alpha_n) \\
        \vdots & \ddots & \vdots \\
        \alpha_1^{t-1} g^{-1}(\alpha_1) & \cdots & \alpha_n^{t-1} g^{-1}(\alpha_n)
    \end{pmatrix} \in \mathbb{F}_{q^m}^{t \times n}.

Khi khai triển mỗi phần tử của :math:`\mathbb{F}_{q^m}` theo một cơ sở cố
định trên :math:`\mathbb{F}_q`, ta thu được ma trận kiểm tra chẵn lẻ
trên trường cơ sở thuộc :math:`\mathbb{F}_q^{mt \times n}`.


Decode với Goppa code
---------------------

Khoảng cách tối thiểu (minimal distance) của :math:`\Gamma(L, g)` 
là :math:`d \geqslant t + 1`. Đặc biệt, khi :math:`q = 2` và :math:`g` 
là separable (tức là :math:`g` có đủ :math:`t` nghiệm phân biệt 
trên một trường mở rộng nào đó của :math:`\mathbb{F}_{q^m}`) 
thì :math:`d \geqslant 2t + 1` (bài tập).

Giả sử ta nhận được vector qua kênh truyền là

.. math:: \bm{y} = (y_1, \ldots, y_n) = \underbrace{(c_1, \ldots, c_n)}_{\bm{c}} + \underbrace{(e_1, \ldots, e_n)}_{\bm{e}},

trong đó :math:`\bm{e}` là lỗi. Khi đó 
:math:`\mathrm{wt}(\bm{e}) \leqslant \left\lfloor\dfrac{d-1}{2}\right\rfloor` 
với :math:`\mathrm{wt}(\bm{e})` là trọng số 
của vector :math:`\bm{e}`.

Đặt :math:`\mathcal{B} = \{ i : e_i \neq 0 \}` là tập 
các vị trí xảy ra lỗi. Khi đó :math:`\lvert \mathcal{B} \rvert = \mathrm{wt}(\bm{e})`.

Đặt

.. math:: s(x) = \sum_{i=1}^n \frac{y_i}{x - \alpha_i} = \sum_{i=1}^n \frac{e_i}{x - \alpha_i} \bmod{g(x)}

thì đây là syndrome của :math:`\bm{y}` và chúng ta 
sẽ decode dựa trên :math:`s(x)`.

Ta cần hai đa thức bổ trợ nữa là

.. math:: \sigma(x) = \prod_{i \in \mathcal{B}} (x - \alpha_i)

gọi là đa thức định vị lỗi (error locator polynomial), 
và đa thức

.. math:: w(x) = \sum_{i \in \mathcal{B}} e_i \prod_{j \in \mathcal{B}, j \neq i} (x - \alpha_j).

Khi đó ta suy ra

.. math:: e_k = \frac{w(\alpha_k)}{\sigma'(\alpha_k)}

với mọi :math:`k \in \mathcal{B}`.

Ta cũng suy ra

.. math:: \sigma(x) \cdot s(x) = w(x) \bmod{g(x)}.

Khi đó

.. math:: \deg \sigma(x) = \lvert \mathcal{B} \rvert, \quad \deg w(x) = \mathrm{wt}(\bm{e}) - 1.

Lúc này ta có :math:`\deg g = t` phương trình và khoảng
:math:`2\mathrm{wt}(\bm{e})` hệ số cần xác định (sau khi chuẩn hóa
:math:`\sigma` thành monic).

Đối với Goppa code tổng quát, phương trình khóa trên cho phép giải duy
nhất trong bán kính :math:`\lfloor t/2\rfloor`. Riêng Goppa code nhị
phân với :math:`g` square-free có khoảng cách ít nhất :math:`2t+1` và
có thể sửa tới :math:`t` lỗi bằng thuật toán Patterson.

Ví dụ
-----

Xét :math:`q = 2` và :math:`m = 3`, :math:`\FF_{2^3} = \FF_2[x] / (x^3 + x + 1)`.

Đặt

.. math:: L = \FF_{2^3} = \{ 0, 1, \alpha, \alpha^2, \alpha + 1, \alpha^2 + \alpha, \alpha^2 + \alpha + 1, \alpha^2 + 1 \}

với :math:`\alpha^3 + \alpha + 1 = 0`.

Khi đó

.. math:: 

    \overline{\bm{H}} = \left(\begin{array}{cccccccc}
        1 & 1 & \alpha^2 & \alpha^4 & \alpha^2 & \alpha & \alpha & \alpha^4 \\
        0 & 1 & \alpha^3 & \alpha^6 & \alpha^5 & \alpha^5 & \alpha^6 & \alpha^2
    \end{array}\right) \ \text{trên} \ \FF_{2^3},

.. math:: 

    \bm{H} = \left(\begin{array}{cccccccc}
        1 & 1 & 0 & 0 & 0 & 0 & 0 & 0 \\
        0 & 0 & 0 & 1 & 0 & 1 & 1 & 1 \\
        0 & 0 & 1 & 1 & 1 & 0 & 0 & 1 \\
        \hline
        0 & 1 & 1 & 1 & 1 & 1 & 1 & 1 \\
        0 & 0 & 1 & 0 & 1 & 1 & 0 & 1 \\
        0 & 0 & 0 & 1 & 1 & 1 & 1 & 0
    \end{array}\right).

Giả sử ta gửi đi codeword

.. math:: 
    
    \bm{c} & = (1, 0, 1, 0, 1, 1, 1, 0) \\
        & = \frac{1}{x - 0} + \frac{0}{x - 1} + \frac{1}{x - \alpha} + \frac{0}{x - \alpha^2} + \frac{1}{x - (\alpha + 1)} + \frac{1}{x - (\alpha^2 + \alpha)} \\ 
        & + \frac{1}{x - (\alpha^2 + \alpha + 1)} + \frac{0}{x - (\alpha^2 + 1)} \bmod{(x^3 + x + 1)}.

Đặt :math:`g(x) = x^2 + x + 1`. Ta có

.. math:: 

    g(0) & = 1 \Longrightarrow g^{-1}(0) = 1, \frac{1}{x - 0} = x + 1 \\
    g(\alpha) & = a^2 + \alpha + 1 \Longrightarrow g^{-1}(\alpha) = a^2, \frac{1}{x - \alpha} = \alpha^2 x + (\alpha^2 + \alpha + 1) \\ 
    g(\alpha + 1) & = \alpha^2 + \alpha + 1 \Longrightarrow g^{-1}(\alpha + 1) = \alpha^2, \frac{1}{x - (\alpha + 1)} = \alpha^2 x + (\alpha + 1) \\
    g(\alpha^2 + \alpha) & = \alpha^2 + 1 \Longrightarrow g^{-1}(\alpha^2 + \alpha) = \alpha + 1, \frac{1}{x - (\alpha^2 + \alpha)} = (\alpha + 1) x + \alpha \\
    g(\alpha^2 + \alpha + 1) & = \alpha^2 + 1 \Longrightarrow g^{-1}(\alpha^2 + \alpha + 1) = \alpha, \frac{1}{x - (\alpha^2 + \alpha + 1)} = \alpha x + (\alpha^2 + \alpha + 1)

Thay các :math:`g` trên vào :math:`\bm{c}` thì ta có

.. math:: 
    
    \bm{c} & = c(x) = (x + 1) + \left(\alpha^2 x + (\alpha^2 + \alpha + 1)\right) + \left(\alpha^2 x + (\alpha + 1)\right) \\
    & + \left((\alpha + 1) x + \alpha\right) + \left(\alpha x + (\alpha^2 + \alpha + 1)\right) \\ 
    & = \left(1 + \alpha^2 + \alpha^2 + (\alpha + 1) + \alpha\right) x \\
    & + \left(1 + (\alpha^2 + \alpha + 1) + (\alpha + 1) + \alpha + (\alpha^2 + \alpha + 1)\right) = 0.

Như vậy :math:`\bm{c}` là một codeword.

Giả sử ở bên nhận ta nhận được vector

.. math:: \bm{y} = (1, 1, 1, 0, 1, 1, 1, 0).

Bằng trực quan ta thấy :math:`\bm{y}` đã sai bit thứ hai so với :math:`\bm{c}`. Sau đây ta sẽ sử dụng phương pháp sửa lỗi của Goppa code để tìm ra vị trí lỗi (trên điều kiện là không biết :math:`\bm{c}`).

Ta tính

.. math:: 

    \bm{y} & = (1, 1, 1, 0, 1, 1, 1, 0) \\
            & = \frac{1}{x - 0} + \frac{1}{x - 1} + \frac{1}{x - \alpha} + \frac{0}{x - \alpha^2} + \frac{1}{x - (\alpha + 1)} + \frac{1}{x - (\alpha^2 + \alpha)} \\ 
            & + \frac{1}{x - (\alpha^2 + \alpha + 1)} + \frac{0}{x - (\alpha^2 + 1)} \bmod{(x^3 + x + 1)} \\ 
            & = x \Longrightarrow s(x) = x.

Ta tìm các đa thức :math:`\sigma(x) \cdot s(x) \equiv w(x) \bmod{g(x)}`, tương đương với tìm các đa thức :math:`\sigma(x)` và :math:`u(x)` sao cho

.. math:: \sigma(x) \cdot s(x) + u(x) \cdot g(x) = w(x).

Sử dụng thuật toán Euclide ta có

.. math:: u(x) = 1 \ \text{và} \ \sigma(x) = x + 1, w(x) = 1.

Như vậy, vì

.. math:: \sigma(x) = x + 1 = x - 1 = \prod_{i \in \{ 1 \}} (x - \alpha_1),

nên lỗi xảy ra ở vị trí :math:`1` (chỉ số dãy :math:`\alpha_i` bắt đầu từ :math:`0`).
