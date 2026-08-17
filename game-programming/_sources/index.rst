Toán học cho đồ họa máy tính
############################

Đồ họa máy tính biến một mô hình hình học thành ảnh số. Phần này tập trung vào các cấu trúc toán học đứng sau quá trình đó, không phụ thuộc DirectX, OpenGL, Vulkan hay một game engine cụ thể.

Một pipeline dựng hình điển hình thực hiện chuỗi biến đổi

.. math::

   \text{model}
   \longrightarrow \text{world}
   \longrightarrow \text{view}
   \longrightarrow \text{clip}
   \longrightarrow \text{NDC}
   \longrightarrow \text{screen}.

Sau phần biến đổi hình học, primitive được cắt, rasterize thành fragment, tô bóng, kiểm tra độ sâu và tổng hợp vào framebuffer. Bài toán khử đường khuất của đa diện là một hiện thực hình học cụ thể của cùng nguyên lý visibility.

.. toctree::
   :maxdepth: 2

   mathematical-foundations
   geometric-modeling
   curved-geometry
   camera-and-pipeline
   rasterization-and-lighting
   polyhedron-visibility

Hình học và ứng dụng
====================

.. toctree::
   :maxdepth: 2

   lunar-calendar-geometry

Tài liệu tham khảo
==================

.. bibliography::
   :style: unsrt
