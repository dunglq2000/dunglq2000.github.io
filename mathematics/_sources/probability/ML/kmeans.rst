==================
K-Means clustering
==================

Một công việc thường được quan tâm khi xử lý dữ liệu là phân loại một nhóm các đối tượng thành những nhóm nhỏ hơn theo những tiêu chí nhất định.

Tương tự như phần trước, chúng ta có :math:`N` điểm dữ liệu :math:`\bm{x}_i` thuộc :math:`\mathbb{R}^d`. Ta muốn phân cụm các vector này vào những cluster (cụm) sao cho chúng gần nhau nhất (về mặt khoảng cách Euclid).

Giả sử ta muốn phân :math:`N` điểm dữ liệu trên vào :math:`K < N` cluster. Ta cần tìm các điểm :math:`\bm{m}_1`, :math:`\bm{m}_2`, ..., :math:`\bm{m}_K` là tâm của các cụm, sao cho tổng khoảng cách từ các điểm :math:`\bm{x}_i` tới tâm cluster mà nó được phân vào là nhỏ nhất. Nghĩa là ứng với center :math:`\bm{m}_1` ta cần tìm các điểm :math:`\bm{x}_{i_1}`, :math:`\bm{x}_{i_2}`, ..., :math:`\bm{x}_{i_t}` sao cho :math:`\sum\limits_{j=1}^t \lVert \bm{x}_{i_j} - \bm{m}_1 \rVert^2` nhỏ nhất. Tương tự cho các tâm khác.

Nhưng câu chuyện phức tạp ở đây là, tâm nằm ở đâu để có thể bao quát các điểm? Tâm được chọn phải có tính tổng quát, và việc phân các điểm vào cluster tương ứng với tâm thực hiện như thế nào?

Một kỹ thuật thường được sử dụng là **one-hot**. Với mỗi điểm dữ liệu :math:`\bm{x}_i` ta thêm một label :math:`\bm{y}_i = (y_{i1}, \ldots y_{iK})`. Điểm :math:`\bm{x}_i` sẽ thuộc cluster :math:`j` khi :math:`y_{ij} = 1`, không thuộc thì bằng :math:`0`. Như vậy chỉ có đúng một phần tử của :math:`\bm{y}_i` bằng :math:`1`, còn lại bằng :math:`0`, suy ra ràng buộc của :math:`\bm{y}_i = (y_{i1}, y_{i2}, \ldots, y_{iK})` là :math:`y_{ij} \in \{ 0, 1 \}` và :math:`\sum\limits_{j=1}^K y_{ij} = 1`.

Khi đó, ta mong muốn phân các điểm :math:`\bm{x}_i` vào cluster :math:`\bm{m}_k` để khoảng cách tới tâm :math:`\bm{m}_k` là ngắn nhất, hay :math:`\lVert \bm{x}_i - \bm{m}_k \rVert^2 \to \min`. Thêm nữa, với cách kí hiệu :math:`y_{ij}` như trên, biểu thức tương đương với

.. math:: \lVert \bm{x}_i - \bm{m}_k \rVert^2 = y_{ik} \lVert \bm{x}_i - \bm{m}_k \rVert^2 = \sum_{j=1}^K y_{ij} \lVert \bm{x}_i - \bm{m}_j \rVert^2

vì điểm :math:`\bm{x}_i` sẽ thuộc cluster :math:`\bm{m}_k` nào đó với :math:`1 \leqslant k \leqslant K`.

Sai số cho toàn bộ dữ liệu lúc này sẽ là

.. math:: \mathcal{L} (\bm{Y}, \bm{M}) = \sum_{i=1}^N \sum_{j=1}^K y_{ij} \lVert \bm{x}_i - \bm{m}_j \rVert^2.

Ta cần tối ưu :math:`\bm{Y}` và :math:`\bm{M}`. Việc tối ưu hai ma trận cùng lúc là rất khó thậm chí bất khả thi. Do đó chúng ta có một cách tiếp cận khác là luân phiên cố định một bên và tối ưu bên còn lại. Từ đó công việc được chia làm hai bước.

**Bước 1.** Cố định :math:`\bm{M}`, tìm :math:`\bm{Y}`.

Giả sử ta đã biết các center :math:`\bm{m}_1`, :math:`\bm{m}_2`, ..., :math:`\bm{m}_K`. Lúc này ta cần phân các điểm :math:`\bm{x}_i` vào cluster gần nó nhất. Dễ thấy rằng center gần nó nhất sẽ có khoảng cách Euclid ngắn nhất. Do đó ta tìm :math:`j` sao cho :math:`\lVert \bm{x}_i - \bm{m}_j \rVert^2` đạt nhỏ nhất. Không cần thiết phải tính căn bậc hai để giảm độ phức tạp.

**Bước 2.** Cố định :math:`\bm{Y}`, tìm :math:`\bm{M}`.

Khi đã biết :math:`\bm{Y}` tức là ta đã biết điểm nào được phân vào cluster nào. Khi đó ta cần tìm tâm cho từng cluster. Gọi :math:`l(\bm{m}_j)` là hàm tổng bình phương khoảng cách các điểm trong cluster tới tâm :math:`\bm{m}_j`, nghĩa là

.. math:: l (\bm{m}_j) = \sum_{i=1}^N y_{ij} \lVert \bm{x}_i - \bm{m}_j \rVert^2.

Mục tiêu của chúng ta là tối ưu tâm :math:`\bm{m}_j`. Do đó ta đạo hàm theo vector :math:`\bm{m}_j` thu được

.. math:: \dfrac{\partial l(\bm{m}_j)}{\partial \bm{m}_j} = \sum_{i=1}^N 2 \cdot y_{ij} (\bm{x}_i - \bm{m}_j).

Cho đạo hàm bằng :math:`0` và biến đổi ta có

.. math:: 
    
    & 2 \sum_{i=1}^N y_{ij} (\bm{x}_i - \bm{m}_j) = 0 \\
    \Longleftrightarrow \, & \bm{m}_j \sum_{i=1}^N y_{ij} = \sum_{i=1}^N y_{ij} \bm{x}_i \\
    \Longleftrightarrow \, & \bm{m}_j = \dfrac{\sum_{i=1}^N y_{ij} \bm{x}_i}{\sum_{i=1}^N y_{ij}}.

Để ý rằng, :math:`\sum\limits_{i=1}^N y_{ij}` là số lượng điểm trong cluster, và :math:`\sum\limits_{i=1}^N y_{ij} \bm{x}_i` là tổng các điểm trong cluster. Như vậy :math:`\bm{m}_j` là trung bình cộng các điểm trong cluster :math:`j`.

.. prf:algorithm:: Thuật toán K-Means clustering
    :label: algo-kmeans-clustering

    **Input:** Dữ liệu :math:`\bm{X}` (có :math:`N` điểm dữ liệu) và số cluster :math:`K`

    **Output:** Các center :math:`\bm{M}` và label :math:`\bm{y}` cho mỗi điểm dữ liệu

    1. Chọn :math:`K` điểm bất kì làm các cluster ban đầu.
    2. Phân mỗi điểm dữ liệu vào cluster gần nó nhất (cố định :math:`M`, tìm :math:`Y`).
    3. Nếu việc phân dữ liệu vào các cluster ở bước 2 không thay đổi so với trước đó thì dừng thuật toán.
    4. Cập nhật center mới cho mỗi cluster bằng cách lấy trung bình cộng các điểm trong cluster (cố định :math:`Y`, tìm :math:`M`).
    5. Quay lại bước 2.
