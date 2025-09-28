Ngoài lề
########

.. toctree:: 
    :maxdepth: 2

    game/index
    graphics
    about-godel
    about-education
    about-stoicism

.. only:: html

    .. toctree:: 
        :maxdepth: 2

        latex/index
        
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