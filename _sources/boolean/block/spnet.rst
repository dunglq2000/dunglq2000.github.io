SP network
==========

SP network
----------

Mạng SP (SP network) là một cách xây dựng thuật toán mã hóa bên cạnh Feistel.

Mạng SP thường sử dụng một S-box làm nhiệm vụ xáo trộn và một P-box làm nhiệm vụ hoán vị. Hai nhiệm vụ có vẻ khá giống nhau, tuy nhiên S-box thường là một ánh xạ không tuyến tính và đôi khi làm giảm số bit đầu ra so với đầu vào (S-box của DES), còn P-box thường làm việc hoán vị vị trí các bit đầu vào (P-box của DES). Có thể thấy rằng P-box là ánh xạ tuyến tính (nhân với ma trận mà mỗi hàng và mỗi cột chứa đúng một số :math:`1`, còn lại là :math:`0`).

.. figure:: ../../figures/spnet/spnet-1.*

    Ví dụ SP network


.. figure:: ../../figures/spnet/spnet-2.*
    
    Ví dụ SP network

Tính chất của SP network
------------------------

Các thuật toán được xây dựng dựa trên SP network thường gồm hai phần:

1. Phần không tuyến tính (S-box).
2. Phần tuyến tính.

Đối với mỗi phép biến đổi của SP network đều cần có biến đối ngược của nó cho quá trình giải mã. Đây là điểm khác nhau cơ bản đối với mô hình Feistel.

Một số thuật toán sử dụng SP network
------------------------------------

Một số thuật toán sử dụng SP network: AES (tiêu chuẩn mã hóa Hoa Kì, định nghĩa trong FISP 197), Kuznyechik (tiêu chuẩn mã hóa Nga, định nghĩa trong GOST 34.12.2015, version :math:`128` bit).
