Câu hỏi ôn thi mật mã học
*************************

Môn "Các phương pháp bảo vệ thông tin bằng mật mã"
==================================================

Задачи криптографической защиты информации и средства их решения
----------------------------------------------------------------

Bốn mục tiêu chính là: **bí mật** bằng mã hóa; **toàn vẹn** bằng MAC hoặc chữ ký; **xác thực** bằng mật khẩu, challenge--response, chứng thư; và **chống chối bỏ** bằng chữ ký số cùng cơ chế ghi nhận thời gian.

Симметричные, асимметричные и комбинированные криптосистемы
-----------------------------------------------------------

Mật mã đối xứng dùng cùng khóa để mã hóa và giải mã, nhanh nhưng khó phân phối khóa. Mật mã bất đối xứng dùng cặp khóa công khai--bí mật, chậm hơn nhưng thuận tiện trao đổi khóa và ký số. Hệ lai dùng bất đối xứng bảo vệ khóa phiên và dùng đối xứng mã hóa dữ liệu lớn.

Шифры, алгебраическая модель шифра, примеры
-------------------------------------------

Một hệ mã là :math:`(\mathcal X,\mathcal K,\mathcal Y,E,D)` sao cho :math:`D_k(E_k(x))=x`. Với mỗi khóa :math:`k`, :math:`E_k` phải là đơn ánh; nếu :math:`\mathcal X=\mathcal Y` hữu hạn thì là một hoán vị. Ví dụ: Caesar, Vigenère, AES và RSA.

Шифры, вероятностная модель шифра, примеры
------------------------------------------

Mô hình xác suất bổ sung phân phối :math:`P_X`, :math:`P_K` và có thể cả randomness. Khi đó

.. math:: P_Y(y)=\sum_{E_k(x)=y}P_X(x)P_K(k).

Ví dụ: one-time pad với khóa đều; ElGamal và RSA-OAEP là mã xác suất.

Модели и критерии распознавания открытых текстов
------------------------------------------------

Plaintext được mô hình bằng nguồn ngôn ngữ có phân phối không đều. Có thể nhận dạng bằng tần suất ký tự/n-gram, entropy, redundancy, từ điển hoặc điểm log-likelihood; plaintext đúng thường có điểm thống kê cao hơn chuỗi ngẫu nhiên.

Криптоанализ классических шифров. Дешифрование шифра Виженера
-------------------------------------------------------------

Tìm chu kỳ khóa bằng Kasiski hoặc chỉ số trùng hợp. Chia ciphertext thành các cột theo chu kỳ; mỗi cột là Caesar nên tìm dịch chuyển bằng phân tích tần suất hoặc :math:`\chi^2`, rồi ghép các ký tự khóa.

Классификации шифров
--------------------

Phân loại theo khóa: đối xứng, bất đối xứng, lai; theo đơn vị xử lý: khối và dòng; theo biến đổi: thay thế, hoán vị, SPN, Feistel; theo tính ngẫu nhiên: tất định và xác suất.

Теоретическая и практическая стойкость шифров
---------------------------------------------

An toàn lý thuyết không phụ thuộc năng lực tính toán, điển hình là one-time pad. An toàn thực tế dựa trên chi phí phá mã vượt nguồn lực trong thời hạn cần bảo vệ; được đánh giá bằng mô hình tấn công, độ dài khóa và thuật toán tốt nhất.

Совершенные шифры
-----------------

Hệ mã hoàn hảo khi ciphertext không tiết lộ thông tin về plaintext: :math:`P(X=x\mid Y=y)=P(X=x)`, tương đương :math:`I(X;Y)=0`. One-time pad đạt tính chất này nếu khóa ngẫu nhiên đều, dài bằng thông điệp và chỉ dùng một lần.

Шифры замены и их криптоанализ
------------------------------

Mã thay thế ánh xạ mỗi ký hiệu hoặc nhóm ký hiệu sang ký hiệu khác. Mã thay thế đơn bảo toàn tần suất nên bị phá bằng tần suất chữ, digram/trigram và cấu trúc ngôn ngữ; mã đa bảng cần thêm bước tìm chu kỳ.

Шифры перестановки и их криптоанализ
------------------------------------

Mã hoán vị chỉ đổi vị trí ký tự nên giữ nguyên tần suất. Phá mã bằng thử độ dài khối, xét anagram/n-gram và tìm hoán vị tối ưu; không gian khóa tối đa của khối :math:`n` ký tự là :math:`n!`.

