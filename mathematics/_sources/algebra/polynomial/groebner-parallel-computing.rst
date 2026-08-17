Tính cơ sở Gröbner song song trên CPU và GPU
============================================

Không phải mọi phần của một thuật toán cơ sở Gröbner đều song song hóa hiệu quả.
Kết quả thực nghiệm của dự án ``CudaPolynomial`` cho thấy điều quan trọng là
chọn đúng hạt nhân tính toán và đúng cách biểu diễn dữ liệu.

Phần nào có thể chạy song song?
-------------------------------

Vòng lặp Buchberger có phụ thuộc dữ liệu: phần dư của một cặp có thể được thêm
vào cơ sở và thay đổi phép rút gọn của mọi cặp sau. Vì vậy, xử lý ngây thơ nhiều
cặp đồng thời có thể làm thay đổi thuật toán hoặc tạo nhiều công việc dư thừa.

F4 tạo ra ranh giới song song rõ hơn:

* bậc BCNN của các cặp có thể được tính độc lập;
* nhiều thao tác trong tiền xử lý tượng trưng có thể được gom nhóm;
* các phép XOR dùng để khử nhiều hàng ma trận có thể chạy đồng thời.

Trong dự án, hạt nhân chính được tăng tốc là phép khử hàng của ma trận Macaulay.

Biểu diễn ma trận trên :math:`\FF_2`
------------------------------------

Cách trực tiếp lưu mỗi hệ số bằng một ``int`` đơn giản nhưng lãng phí: một giá
trị chỉ cần một bit lại chiếm cả từ máy. Nếu ma trận có :math:`R` hàng và
:math:`C` cột, cách này cần xấp xỉ :math:`4RC` byte khi ``int`` có 32 bit.

Bit packing đặt 32 hệ số liên tiếp vào một từ 32 bit, giảm dung lượng lý thuyết
khoảng 32 lần. Phép cộng hai hàng trên :math:`\FF_2` trở thành XOR từng từ:

.. math::

   \text{row}_i\leftarrow\text{row}_i\oplus\text{row}_p.

Lợi ích không chỉ là tiết kiệm bộ nhớ. Một lệnh XOR xử lý nhiều hệ số và lượng
dữ liệu truyền giữa RAM, bộ nhớ GPU và các đơn vị tính toán giảm mạnh.

Chi phí truyền dữ liệu
----------------------

Chạy kernel nhanh không bảo đảm toàn chương trình nhanh. Một vòng F4 còn có các
bước tuần tự như xây danh sách đơn thức, tạo ma trận, sao chép host–device và
khôi phục đa thức. Với ma trận nhỏ, thời gian cấp phát, truyền dữ liệu và khởi
chạy kernel có thể lớn hơn phần thời gian tiết kiệm được nhờ GPU.

Theo các benchmark trong luận văn, khi số biến tăng thì thời gian của cả
Buchberger và F4 đều tăng rất nhanh; Buchberger bắt đầu tăng mạnh sớm hơn. Các
backend CPU, OpenMP và GPU dùng phần tử nguyên không tạo khác biệt lớn trên các
bộ dữ liệu nhỏ của thí nghiệm. GPU trở nên có ý nghĩa khi kết hợp với đóng gói
bit, bởi nó đồng thời giảm bộ nhớ và chi phí truyền dữ liệu.

Các nguyên tắc triển khai
-------------------------

Từ cấu trúc mã nguồn và kết quả thực nghiệm có thể rút ra một số nguyên tắc:

* đo toàn bộ vòng lặp F4, không chỉ thời gian kernel;
* dùng ma trận thưa hoặc bitset trước khi tăng số luồng;
* gom đủ công việc cho mỗi lần chuyển dữ liệu sang GPU;
* giữ dữ liệu trên device qua nhiều bước nếu kiến trúc chương trình cho phép;
* tách tiền xử lý tượng trưng khỏi khử số để dễ thay backend;
* so sánh kết quả bằng cơ sở Gröbner rút gọn, không so trực tiếp các cơ sở trung
  gian có thể khác nhau.

Giới hạn trong mật mã đại số
----------------------------

Mô hình hóa một mã khối tạo rất nhiều biến trung gian và phương trình Boolean.
Số đơn thức tiềm năng tăng theo hàm mũ, vì vậy ma trận Macaulay có thể vượt bộ
nhớ trước khi GPU đạt công suất tính toán tối đa. Song song hóa không thay đổi
độ phức tạp bản chất này; nó chỉ làm nhanh phần đại số tuyến tính đủ lớn và có
cấu trúc phù hợp. Do đó chọn mô hình phương trình, chiến lược chọn cặp, loại bỏ
cặp dư thừa và nén dữ liệu quan trọng không kém số lõi xử lý.
