================
Gradient Descent
================

Trong nhiều trường hợp chúng ta thường không thể tìm nghiệm của phương trình đạo hàm để từ đó tìm các cực trị địa phương. Một phương pháp hiệu quả là gradient descent.

------------
Hàm một biến
------------

Giả sử :math:`x^*` là local extremum (cực trị địa phương) của hàm số :math:`f(x)`. Khi đó chúng ta xây dựng dãy số :math:`\{ x_n \}` hội tụ về :math:`x^*`. Ý tưởng thực hiện là dựa trên nhận xét, nếu :math:`x_n` nằm bên phải :math:`x^*` thì :math:`x_{n+1}` nằm giữa :math:`x^*` và :math:`x_n`. Ta đã biết nếu :math:`x^*` là một điểm cực trị thì :math:`f'(x) > 0` với :math:`x > x^*` (trường hợp cực tiểu), mà :math:`x_n` đi từ bên phải sang bên trái (ngược chiều :math:`Ox` nên mang dấu âm). Từ đó chúng ta có công thức chung sau

.. math:: x_{n+1} = x_n - \eta f'(x_n).

Trong đó :math:`\eta` là một số dương nhỏ, gọi là *learning rate* (tốc độ học).

Ta chọn :math:`x_0` là một điểm bất kì. Tuy nhiên việc chọn :math:`x_0` cũng có thể ảnh hưởng đến tốc độ hội tụ.

Ví dụ với hàm số :math:`f(x) = x^2 + 5 \sin x`. Ta có đạo hàm là :math:`f'(x) = 2x + 5 \cos x`. Việc giải phương trình đạo hàm bằng :math:`0` là điều không dễ dàng. Do đó gradient descent tỏ ra hiệu quả trong trường hợp này.

Chọn :math:`\eta = 0,1` và :math:`x_0 = 5`. Sau đó chọn :math:`\eta = 0,1` và :math:`x_0 = -5`. Ta thấy trường hợp sau tốn ít vòng lặp hơn do :math:`x_0 = -5` gần điểm cực trị hơn (:math:`\approx -1.11`).

--------------
Hàm nhiều biến
--------------

Lúc này đầu vào của hàm số là một vector :math:`\bm{x}`. Đặt :math:`\nabla f(\bm{x})` là đạo hàm của hàm :math:`f` theo vector :math:`\bm{x}`. Tương tự, ta xây dựng dãy vector :math:`\{ \bm{x}_n \}` hội tụ về cực trị :math:`\bm{x}^*`. Công thức lúc này là

.. math:: \bm{x}_{n+1} = \bm{x}_n - \eta \cdot \nabla f(\bm{x}_n).

Ta đã biết đạo hàm của hàm số theo vector cũng là vector cùng cỡ. Do đó giả sử :math:`f(\bm{x}) = f(x_1, x_2, \ldots, x_n)` thì đạo hàm của nó là

.. math:: \nabla f(\bm{x}) = \left( \dfrac{\partial f}{\partial x_1}, \dfrac{\partial f}{\partial x_2}, \ldots, \dfrac{\partial f}{\partial x_n} \right).

Với ví dụ là bài toán Linear Regression, lúc này hàm mất mát là

.. math:: \mathcal{L} = \dfrac{1}{2N} \sum_{i=1}^N \lVert y_i - \bm{x}_i \bm{w}^T \rVert^2 = \dfrac{1}{2N} \lVert \bm{y} - \bm{X} \bm{w}^T \rVert^2.

Đạo hàm của hàm mất mát là

.. math:: \nabla \mathcal{L} = \dfrac{1}{N} (\bm{w} \bm{X}^T - \bm{y}) \bm{X}.

Lúc này, với vector khởi đầu :math:`\bm{w}_0` chúng ta xây dựng dãy :math:`\{ \bm{w}_n \}` tới khi nhận được :math:`\bm{w}_n / d < \varepsilon`, với :math:`d` là độ dài vector :math:`\bm{w}`.