Шифрование методом гаммирования и его криптоанализ
--------------------------------------------------

Mã hóa dòng thường tính :math:`C_i=P_i\oplus\gamma_i`. Nếu gamma thật sự ngẫu nhiên và dùng một lần thì là OTP; nếu tái sử dụng, :math:`C\oplus C'` loại gamma và làm lộ quan hệ giữa hai plaintext.

Криптоаналитические атаки и их классификация
--------------------------------------------

Các mô hình chính: ciphertext-only, known-plaintext, chosen-plaintext (CPA), chosen-ciphertext (CCA), related-key và adaptive. Kỹ thuật gồm vét cạn, time--memory tradeoff, phân tích vi sai/tuyến tính, đại số, lỗi và side channel.

Блочные шифры. Принципы построения симметричных блочных шифров
----------------------------------------------------------------

Block cipher là họ hoán vị có khóa trên khối :math:`n` bit. Thiết kế thường dùng mạng Feistel hoặc SPN, lặp nhiều vòng để tạo confusion và diffusion; S-box cung cấp phi tuyến, permutation/mixing khuếch tán sai khác.

Режимы работы блочных шифров и их сравнение
-------------------------------------------

ECB độc lập nhưng lộ mẫu. CBC che mẫu và cần IV ngẫu nhiên. CFB/OFB biến block cipher thành stream cipher. CTR song song, truy cập ngẫu nhiên và nhanh nhưng không được lặp nonce/counter. Các mode này không tự xác thực; nên dùng AEAD như GCM hoặc CCM.

Методы анализа алгоритмов блочного шифрования
---------------------------------------------

Các phương pháp chính: vét cạn khóa, vi sai, tuyến tính, vi sai bất khả thi, integral, boomerang, meet-in-the-middle, đại số, related-key và side channel. So sánh chi phí với vét cạn :math:`2^k` và birthday bound theo kích thước khối.

Стандарт шифрования данных DES
------------------------------

DES là mạng Feistel 16 vòng, khối 64 bit, khóa hiệu dụng 56 bit và khóa vòng 48 bit. Hàm vòng mở rộng 32→48 bit, XOR khóa, qua 8 S-box rồi hoán vị. DES nay không an toàn vì khóa ngắn.

Развертывание раундовых ключей в DES
------------------------------------

Khóa 64 bit chứa 8 bit parity. PC-1 chọn 56 bit thành :math:`C_0,D_0`; mỗi vòng dịch trái 1 hoặc 2 bit, rồi PC-2 chọn 48 bit tạo :math:`K_i`. Dịch 1 bit ở vòng 1, 2, 9, 16; các vòng khác dịch 2 bit.

Режим сцепления блоков шифра (CBC) на примере DES
-------------------------------------------------

Với IV :math:`C_0`, mã hóa :math:`C_i=E_K(P_i\oplus C_{i-1})`; giải mã :math:`P_i=D_K(C_i)\oplus C_{i-1}`. IV phải không dự đoán được. Lỗi ở :math:`C_i` phá :math:`P_i` và lật bit tương ứng ở :math:`P_{i+1}`.

Режим обратной связи по выходу (OFB) на примере DES
---------------------------------------------------

Sinh :math:`O_i=E_K(O_{i-1})`, :math:`O_0=IV`, rồi :math:`C_i=P_i\oplus O_i`. Mã hóa và giải mã giống nhau; lỗi bit không lan truyền. Không được lặp IV với cùng khóa.

Режим обратной связи по шифртексту (CFB) на примере DES
-------------------------------------------------------

Với CFB toàn khối: :math:`C_i=P_i\oplus E_K(C_{i-1})`, :math:`C_0=IV`; giải mã dùng cùng :math:`E_K`. Mode tự đồng bộ nhưng lỗi ciphertext ảnh hưởng đoạn hiện tại và đoạn kế tiếp.

Имитостойкость шифров
---------------------

Đây là khả năng chống giả mạo/thay đổi dữ liệu. Cơ chế chuẩn là MAC (CMAC, HMAC, GMAC) hoặc AEAD. Checksum/parity không khóa chỉ phát hiện lỗi ngẫu nhiên, không chống đối thủ chủ động.

Стандарт шифрования данных AES
------------------------------

AES là SPN khối 128 bit, khóa 128/192/256 bit tương ứng 10/12/14 vòng. Mỗi vòng gồm SubBytes, ShiftRows, MixColumns, AddRoundKey; vòng cuối bỏ MixColumns.

