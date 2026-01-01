Ring kernel và ring homomorphism
================================

Xét vành :math:`(R, +, \times)`. Khi đó:

- với mọi :math:`a \in R`, :math:`a \times 0 = 0 \times a = 0`;
- :math:`(-a) \times b = - (a \times b)`.

.. prf:definition:: Ring homomorphism
   :label: def-ring-homomorphism

   Xét hai vành là :math:`(R_1, +, \times)` và :math:`(R_2, \boxplus, \otimes)` và ánh xạ :math:`f: \, R_1 \to R_2`.

   Ánh xạ :math:`f` được gọi là **homomorphism** trên hai vành nếu :math:`f` là homomorphism trên phép cộng và phép nhân, nghĩa là:

   - với mọi :math:`a, b \in R_1`, :math:`f(a) \boxplus f(b) = f(a + b)`;
   - với mọi :math:`a, b \in R_1`, :math:`f(a) \otimes f(b) = f(a \times b)`.

.. prf:definition:: Hạt nhân
   :label: def-ring-hom-kernel
   
   **Hạt nhân** (hay **kernel**, **ядро**) của :math:`f` là

   .. math:: \ker f = \{ x : x \in R_1, f(x) = 0_{2} \}

   với :math:`0_{2}` là phần tử trung hòa của :math:`R_2`.

.. prf:theorem:: 
   :label: thm-ring-kernel-ideal
   
   :math:`\ker f` là một ideal của :math:`R_1`.

.. admonition:: Chứng minh
   :class: danger, dropdown

   Ta có :math:`f(0_1) = 0_2` theo định nghĩa homomorphism. Do đó với mọi :math:`a \in R_1` và với mọi :math:`b \in \ker f` thì
   
   .. math:: f(a) \otimes f(b) = f(a) \otimes 0_2 = 0_2 = f(a \times b).

   Do đó :math:`a \times b \in \ker f`, suy ra :math:`\ker f` là ideal trái của :math:`R_1`.

   Tương tự cho với mọi :math:`a \in R_1` và với mọi :math:`b \in \ker f` thì
   
   .. math:: f(b) \otimes f(a) = 0_2 = f(b \times a),
      
   suy ra :math:`b \times a \in \ker f` nên :math:`\ker f` cũng là ideal phải của :math:`R_1`.

   Kết luận: :math:`\ker f` là ideal của :math:`R_1`.

.. raw:: html

   <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-2343650775986433"
     crossorigin="anonymous"></script>
   <!-- First Ads -->
   <ins class="adsbygoogle"
      style="display:block"
      data-ad-client="ca-pub-2343650775986433"
      data-ad-slot="4417625951"
      data-ad-format="auto"
      data-full-width-responsive="true"></ins>
   <script>
      (adsbygoogle = window.adsbygoogle || []).push({});
   </script>
