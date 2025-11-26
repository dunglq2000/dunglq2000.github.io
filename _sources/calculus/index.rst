Giải tích
#########

.. toctree:: 
    :numbered:
    :maxdepth: 2

    calculus/index
    differential-equation/index
    series/index

Hàm gamma, hàm beta, hàm zeta
*****************************

[TODO] Triển khai hàm gamma và beta thành mục riêng.

Hàm gamma được định nghĩa bởi tích phân

.. math:: \Gamma(z) = \int\limits_0^{\infty} t^{z-1} e^{-t} \, dt,

với :math:`z \in \mathbb{C}` và :math:`\mathrm{Re}(z) > 0`.

Hàm gamma có một số tính chất thú vị:

- :math:`\Gamma(n) = (n - 1)!` khi :math:`n` là số nguyên dương với :math:`\Gamma(1) = 1`;
- :math:`\Gamma(z + 1) = z \Gamma(z)`.

Tính chất thứ hai có thể chứng minh bằng tích phân từng phần

.. math:: 

    \Gamma(z + 1) & = \int\limits_0^{\infty} t^z e^{-t} \, dt = (-t^z e^{-t})\Big|_0^{\infty} + \int\limits_0^{\infty} z t^{z-1} e^{-t} \, dt \\
    & = z \int\limits_0^{\infty} t^{z-1} e^{-t} \, dt = z \Gamma(z).

Euler's reflection formula:

.. math:: \Gamma(1 - z) \cdot \Gamma(z) = \dfrac{\pi}{\sin \pi z}, \ z \not\in \mathbb{Z}.

Từ công thức Euler ta suy ra

.. math:: \Gamma(z - n) = (-1)^{n-1} \dfrac{\Gamma(-z) \cdot \Gamma(1 + z)}{\Gamma(n + 1 - z)}, \ n \in \mathbb{Z}.

Legendre duplication formula:

.. math:: \Gamma(z) \cdot \Gamma(z + \dfrac{1}{2}) = 2^{1 - 2z} \sqrt{\pi} \Gamma(2z).

Từ công thức Legendre có thể suy ra một số tính chất:

- :math:`\Gamma(1/2) = \sqrt{\pi}`;
- nếu :math:`\overline{\Gamma(z)} = \Gamma(\overline{z})` thì :math:`\Gamma(z) \cdot \Gamma(\overline{z}) \in \mathbb{R}`.

Tính chất thứ hai, cụ thể hơn, nếu đặt :math:`z = a + bi` thì

.. math:: \lvert \Gamma(a + b) \rvert^2 = \lvert \Gamma(a) \rvert^2 \prod_{k=0}^{\infty} \dfrac{1}{1 + \dfrac{b^2}{(a + k)^2}}.

Ta có thể mở rộng hàm gamma cho phần thực âm với công thức Euler

.. math:: \Gamma(-x) = \dfrac{1}{\Gamma(x + 1)} \cdot \dfrac{\pi}{\sin(\pi(x+1))},

hoặc tính chất của hàm gamma ở trên

.. math:: \Gamma(-x + 1) = (-x) \cdot \Gamma(-x) \Rightarrow \Gamma(-x) = -\dfrac{1}{x} \Gamma(-x + 1), \ x \not\in \mathbb{Z}.

Hàm beta được định nghĩa bởi tích phân

.. math:: B(z_1, z_2) = \int\limits_0^1 t^{z_1 - 1} (1 - t)^{z_2 - 1} \, dt

với đầu vào là các số phức :math:`z_1`, :math:`z_2` mà :math:`\mathrm{Re}(z_1) > 0`, :math:`\mathrm{Re}(z_2) > 0`.

Hàm beta còn được định nghĩa thông qua tích phân

.. math:: B(z_1, z_2) = \int\limits_0^{\infty} \dfrac{u^{z_1 - 1}}{(1 + u)^{z_1 + z_2}} \, du.

