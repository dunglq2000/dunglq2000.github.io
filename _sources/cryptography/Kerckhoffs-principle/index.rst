Nguyên tắc Kerckhoffs và mật mã học
************************************

Khi mình kể với mọi người rằng mình đang học mật mã thì mình nhận ra 
một điều thú vị là rất nhiều người hiểu lầm về mật mã. Trong quan điểm 
của đa số thì mật mã là một thứ gì đó cực kì bí mật và chỉ sử dụng 
trong quân sự. Điều này đúng từ nửa đầu thế kỉ 20 trở về trước, nhưng 
hiện tại thì mật mã được sử dụng rộng rãi trong dân sự, thậm chí là 
bắt buộc để đảm bảo an toàn thông tin trên Internet. Bài viết này sẽ 
giải thích một số khía cạnh của mật mã được sử dụng trong việc truyền 
thông tin.

Các bạn có thể xem phim "The Imitation Game" (năm 2014) về đội giải mã 
Enigma và nhà toán học Alan Turing để có cái nhìn tổng quan hơn những 
điều mình sắp nói.

.. figure:: The_Imitation_Game_(2014).png

    Nguồn: Wikipedia

Nguyên lý Kerckhoffs được phát biểu như sau:

.. epigraph:: 

    Độ an toàn của hệ thống mật mã không phụ thuộc vào việc giữ bí mật 
    thuật toán mã hóa mà phụ thuộc vào việc giữ bí mật khóa.

Các bạn cũng có thể đọc hai bài viết sau:

- `Nguyên lý Kerckhoffs - công trình khoa học mật mã uyên bác từ thế kỷ XIX <https://m.antoanthongtin.gov.vn/mat-ma-dan-su/nguyen-ly-kerckhoffs---cong-trinh-khoa-hoc-mat-ma-uyen-bac-tu-the-ky-xix-106784>`_.
- `Mật mã hiện đại (1) <https://vnhacker.blogspot.com/2010/05/mat-ma-hien-ai-1.html>`_.


Vấn đề truyền tin trên kênh mở
===============================

Thông tin có thể được truyền đi dưới nhiều dạng:

- tiếng nói;
- sóng điện từ (sóng radio);
- tín hiệu điện tử (qua cáp đồng);
- tín hiệu ánh sáng (qua cáp quang);
- vân vân và mây mây.

Thông thường chúng ta sử dụng các loại sóng vô tuyến, cáp quang để truyền 
tín hiệu đi xa. Vấn đề là các tín hiệu đó có thể bị bắt (chặn) lại bằng 
nhiều dụng cụ vật lý.

Trong phim "The Imitation Game", bộ phận thu sóng của quân Đồng minh chặn 
được hàng tá thông điệp của quân Phát xít gửi bằng radio mỗi ngày (từ bộ 
chỉ huy gửi tới đơn vị tác chiến) bằng các thiết bị chuyên dụng. Như vậy 
các kênh truyền trên trở thành các kênh mở, không chỉ người gửi và người 
nhận có thể biết thông điệp (tín hiệu) mà những bên có các thiết bị 
chuyên dụng cũng có thể đọc được.


Mã Caesar - nguồn gốc mật mã học
=================================

Thời xa xưa, cụ thể là thế kỉ 3 Sau Công Nguyên, hệ mã hóa đầu tiên là Caesar 
ra đời nhằm phục vụ chiến tranh. Các chỉ thị từ bộ chỉ huy được gửi tới các trạm, 
nhưng nếu gửi văn bản bình thường sẽ rất nguy hiểm nếu người đưa tin bị địch tóm. 
Như vậy mật mã sẽ giải quyết vấn đề này.

Mật mã gồm hai quá trình ngược nhau là **mã hóa** (hay **encrypt**) và **giải mã** 
(hay **decrypt**). Câu chuyện về mật mã Caesar như sau.

Giả sử ông Caesar muốn gửi thông điệp "It is rainy today" (thông tin về thời tiết). 
Ông Caesar sẽ không viết thông điệp này lên tờ giấy, xếp gọn lại, rồi đưa cho anh 
shipper gửi tới tiền tuyến. Thay vào đó, ông ấy viết từng ký tự trong thông điệp 
bởi chữ cái đứng sau nó ba ký tự trong bảng chữ cái. Nghĩa là "I" thành "L", "t" 
thành "w", vân vân và mây mây. Như vậy thông điệp sau khi biến đổi là "Lw lv udlqb 
wrgdb". Đây là quá trình **mã hóa**, biến đổi thông điệp gốc thành thành thông điệp 
mới khác ban đầu (và đa phần không có ý nghĩa).

.. note:: 

    Thông điệp ban đầu được gọi là **bản rõ** (hay **plaintext**).

    Thông điệp đã bị mã hóa được gọi là **bản mã** (hay **ciphertext**).

