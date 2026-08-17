========
Giới hạn
========

-------------------
Giới hạn của dãy số
-------------------

.. prf:definition:: Giới hạn hữu hạn của dãy số
    :label: def-lim-list

    Cho dãy số :math:`\{ a_n \}`. Ta nói dãy :math:`\{ a_n \}` có giới hạn hữu hạn :math:`L` nếu với mọi :math:`\varepsilon > 0`, tồn tại :math:`n_0 \in \mathbb{N}` sao cho với mọi :math:`n \geqslant n_0` thì

    .. math:: | a_{n} - L | < \varepsilon.

    Kí hiệu: :math:`\displaystyle{\lim_{n \to \infty} a_n = L}`.

.. prf:example:: 
    :label: exp-lim-list

    Xét dãy số cho bởi công thức :math:`a_n = \dfrac{1}{n}`. Ta chứng minh dãy số có giới hạn hữu hạn là :math:`0`.

    Với mọi :math:`\varepsilon > 0` tùy ý, ta cần chứng minh tồn tại số :math:`n_0 \geqslant 1` sao cho với mọi :math:`n \geqslant n_0` thì :math:`\lvert a_n - 0 \rvert < \varepsilon`.

    Nói cách khác :math:`a_{n_0} < \varepsilon`, hay tương đương với
    
    .. math:: \dfrac{1}{n_0} < \varepsilon \Leftrightarrow n_0 > \dfrac{1}{\varepsilon}.

    Vậy ta chỉ cần chọn :math:`n_0` thỏa bất đẳng thức trên (luôn tìm được).

    Kết luận: :math:`\displaystyle{\lim_{n \to \infty} a_n = 0}`.

.. prf:definition:: Dãy số có giới hạn vô cực
    :label: def-lim-list-inf

    Cho dãy số :math:`\{a_n\}`. Ta nói dãy số có giới hạn ở dương vô cực nếu với mọi :math:`M > 0`, tồn tại :math:`n_0 \in \mathbb{N}` sao cho với mọi :math:`n \geqslant n_0` thì :math:`a_n > M`.

Nói cách khác, nếu ta chọn một số :math:`M` rất lớn bất kì, thì mọi số hạng của dãy số kể từ một số hạng nào đó trở đi luôn lớn hơn :math:`M`. Định nghĩa về dãy số có giới hạn ở âm vô cực cũng tương tự.

-------------------
Giới hạn của hàm số
-------------------

Để định nghĩa giới hạn của hàm số :math:`y = f(x)` khi :math:`x` tiến tới :math:`x_0` ta có hai loại định nghĩa.

.. prf:definition:: Giới hạn hàm số qua giới hạn dãy số
    :label: def-lim-func-as-list

    Xét hàm số :math:`f(x)`. Ta nói hàm số có giới hạn hữu hạn :math:`L` khi :math:`x` tiến tới :math:`x_0`, nếu với mọi dãy số :math:`\{x_n\}` mà :math:`\displaystyle{\lim_{n \to \infty} x_n = x_0}`, thì :math:`\displaystyle{\lim_{n \to \infty} f(x_n) = L}`.

Định nghĩa này tuân theo giới hạn của dãy số. Khi đó mọi phần tử của dãy số từ một số hạng nào đó trở đi cho giá trị :math:`f(x_n)` tiến về :math:`L`.

Định nghĩa của hàm số theo kiểu Cauchy (hay còn được gọi là ngôn ngữ :math:`\delta-\varepsilon`) là kiểu định nghĩa phổ biến được giảng dạy trong nhà trường.

.. prf:definition:: Giới hạn hàm số kiểu Cauchy
    :label: def-lim-func-cauchy
    
    Xét hàm số :math:`f(x)`. Ta nói hàm số có giới hạn hữu hạn :math:`L` khi :math:`x` tiến tới :math:`x_0`, nếu với mọi :math:`\varepsilon > 0`, tồn tại  :math:`\delta > 0` sao cho với mọi :math:`x` mà :math:`\lvert x - x_0 \rvert < \delta` thì :math:`\lvert f(x) - L \rvert < \varepsilon`.

    Kí hiệu: :math:`\displaystyle{\lim_{x \to x_0} f(x) = L}`.

Ta có thể thấy ở đây :math:`x` tiến về :math:`x_0` (khá giống định nghĩa giới hạn hàm số) và :math:`f(x)` tương ứng tiến về :math:`L`.

Tương tự ta cũng có giới hạn hàm số ở vô cực.

.. prf:definition:: Giới hạn hàm số ở vô cực
    :label: def-lim-func-inf
    
    Với hàm số :math:`f(x)`, ta nói hàm số có giới hạn tại dương vô cực khi :math:`x` tiến về :math:`x_0` nếu với mọi :math:`M > 0`, tồn tại :math:`\delta > 0` sao cho với mọi :math:`x` mà :math:`\lvert x - x_0 \rvert < \delta` thì :math:`f(x) > M`.

    Kí hiệu: :math:`\displaystyle{\lim_{x \to x_0} f(x) = +\infty}`.

.. prf:definition:: Giới hạn một bên
    :label: def-lim-oneside

    Ta nói hàm số :math:`f(x)` có giới hạn phải :math:`L` tại :math:`x_0` khi :math:`x` tiến về bên phải :math:`x_0` nếu với mọi :math:`\varepsilon > 0`, tồn tại :math:`\delta > 0` sao cho với mọi :math:`0 < x - x_0 < \delta`  thì :math:`\lvert f(x) - L \rvert < \varepsilon`.

    Kí hiệu: :math:`\displaystyle{\lim_{x \to x_0^+} f(x) = L}`.

Nghĩa là chúng ta chỉ xét giới hạn khi :math:`x` tiến tới :math:`x_0` từ bên phải :math:`x > x_0`. Tương tự cho giới hạn trái.

Lưu ý rằng trong nhiều trường hợp, mặc dù cùng tiến tới :math:`x_0` nhưng giới hạn trái và giới hạn phải có thể không bằng nhau.

.. prf:example:: 
    :label: exp-uncontinuous

    Xét hàm số :math:`y = \dfrac{1}{x}`. Ta thấy hàm số không xác định tại :math:`x = 0`, và giới hạn trái và phải khác nhau do

    .. math:: \lim_{x \to 0^+} = +\infty, \quad \lim_{x \to 0^-} = -\infty.
