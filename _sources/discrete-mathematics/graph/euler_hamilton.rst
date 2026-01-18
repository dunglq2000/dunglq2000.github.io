Đồ thị Euler và đồ thị Hamilton
===============================

Đồ thị Euler
------------

Leonhard Euler là người đầu tiên mô hình hóa bài toán rời rạc này thành một hệ thống hoàn chỉnh là Lý thuyết đồ thị hiện nay.

.. prf:definition:: Chu trình Euler
   :label: def-euler-cycle

   Chu trình đi qua tất cả các cạnh của đồ thị, mỗi cạnh đúng một lần, được gọi là **chu trình Euler** (hay **Euler circuit**, **Euler circle**, **Euler tour**).

.. prf:definition:: Đường đi Euler
   :label: def-euler-path

   Đường đi đi qua tất cả các cạnh của đồ thị, mỗi cạnh đúng một lần, được gọi là **đường đi Euler**.

Lúc này, bài toán :math:`7` cây cầu nổi tiếng của thành phố Konigsberg (nay là thành phố Kaliningrad thuộc Liên bang Nga) trở thành bài toán xác định xem có tồn tại chu trình Euler hay không.

.. prf:definition:: Đồ thị Euler
   :label: def-euler-graph
   
   Đồ thị có chu trình Euler được gọi là **đồ thị Euler** (hay **Eulerian graph**, **unicursal graph**).

.. prf:definition:: Đồ thị nửa Euler
   :label: def-half-euler-graph

   Đồ thị có đường đi Euler được gọi là **đồ thị nửa Euler** (hay **Semi-Eulerian graph**, **Traversable graph**).

Các định lí và thuật toán trên đồ thị Euler
-------------------------------------------

.. prf:theorem:: 
   :label: thm-connected-graph-euler-cycle

   Một đồ thị vô hướng liên thông :math:`G = (V, E)` có chu trình Euler khi và chỉ khi mọi đỉnh của nó đều có bậc chẵn.

.. admonition:: [TODO] Chứng minh
   :class: danger, dropdown

   **Chiều thuận.** Nếu :math:`G` có chu trình Euler thì khi đi theo chu trình đó, mỗi đỉnh sẽ đi vào một lần và đi ra một lần nên bậc của nó tăng lên :math:`2`. Áp dụng cho mỗi lần gặp một đỉnh thì cuối cùng bậc của mỗi đỉnh phải là số chẵn

   [TODO] **Chiều ngược.** Nếu mọi đỉnh của đồ thị đều có bậc chẵn, ta cần xây dựng cách tìm chu trình Euler. 

.. prf:corollary:: 
   :label: cor-euler-path

   Một đồ thị vô hướng liên thông :math:`G = (V, E)` có đường đi Euler khi và chỉ khi nó có đúng hai đỉnh bậc lẻ.

.. admonition:: Chứng minh
   :class: danger, dropdown

   Điều kiện của đường đi Euler "lỏng hơn" chu trình vì điểm đầu không cần phải trùng với điểm cuối. Do đó nếu :math:`G` có đường đi Euler thì đỉnh bắt đầu và kết thúc sẽ có bậc lẻ, các đỉnh còn lại có bậc chẵn. Ngược lại nếu đồ thị liên thông có đúng hai đỉnh bậc lẻ, khi đó ta vẽ cạnh nối hai đỉnh đó thì tất cả đỉnh của đồ thị đều có bậc chẵn, nghĩa là tồn tại chu trình Euler. Loại bỏ cạnh đó thì ta có đường đi Euler.

[TODO] Chu trình Euler và đường đi Euler của đồ thị có hướng liên thông yếu.

Đồ thị Hamilton
---------------

Khái niệm đường đi và chu trình Hamilton được đưa ra bởi William Rowan Hamilton (1856).

.. prf:definition:: Chu trình Hamilton và đồ thị Hamilton
   :label: def-hamilton-cycle-path

   Đồ thị :math:`G = (V, E)` được gọi là **đồ thị Hamilton** (hay **Hamilton graph**) nếu tồn tại chu trình đơn đi qua tất cả các đỉnh.

   Chu trình đơn đi qua tất cả các đỉnh gọi là **chu trình Hamilton** (hay **Hamiltonian circuit**, **Hamilton circle**).

Người ta quy ước rằng đồ thị chỉ gồm một đỉnh là đồ thị Hamilton nhưng đồ thị gồm hai đỉnh liên thông không phải là đồ thị Hamilton.