Развертывание раундовых ключей в AES
------------------------------------

Khóa chia thành word 32 bit. Word mới là XOR với word cách :math:`N_k` vị trí; tại biên vòng áp dụng RotWord, SubWord và Rcon. AES-256 còn áp dụng SubWord khi :math:`i\equiv4\pmod8`.

Российский стандарт шифрования данных МАГМА (ГОСТ Р 34.12-2015)
---------------------------------------------------------------

Magma là Feistel 32 vòng, khối 64 bit, khóa 256 bit. Hàm vòng cộng modulo :math:`2^{32}` với khóa vòng, thay thế qua 8 S-box 4 bit, quay trái 11 bit rồi XOR nửa còn lại.

Развертывание раундовых ключей в стандарте МАГМА, количество слабых и 2-слабых ключей
-------------------------------------------------------------------------------------

Khóa 256 bit tách thành tám word 32 bit. Vòng 1--24 dùng :math:`K_1,\ldots,K_8` lặp ba lần; vòng 25--32 dùng :math:`K_8,\ldots,K_1`. Có :math:`2^{32}` khóa yếu dạng :math:`K_1=\cdots=K_8`; chuẩn Magma không quy định một số lượng chính thức cho lớp “2-yếu”.

Российский стандарт шифрования данных КУЗНЕЧИК (ГОСТ Р 34.12-2015)
------------------------------------------------------------------

Kuznyechik là SPN khối 128 bit, khóa 256 bit và 10 khóa vòng. Một vòng dùng XOR khóa, biến đổi phi tuyến S và tuyến tính L; vòng cuối chỉ XOR khóa.

Развертывание раундовых ключей в стандарте КУЗНЕЧИК
---------------------------------------------------

Hai nửa 128 bit của khóa là :math:`K_1,K_2`. Dùng mạng Feistel với 32 hằng số :math:`C_i=L(\mathrm{Vec}_{128}(i))`; sau mỗi 8 bước thu thêm một cặp khóa, tổng cộng 10 khóa vòng.

Поточные шифры. Принципы их построения
--------------------------------------

Stream cipher sinh keystream từ khóa và nonce rồi XOR dữ liệu. Yêu cầu: chu kỳ dài, gần đều, khó dự đoán, không lặp cặp khóa--nonce và có diffusion tốt từ trạng thái nội bộ.

Методы генерации и анализа псевдослучайных последовательностей
--------------------------------------------------------------

Có thể sinh bằng LFSR kết hợp phi tuyến, block cipher CTR/OFB hoặc CSPRNG dựa trên hash/stream cipher. Phân tích gồm chu kỳ, cân bằng, autocorrelation, linear complexity, kiểm thử thống kê và khả năng dự đoán.

Регистры сдвига, критерий регулярности
--------------------------------------

LFSR cập nhật trạng thái bằng recurrence tuyến tính trên :math:`\mathrm{GF}(2)`. Dãy là regular khi đa thức đặc trưng không có nghiệm bội, tương đương :math:`\gcd(f,f')=1`; khi đó không có thành phần lũy linh.

Регистры сдвига максимального периода
-------------------------------------

LFSR :math:`n` bit có chu kỳ cực đại :math:`2^n-1` với mọi trạng thái khác 0 khi và chỉ khi đa thức hồi tiếp bậc :math:`n` là primitive trên :math:`\mathrm{GF}(2)`.

Криптоанализ поточных шифров
----------------------------

Gồm correlation, fast correlation, algebraic, guess-and-determine, time--memory--data tradeoff và nonce reuse. Với LFSR đơn, Berlekamp--Massey khôi phục recurrence từ khoảng :math:`2L` bit, với :math:`L` là linear complexity.

Системы шифрования с открытыми ключами. Принципы их построения
----------------------------------------------------------------

Dựa trên hàm một chiều có cửa sập: khóa công khai cho phép mã hóa/kiểm tra, khóa bí mật cho phép giải mã/ký. Mã hóa thực tế phải xác suất và đạt ít nhất IND-CPA, thường hướng tới IND-CCA.

Анализ асимметричных криптосистем
---------------------------------

Kiểm tra bài toán nền, kích thước tham số, sinh khóa, padding/encoding, mô hình IND-CPA/CCA hoặc EUF-CMA, chi phí thuật toán tốt nhất và khả năng chống side channel.

