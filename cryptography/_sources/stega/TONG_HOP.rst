Tổng hợp bài lab môn Bảo vệ thông tin bằng kỹ thuật giấu tin
============================================================


Tài liệu tổng hợp ba báo cáo lab trong ``notes/stega``. Khi đọc nguồn đã loại bỏ các thư mục ``exam*``, PDF, ảnh, ``setup.sh``, ``signature.png``, ``preamable.tex``, ``*.bbx``, ``*.txt`` và toàn bộ phần comment trong LaTeX.

Lab 1. Giấu tin trong văn bản bằng ký tự zero-width
---------------------------------------------------


Mục tiêu
~~~~~~~~


Cài đặt thuật toán steganography dùng văn bản làm container và một câu hát làm thông điệp bí mật.

Ý tưởng và thuật toán
~~~~~~~~~~~~~~~~~~~~~


Thuật toán dùng hai ký tự Unicode không có độ rộng, thường không nhìn thấy trong trình soạn thảo:

- U+200B (zero-width space) biểu diễn bit ``0``;
- U+200D (zero-width joiner) biểu diễn bit ``1``.

Giả sử thông điệp bí mật là :math:`a_0, a_1, \ldots, a_{n - 1}` và văn bản container là :math:`b_0, b_1, \ldots, b_{m - 1}`. Mỗi ký tự của thông điệp được biểu diễn bằng 12 bit, tạo thành dãy

.. math::

   a'_0, a'_1, \ldots, a'_{12 n - 1}.


Độ dài stego-text là

.. math::

   L = 12 n + m.


Chọn khóa :math:`k` thỏa

.. math::

   3 \le k < L, \qquad \gcd(k, L) = 1.


Bit thứ :math:`i` được đặt tại vị trí

.. math::

   j_i = k i \bmod L.


Do :math:`k` khả nghịch modulo :math:`L`, ánh xạ :math:`i \mapsto k i \bmod L` là một hoán vị, vì vậy các bit không tranh chấp vị trí. Tại vị trí :math:`j_i`, ghi U+200B nếu :math:`a'_i = 0` và U+200D nếu :math:`a'_i = 1`. Sau đó điền tuần tự các ký tự :math:`b_i` vào những vị trí còn trống.

Giải mã dùng đúng khóa :math:`k` và đọc các vị trí :math:`k i \bmod L`:

.. math::

   a'_i = \begin{cases} 0, & c_{k i \bmod L} = \mathsf{U+200B}, \\ 1, & c_{k i \bmod L} = \mathsf{U+200D}. \end{cases}


Cuối cùng ghép từng nhóm 12 bit và chuyển lại thành ký tự Unicode.

Đặc điểm
~~~~~~~~


- Không xảy ra va chạm vị trí nếu :math:`\gcd(k, L) = 1`.
- Mã hóa và giải mã chỉ cần phép nhân modulo nên có chi phí thấp.
- Hai bên phải thống nhất bí mật :math:`k`.
- Ký tự zero-width có thể bị công cụ phân tích phát hiện hoặc bị phần mềm xử lý văn bản loại bỏ. Vì vậy đây là kỹ thuật che giấu, không thay thế mã hóa.
- Có thể thay ánh xạ nhân modulo bằng một hoán vị giả ngẫu nhiên sinh từ seed, rồi dùng các phần tử đầu của hoán vị làm vị trí nhúng.

Code demo
~~~~~~~~~


