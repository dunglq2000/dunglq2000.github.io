Ngoài lề
########

.. .. toctree:: 

..    opinions/index
   
Sưu tầm 1
==========

Nguồn: https://vk.com/po_matematike

**Tiêu đề gốc**. Метод сопряжённых градиентов: линейная алгебра с ускорением.

**Tiêu đề**. Phương pháp gradient liên hợp: đại số tuyến tính với tốc độ cao.

Khi hệ phương trình tuyến tính :math:`\bm{A} \bm{x} = \bm{b}` có 
quy mô cực lớn (hàng triệu biến), việc lưu trữ toàn bộ ma trận :math:`\bm{A}` 
và sử dụng các phương pháp trực tiếp như phân tích LU trở nên bất khả thi. 
Đặc biệt khi :math:`\bm{A}` là ma trận thưa, đối xứng và xác định dương (định thức dương?). 
Trong trường hợp này, phương pháp Gradient liên hợp (Conjugate Gradients - CG) 
là một trong những thuật toán lặp hiệu quả nhất.

Khác với phương pháp Gradient Descent, CG không chỉ "tiến dần" về cực tiểu 
của hàm bậc hai:

.. math:: f(\bm{x}) = \frac{1}{2} \cdot \bm{x}^\top \bm{A} \bm{x} - \bm{b}^\top \bm{x}

mà di chuyển theo các hướng liên hợp với nhau, giúp tránh lãng phí bước đi. 
Về lý thuyết, sau đúng :math:`n` bước, CG tìm được nghiệm chính xác, nhưng 
trên thực tế, quá trình hội tụ thường đạt được sớm hơn nhiều.

**Ý tưởng chính**. Thay vì chọn hướng gradient :math:`\bm{r}_k = \bm{b} - \bm{A} \bm{x}_k` 
ở mỗi bước, CG chọn hướng :math:`\bm{p}_k` liên hợp với các hướng trước đó theo :math:`\bm{A}`:

.. math:: \bm{p}_{k+1} = \bm{r}_{k+1} + \beta_k \bm{p}_k, \quad \beta_k = \frac{\bm{r}_{k+1}^\top \bm{r}_{k+1}}{\bm{r}_k^\top \bm{r}_k}.

**Cập nhật nghiệm**. Nghiệm mới được tính bằng:

.. math:: \bm{x}_{k+1} = \bm{x}_k + \alpha_k \bm{p}_k, \quad \alpha_k = \frac{\bm{r}_k^\top \bm{r}_k}{\bm{p}_k^\top \bm{A} \bm{p}_k}.

**Ưu điểm quan trọng**. Không cần lưu trữ toàn bộ ma trận :math:`\bm{A}`, chỉ cần khả năng tính nhanh :math:`\bm{A} \bm{x}`.

Ứng dụng rộng rãi trong:

- phương pháp tính;
- học máy;
- đồ họa máy tính;
- giải phương trình đạo hàm riêng.

Phương pháp này minh họa cách lựa chọn hình học thông 
minh (liên hợp thay vì trực giao) giúp tăng tốc đáng kể tính toán.

.. Sưu tầm 2
.. =========

.. Контрольная работа.

.. Задание 1. Докажите или опровергните утверждение :math:`n^2 = o(2n^2)`.

.. Задание 2. Расположите следующие функции в порядке увеличения скорости из роста, отметив среди них :math:`\Theta`-эквивалентные: :math:`f(n) = 4^{\log n}`, :math:`g(n) = 4n^2`, :math:`h(n) = n \log(n^4)`.

.. Задание 3. Пусть :math:`f(n)` и :math:`g(n)` - асимптотически положительные функции. Докажите или опровергните следующее утверждение: :math:`f(n) + g(n) = O(\min (f(n), g(n)))`.

.. Một số đồ thị hàm số sưu tầm
.. ============================

.. Để vẽ trái tim như ở `đây <https://vk.com/wall-216361286_445>`_ ta dùng phương trình

.. .. math::
..     y = x^{2/3} + 0,9 (3,3 - x^2)^{1/2} \cdot \sin(m \cdot \pi \cdot x)

.. với :math:`m = 6,50`.

Bài tập sưu tầm
===============

Đề bài. Tính