Атаки на асимметричные криптосистемы
------------------------------------

Gồm giải bài toán nền, padding oracle, small exponent, reuse randomness, invalid-curve, fault injection, timing/cache/power và tấn công giao thức. Phòng vệ bằng chuẩn mã hóa đúng, kiểm tra đầu vào, blinding và constant-time.

Системы шифрования с открытыми ключами. Криптосистема RSA
---------------------------------------------------------

Chọn :math:`N=pq`, :math:`ed\equiv1\pmod{\lambda(N)}`. Mã hóa thô: :math:`c=m^e\bmod N`; giải mã :math:`m=c^d\bmod N`. Thực tế dùng OAEP cho mã hóa và PSS cho chữ ký.

Системы шифрования с открытыми ключами. Криптосистема Эль-Гамаля
----------------------------------------------------------------

Khóa bí mật :math:`x`, công khai :math:`y=g^x`. Chọn ngẫu nhiên :math:`k`; mã hóa :math:`(c_1,c_2)=(g^k,m y^k)`; giải mã :math:`m=c_2(c_1^x)^{-1}`. Không được lặp :math:`k`.

Управление ключами. Открытое распределение ключей Диффи--Хеллмана
-----------------------------------------------------------------

Alice gửi :math:`A=g^a`, Bob gửi :math:`B=g^b`; cả hai tính :math:`K=g^{ab}`. DH không tự xác thực nên bị man-in-the-middle; cần chữ ký/chứng thư và đưa shared secret qua KDF.

Электронная подпись. Принципы ее формирования
---------------------------------------------

KeyGen tạo :math:`(sk,pk)`; Sign ký hash bằng :math:`sk`; Verify dùng :math:`pk`. Yêu cầu đúng đắn và EUF-CMA. Chữ ký cung cấp toàn vẹn, xác thực nguồn và hỗ trợ chống chối bỏ, không cung cấp bí mật.

Электронная подпись на базе криптосистемы RSA
---------------------------------------------

RSA thô ký :math:`s=H(m)^d\bmod N`, kiểm tra :math:`s^e\equiv H(m)`. Thực tế phải dùng RSA-PSS; không ký trực tiếp thông điệp hay dùng textbook RSA.

Электронная подпись на базе криптосистемы Эль Гамаля
----------------------------------------------------

Chọn :math:`k` khả nghịch modulo :math:`p-1`, tính :math:`r=g^k`, :math:`s=k^{-1}(H(m)-xr)\bmod(p-1)`. Kiểm tra :math:`g^{H(m)}\equiv y^r r^s\pmod p`. Lặp :math:`k` làm lộ khóa bí mật.

Российский стандарт электронной подписи ГОСТ Р 34.10-2012
----------------------------------------------------------

Chuẩn dùng elliptic curve với khóa :math:`d`, :math:`Q=dP`. Với nonce :math:`k`, đặt :math:`r=x(kP)\bmod q`, :math:`s=(rd+ke)\bmod q`, :math:`e=H(m)\bmod q`. Có biến thể 256 và 512 bit.

Хэш-функции, требования к ним
-----------------------------

Hash ánh xạ dữ liệu tùy ý thành digest cố định. Yêu cầu khó tìm preimage, second preimage và collision; avalanche và phân phối đều. Collision security lý tưởng của hash :math:`n` bit là khoảng :math:`2^{n/2}`.

Методы построения функций хэширования
-------------------------------------

Cấu trúc phổ biến: Merkle--Damgård, HAIFA, sponge/duplex và tree hashing. Có thể xây compression function từ block cipher bằng Davies--Meyer hoặc Miyaguchi--Preneel.

Российский стандарт хэш-функции ГОСТ Р 34.11-2012
-------------------------------------------------

Streebog nhận thông điệp tùy ý và cho digest 256 hoặc 512 bit. Hàm nén dùng biến đổi S, P, L và 12 vòng; trạng thái còn theo dõi tổng độ dài và checksum modulo :math:`2^{512}`.

Криптографические протоколы и их классификация
----------------------------------------------

Protocol là chuỗi thông điệp/quy tắc để đạt mục tiêu mật mã. Phân loại theo mục tiêu: trao đổi khóa, xác thực, cam kết, chữ ký, zero-knowledge, bỏ phiếu; theo tương tác và số bên.

Системы аутентификации
----------------------

