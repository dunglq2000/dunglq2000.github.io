=============================
Perceptron Learning Algorithm
=============================

Một trong những nhiệm vụ quan trọng nhất của ML là phân loại (tiếng Anh - classification).

Perceptron là thuật toán phân loại cho trường hợp đơn giản nhất khi có hai lớp. Nếu ta có các điểm dữ liệu cho trước trong không gian :math:`d` chiều, ta muốn tìm một siêu phẳng (hình học affine gọi là :math:`(d-1)`-phẳng) chia các điểm dữ liệu đó thành hai phần. Sau đó khi có một điểm dữ liệu mới ta chỉ cần bỏ nó vào bên này hoặc bên kia của siêu phẳng.

Trong dạng này, mỗi điểm dữ liệu được biểu diễn ở dạng cột của ma trận. Giả sử các điểm dữ liệu là :math:`\bm{x}_1`, :math:`\bm{x}_2`, ..., :math:`\bm{x}_N`, với :math:`\bm{x}_i \in \mathbb{R}^d`, thì ma trận dữ liệu là

.. math:: 
    
    \bm{X} = \begin{pmatrix}
        \bm{x}_1^\top & \bm{x}_2^\top & \cdots & \bm{x}_N^\top
    \end{pmatrix}.
    
Ta gọi nhãn tương ứng với :math:`N` điểm dữ liệu trên là vector :math:`\bm{y} = (y_1, y_2, \ldots, y_N)` với :math:`y_i = 1` nếu :math:`\bm{x}_i` thuộc class xanh, và :math:`y_i = -1` nếu :math:`\bm{x}_i` thuộc class đỏ.

Một siêu phẳng có phương trình là

.. math:: f_{\bm{w}} (\bm{x}) = w_0 + w_1 x_1 + \ldots + w_d x_d = \bm{w} \cdot \bm{x}^\top.

Một điểm thuộc nửa không gian (tạm gọi là *bên này*) đối với siêu phẳng thì :math:`f_{\bm{w}} (\bm{x}) < 0`, nếu thuộc nửa *bên kia* thì :math:`f_{\bm{w}} (\bm{x}) > 0`, nếu nằm trên phẳng thì bằng :math:`0`.

Gọi :math:`\mathrm{label} (\bm{x})` là nhãn của điểm :math:`\bm{x}`. Khi đó điểm :math:`\bm{x}` thuộc một trong hai bên của phẳng nên :math:`\mathrm{label} (\bm{x}) = \mathrm{sgn} (\bm{w} \cdot \bm{x}^\top)` với :math:`\mathrm{sgn}` là hàm dấu. Ta quy ước :math:`\mathrm{sgn} (0) = 1`.

Khi một điểm bị phân loại sai class thì ta nói điểm đó bị **misclassified**. Ý tưởng của thuật toán là làm giảm thiểu số lượng điểm bị misclassified qua nhiều lần lặp. Đặt

.. math:: J_1 (\bm{w}) = \sum_{\bm{x}_i \in \mathcal{M}} (-y_i \cdot \mathrm{sgn} (\bm{w} \cdot \bm{w}_i^\top)),

trong đó :math:`\mathcal{M}` là tập các điểm bị misclassified (tập này sẽ thay đổi theo :math:`\bm{w}`).

Nếu :math:`\bm{x}_i` bị misclassified thì :math:`y_i` và :math:`\mathrm{sgn} (\bm{w} \cdot \bm{x}_i^\top)` ngược dấu nhau. Nói cách khác, :math:`-y_i \cdot \mathrm{sgn} (\bm{w} \cdot \bm{x}_i^\top) = 1`. Từ đó :math:`J_1(\bm{w})` là hàm đếm số lượng điểm bị misclassified. Ta thấy rằng :math:`J_1(\bm{w}) \geqslant 0` nên ta cần tối ưu để hàm này đạt giá trị nhỏ nhất bằng :math:`0`. Khi đó không điểm nào bị misclassified.

Tuy nhiên có một vấn đề. Hàm :math:`J_1(\bm{w})` là hàm rời rạc (hàm :math:`\mathrm{sgn}`) nên rất khó tối ưu vì không thể tính đạo hàm. Do đó chúng ta cần một cách tiếp cận khác, một hàm mất mát khác tốt hơn.

Nếu ta bỏ đi hàm :math:`\mathrm{sgn}` thì có hàm

.. math:: J(\bm{w}) = \sum_{\bm{x}_i \in \mathcal{M}} (-y_i \cdot \bm{w} \cdot \bm{x}^\top).

**Nhận xét.** Một điểm bị misclassified nằm càng xa biên giới (siêu phẳng) thì giá trị :math:`\bm{w} \cdot \bm{x}_i^\top` càng lớn, tức là hàm :math:`J` đi ra xa so với giá trị nhỏ nhất. Hàm :math:`J` cũng đạt min ở :math:`0` nên ta cũng có thể dùng hàm này để loại bỏ các điểm bị misclassified.

Lúc này hàm :math:`J(\bm{x})` khả vi nên ta có thể dùng GD hoặc SGD để tìm nghiệm cho bài toán.

Nếu xét tại một điểm thì

.. math:: J(\bm{w}, \bm{x}_i, y_i) = -y_i \cdot \bm{w} \cdot \bm{x}_i^\top \Rightarrow \dfrac{\partial J}{\partial \bm{w}} = -y_i \bm{x}_i.

Khi đó quy tắc để cập nhật là :math:`\bm{w} = \bm{w} + \eta \cdot y_i \cdot \bm{x}_i` với :math:`\eta` là learning rate (thường chọn bằng :math:`1`). Nói cách khác ta đang xây dựng dãy :math:`\{ \bm{w}_n \}` hội tụ lại nghiệm bài toán với công thức :math:`\bm{w}_{i+1} = \bm{w}_i + \eta \cdot y_i \cdot \bm{x}_i`.

Thuật toán Perceptron Learning Algorithm (PLA) có thể được mô tả như sau:

1. Chọn ngẫu nhiên vector :math:`\bm{w}` với :math:`w_i` xấp xỉ :math:`0`.
2. Duyệt ngẫu nhiên qua các :math:`\bm{x}_i`:

   - nếu :math:`\bm{x}_i` được phân lớp đúng, tức :math:`\mathrm{sgn} (\bm{w} \cdot \bm{x}_i^\top) = y_i` thì ta không cần làm gì;
   - nếu :math:`\bm{x}_i` bị misclassified, ta cập nhật :math:`\bm{w}` theo công thức :math:`\bm{w} = \bm{w} + \eta \cdot y_i \cdot \bm{x}`.

3. Kiểm tra xem có bao nhiêu điểm bị misclassified. Nếu không còn điểm nào thì ta dừng thuật toán, ngược lại thì quay lại bước 2.