.. math:: \lim_{T \to +\infty} \dfrac{1}{\sqrt{T}} \int\limits_0^T \ln\left(1 + \dfrac{1}{\sqrt{x}}\right)\,dx.

Đặt

.. math:: I = \int\limits_0^T \ln\left(1 + \dfrac{1}{\sqrt{x}}\right)\,dx.

Đặt :math:`u = \ln\left(1 + \dfrac{1}{\sqrt{x}}\right)` và :math:`dv = dx` thì

.. math:: du = -\dfrac{1}{2} \dfrac{1}{\sqrt{x}}\,dx, \ v = x

thì

.. math:: I = x \ln\left(1 + \dfrac{1}{\sqrt{x}}\right) - \int\limits_0^T \dfrac{-dx}{2\sqrt{x}} = \left.\left(x \ln\left(1 + \dfrac{1}{\sqrt{x}}\right)\right)\right\vert_0^T = T \ln\left(1 + \dfrac{1}{\sqrt{T}}\right) + \sqrt{T}.

Đặt :math:`t = \ln\left(1 + \dfrac{1}{\sqrt{x}}\right)` thì :math:`e^t = 1 + \dfrac{1}{\sqrt{x}}`. Khi :math:`x \to 0` thì :math:`t \to +\infty`. Khi đó

.. math:: \lim_{T \to +\infty} \dfrac{1}{\sqrt{T}} \left(T \ln\left(1 + \dfrac{1}{\sqrt{T}}\right) + \sqrt{T}\right) = \lim_{T \to +\infty} \sqrt{T}\ln\left(1 + \dfrac{1}{\sqrt{T}}\right) = \lim_{T \to +\infty} \dfrac{\ln\left(1 + \dfrac{1}{\sqrt{T}}\right)}{\dfrac{1}{\sqrt{T}}} = 1.

Bài 1. Tính

.. math:: \int \dfrac{\sin \cos^3 x}{1 + \cos^2 x}\,dx.

Giải

.. math:: I = \int \dfrac{\sin \cos^3 x}{1 + \cos^2 x}\,dx = \int \dfrac{\sin x \left(\cos^3 x + \cos x - \cos x\right)}{1 + \cos^2 x}\,dx \\ = \int \sin x \cos x \,dx - \int\dfrac{\sin x \cos x}{1 + \cos^2 x}.

Đặt :math:`u = 1 + \cos^2 x` thì :math:`du = -2 \sin x \cos x \,dx`. Khi đó

.. math:: I = \int \sin x \,d(\sin x) - \int\dfrac{-du}{2u} = \dfrac{\sin^2 x}{2} + \frac{1}{2} \ln\left(u\right) + C= \frac{\sin^2 x}{2} + \frac{1}{2} \ln(1 + \cos^2 x) + C.

Bài 2. Tính 

.. math:: \int\dfrac{\arcsin x}{x^2}\,dx.

Giải. Đặt

.. math:: I = \int\dfrac{\arcsin x}{x^2}\,dx.

Đặt :math:`t = \arcsin x` thì :math:`x = \sin t`, hay :math:`dx = \cos t\,dt`, suy ra

.. math:: I = \int\dfrac{t}{\sin^2 t} \cos t \,dt.

Đặt :math:`u = t` và :math:`dv = \dfrac{\cos t}{\sin^2 t} \,dt`. Khi đó :math:`du = dt` và :math:`v = -1 / \sin t`, hay

.. math:: I = \dfrac{-t}{\sin t} - \int\dfrac{-dt}{\sin t} = \dfrac{-t}{\sin t} + \int\dfrac{dt}{\sin t}.

Ta có

.. math:: \int\dfrac{dt}{\sin t} = \int\dfrac{\sin t}{\sin^2 t}\,dt = -\int\dfrac{d(\cos t)}{1 - \cos^2 t} = -\int\dfrac{d(\cos t)}{(1 - \cos t)(1 + \cos t)} \\ = -\dfrac{1}{2} \int\left(\dfrac{1}{1 - \cos t} + \dfrac{1}{1 + \cos t}\right)\,d(\cos t) \\ = -\dfrac{1}{2} \left(-\ln \lvert 1 - \cos t \rvert + \ln \lvert 1 + \cos t \rvert\right) + C \\ = -\dfrac{1}{2} \ln\left\lvert\dfrac{1 + \cos t}{1 - \cos t}\right\rvert + C.

