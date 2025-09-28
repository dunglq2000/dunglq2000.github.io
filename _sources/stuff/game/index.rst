******************
Lý thuyết trò chơi
******************

===========================
Nhập môn lý thuyết trò chơi
===========================

Phần này mình tham khảo từ quyển Tài liệu chuyên tin học quyển 3 :cite:`TLCT3`.

----------------
Một số khái niệm
----------------

1. *Trạng thái* (hay *state*) (trong sách Tài liệu chuyên tin gọi là *vị trí* nhưng để phù hợp với nhiều bài viết khác như máy Turing, máy trạng thái thì gọi là *trạng thái* sẽ hợp lý hơn) là tập hợp thông tin về trò chơi tại từng thời điểm. Ví dụ như vị trí các quân cờ trên bàn cờ vua tại nước đi thứ :math:`1`, thứ :math:`2`, ...

Ta chia trạng thái làm hai loại:

- Những trạng thái chứa khả năng dẫn tới chiến thắng được gọi là trạng thái có lợi.
- Ngược lại thì gọi là trạng thái không có lợi.

2. *Luật chơi* (hay *rule*) là những quy định cho phép người chơi thực hiện các biến đổi chuyển trò chơi từ trạng thái này sang trạng thái khác. Ví dụ như cách di chuyển của mỗi quân cờ trong cờ vua (đi như thế nào, ăn quân như nào, ...).

Một bước đi hợp lệ là phép biến đổi theo đúng luật chơi.

Trạng thái kết thúc là trạng thái từ đó không thể di chuyển tiếp.

3. Trò chơi đối kháng là trò chơi hai người, khi một người có lợi thế thì người kia gặp bất lợi.

Có hai loại trò chơi đối kháng

- Trò chơi có thông tin đầy đủ - người chơi biết mọi thông tin về trạng thái hiện tại của đối phương. Ví dụ trong cờ vua, mỗi người chơi biết vị trí của tất cả quân cờ của đối thủ.
- Trò chơi có thông tin không đầy đủ - người chơi biết một phần hoặc không biết thông tin về trạng thái hiện tại của đối phương. Ví dụ chơi bài tây thì mỗi người không biết người khác có những quân bài gì. Ví dụ khác là trò chơi bầu cua, người đặt cược không biết được thông tin của ba quân súc sắc khi đặt cược.

4. Trong mọi trò chơi, quá trình chơi có thể được biểu diễn dưới dạng cấu trúc cây có hướng (đôi khi là đồ thị có hướng) gọi là *cây trò chơi*. Trong đó:

- *Nút* biểu diễn trạng thái.
- *Nút gốc* là trạng thái khởi đầu.
- *Nút lá* là trạng thái kết thúc.
- *Cung* :math:`(i, j)` thể hiện bước đi hợp lệ từ trạng thái :math:`i` tới trạng thái :math:`j`.

------------------------
Trò chơi tổ hợp cân bằng
------------------------

^^^^^
Mô tả
^^^^^

Trò chơi tổ hợp cân bằng là trò chơi đối kháng thỏa mãn các điều kiện:

- có hai người chơi (từ đây về sau, người đi đầu kí hiệu là :math:`A` và người đi sau là :math:`B`);
- có một tập hữu hạn các trạng thái có thể xảy ra của trò chơi, kí hiệu là :math:`X`;
- có luật chơi :math:`Q`. Quy luật chơi áp dụng cho hai người chơi là cân bằng, nghĩa là mỗi người chơi tới lượt mình đều có quyền chọn một phép di chuyển hợp lệ tùy ý;
- hai người chơi lần lượt, mỗi lần thực hiện một phép di chuyển hợp lệ;
- trò chơi kết thúc khi đạt trạng thái kết thúc;
- nếu trò chơi không bao giờ kết thúc thì có thể sử dụng rút thăm, hoặc giới hạn số lượng bước đi tối đa, hoặc cầu hòa.

^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Tập :math:`P`. Tập :math:`N`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. Tất cả các trạng thái kết thúc đều thuộc :math:`P`.
2. Từ mỗi trạng thái thuộc :math:`N` luôn có ít nhất một di chuyển tới trạng thái thuộc :math:`P`.
3. Từ mỗi trạng thái thuộc :math:`P`, mọi di chuyển đều tới trạng thái thuộc :math:`N`.

Như vậy ta cần xây dựng **thuật toán giành thắng** cho đấu thủ :math:`A` khi **ban đầu** :math:`A` **nhận trạng thái thuộc** :math:`N` là: đấu thủ :math:`A` **luôn di chuyển tới các trạng thái thuộc** :math:`P` để ép đối thủ :math:`B` chỉ có thể đi tới trạng thái thuộc :math:`N`.

^^^^^^^^^^^^^^^^^^^^^^
Tổng Nim. Trò chơi Nim
^^^^^^^^^^^^^^^^^^^^^^

Để dễ xác định tập :math:`P` và :math:`N` ta dùng khái niệm tổng Nim.

**Tổng Nim** là phép XOR hai số nguyên không âm.

**Trò chơi Nim chuẩn** là trò chơi có ba cọc lần lượt chứa :math:`x_1`, :math:`x_2` và :math:`x_3` quân. Hai người chơi lần lượt tạo các bước di chuyển quân với quy tắc: chọn một cọc tùy ý còn quân và lấy bớt một số quân từ cọc này. Người thắng là người lấy được quân cuối cùng.

Chúng ta có thể sử dụng tổng Nim để xác định tập :math:`P` với định lí Bouton.

.. prf:theorem:: Định lí Bouton
    :label: thm-bouton

    Mỗi trạng thái :math:`(x_1, x_2, x_3)` trong trò chơi Nim ba cọc là trạng thái :math:`P` khi và chỉ khi tổng Nim :math:`x_1 \oplus x_2 \oplus x_3 = 0`.

Từ định lí Bouton ta xây dựng chiến thuật giành thắng như sau.

Giả sử trạng thái hiện tại (cho trò chơi Nim với :math:`n` cọc) là :math:`(x_1, \ldots, x_n)`, ứng với tổng Nim

.. math:: g = x_1 \oplus x_2 \oplus \cdots \oplus x_n  > 0.

Ta có thể chứng minh tồn tại phần tử :math:`x_i` sao cho :math:`x_i' = (g \oplus x_i) \leqslant x_i`. Đây là cách đi giành thắng với mục tiêu là giảm cọc thứ :math:`i` từ :math:`x_i` quân thành :math:`x_i'` quân.

.. prf:example:: 
    :label: exp-nim-game

    Ví dụ đơn giản nhất với hai cọc :math:`(x_1, x_2)`. Như vậy trạng thái thuộc :math:`P` tương đương với :math:`x_1 \oplus x_2 = 0`, hay :math:`x_1 = x_2`. Từ đây suy ra trạng thái thuộc :math:`N` khi :math:`x_1 \neq x_2`.

    Giả sử :math:`A` là người chơi trước. Theo thuật toán giành thắng ở trên thì nếu :math:`A` ở trạng thái thuộc :math:`N` thì :math:`A` luôn thắng. Nghĩa là khi trạng thái là :math:`(x_1, x_2)` với giả sử :math:`x_1 < x_2` (trường hợp :math:`x_1 > x_2` tương tự) thì :math:`A` chỉ cần lấy đi ở cọc thứ hai một lượng :math:`x_2 - x_1` để hai cọc có số quân bằng nhau. Cuối cùng thì trạng thái kết thúc là :math:`(0, 0)` và :math:`A` sẽ chiến thắng.