Xác thực dựa trên yếu tố biết (mật khẩu), có (token/khóa), hoặc là (sinh trắc). Dùng nonce/challenge chống replay, lưu mật khẩu bằng salted password hash và ưu tiên MFA.

Алгоритмы «облегченной» (lightweight) криптографии и их предназначение
------------------------------------------------------------------------

Lightweight cryptography tối ưu diện tích mạch, RAM, năng lượng và độ trễ cho IoT/RFID. Ví dụ: Ascon-AEAD128 và Ascon-Hash256.

Криптографические средства защиты информации в ОС Windows
----------------------------------------------------------

Windows cung cấp CNG/CryptoAPI, DPAPI, BitLocker, EFS, TLS/SChannel, Credential Guard và kho chứng thư. Ứng dụng nên dùng API cấp cao và bảo vệ khóa bằng hệ điều hành/TPM.

Криптографические средства защиты информации в MSDN
----------------------------------------------------

.NET có ``System.Security.Cryptography``: AES, RSA, ECDSA, ECDH, hash, HMAC, RNG và X.509. Dùng ``RandomNumberGenerator``, AEAD như ``AesGcm``; tránh DES, RC2, SHA-1.

Реализация операций над байтами в стандарте AES
-----------------------------------------------

Byte AES là phần tử :math:`\mathrm{GF}(2^8)` theo :math:`x^8+x^4+x^3+x+1`. Cộng là XOR; nhân là nhân đa thức rồi rút gọn. ``xtime`` dịch trái và XOR ``0x1B`` nếu bit cao ban đầu bằng 1.

Реализация преобразования SubBytes в стандарте AES
--------------------------------------------------

Lấy nghịch đảo nhân của byte trong :math:`\mathrm{GF}(2^8)` (:math:`0\mapsto0`), sau đó áp dụng affine transform và XOR ``0x63``. Inverse SubBytes dùng phép biến đổi ngược.

Реализация нелинейного узла замены в стандарте DES
--------------------------------------------------

Mỗi S-box DES nhận 6 bit, trả 4 bit. Hai bit ngoài chọn hàng, bốn bit giữa chọn cột; tra bảng :math:`S_i`. Tám S-box biến 48 bit thành 32 bit.

Вычисления в группе точек эллиптических кривых
----------------------------------------------

Trên :math:`y^2=x^3+ax+b`, nếu :math:`P\ne Q` thì :math:`\lambda=(y_Q-y_P)/(x_Q-x_P)`; nếu nhân đôi, :math:`\lambda=(3x_P^2+a)/(2y_P)`. Sau đó :math:`x_R=\lambda^2-x_P-x_Q`, :math:`y_R=\lambda(x_P-x_R)-y_P`.

Криптосистемы на эллиптических кривых. Принципы их построения
-------------------------------------------------------------

ECC dùng nhóm điểm đường cong, an toàn dựa trên ECDLP. Với cùng mức an toàn, khóa nhỏ hơn RSA. Phải kiểm tra điểm, dùng subgroup bậc lớn và scalar multiplication chống side channel.

Распределение ключей с использованием эллиптических кривых. Протокол Диффи--Хеллмана
-------------------------------------------------------------------------------------

Alice gửi :math:`A=aG`, Bob gửi :math:`B=bG`; shared point là :math:`aB=bA=abG`. Đưa encoding của điểm qua KDF; ECDH cần xác thực và kiểm tra public point.

Криптосистема Эль-Гамаля на эллиптических кривых
------------------------------------------------

Khóa công khai :math:`Q=dG`. Mã hóa điểm :math:`M`: :math:`(C_1,C_2)=(kG,M+kQ)`; giải mã :math:`M=C_2-dC_1`. Thực tế dùng ECIES/KEM-DEM.

Электронная подпись Эль-Гамаля на эллиптических кривых
------------------------------------------------------

ECDSA: :math:`r=x(kG)\bmod n`, :math:`s=k^{-1}(H(m)+dr)\bmod n`. Verify dùng :math:`u_1=H(m)s^{-1}`, :math:`u_2=rs^{-1}` và kiểm tra hoành độ của :math:`u_1G+u_2Q`. Nonce không được lặp.

Квантовая криптография, протоколы открытого распределения ключей
----------------------------------------------------------------

QKD phân phối khóa bằng trạng thái lượng tử; nghe lén gây nhiễu có thể phát hiện. BB84 dùng hai basis, rồi sifting, ước lượng lỗi, error correction và privacy amplification. Kênh cổ điển vẫn phải xác thực.
