Thuật toán F4 và ma trận Macaulay
=================================

F4 vẫn dựa trên các cặp tới hạn và đa thức S như Buchberger, nhưng xử lý một
nhóm cặp trong cùng một bước. Thay vì chia từng đa thức riêng lẻ, F4 mã hóa các
phép khử thành phép khử Gauss trên một ma trận thưa.

Từ đa thức tới ma trận
----------------------

Giả sử tập đa thức cần khử chứa các đơn thức khác nhau
:math:`m_1\succ m_2\succ\cdots\succ m_N`. Mỗi đa thức

.. math::

   f=a_1m_1+\cdots+a_Nm_N

được biểu diễn bởi hàng :math:`(a_1,\ldots,a_N)`. Các cột của **ma trận
Macaulay** tương ứng với đơn thức, còn các hàng tương ứng với đa thức. Trên
:math:`\FF_2`, phần tử ma trận chỉ là bit và phép cộng hàng là XOR.

Ví dụ, với thứ tự cột :math:`x^2\succ xy\succ y^2\succ x\succ y\succ1`, ba
đa thức :math:`x^2+y`, :math:`xy+1`, :math:`x+y^2` cho ma trận

.. math::

   \begin{pmatrix}
   1&0&0&0&1&0\\
   0&1&0&0&0&1\\
   0&0&1&1&0&0
   \end{pmatrix}.

Khử hàng trên ma trận thực hiện đồng thời nhiều phép khử hạng tử dẫn đầu.

Một vòng lặp F4
---------------

Mỗi vòng lặp gồm bốn công đoạn:

#. **Selection:** chọn các cặp tới hạn có BCNN của đơn thức dẫn đầu cùng bậc
   nhỏ nhất.
#. **Symbolic preprocessing:** tạo hai bội đa thức ứng với mỗi cặp, rồi bổ sung
   các bội của phần tử trong cơ sở cần thiết để khử mọi đơn thức xuất hiện.
#. **Reduction:** dựng ma trận Macaulay, đưa nó về dạng bậc thang rút gọn và đổi
   các hàng trở lại thành đa thức.
#. **Update:** giữ các hàng có đơn thức dẫn đầu mới, thêm chúng vào cơ sở và tạo
   các cặp tới hạn mới.

Tiền xử lý tượng trưng là bước bảo đảm ma trận chứa đủ reducer. Nếu một đơn thức
:math:`m` trong các hàng hiện tại chia hết cho :math:`\LM(g)`, thuật toán thêm
:math:`(m/\LM(g))g`; quá trình lặp tới khi không xuất hiện đơn thức chưa xử lý.

So sánh với Buchberger
----------------------

Hai thuật toán cùng tạo và xử lý các cặp tới hạn. Khác biệt nằm ở đơn vị công
việc:

* Buchberger lấy một cặp, tạo một đa thức S và thực hiện phép chia đa thức;
* F4 lấy một nhóm cặp và gom nhiều phép khử vào một bài toán đại số tuyến tính.

F4 thường nhanh hơn vì phép khử ma trận có tính cục bộ dữ liệu tốt, có thể dùng
các thư viện đại số tuyến tính và có nhiều phép toán độc lập. Đổi lại, nó cần
thêm bộ nhớ cho tập đơn thức, ma trận Macaulay và tiền xử lý tượng trưng.

Hiện thực trong ``CudaPolynomial``
----------------------------------

Hai lớp ``F4Algorithm`` và ``F4AlgorithmB`` hiện thực đúng chu trình trên.
``Selection`` gom mọi cặp có bậc BCNN nhỏ nhất. ``SymbolicPreprocessing`` xây
tập hàng, còn ``MacaulayMatrix`` ánh xạ chúng sang ma trận và khôi phục đa thức
sau khi khử.

Phần khử hàng được trừu tượng hóa thành nhiều backend:

* ``CPUInteger``: khử tuần tự trên CPU;
* ``OMPInteger``: khử song song bằng OpenMP;
* ``GPUInteger``: khử trên GPU bằng CUDA với phần tử nguyên;
* ``GPUBitPack``: khử CUDA với nhiều hệ số :math:`\FF_2` đóng gói trong một từ
  máy.

Sau khử, chương trình so sánh đơn thức dẫn đầu của các hàng với tập đơn thức dẫn
đầu trước đó và chỉ trả về những đa thức tạo pivot mới.
