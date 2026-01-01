Cơ sở xây dựng notebook
***********************

Mục tiêu của notebook
=====================

Notebook này được xây dựng từ kiến thức của bản thân 
mình, những điều thú vị đối với mình trên con đường học 
toán và mật mã học. Lượng kiến thức và công bố khoa học 
ngày nay quá nhiều nên mình chỉ ghi lại những điều mình 
thích và mình nghĩ là quan trọng với mình.

Notebook này được mình xây dựng cho bản thân trong tương 
lai. Tuy vậy mình cũng hy vọng một ngày đẹp trời nào đó 
notebook này trở thành nơi giúp cộng đồng khoa học Việt 
Nam phát triển mạnh.


Công cụ phát triển notebook
===========================

Ban đầu, notebook được viết bởi LaTeX PDF. Phần cũ mình 
đã lưu ở `đây <https://github.com/dunglq2000/mynotes>`_, 
các bạn có thể xem nếu hứng thú.

Cá nhân mình rất thích font chữ trên LaTeX PDF (CMU Serif) 
nên mình bắt đầu viết vào tháng 3 năm 2023. Tuy nhiên sau nhiều 
suy nghĩ và tham khảo ý kiến thì mình đã quyết định chuyển 
hết sang dạng web vào tháng 10 năm 2024.

Việc viết notebook ở dạng web có một số ưu điểm so với PDF:

- cỡ chữ phù hợp với việc đọc trên điện thoại: mặc dù cùng 
  cỡ chữ 12pt nhưng trên điện thoại đọc PDF khó khăn hơn 
  đọc web;
- khả năng đưa code (Python, C++) vào: việc bỏ code vào 
  web không bị giới hạn bởi lề web và những đoạn code 
  quá dài không cần phải suy nghĩ nên xuống dòng như 
  thế nào như trên PDF;
- một tính năng thú vị mà mình hay dùng của package 
  ``sphinx`` (Python) là các admonition. Mình sử dụng 
  hai class là ``danger`` và ``dropdown`` cho các phần 
  chứng minh và sau này mình dùng ``dropdown`` cho các 
  phần code. Lý do cho việc này mình sẽ giải thích rõ 
  ở phần sau;
- mình sử dụng package ``sphinx-proof`` để đánh số thứ 
  tự cho định nghĩa, định lí, nhận xét, tương tự như 
  việc khai báo ``newenvironment`` hay ``newtheorem`` 
  trong LaTeX. Hiện tại nhược điểm của package này là 
  chưa hỗ trợ tiếng Việt và mình cũng chưa biết đóng 
  góp hay chỉnh sửa ra sao.

Tuy nhiên một số nhược điểm ở dạng web cũng khá khó chịu:

- các công thức toán "inline", tức là được đặt trong cặp 
  dollar ``$...$`` không tự động xuống dòng nên dễ bị tràn 
  ra bên phải. Thực ra chúng ta có thể kéo màn hình qua 
  và đọc được nhưng không "mượt";
- font chữ: mình sử dụng theme ``Furo`` giống với trang tài 
  liệu của SageMath (phiên bản 2025) và nhà thiết kế theme 
  nói rằng font chữ được lựa chọn cẩn thận để phù hợp với 
  việc đọc trên web. Mình đồng ý với họ vì nhìn các font 
  LaTeX (CMU Serif) trên web lại không thuận mắt như trên 
  PDF. Cơ mà nếu được thì mình vẫn thích các font LaTeX 
  hơn.

Các hình vẽ chất lượng cao được vẽ từ TikZ và sau đó mình 
chuyển đổi PDF thành JPEG để đưa vào web nên chất lượng bị giảm.

UPDATE ngày 07/04/2025: ban đầu mình viết notebook bằng markdown 
(sử dụng Jupyter Book) nhưng vì Jupyter Book dựa trên Sphinx 
mà Sphinx có nhiều tính năng hay ho hơn nên mình chuyển sang 
viết bằng reStructuredText (rST) thay vì markdown. Dù vậy 
nếu độc giả vẫn có thể đóng góp bằng markdown (như bên dưới 
mình có trình bày) và mình sẽ tự sửa thành rST, tất nhiên là 
kèm credit.

Nguyên lí xây dựng notebook
===========================


Chứng minh là bắt buộc, nhưng dễ gây chán
-----------------------------------------

Mình nhận thấy nhiều quyển sách bị đánh giá thấp vì lối 
viết định lí rồi sau đó chứng minh, rồi lại tiếp tục như 
vậy. Đây thường là sách giáo trình được viết theo khuôn 
mẫu của nhà xuất bản nên điều này dễ hiểu. Tuy nhiên 
mình muốn ghi lại nhiều nội dung và việc ghi chứng minh 
sẽ khiến bài viết dài lê thê.

Chứng minh là bắt buộc nên mình vẫn viết nhưng sử dụng 
admonition của ``sphinx`` với class ``dropdown`` nhằm 
ẩn phần chứng minh đi. Các bạn có thể bấm vào chữ 
"Chứng minh" để xem đầy đủ. Template thông thường 
của chứng minh sẽ có dạng

.. code-block:: 

    .. admonition:: Chứng minh
        :class: danger, dropdown

        Ở đây viết chứng minh.

Kết quả sẽ như sau:

.. admonition:: Chứng minh
    :class: danger, dropdown
    
    Ở đây viết chứng minh.