.. code-block:: python

   import random

   def gcd(a: int, b: int) -> int:
       while b:
           a, b = b, a % b
       return a

   class MyStegaAlgo1:
       def __init__(self, hidden_message: str):
           self.hidden_text = hidden_message
           self.bits = list(map(int, "".join(
               f"{ord(c):012b}" for c in self.hidden_text
           )))

       def encode_message(self, container_message: str):
           n = len(self.bits)
           m = len(container_message)
           L = n + m
           result = [-1] * L

           while True:
               k = random.randint(2, L - 1)
               if gcd(k, L) == 1:
                   break

           for i, bit in enumerate(self.bits):
               result[(k * i) % L] = ord("\u200b" if bit == 0 else "\u200d")

           j = 0
           for i in range(L):
               if result[i] != -1:
                   continue
               result[i] = ord(container_message[j])
               j += 1

           return "".join(chr(c) for c in result), k

       @staticmethod
       def decode_message(encoded_message: str, secret_key: int) -> str:
           L = len(encoded_message)
           bit_count = (
               encoded_message.count("\u200b")
               + encoded_message.count("\u200d")
           )
           bits = []

           for i in range(bit_count):
               char = encoded_message[(secret_key * i) % L]
               if char == "\u200b":
                   bits.append("0")
               elif char == "\u200d":
                   bits.append("1")
               else:
                   raise ValueError("Invalid secret key or damaged container")

           code_points = [
               int("".join(bits[i:i + 12]), 2)
               for i in range(0, len(bits), 12)
           ]
           return "".join(chr(c) for c in code_points)

   hidden_message = "Не, не, не задавай вопросов, не забивай голову проблемами"
   stega = MyStegaAlgo1(hidden_message)
   encoded_message, secret_key = stega.encode_message("Завтра я еду в вуз")
   decoded_message = MyStegaAlgo1.decode_message(encoded_message, secret_key)
   assert decoded_message == hidden_message
   print(decoded_message)


Kết luận
~~~~~~~~


Lab đã xây dựng được quá trình nhúng và trích xuất thông điệp trong văn bản bằng ký tự zero-width. Khóa :math:`k` quyết định thứ tự các vị trí chứa bit, còn nội dung hiển thị của container không thay đổi bằng mắt thường.

Lab 2. Giấu tin trong ảnh BMP bằng LSB và PRNG
----------------------------------------------


Mục tiêu
~~~~~~~~


Cài đặt thuật toán giấu một câu hát trong ảnh RGB24 định dạng BMP bằng phương pháp least significant bit (LSB).

Ý tưởng và thuật toán
~~~~~~~~~~~~~~~~~~~~~


Mỗi kênh màu của một pixel chứa một byte. Thay bit thấp nhất của byte chỉ làm giá trị kênh thay đổi tối đa 1, thường khó nhận biết bằng mắt. Seed bí mật khởi tạo PRNG; PRNG sinh tuần tự tọa độ :math:`(x, y)` và kênh màu trong tập :math:`\{R, G, B\}`.

Luồng bit được nhúng gồm:

1. 24 bit biểu diễn số ký tự :math:`L` của thông điệp;
2. mỗi ký tự được biểu diễn bằng 12 bit;
3. marker kết thúc ``111111111110`` dài 12 bit.

Với bit :math:`b_i` và giá trị kênh màu :math:`v_i`, thao tác nhúng là

.. math::

   v'_i = (v_i \mathbin{\&} \mathtt{0xFE}) \mathbin{|} b_i.


Khi giải mã, khởi tạo lại PRNG bằng cùng seed, tái tạo đúng chuỗi vị trí, đọc 24 bit độ dài rồi đọc :math:`12 L + 12` bit còn lại. Các nhóm 12 bit được chuyển về ký tự sau khi loại marker.

Giới hạn quan trọng
~~~~~~~~~~~~~~~~~~~


Code nguồn lấy mẫu vị trí có hoàn lại, nên cùng một tọa độ/kênh có thể xuất hiện nhiều lần. Lần ghi sau sẽ ghi đè bit trước và làm hỏng thông điệp; vì vậy phát biểu “va chạm có xác suất thấp” chỉ đúng khi payload rất nhỏ so với sức chứa ảnh. Cách chắc chắn hơn là tạo toàn bộ danh sách vị trí, trộn bằng PRNG rồi lấy các vị trí không lặp.

Ngoài ra:

- seed phải được bảo mật và hai bên phải dùng cùng seed;
- nên dùng định dạng lossless như BMP hoặc PNG, vì nén mất dữ liệu sẽ phá LSB;
- cần kiểm tra sức chứa theo số **vị trí duy nhất**, không chỉ theo :math:`rows \times cols \times 3`;
- một đối tượng ``LSBRandom`` chỉ nên dùng cho một thao tác encode hoặc decode vì trạng thái PRNG thay đổi sau mỗi lần gọi.

Code demo
~~~~~~~~~


