Ứng dụng 3: mạng xã hội
=======================

Tổng quan
---------

Trong xã hội học, mạng lưới xã hội là một cấu trúc được mô hình hóa bằng đồ thị, thể hiện sự gắn kết và tương tác lẫn nhau giữa các đối tượng xã hội. Sự mô hình hóa trên cho phép chúng ta đánh giá định tính các mạng lưới bằng cách điều chỉnh sự hiển thị của các đỉnh và cạnh để làm nổi bật các thuộc tính mà ta quan tâm. Phần này được tham khảo từ slide bài giảng của A. Costan :cite:`Costan`.

Dưới đây là minh họa mô hình đồ thị LinkedIn của một người:

.. figure:: figures/graph_linkedin.png
    
Mạng lưới xã hội bao gồm các thành phần:

1. Đỉnh: đỉnh trong mạng thường thể hiện một đối tượng xã hội như một cá nhân hay một tổ chức.
2. Liên kết (tie): trong xã hội học, nói nôm na thì nếu giữa hai người là bạn bè với nhau thì gọi là liên kết mạnh (strong ties), còn nếu hai người chỉ quen biết nhau thì gọi là liên kết yếu (weak ties).
3. Phân cụm (clustering): dựa vào các kết nối trên, thông thường sẽ có một số tập các đỉnh được kết nối với nhau dày hơn, tạo thành các cụm (cluster). Tính chất này thường thể hiện rõ trong xã hội thực tế. Ví dụ như ở mạng lưới xã hội của một trường, mỗi lớp thường sẽ tạo thành một cụm, và một vài thành viên sẽ có kết nối đến các lớp/cụm khác.

   .. figure:: figures/graph_clusters.png

   Fun fact: Khi tìm việc làm, một người sẽ dễ tìm việc khi dựa vào các liên kết yếu hơn. Vì khi nhờ sự giúp đỡ của người quen, họ sẽ tìm trong các kết nối của chính họ, là những mối quan hệ mà ta không với đến được. Còn nếu nhờ bạn bè và người thân, thường họ sẽ cùng chung một cụm với ta nên khả năng tiếp cận không cao hơn đáng kể so với tự tìm việc.

4. Bao đóng tam giác (triadic closure): khi nào thì một cạnh được sinh ra?

   Nếu hai người trong một mạng lưới xã hội có **cùng một bạn chung**, thì khả năng hai người đó **trở thành bạn** với nhau trong tương lai sẽ cao hơn.

   .. figure:: figures/triadic_closure-1.*

   Sau một thời gian, các cạnh mới sẽ được sinh ra:

   .. figure:: figures/triadic_closure-2.*

   Ý nghĩa của bao đóng tam giác?

   1. Mạng tin cậy (Trust network): Nếu A tin tưởng B, và B tin tưởng C, thì A có cơ sở chính đáng để có thể tin tưởng C.
   2. Mạng lưới xã hội: A và C sẽ nếu có bạn chung là B, sẽ có nhiều cơ hội gặp gỡ nên sẽ ít nhất tạo nên một liên kết yếu.
   3. Bao đóng tam giác giúp nghiên cứu đồ thị thay đổi theo thời gian.
   4. ...

Ứng dụng
--------

Mô hình trên được áp dụng trong các mạng xã hội lớn, ví dụ như sau đây là của Facebook:

.. figure:: figures/graph8.png

Nhờ vào cấu trúc cơ bản như trên, các mạng xã hội có thể xây dựng các cấu trúc và tương tác phức tạp hơn như đăng bài viết, like, share, chat, gia nhập các group, ...

Hơn nữa, trong mạng xã hội Facebook, mọi thứ đều là một nút của đồ thị. Các tương tác giữa các đối tượng đều được lưu trữ lại để phân tích, và dùng để dựng nên một dạng đồ thị khác: **Interest Graph**.

Interest Graph
--------------

Interest graph là một cấu trúc thể hiện những chủ đề mà các cá nhân có hứng thú đến. Đồ thị này nhận được sự quan tâm to lớn bởi vì sở thích là một phần lớn của tính cách của một người, tạo nên danh tính của người đó, và có thể dùng để dự đoán họ "muốn làm gì", "muốn mua gì", "muốn gặp ai", "muốn bỏ phiếu bầu cho ai", ...

.. figure:: figures/graph9.png

Để xây dựng Interest Graph cần các bước chính:

1. Thu thập dữ liệu. Các tương tác lẫn nhau hằng ngày của người dùng là nguồn dữ liệu khổng lồ.
2. Đánh giá độ quan trọng của dữ liệu. Ví dụ, để đánh giá "sự quan tâm", thì tất nhiên một nút like sẽ có trọng số thấp so với hơn một lần check-in.
3. Tìm ra sự tương tự. Ví dụ như như mối quan tâm về "biển" có thể gắn liền với "du lịch" và "bơi lội", ...
4. Xây dựng và sử dụng. Từ dữ liệu ban đầu, xây dựng nên Interest Graph và đánh giá độ sự quan tâm của người dùng để áp dụng các chiến thuật phù hợp.

Interest Graph khác Social Graph ở chỗ, Social Graph dựa trên các *mối quan hệ* giữa hai cá nhân như bạn bè, đồng nghiệp, ... còn Interest Graph dựa trên *sở thích*, *mong muốn*, *mối quan tâm* của các cá nhân. Từ đó, dữ liệu này được dùng để phân loại người dùng thành các cụm dựa trên sở thích để gợi ý các trang, bài viết, nhóm phù hợp, hay để hiển thị quảng cáo, giảm giá đúng đối tượng, tăng khả năng tương tác (targeted ads), ...

Và đó là cách mà đồ thị được sử dụng trong các dịch vụ mạng xã hội.

Xử lý đồ thị lớn: trong thực tế, đồ thị được các công ty công nghệ lớn sử dụng rất phức tạp, và phải xử lý trên một mạng lưới máy tính thay vì một máy. Có nhiều giải pháp được đưa ra:

1. **Pregel** của Google. Được sử dụng ở thuật toán PageRank để đánh giá kết quả tìm kiếm từ Google Search.
2. **Giraph** của Apache. Mã nguồn mở, được viết dựa trên Pregel. Được sử dụng ở Facebook.
3. **Cassovary** của Twitter.
4. ...
