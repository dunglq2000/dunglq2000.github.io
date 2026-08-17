Các heuristic cho lattice
=========================


Hai phương pháp heuristic thường được dùng là Gaussian Heuristic (GH) và Geometric Series Assumption (GSA).

Gaussian Heuristic
------------------

GH là một ước lượng của :math:`\lambda_1(\mathcal{L})`. Mật độ các điểm là :math:`1 / \det(\mathcal{L})`, vì vậy trong một quả cầu bán kính :math:`r` ta kỳ vọng có khoảng :math:`v_n \cdot r^n / \det(\mathcal{L})` điểm lattice, trong đó :math:`v_n` là thể tích quả cầu đơn vị :math:`n` chiều.

Cụ thể, :math:`v_n \lambda_1^n / \det(\mathcal{L}) \approx 1`, do đó :math:`\lambda_1 \approx (\det(\mathcal{L}) / v_n)^{1/n}`.

Vì thể tích quả cầu đơn vị là:

.. math::

   v_n \approx \dfrac{1}{\sqrt{n \pi}} \left( \dfrac{2 \pi e}{n} \right)^{n/2}


GH suy ra:

.. math::

   \lambda_1 \approx \det(\mathcal{L})^{1/n} \sqrt{\dfrac{n}{2 \pi e}}.

Geometric Series Assumption
---------------------------

GSA mô hình hóa độ dài các vector Gram--Schmidt của một cơ sở đã rút gọn như một cấp số nhân. Nếu :math:`\bm{b}_1^*, \ldots, \bm{b}_n^*` là các vector Gram--Schmidt, ta giả sử tồn tại :math:`r \in (0, 1)` sao cho

.. math::

   \lVert \bm{b}_{i+1}^* \rVert^2 \approx r \lVert \bm{b}_i^* \rVert^2.

Vì :math:`\prod_{i=1}^n \lVert \bm{b}_i^* \rVert = \det(\mathcal{L})`, giả định này cho phép ước lượng toàn bộ profile Gram--Schmidt từ định thức và hệ số :math:`r`. Trong phân tích BKZ, :math:`r` thường được biểu diễn qua root-Hermite factor :math:`\delta_0`:

.. math::

   \lVert \bm{b}_i^* \rVert \approx
   \delta_0^{\,n-2i+1} \det(\mathcal{L})^{1/n}.

GH ước lượng độ dài vector ngắn nhất, còn GSA ước lượng hình dạng của cả cơ sở sau rút gọn; hai heuristic thường được dùng cùng nhau khi đánh giá chi phí tấn công lattice.