.. code-block:: python

   import cv2
   from random import Random

   class LSBRandom:
       def __init__(self, seed: int):
           self.random = Random(seed)

       def encode(self, image_path: str, message: str, output_path: str):
           img = cv2.imread(image_path, cv2.IMREAD_COLOR)
           if img is None:
               raise FileNotFoundError("Image not found")

           rows, cols, _ = img.shape
           bits = f"{len(message):024b}"
           bits += "".join(f"{ord(char):012b}" for char in message)
           bits += "111111111110"

           if len(bits) > rows * cols * 3:
               raise ValueError("Message is too long")

           for bit in bits:
               x = self.random.randint(0, rows - 1)
               y = self.random.randint(0, cols - 1)
               channel = self.random.randint(0, 2)
               img[x, y, channel] = (img[x, y, channel] & 0xFE) | int(bit)

           cv2.imwrite(output_path, img)

       def decode(self, image_path: str) -> str:
           img = cv2.imread(image_path, cv2.IMREAD_COLOR)
           if img is None:
               raise FileNotFoundError("Image not found")

           def read_bit() -> str:
               x = self.random.randint(0, img.shape[0] - 1)
               y = self.random.randint(0, img.shape[1] - 1)
               channel = self.random.randint(0, 2)
               return str(img[x, y, channel] & 1)

           message_length = int("".join(read_bit() for _ in range(24)), 2)
           payload = "".join(read_bit() for _ in range(message_length * 12 + 12))
           marker = "111111111110"
           end = payload.find(marker)
           if end == -1:
               raise ValueError("Cannot find end marker")

           payload = payload[:end]
           return "".join(
               chr(int(payload[i:i + 12], 2))
               for i in range(0, len(payload), 12)
           )

   message = 'Я сказал: "Иди сюда", и ты сказала: "Да, да, да"'
   LSBRandom(1234).encode("greenland_grid_velo.bmp", message, "result.bmp")
   decoded = LSBRandom(1234).decode("result.bmp")
   assert decoded == message
   print(decoded)


Kết luận
~~~~~~~~


Lab đã cài đặt phương pháp LSB với thứ tự vị trí phụ thuộc seed. Ảnh sau khi nhúng gần như không khác ảnh gốc bằng mắt thường, còn người nhận có seed có thể tái tạo chuỗi vị trí để trích xuất thông điệp.

Lab 3. Giấu tin trong âm thanh WAV bằng pha DFT
-----------------------------------------------


Mục tiêu
~~~~~~~~


Cài đặt thuật toán giấu văn bản trong file WAV bằng một biến thể phase coding dựa trên biến đổi Fourier rời rạc, theo bài báo *An Improved Phase Coding Audio Steganography Algorithm* của Guang Yang (2024, arXiv:2408.13277).

Ý tưởng và thuật toán
~~~~~~~~~~~~~~~~~~~~~


Thông điệp được chuyển sang chuỗi bit 8 bit cho mỗi ký tự. Với :math:`B` là số bit thông điệp, chiều dài segment được chọn là

.. math::

   L_s = 2 \cdot 2^{\lceil \log_2(2 B) \rceil}.


Audio được chia thành :math:`N_s` segment độ dài :math:`L_s` và bổ sung mẫu để đủ segment cuối. Với mỗi segment :math:`i`, tính DFT

.. math::

   X_i[k] = \operatorname{FFT}(x_i)[k] = M_i[k] e^{j P_i[k]}.


Biên độ :math:`M_i` được giữ nguyên. Mỗi bit thông điệp được ánh xạ thành pha

.. math::

   0 \mapsto -\frac{\pi}{2}, \qquad 1 \mapsto \frac{\pi}{2}.


Các pha này được phân phối vào vùng ngay trước tần số giữa của các segment. Để phổ vẫn có đối xứng liên hợp và tín hiệu IFFT là thực, nửa phổ phía sau được gán pha đối dấu theo thứ tự đảo ngược. Tín hiệu stego được tái tạo bởi

.. math::

   x'_i = \operatorname{Re}\!\left(\operatorname{IFFT}\left(M_i e^{j P'_i}\right)\right).


Khi trích xuất, thực hiện FFT trên từng segment và đọc dấu của pha tại các vị trí đã dùng:

.. math::

   P'_i[k] < 0 \Rightarrow 1, \qquad P'_i[k] \ge 0 \Rightarrow 0.