Class ``danger`` để màu đỏ cho đẹp. :)))


Nếu có thể ẩn phần code thì mình sẽ ẩn
--------------------------------------

Notebook này có rất nhiều demo phá mã với 
code, cũng như writeup CTF. Mình nhận thấy cần 
có code để dễ theo dõi (cả đề lẫn lời giải). Tuy 
nhiên đôi khi code khá dài và việc này cũng khiến 
bài viết nhìn có vẻ dài. Do đó mình cũng sử dụng 
class ``dropdown`` để ẩn phần code đi hoặc chuyển 
thành đường dẫn tải xuống, và nếu các bạn muốn đọc 
chi tiết thì chỉ cần ấn vào để xem. Templete lúc 
này có dạng

.. code-block:: 

    .. admonition:: main.py
        :class: dropdown

        .. code-block:: python

            print("Hello, World")

Kết quả sẽ là:

.. admonition:: main.py
    :class: dropdown
    
    .. code-block:: python

        print("Hello, World")

Tiếng Việt là nền tảng
----------------------

Mình rất thích tiếng Việt và mình cũng không nghĩ là 
nên làm khó bản thân trong tương lai, thậm chí độc giả, 
bằng việc viết ngôn ngữ khác. Tiếng Việt rất giàu đẹp, 
phong phú, và sẽ luôn là xương sống cho notebook này.

Một vấn đề khá đau đầu là rất nhiều từ vựng chuyên ngành 
hiện tại chưa có thuật ngữ tương đương trong tiếng Việt. 
Các thuật ngữ mình dùng đa phần là lấy từ wikipedia hoặc 
đọc từ các sách tiếng Việt, còn nếu không có thì mình sẽ 
giữ nguyên tiếng Anh. Đôi khi các thuật ngữ lại nghe khá 
... chuối và các tay to nước nhà đã cải thiện dịch thuật. 
Ví dụ như "Dynamic programming" trong bảng dịch quyển 
"Introduction to Algorithm" của MIT năm 2006 được gọi là 
"Lập trình động", rất sát từ (mà giờ nhiều người gọi là 
dịch kiểu word-by-word). Lúc mình học cấp 3 (2015-2018) 
thì được là "Quy hoạch động" nghe vui hơn :)))

Một vấn đề đau đầu tương tự là sự trùng lặp thuật ngữ tiếng 
Việt. Hiện tại hai từ **encode** và **encrypt** đều được 
dịch là **mã hóa**, nhưng về bản chất của hai hành động 
là khác nhau hoàn toàn. Encode sẽ chuyển đổi giữa hai bảng 
chữ cái, ví dụ chuyển các kí tự trên bàn phím thành các 
số nhị phân gọi là bảng mã ASCII, hoặc trong lý thuyết 
coding là :math:`\mathbb{F}_2^n \to \mathbb{F}_2^m` với 
:math:`m` và :math:`n` không nhất thiết giống nhau. Trong 
khi đó encrypt sẽ biến đổi trong cùng bảng chữ cái, ví dụ 
RSA là :math:`\mathbb{Z}_n \to \mathbb{Z}_n` bằng phép 
modulo, mã khối nói chung có dạng :math:`\mathbb{F}_2^n \to \mathbb{F}_2^n`. 
Ở notebook này mình sẽ dùng mã hóa để chỉ **encrypt**, còn 
code thì mình sẽ giữ nguyên thuật ngữ tiếng Anh (lý thuyết 
coding, encode, decode, coder, decoder).

Mọi khái niệm, định nghĩa mình sẽ cố gắng viết bằng cả 
tiếng Việt, tiếng Anh và tiếng Nga. Quan trọng nhất là 
các bài viết trên notebook này sẽ chỉ được viết bằng 
tiếng Việt.


Tổng kết
========

Việc xây dựng notebook này giống như tài liệu học tập cho bản 
thân mình. Tuy nhiên nếu may mắn mà notebook này giúp bạn nào 
đó học tốt hơn thì cũng là điều tốt.

Mọi đóng góp của độc giả để giúp notebook tốt hơn, thậm chí đóng 
góp bài viết (ở dạng markdown) càng được hoan nghênh. Mình viết trên 
reStructuredText nhưng có thể không thân thiện với đa số người dùng 
nên các bạn gửi markdown về và mình sẽ tự sửa về rST. Các bạn có 
thể mở issue trên repository nếu có vấn đề với nội dung mình viết. 
Nếu các bạn muốn đóng góp bài viết (contribute) cho repository này, 
các bạn có thể contribute vào repository trên github hoặc gửi file 
markdown qua mail cho mình (dunglq@yandex.ru). Các bạn nhớ để lại 
tên ở cuối bài viết hoặc giới thiệu trong mail vì có khả năng mình 
sẽ biên tập lại bài viết của các bạn (về kí hiệu, bổ sung diễn giải, ...) 
nhưng mình giữ tên tác giả ở đầu bài viết. Như mình đã nói ở trên, 
các bài viết trên notebook này chỉ được viết bằng tiếng Việt nên 
mình xin phép chỉ nhận các bài đóng góp bằng tiếng Việt.

Cám ơn các bạn đã đọc những dòng ghi chú về những cơ sở và động lực 
mình xây dựng notebook này!!!

----

Moscow, ngày 23 tháng 02 năm 2025.
