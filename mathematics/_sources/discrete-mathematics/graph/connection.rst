Tính liên thông của đồ thị
===========================

Tính liên thông trên đồ thị vô hướng
------------------------------------

.. prf:definition:: Đồ thị liên thông
   :label: def-graph-connected

   Một đồ thị vô hướng được gọi là **liên thông** (hay **connected**, hay **связанный**) nếu giữa hai đỉnh bất kì của đồ thị tồn tại đường đi.

Đồ thị chỉ gồm một đỉnh duy nhất cũng được coi là đồ thị liên thông.

.. figure:: ../../figures/graph/connected-graph.*

   Đồ thị liên thông

.. prf:definition:: Thành phần liên thông
   :label: def-connected-component

   Cho đồ thị :math:`G = (V, E)`. Nếu đồ thị con :math:`G' = (V', E')` của :math:`G` là đồ thị liên thông thì :math:`G'` được gọi là **thành phần liên thông** (hay **connected component**, **связанный компонент**) của đồ thị :math:`G`.

.. _connected-component:

.. figure:: ../../figures/graph/connected-component.*
 
   Các thành phần liên thông trên đồ thị

Trên :numref:`hình %s <connected-component>` có ba thành phần liên thông:

- thành phần liên thông thứ nhất gồm hai đỉnh :math:`v_1`, :math:`v_2`, và cạnh :math:`e_{12}`
- thành phần liên thông thứ hai gồm ba đỉnh :math:`v_3`, :math:`v_4`, :math:`v_6`, và các cạnh :math:`e_{36}`, :math:`e_{46}`
- thành phần liên thông thứ ba chỉ gồm đỉnh :math:`v_5`.

Đôi khi việc bỏ đi một đỉnh và tất cả cạnh liên thuộc với nó sẽ tăng số lượng thành phần liên thông hơn so với đồ thị ban đầu. Các đỉnh như vậy gọi là **đỉnh cắt** (hay **cut vertices**), hoặc **nút khớp** (hay **articulation nodes**).

Tương tự, khi bỏ đi một cạnh mà số lượng thành phần liên thông tăng lên thì cạnh đó gọi là **cạnh cắt** (hay **cut edges**) hoặc **cầu** (hay **bridge**).

Ở :numref:`hình %s <bridge>` là một đồ thị liên thông, nếu chúng ta xóa cạnh :math:`e_{24}` (cạnh màu đỏ) thì chúng ta sẽ có hai thành phần liên thông:

- thành phần liên thông thứ nhất gồm hai đỉnh :math:`v_1` và :math:`v_2`
- thành phần liên thông thứ hai gồm bốn đỉnh :math:`v_3`, :math:`v_4`, :math:`v_5` và :math:`v_6`.

.. _bridge:

.. figure:: ../../figures/graph/bridge.*
 
   Ví dụ về cầu

Đồ thị có thể có nhiều cầu. Ở :numref:`hình %s <bridge>`, thay vì xóa cạnh :math:`e_{24}`, nếu ta xóa cạnh :math:`e_{46}` thì cũng làm tăng số thành phần liên thông. Do đó cạnh :math:`e_{46}` cũng là cầu. Tương tự cho cạnh :math:`e_{12}`, ...

Tính liên thông trên đồ thị có hướng
------------------------------------

Một đồ thị có hướng được gọi là:

- **liên thông mạnh** (hay **strongly connected**) nếu tồn tại đường đi giữa hai đỉnh bất kì của đồ thị;
- **liên thông yếu** (hay **weakly connected**) nếu phiên bản vô hướng của nó là đồ thị liên thông.

Bài toán xác định các thành phần liên thông
-------------------------------------------

Bài toán xác định các thành phần liên thông của đồ thị là một bài toán quan trọng trong lý thuyết đồ thị. Bài toán sẽ tìm tất cả thành phần liên thông của đồ thị vô hướng.

Để liệt kê các thành phần liên thông của đồ thị vô hướng :math:`G = (V, E)` ta thực hiện các bước sau:

1. Bắt đầu từ một đỉnh bất kì, ta tìm tất cả đỉnh đến được từ đỉnh đó. Như vậy chúng ta tìm được một thành phần liên thông.
2. Loại những đỉnh ở thành phần liên thông đầu tiên và xét một trong những đỉnh còn lại. Lặp lại công việc ở bước 1, ta tìm tất cả đỉnh đến được từ đỉnh đang xét. Như vậy chúng ta tìm được thêm một thành phần liên thông.
3. Thực hiện đến khi đã xét hết tất cả đỉnh trong đồ thị.

Ở đây, để tìm tất cả đỉnh đến được từ một đỉnh nào đó trong đồ thị ta sử dụng thuật toán DFS (Depth First Search, Duyệt Sâu) hoặc BFS (Breadth First Search, Duyệt Rộng).