Ở ví dụ trên:

- bản rõ "It is rainy today";
- bản mã là "Lw lv udlqb wrgdb".

Sau đó anh shipper mang tờ giấy có thông điệp này tới tiền tuyến. Các chú lính cát ở 
tiền tuyến sẽ làm công việc ngược lại, thay từng ký tự ở thông điệp mới bởi ký tự 
trước đó ba vị trí trong bảng chữ cái. Nghĩa là "L" thành "I", "w" thành "t", và 
tương tự vậy. Đây là quá trình **giải mã**, biến đổi thông điệp mới quay về thông điệp 
gốc ban đầu.

Công việc mã hóa và giải mã sử dụng một quy tắc chung cho tất cả ký tự của thông điệp, 
do đó chúng ta cần một công thức toán học biểu thị quá trình này.

Đầu tiên ta đánh số các ký tự của bảng chữ cái tiếng Anh bắt đầu từ :math:`0`.

.. only:: html

    .. table:: 
        :class: centered-table

        .. include:: caesar-table.rst.inc

.. only:: latex 

    .. tabularcolumns:: |c|c|c|c|c|c|c|c|c|c|c|c|c|

    .. include:: caesar-table.rst.inc

Giả sử bản rõ là dãy các ký tự :math:`p_1`, :math:`p_2`, ..., :math:`p_n` với :math:`p_i` 
là các ký tự thuộc bảng chữ cái tiếng Anh. Như vậy :math:`0 \leqslant p_i \leqslant 25`.

Nếu gọi bản mã là dãy các ký tự tương ứng  :math:`c_1`, :math:`c_2`, ..., :math:`c_n` 
thì việc dịch chuyển ba ký tự sang trái tương đương với công thức

.. math:: c_i = (p_i + 3) \bmod 26.

Ở đây modulo :math:`26` giúp việc tính toán không vượt khỏi bảng chữ cái, mang ý nghĩa 
là nếu đi tới cuối bảng chữ cái thì ta bắt đầu lại từ đầu (ví dụ "Y" sẽ thành "B").

Thay vì sử dụng số :math:`3`, chúng ta có thể sử dụng một số bất kì khác và giữ 
bí mật số này, gọi là **khóa bí mật**. Công thức chung lúc này sẽ là

.. math:: \boxed{c_i = (p_i + k) \bmod 26,}

với :math:`k` là khóa bí mật.


Reverse Engineering và mật mã học
=================================

Nếu chỉ có người gửi và người nhận biết nguyên lý mã hóa và khóa bí mật thì gần như 
không thể phục hồi bản rõ. Tuy nhiên nếu kẻ địch biết nguyên lý mã hóa thì sao? Với 
mã Caesar ở trên, nếu đã biết :math:`c_i = (p_i + k) \bmod 26` thì rõ ràng chúng ta 
có thể thử giải mã với từng khóa :math:`k = 1, 2, \ldots, 25` và xem thông điệp gốc 
nào có ý nghĩa.

Chúng ta thử giải mã thông điệp "Jr jvyy zrrg ng fgngvba". Với từng khóa :math:`k` 
ta giải mã theo công thức ngược lại là

.. math:: p_i = (c_i - k) \bmod 26

và nhận được bản rõ tương ứng theo bảng sau:

.. only:: html

    .. table:: 
        :class: centered-table

        .. include:: caesar-attack.rst.inc

.. only:: latex

    .. tabularcolumns:: |c|c|

    .. include:: caesar-attack.rst.inc

Ta thấy rằng :math:`k = 13` cho bản rõ là một thông điệp có ý nghĩa. 
Như vậy mã Caesar không an toàn trước phương pháp thử tất cả khóa có 
thể (vét cạn, bruteforce).

Vấn đề ở đây là khi đối thủ cũng biết nguyên lý mã hóa thì đối thủ 
có thể đưa ra phương pháp tấn công thuật toán mật mã. Khi thời đại 
phát triển với sự ra đời các máy cơ học, máy tính (phần cứng, phần mềm) 
thì các thuật toán mật mã được "giấu" kỹ bằng các kỹ thuật gây rối 
khác nhau. Tuy nhiên sau một thời gian thì các bên tấn công cũng hiểu được 
toàn bộ cơ chế hoạt động của phần mềm, phần cứng và sau đó là thuật toán. 
Quy trình tìm hiểu cơ chế hoạt động của một thiết bị, thuật toán nào đó 
là **reverse engineering** (dịch ngược). Khi đã biết cơ chế mã hóa 
thì việc phá mã trở nên dễ dàng, như mã RC4 được sử dụng để mã hóa 
tín hiệu WiFi.