Tại sao hai định nghĩa lại tương đương nhau? Các bạn hãy đặt :math:`t = \dfrac{u}{1 + u}`. Khi :math:`u \to \infty` thì :math:`t \to 1` và sử dụng phương pháp đổi biến để biến đổi hai dạng tích phân.

Một số tính chất của hàm beta

- :math:`B(z_1, z_2) = \dfrac{\Gamma(z_1) \cdot \Gamma(z_2)}{\Gamma(z_1 + z_2)}`;
- :math:`B(1, x) = \dfrac{1}{x}`;
- :math:`B(x, 1 - x) = \dfrac{\pi}{\sin \pi x}` với :math:`x \not\in \mathbb{Z}`.

Ví dụ, tính tích phân

.. math:: I = \int\limits_0^{+\infty} \dfrac{x^{1/4}}{(1 + x)^2}\,dx

với tích phân Euler.

Theo định nghĩa hàm beta thì

.. math:: B(p, q) = \int\limits_0^{+\infty} \dfrac{u^{p-1}}{(1 + u)^{p+q}} \,du

nên :math:`I = B\left(\dfrac{5}{4}, \dfrac{3}{4}\right)`.

Theo tính chất của hàm beta (liên hệ với hàm gamma) thì

.. math:: B(p, q) = \dfrac{\Gamma(p) \cdot \Gamma(q)}{\Gamma(p + q)} \Rightarrow I = \dfrac{\Gamma\left(\dfrac{5}{4}\right) \cdot \Gamma\left(\dfrac{3}{4}\right)}{\Gamma(2)}.

Vì :math:`\Gamma(n) = (n-1)!` với :math:`n` là số nguyên dương nên :math:`I = \Gamma\left(\dfrac{5}{4}\right) \cdot \Gamma\left(\dfrac{3}{4}\right)`.

Vì :math:`\Gamma(p + 1) = p \Gamma(p)` với :math:`p > 0` (ở đây :math:`p` là số thực) nên

.. math:: \Gamma\left(\dfrac{5}{4}\right) = \dfrac{1}{4} \cdot \Gamma\left(\dfrac{1}{4}\right),

mà theo tính chất của hàm gamma

.. math:: \Gamma(p) \cdot \Gamma(1 - p) = \dfrac{\pi}{\sin \pi p}

nên

.. math:: \Gamma\left(\dfrac{3}{4}\right) \cdot \Gamma\left(\dfrac{1}{4}\right) = \dfrac{\pi}{\sin(\pi / 4)} = \dfrac{\pi}{\sqrt{2} / 2} = \pi \sqrt{2}.

Như vậy đáp án là

.. math:: I = \Gamma\left(\dfrac{5}{4}\right) \cdot \Gamma\left(\dfrac{3}{4}\right) = \dfrac{1}{4} \cdot \Gamma\left(\dfrac{1}{4}\right) \cdot \Gamma\left(\dfrac{3}{4}\right) = \dfrac{1}{4} \cdot \pi \sqrt{2} = \dfrac{\pi}{2\sqrt{2}}.

Hàm zeta được định nghĩa bởi tích phân

.. math:: \zeta(s) = \sum_{n=1}^{\infty} \dfrac{1}{n^s} = \dfrac{1}{1^s} + \dfrac{1}{2^s} + \cdots

với đầu vào :math:`s \in \mathbb{C}` có :math:`\mathrm{Re}(s) > 1`.

Liên hệ giữa hàm zeta và hàm gamma là

.. math:: \zeta(s) = \sum_{n=1}^{\infty} \dfrac{1}{n^s} = \dfrac{1}{\Gamma(s)} \int\limits_0^{\infty} \dfrac{x^{s-1}}{e^x - 1}\,dx.

.. raw:: html

   <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-2343650775986433"
     crossorigin="anonymous"></script>
   <!-- First Ads -->
   <ins class="adsbygoogle"
      style="display:block"
      data-ad-client="ca-pub-2343650775986433"
      data-ad-slot="4417625951"
      data-ad-format="auto"
      data-full-width-responsive="true"></ins>
   <script>
      (adsbygoogle = window.adsbygoogle || []).push({});
   </script>
   