Trong code nguồn, kết quả sau đó được XOR với ``0xff``; thao tác này bù lại quy ước dấu pha đang đảo bit so với phép ánh xạ khi nhúng.

Code demo
~~~~~~~~~


.. code-block:: python

   import numpy as np
   import scipy.io.wavfile as wavfile

   class ImproveStegaDFT:
       @staticmethod
       def embedding(input_filename: str, output_filename: str, message: str):
           rate, audio = wavfile.read(input_filename)
           audio = audio[:, 0] if len(audio.shape) > 1 else audio.copy()

           msg_len = 8 * len(message)
           seg_len = int(2 * 2 ** np.ceil(np.log2(2 * msg_len)))
           seg_num = int(np.ceil(len(audio) / seg_len))
           audio.resize(seg_num * seg_len, refcheck=False)

           msg_bits = np.ravel([
               [int(bit) for bit in format(ord(char), "08b")]
               for char in message
           ])
           msg_phase = np.where(msg_bits == 0, -np.pi / 2, np.pi / 2)

           spectra = np.fft.fft(audio.reshape((seg_num, seg_len)))
           magnitude, phase = np.abs(spectra), np.angle(spectra)
           middle = seg_len // 2

           for i in range(seg_num):
               start = i * len(msg_phase) // seg_num
               end = (i + 1) * len(msg_phase) // seg_num
               width = end - start
               phase[i, middle - width:middle] = msg_phase[start:end]
               phase[i, middle + 1:middle + 1 + width] = -msg_phase[start:end][::-1]

           encoded = np.fft.ifft(
               magnitude * np.exp(1j * phase)
           ).real.ravel().astype(np.int16)
           wavfile.write(output_filename, rate, encoded)

       @staticmethod
       def extract(input_filename: str, msg_len: int) -> str:
           _, audio = wavfile.read(input_filename)
           seg_len = int(2 * 2 ** np.ceil(np.log2(2 * msg_len)))
           seg_num = int(np.ceil(len(audio) / seg_len))
           middle = seg_len // 2
           bits = []

           for i in range(seg_num):
               spectrum = np.fft.fft(audio[i * seg_len:(i + 1) * seg_len])
               phase = np.angle(spectrum)
               start = i * msg_len // seg_num
               end = (i + 1) * msg_len // seg_num
               bits.extend((phase[middle - (end - start):middle] < 0).astype(np.int8))

           bits = np.array(bits[:msg_len])
           chars = bits.reshape((-1, 8)).dot(
               1 << np.arange(7, -1, -1)
           ).astype(np.uint8)
           return "".join(chr(char ^ 0xff) for char in chars)

   message = "Hello, World"
   ImproveStegaDFT.embedding("file_example_WAV_1MG.wav", "output.wav", message)
   decoded = ImproveStegaDFT.extract("output.wav", 8 * len(message))
   assert decoded == message
   print(decoded)


Kết luận
~~~~~~~~


Lab đã nhúng và khôi phục đúng thông điệp trong WAV bằng cách điều chỉnh pha phổ nhưng giữ biên độ. So với thay trực tiếp mẫu âm thanh, phase coding khai thác miền tần số và duy trì điều kiện đối xứng cần thiết để IFFT trả về tín hiệu thực.

Tổng kết
--------


Ba lab minh họa ba loại container và ba miền nhúng khác nhau:

.. list-table::
   :header-rows: 1

   * - Lab
     - Container
     - Miền nhúng
     - Tham số cần biết để giải mã
   * - 1
     - Văn bản
     - Chuỗi ký tự Unicode zero-width
     - Khóa nhân modulo :math:`k`
   * - 2
     - Ảnh RGB24/BMP
     - LSB của các kênh màu
     - Seed của PRNG
   * - 3
     - Âm thanh WAV
     - Pha của hệ số DFT
     - Độ dài thông điệp


Các phương pháp đều ưu tiên tính khó nhận biết của thay đổi, nhưng không tự cung cấp tính bí mật mật mã. Trong ứng dụng thực tế, thông điệp nên được mã hóa trước khi nhúng và cần đánh giá thêm độ bền trước chuyển mã, nén, chuẩn hóa văn bản và chỉnh sửa container.