Lúc này, mật mã học đi theo một cách tiếp cận khác. Nếu mã hóa là một 
quy trình với hai đầu vào là bản rõ :math:`p` và khóa :math:`k`, đầu ra 
là bản mã :math:`c`, thì quy trình này có thể được viết dưới dạng hàm số

.. math:: c = \mathsf{Enc}(p, k)

với :math:`\mathsf{Enc}` là thuật toán mã hóa. Lúc này, thuật toán 
:math:`\mathsf{Enc}` không cần thiết được giữ bí mật, mà chỉ cần giữ 
bí mật khóa :math:`k`. Như chúng ta đã thấy ở mã Caesar, từ bản mã 
ban đầu :math:`c`, với mỗi khóa :math:`k` chúng ta lại có một bản 
rõ :math:`p` tương ứng. Vậy bản rõ :math:`p` tương ứng khóa :math:`k` 
nào mới là thông điệp đúng, mang ý nghĩa?


Nguyên lý Kerckhoffs và mật mã hiện đại
=======================================

Từ phần trên chúng ta có thể rút ra một số yêu cầu chính đối với mật mã hiện đại.

**Yêu cầu thứ nhất** đối với mật mã an toàn là **tính không bí mật** của thuật toán 
mã hóa. Trong phim "The Imitation Game", quân Đồng Minh biết rõ quân Đức sử dụng 
máy Enigma để mã hóa các thông điệp gửi từ bộ chỉ huy tới đơn vị tác chiến. Họ 
(quân Đồng minh) thậm chí còn "thó" được một máy Enigma và mổ xẻ nó, biết rõ 
cách hoạt động của nó. Nhưng thiết lập của máy Enigma thay đổi mỗi ngày, đó chính 
là khóa bí mật. Dù biết cách máy Enigma hoạt động, nhưng không biết thiết lập 
(không biết khóa) thì cũng không thể giải mã được các thông điệp được gửi đi. 
Như mình đã nói, quân Đồng minh dư sức đọc các tín hiệu điện tử được gửi đi 
bởi quân Đức, nhưng những gì họ nhận được chỉ là những văn bản vô nghĩa, chính là 
bản mã. Enigma trở thành pháo đài vững chãi không thể bị phá thời đó.

Ngày nay, các thuật toán mật mã được sử dụng trên Internet được định nghĩa đầy đủ 
trong các tiêu chuẩn quốc gia, quốc tế (NIST, GOST, RFC, ...). Các tài liệu này 
tất nhiên là được công bố rộng rãi và được nhiều nhà nghiên cứu phân tích, đánh giá 
độ an toàn của các thuật toán mật mã. Ngoài ra, các giao thức mạng về mật mã (SSL/TLS) 
cũng chỉ rõ thuật toán mã hóa nào được sử dụng, yêu cầu với các tham số đầu 
vào, vân vân.

Trên đây chính là nội dung của nguyên lý Kerckhoffs. Ông viết nguyên lý này trong một 
tài liệu tên là "Mật mã trong quân sự" (tên gốc là "La Cryptographie Militaire"). Tuy 
nhiên ý nghĩa của nó không chỉ dừng lại ở quân sự mà còn cả dân sự, là môi trường 
Internet chúng ta đang sử dụng hằng ngày.

**Yêu cầu thứ hai** đối với mật mã an toàn là **không gian khóa phải đủ lớn**. Ở mã 
Caesar, không gian khóa có :math:`25` phần tử (vì :math:`k = 0` cho bản mã y hệt bản 
rõ nên không có ý nghĩa che giấu thông tin) nên rất dễ phá, thậm chí có thể thử bằng 
giấy và bút. Ngày nay các thuật toán mã hóa khối có không gian khóa rất lớn với các 
khóa có độ dài :math:`128` bit hoặc :math:`256` bit. Khi đó có :math:`2^{128}` trường 
hợp khóa nếu khóa có độ dài :math:`128` bit, cụ thể thì

.. math:: 2^{128} = 340282366920938463463374607431768211456,

một con số khổng lồ nếu chúng ta thử từng trường hợp, kể cả có sử dụng các máy tính 
mạnh nhất hiện tại. Ví dụ như thuật toán AES với trường hợp khóa :math:`256` bit được 
đánh giá là an toàn nhất hiện nay và sẽ còn an toàn trong nhiều năm tới.

Trên đây là hai yêu cầu đơn giản đối với mật mã an toàn hiện nay. Theo sự phát triển của 
khoa học và công nghệ thì nhiều phương pháp phá mã phức tạp (về mặt toán học) đã ra đời 
nên cũng có nhiều tiêu chí khác đánh giá độ an toàn của mật mã. Tuy nhiên các tiêu chí kia 
rất phức tạp nên mình sẽ không đề cập ở đây.

Cám ơn các bạn đã đọc bài viết của mình.

----

Moscow, ngày 23 tháng 1 năm 2025.
