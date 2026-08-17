Hình học trên bề mặt cong
=========================

Metric cảm sinh
---------------

Trên một bề mặt, khoảng cách nên được đo dọc theo bề mặt chứ không phải bằng
đoạn thẳng xuyên qua không gian bao quanh. Với tham số hóa
:math:`\bm{s}(u, v)`, vi phân vị trí là

.. math:: d \bm{s} = \bm{s}_u\, du + \bm{s}_v\, dv.

Bình phương độ dài vi phân có dạng

.. math::

   dl^2 = E\, du^2 + 2 F\, du\, dv + G\, dv^2,

trong đó

.. math::

   E = \bm{s}_u \cdot \bm{s}_u,
   \qquad
   F = \bm{s}_u \cdot \bm{s}_v,
   \qquad
   G = \bm{s}_v \cdot \bm{s}_v.

Ma trận

.. math::

   g = \begin{bmatrix} E & F \\ F & G \end{bmatrix}

là metric cục bộ. Nó quyết định độ dài, góc và phần tử diện tích
:math:`dA = \sqrt{\det g}\, du\, dv`. Trong đồ họa, metric giúp đánh giá độ méo
texture, chọn mật độ tessellation và tính chuyển động bị ràng buộc trên mặt.

Mặt cầu
-------

Mặt cầu bán kính :math:`R` có tham số hóa

.. math::

   \bm{s}(\theta, \varphi)
   = R(\sin \theta \cos \varphi,
       \sin \theta \sin \varphi,
       \cos \theta).

Metric tương ứng là

.. math:: dl^2 = R^2\, d \theta^2 + R^2 \sin^2 \theta\, d \varphi^2.

Nếu :math:`\widehat{\bm{p}}` và :math:`\widehat{\bm{q}}` là hai hướng đơn
vị, khoảng cách cung ngắn nhất bằng

.. math::

   d(\bm{p}, \bm{q})
   = R \arccos \bigl(\operatorname{clamp}
      (\widehat{\bm{p}} \cdot \widehat{\bm{q}}, -1, 1)\bigr).

Phép ``clamp`` tránh lỗi số làm đối số vượt khỏi miền của :math:`\arccos`.
Đường đi ngắn nhất là cung của một đường tròn lớn. Đây là mô hình tự nhiên
cho camera quỹ đạo, hành tinh và nội suy hướng.

Phép chiếu lập thể
------------------

Phép chiếu từ một cực của mặt cầu đơn vị xuống mặt phẳng tạo ánh xạ

.. math::

   (x, y, z) \longmapsto
   (u, v) = \left(\frac{x}{1 - z}, \frac{y}{1 - z} \right).

.. figure:: ../figures/stereographic-projection/proj-3d.*
   :name: fig-stereographic-projection-3d
   :align: center
   :width: 70%

   Phép chiếu một điểm trên mặt cầu xuống mặt phẳng.

Ánh xạ ngược là

.. math::

   x = \frac{2 u}{1 + u^2 + v^2},
   \qquad
   y = \frac{2 v}{1 + u^2 + v^2},
   \qquad
   z = \frac{u^2 + v^2 - 1}{1 + u^2 + v^2}.

Phép chiếu này bảo toàn góc cục bộ nhưng không bảo toàn diện tích hoặc độ
dài. Do đó nó hữu ích khi hướng quan trọng hơn kích thước, nhưng không nên
dùng trực tiếp cho texture cần mật độ texel đồng đều.

.. figure:: ../figures/stereographic-projection/proj-2d.*
   :name: fig-stereographic-projection-section
   :align: center
   :width: 65%

   Lát cắt hai chiều cho thấy tia chiếu và ảnh của điểm.

Mô hình metric trên đĩa
-----------------------

Một metric cong âm có thể được biểu diễn trên đĩa đơn vị
:math:`u^2 + v^2 < 1` bởi

.. math::

   dl^2 = \frac{4(du^2 + dv^2)}{(1 - u^2 - v^2)^2}.

Hệ số tỉ lệ tăng vô hạn khi tiến đến biên: biên hữu hạn trong tọa độ ảnh
nhưng ở xa vô hạn theo metric. Các đường trắc địa trong mô hình này là đường
kính hoặc cung tròn vuông góc với biên. Cấu trúc đó được dùng để trực quan
hóa không gian phân cấp, thế giới cong và các phép lát lặp.

.. figure:: ../figures/stereographic-projection/proj-pseudo-2d.*
   :name: fig-negative-curvature-projection
   :align: center
   :width: 65%

   Lát cắt của phép chiếu từ một mặt có metric cong âm.

Đường trắc địa và tính toán rời rạc
-----------------------------------

Đường trắc địa giữa hai điểm làm cực trị phiếm hàm độ dài

.. math::

   L[\gamma]
   = \int_a^b
    \sqrt{\dot{\gamma}(t)^{\mathsf T}
           g(\gamma(t))\dot{\gamma}(t)}\, dt.

Trên mesh tam giác, thường không giải trực tiếp phương trình vi phân. Hai
xấp xỉ thực dụng là:

- coi cạnh mesh là đồ thị có trọng số rồi tìm đường ngắn nhất;
- dùng khoảng cách trên mặt theo phương pháp lan truyền, sau đó lần ngược
  gradient của trường khoảng cách.

Độ chính xác phụ thuộc mật độ và chất lượng tam giác. Nếu mesh có tam giác
dài, mảnh hoặc phân bố không đều, khoảng cách rời rạc có thể lệch đáng kể so
với metric của bề mặt trơn.