Bài 3. Tính

.. math:: \int\dfrac{dx}{x + \sqrt{x^2 + x + 1}}.

Đặt :math:`t = x + \sqrt{x^2 + x + 1}`. Ta có

.. math:: t - x = \sqrt{x^2 + x + 1} \Longrightarrow (t - x)^2 = x^2 + x + 1 \Longleftrightarrow t^2 - 2tx = x + 1 \\ \Longleftrightarrow (2t + 1)x = t^2 - 1 \Longleftrightarrow x = \dfrac{t^2 - 1}{2t + 1}.

Như vậy

.. math:: dx = \dfrac{2t(2t + 1) - 2(t^2 - 1)}{(2t + 1)^2}\,dt = \dfrac{2(t^2 + t + 1)}{(2t+1)^2}\,dt.

.. math:: I = \int\dfrac{dx}{x + \sqrt{x^2 + x + 1}} = \int\dfrac{t^2 + t + 1}{t(2t + 1)^2}\,dt = \int\left(\dfrac{A}{t} + \dfrac{B}{2t + 1} + \dfrac{C}{(2t + 1)^2}\right)\,dt.

Tìm được :math:`A`, :math:`B` và :math:`C` ta được

.. math:: I = 2\ln\lvert t \rvert - 3\ln\lvert 2t + 1 \rvert + \dfrac{1}{2(2t + 1)} + C.

Зимина О.В.

Bài giải trong :cite:`Zimina01`.

Tính tổng

.. math:: \sum_{n=1}^{\infty} \dfrac{3^{n+1}}{n x^{n+1}}.

Đặt :math:`x = 3/t`. Khi đó chuỗi có dạng

.. math:: Z = \sum_{n=1}^{\infty} \dfrac{t^{n+1}}{n}.

Đặt

.. math:: S = \sum_{n=1}^{\infty} \dfrac{t^n}{n}.

Khi đó :math:`Z = tS` và ta sẽ tìm :math:`S`. Ta có

.. math:: \sum_{n=0}^{\infty} t^n = \dfrac{1}{1 - t} \Longrightarrow \sum_{n=1}^{\infty} t^n = \dfrac{1}{1 - t} - 1 = \dfrac{t}{1 - t},

nên khi chia cho :math:`t` ta có

.. math:: \sum_{n=1}^{\infty} t^{n-1} = \dfrac{1}{1 - t}.

Lấy nguyên hàm hai vế ta có

.. math:: \sum_{n=1}^{\infty} \int\limits t^{n-1}\,dt = \sum_{n=1}^{\infty} \dfrac{t^n}{n} = S = \int\limits \dfrac{dt}{1 - t} = -\ln (1 - t).

Từ đó :math:`Z = tS = -t \ln (1 - t)`. Ta thay lại :math:`t = 3/x` như trên và được

.. math:: \sum_{n=1}^{\infty} \dfrac{3^{n+1}}{n x^{n+1}} = -\dfrac{3}{x} \ln \left(1 - \dfrac{3}{x}\right).

---

Tính tổng

.. math:: \sum_{n=2}^{\infty} nx^{n+1}.

Ta có

.. math:: \sum_{n=0}^{\infty} x^n = \dfrac{1}{1 - x} \Longrightarrow \sum_{n=1}^{\infty} x^n = \dfrac{1}{1 - x} - 1 = \dfrac{x}{1 - x}.

Lấy đạo hàm hai vế ta có

.. math:: \sum_{n=1}^{\infty} n x^{n-1} = \dfrac{1}{(1 - x)^2}.

Nhân hai vế cho :math:`x^2` ta có

.. math:: \sum_{n=1}^{\infty} n x^{n+1} = \dfrac{x^2}{(1 - x)^2}.

Dễ thấy

.. math:: \sum_{n=1}^{\infty} n x^{n+1} = x^2 + \sum_{n=2}^{\infty} n x^{n+1},

nên suy ra

.. math:: \sum_{n=2}^{\infty} n x^{n+1} = \dfrac{x^2}{(1 - x)^2} - x^2.
