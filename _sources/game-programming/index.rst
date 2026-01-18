Lý thuyết lập trình game
########################

Phần này mình sẽ trình bày các lý thuyết cơ bản trong lập trình game và sử dụng DirectX 11 để demo. Tài liệu tham khảo chính là :cite:`LunaDX11`.

Model presentation
******************

Mỗi object 3D được biểu diễn dưới dạng xấp xỉ các tam giác, gọi là tam giác mesh, liền kề nhau và tạo nên mô hình 3D.

Để tùy chỉnh độ mạnh yếu (intensity) của ánh sáng, ta sử dụng số thực từ :math:`0` tới :math:`1`.

Ví dụ, trong hệ màu RGB thì :math:`(0,25; 0,67; 1,00)` biểu diễn :math:`25\%` độ mạnh màu đỏ, :math:`67\%` độ mạnh màu xanh lá và :math:`100\%` độ mạnh màu xanh dương.

Như vậy, trong hệ màu RGB, màu sắc được biểu diễn bởi vector :math:`(r, g, b)` với :math:`0 \leqslant r, g, b \leqslant 1`.

Color Operations
================

Ta có thể cộng, trừ hai màu :math:`(r_1, g_1, r_1)` và :math:`(r_2, g_2, b_2)` thì được kết quả

.. math:: (r_1, g_1, b_1) \pm (r_2, g_2, b_2) = (r_1 \pm r_2, g_1 \pm g_2, b_1 \pm b_2).

Modulation hay componentwise multiplication (nhân đôi một) thực hiện phép nhân theo từng vị trí

.. math:: (r_1, g_1, b_1) \otimes (r_2, g_2, b_2) = (r_1 r_2, g_1 g_2, b_1 b_2).

128-bit color
=============

Một thành phần bổ sung ngoài R, G, B là A (alpha). Alpha xác định độ mờ (opacity) trong *blending*.

Khi đó, để xác định màu có alpha ta dùng vector bốn chiều :math:`(r, g, b, a)` với :math:`0 \leqslant r, g, b, a \leqslant 1`.

32-bit color
============

Để biểu diễn màu với :math:`32` bit, mỗi thành phần :math:`(r, g, b, a)` được biểu diễn bởi một byte. Tương tự, :math:`0` là độ mạnh thấp nhất (không có) và :math:`255` là độ mạnh lớn nhất.

.. note:: 

   Màu 32-bit có thể chuyển thành màu 128-bit bằng việc chia cho :math:`255` vì mỗi thành phần đều nằm thỏa :math:`0 \leqslant n \leqslant 255` nên :math:`0 \leqslant n / 255 \leqslant 1`.

   Ngược lại, màu 128-bit có thể chuyển thành màu 32-bit bằng phép nhân cho :math:`255` và làm tròn tới số nguyên gần nhất.

Trong DirectX, ``XMCOLOR`` biểu diễn alpha, red, green, blue theo thứ tự.

Rendering Pipeline
******************

Rendering Pipeline bao gồm các công đoạn được thể hiện ở :numref:`hình %s <fig-rendering-pipeline>`.

.. _fig-rendering-pipeline: 

.. figure:: rendering-pipeline.*
    
   Rendering Pipeline

Input Assembler Stage
*********************

Công đoạn Input Assembler (IA) đọc các dữ liệu hình học, bao gồm đỉnh (vertice) và chỉ số (indice), để thành lập các cơ chế (primitive) hình học như điểm, đường thẳng, tam giác.

Vertex
======

Đỉnh là một điểm trong không gian.

Primitive Topology
==================

Đỉnh được đóng gói (bound) và rendering pipeline bởi **vertex buffer**, là một cấu trúc dữ liệu trong DirectX.

Sử dụng **primitive topology** ta chỉ định liên kết giữa các đỉnh để hình thành các đối tượng hình học (đỉnh đơn, đoạn thẳng nối hai đỉnh, tam giác nối ba đỉnh, ...).

.. code-block:: C++

   void ID3D11DeviceContext::IASetPrimitiveTopology(...);

Khi ta có một danh sách các đỉnh thì có thể áp dụng một trong các topology sau để vẽ chúng.

1. Point List: mỗi đỉnh được vẽ như một đỉnh độc lập.
2. Line Strip: các đỉnh thành lập các đoạn thẳng nối liền nhau. Giả sử ta có :math:`n` đỉnh là :math:`v_1`, :math:`v_2`, ..., :math:`v_n` thì ta vẽ :math:`n-1` cạnh là :math:`v_1 v_2`, :math:`v_2 v_3`, ..., :math:`v_{n-1} v_n`.
3. Line List: cứ hai đỉnh sẽ vẽ một cạnh. Giả sử ta có :math:`2n` đỉnh là :math:`v_1`, :math:`v_2`, ..., :math:`v_{2n}` thì ta vẽ :math:`n` cạnh :math:`v_1 v_2`, :math:`v_3 v_4`, ..., :math:`v_{2n-1} v_{2n}`.
4. Triangle Strip: các đỉnh thành lập các tam giác nối liền nhau. Giả sử ta có :math:`n` đỉnh là :math:`v_1`, :math:`v_2`, ..., :math:`v_n` thì ta vẽ :math:`n-2` tam giác :math:`v_1 v_2 v_3`, :math:`v_2 v_3 v_4`, ..., :math:`v_{n-2} v_{n-1} v_n`.
5. Triangle List: cứ ba đỉnh ta vẽ một tam giác. Khi đó với :math:`3n` đỉnh ta có :math:`n` tam giác.
6. Primitives with Adjacency: một triangle list được gọi là adjacency nếu một tam giác kề với một tam giác khác.
7. Control Point Patch List: optional cho tessellation stage.

Index
=====

Ta sử dụng chỉ số (index) thay vì đỉnh (vertex) nhằm giảm bộ nhớ lưu trữ và xử lý.

Xét :numref:`hình %s <fig-rectangle>`. Hình chữ nhật được tạo từ bốn đỉnh :math:`v_0`, :math:`v_1`, :math:`v_2` và :math:`v_3`.

.. _fig-rectangle: 

.. figure:: rectangle.*

   Hình chữ nhật ghép từ hai hình tam giác

Ta có thể lưu mảng các đỉnh và sau đó là mảng các chỉ số tương ứng với từng tam giác.

.. code-block:: C++

   Vertex v[4] = { v0, v1, v2, v3 };

   UINT indice[6] = {
      0, 1, 2, // tam giác v0 -> v1 -> v2
      0, 2, 3, // tam giác v0 -> v2 -> v3
   };

Một điều cần lưu ý là thứ tự đỉnh trong các tam giác phải giống nhau (cùng chiều hoặc ngược chiều kim đồng hồ). Lý do cho việc này là để xác định mặt trước và sau, và sẽ được giải thích rõ hơn trong công đoạn *culling*.

Vertex Shader Stage
*******************

Sau khi chỉ định primitives để assembler, các đỉnh sẽ được chuyển tới vertex shader stage.

Có thể hiểu rằng, vertex shader stage lấy đầu vào là từng đỉnh và đầu ra cũng là đỉnh.

Hàm ``VertexShader`` chúng ta cài đặt để chỉ dẫn cho GPU xử lý.

Các công dụng của vertex shader gồm:

- transformation: là các phép biến hình, bao gồm tịnh tiến (translation), quay (rotation) và co dãn (scale);
- lighting: ánh sáng;
- displacement mapping (?).

Chúng ta không những có thể truy cập dữ liệu của input vertex mà còn truy cập được texture, ma trận của phép biến hình, scene light.

Local Space và World Space
==========================

World Space là hệ tọa độ toàn cục (global) chứa tất cả object trong không gian 3D.

Đôi khi một object sẽ có vị trí tương đối so với object khác thay vì gốc tọa độ. Ví dụ cánh tay gắn với cơ thể thì local space sẽ dễ dùng hơn.

Local Space là hệ tọa độ gắn với một object nào đó và xác định vị trí của một số object khác theo vị trí tương đối đối với object làm gốc.

Câu hỏi là: làm sao dời tất cả object từ local space tới world space? Chúng ta sẽ sử dụng phép biến đổi world transform và tính toán trên world matrix.

Thuận lợi khi dùng world transform là:

1. Đơn giản: thông thường trong local space thì object nằm ở tâm nên sẽ dễ dàng tính theo world space.
2. Một object có thể dùng trong nhiều scene khác nhau nên không cần thiết phải chỉ định tọa độ cố định world space (không phải chỉ định tọa độ cho từng scene).
3. Đôi khi ta vẽ cùng object nhiều lần trên scene nhưng khác tọa độ, hướng, kích cỡ. Mỗi lần vẽ ta gọi là một *instance*.

Giả sử:

- :math:`\bm{Q}_w = (Q_x, Q_y, Q_z)` là tọa độ của object ban đầu;
- :math:`\bm{u}_w = (u_x, u_y, u_z)` là trục :math:`x` của local space;
- :math:`\bm{v}_w = (v_x, v_y, v_z)` là trục :math:`y` của local space;
- :math:`\bm{w}_w = (w_x, w_y, w_z)` là trục :math:`z` của local space;

Khi đó ma trận chuyển từ local space sang world space là

.. math:: 

    \bm{W} = \begin{pmatrix}
        u_x & u_y & u_z & 0 \\
        v_x & v_y & v_z & 0 \\
        w_x & w_y & w_z & 0 \\
        Q_x & Q_y & Q_z & 1
    \end{pmatrix}.

Thông thường :math:`\bm{W}` là một dãy các biến đôi liên tiếp, ví dụ :math:`\bm{W} = \bm{S} \bm{R} \bm{T}`, trong đó:

- :math:`\bm{S}` là ma trận co dãn (scale matrix);
- :math:`\bm{R}` là ma trận xoay (rotation matrix);
- :math:`\bm{T}` là ma trận tịnh tiến (translation matrix).

Ví dụ:

.. math:: 

    \bm{S} = \begin{pmatrix}
        2 & 0 & 0 & 0 \\
        0 & 1 & 0 & 0 \\
        0 & 0 & 2 & 1 \\
        0 & 0 & 0 & 1 \\
    \end{pmatrix}, \ \bm{R} = \begin{pmatrix}
        \sqrt{2} / 2 & 0 & -\sqrt{2} / 2 & 0 \\
        0 & 1 & 0 & 0 \\
        \sqrt{2} / 2 & 0 & \sqrt{2} / 2 & 0 \\
        0 & 0 & 0 & 1
    \end{pmatrix}, \ \bm{T} = \begin{pmatrix}
        1 & 0 & 0 & 0 \\
        0 & 1 & 0 & 0 \\
        0 & 0 & 1 & 0 \\
        10 & 0 & 10 & 1
    \end{pmatrix}.

Khi đó

.. math:: 
    
    \bm{W} = \bm{S} \bm{R} \bm{T} = \begin{pmatrix}
        \sqrt{2} & 0 & -\sqrt{2} & 0 \\
        0 & 1 & 0 & 0 \\
        \sqrt{2} & 0 & \sqrt{2} & 0 \\
        10 & 0 & 10 & 1
    \end{pmatrix}

Mở đầu với lập trình Windows và DirectX
***************************************

Lập trình Windows Application
=============================

Khi viết bài này mình dùng Visual Studio 2022. Chọn ``System`` là ``Windows`` thay vì ``Console``. Lúc này, hàm chính của chương trình không phải là ``main`` nữa mà là ``wWinMain`` có prototype như sau:

.. code-block:: cpp

   INT WINAPI wWinMain(HINSTANCE hInstance, HINSTANCE hPrevInstance, LPTSTR lpCmdLine, int nCmdShow);

Ở đây có hai tham số cần lưu ý là ``hInstance`` và ``nCmdShow``. Trong đó ``hInstance`` chỉ bản thân process, tức "thể hiện" của nó, còn ``nCmdShow`` chỉ việc window khi được tạo sẽ hiện hay không. Trong nhiều trường hợp, để xem trước đó chương trình đã được chạy hay chưa chúng ta dùng ``hPrevInstance``. 

Ví dụ, chúng ta sẽ không muốn file game bị chạy nhiều lần, nên cần kiểm tra xem trước đó file exe đã được load lên chưa thông qua ``hPrevInstance``.

Để điều khiển cửa sổ mình thực hiện ba bước:

1. Tạo ``WNDCLASSEX``

   - Đối với ``WNDCLASSEX`` ta phải set trường ``cbSize`` của thành ``sizeof(WNDCLASSEX)``. Trong khi đó một số biến thể khác của struct này như ``WNDCLASS`` thì không cần.
   - Ta cần chú ý trường ``lpfnWndProc``. Trường này là con trỏ tới hàm ``WndProc`` (windows process) sẽ xử lý các sự kiện của window.
    
2. Sử dụng kiểu dữ liệu ``HWND`` để handle tới cửa sổ (HWND - handle window). Nhiều đối tượng khác cũng có thể handle.
3. Xử lý các message (sự kiện) được truyền vào cửa sổ (nhấn nút tắt, gõ phím, click chuột, ...)

Templete sau định nghĩa hàm ``WndProc`` sẽ kết thúc chương trình khi click vào nút tắt.

.. code-block:: cpp

   #include <Windows.h>

   #define APPTITLE L"Sample Window"

   LRESULT CALLBACK WndProc(HWND hwnd, UINT msg, WPARAM wParam, LPARAM lParam);

   INT WINAPI wWinMain(HINSTANCE hInstance, HINSTANCE hPrevInstance, LPTSTR lpCmdLine, int nCmdShow)
   {
      HWND hwnd = 0;
      WNDCLASSEX wc;
      ZeroMemory(&wc, sizeof(WNDCLASSEX));
      wc.cbSize = sizeof(WNDCLASSEX);
      wc.hInstance = hInstance;
      wc.lpszClassName = APPTITLE;
      wc.hbrBackground = (HBRUSH)GetStockObject(WHITE_BRUSH);
      wc.hCursor = LoadCursor(NULL, IDC_ARROW);
      wc.lpfnWndProc = WndProc;
      wc.style = CS_HREDRAW | CS_VREDRAW;
      
      RegisterClassEx(&wc);
      
      hwnd = CreateWindowExW(
         0,
         APPTITLE,
         APPTITLE,
         WS_OVERLAPPEDWINDOW,
         CW_USEDEFAULT, CW_USEDEFAULT,
         640, 480,
         NULL, NULL, hInstance, NULL);
      
      if (hwnd == 0)
      {
         return FALSE;
      }
      UpdateWindow(hwnd);
      ShowWindow(hwnd, nCmdShow);
      
      MSG msg = { 0 };
      while (GetMessage(&msg, NULL, NULL, NULL))
      {
         TranslateMessage(&msg);
         DispatchMessageW(&msg);
      }
      return msg.wParam;
   }

   LRESULT CALLBACK WndProc(HWND hwnd, UINT msg, WPARAM wParam, LPARAM lParam)
   {
      switch (msg)
      {
      case WM_DESTROY:
         PostQuitMessage(0);
         break;
      default:
         return DefWindowProc(hwnd, msg, wParam, lParam);
      }
      return 0;
   }

Lập trình DirectX 11
====================

.. Để sử dụng DirectX cần download SDK về máy, xong config path (Include và Library) vào project.

Các bước render hình ảnh
========================

Biểu diễn model
---------------

Mỗi scene (cảnh) chứa nhiều object (hay model). Ví dụ, mỗi màn chơi trong Mario là một scene. Khi chơi mỗi màn trong Mario thì các object (hay model) sẽ là nhân vật Mario, cục gạch, con rùa, ... Các model thực chất được biểu diễn bởi nhiều hình tam giác (triangle mesh) một cách xấp xỉ. Càng nhiều tam giác, hình ảnh càng chi tiết và đẹp hơn, và tất nhiên cũng tốn bộ nhớ hơn để lưu trữ và tính toán.

Lý do của việc biểu diễn model bằng các tam giác là vì trong không gian ba chiều :math:`Oxyz`, các đường cong phức tạp đòi hỏi các phương trình toán học phức tạp để biểu diễn hoặc thậm chí không thể biểu diễn bằng phương trình sơ cấp. Bằng việc ghép các tam giác lại, ta có thể xấp xỉ đường cong bởi nhiều đọan thẳng liền kề.

1. Cấu trúc đỉnh (Vertex Format).

   Với mỗi đỉnh của tam giác ta cần định nghĩa cấu trúc của nó:
   
   - Cách 1: tọa độ :math:`(x, y, z)` và màu tại đỉnh đó. Với cách này, khi khai báo ba đỉnh của tam giác thì màu được tô bên trong tam giác có thể là màu của đỉnh đầu tiên hoặc trung bình của ba màu tùy theo thiết lập.
   - Cách 2: tọa độ :math:`(x, y, z)`, pháp tuyến tại đó và tọa độ texture. Với cách này ta xác định pháp tuyến tại vị đỉnh, thường dùng khi có ánh sáng để tính toán độ sáng tối, và tọa độ texture thuộc khoảng :math:`[0, 1]` để xác định texture khi load lên sẽ có 4 góc tương ứng thế nào với hình chữ nhật (ghép hai tam giác).
   
2. Tam giác (Triangle).

   Để định nghĩa một hình chữ nhật với 4 đỉnh theo chiều kim đồng hồ là v0->v1->v2->v3 ta cần định nghĩa hai tam giác v0->v1->v2 và v0->v2->v3. Như vậy cần 6 vertices để biểu diễn hai tam giác.
    
   Lưu ý: thứ tự của đỉnh rất quan trọng và được gọi là winding order.
   
3. Chỉ số (Index - Indices)

   Việc khai báo 6 vertices như trước gây lãng phí bộ nhớ (v0 và v2 khai báo hai lần). Do đó mình sẽ dùng một mảng liệt kê danh sách các vertices gọi là vertex buffer, và một mảng xác định chỉ số của vertex cấu thành tam giác gọi là index buffer.

   Lúc này, index buffer là mảng WORD xác định index của vertex tạo nên tam giác, ví dụ 0, 1, 2 cho tam giác đầu và 0, 2, 3 cho tam giác sau. Việc dùng WORD tiết kiệm bộ nhớ hơn.

Virtual Camera
--------------

Lấy một điểm nằm ngoài màn hình máy tính làm gốc. Mình chọn góc dọc và ngang về hướng màn hình, khi đó vùng nhìn thấy sẽ có dạng hình chóp vô hạn. Mình tiếp tục giới hạn lại vùng này bằng mặt phẳng xa và mặt phẳng gần. Khoảng không gian có dạng nón cụt này sẽ được thể hiện trên màn hình khi render game và được gọi là **frustum**. Quá trình loại bỏ mọi thứ bên ngoài vùng này khi render gọi là **clipping**.

.. figure:: virtual_camera.*

   Virtual Camera

Ở hình trên, mặt phẳng màu xanh lá gọi là **projection window** ứng với :math:`z = 1`. Đây là mặt phẳng sẽ được hiển thị trên cửa sổ game.

Mặt phẳng màu đỏ là **mặt phẳng gần** và màu xanh là **mặt phẳng xa**. Hai mặt phẳng này giới hạn vùng không gian sẽ được hiển thị trên cửa sổ. Quá trình clipping sẽ xác định phần nào sẽ được hiển thị dựa vào điểm ngắm và ba mặt phẳng trên, cùng với góc dọc và góc ngang giúp xác định kích thước hình chữ nhật ở ba mặt phẳng.

Rendering Pipeline (Quy trình render)
-------------------------------------

Local Space :math:`\to` World Space :math:`\to` View Space :math:`\to` Backface culling :math:`\to` Lighting :math:`\to` Clipping :math:`\to` Projection :math:`\to` View Point Space :math:`\to` Rasterization.

1. **Local space**, hay còn gọi là modeling space, khi một model đứng riêng lẻ, ta có thể chọn một hệ tọa độ lấy tâm là tâm của chính model đó. Trên hệ tọa độ này hiện tại chỉ có duy nhất một model.  
2. **World space**. Trên thực tế có rất nhiều object trong không gian. Mỗi object là một local space với gốc ở :math:`(x, y, z)`. Quá trình chuyển từ local space sang world space được gọi là **transform**, bao gồm: phép tịnh tiến (translation), phép quay (rotation) và phép co dãn (scaling).
3. **View space**. Ta cần đặt góc nhìn (camera) ở đâu? Thông thường các phép tính sẽ khá phức tạp nên ta thường đưa về gốc tọa độ và hướng (trục) theo chiều dương của trục :math:`z`. Đồng thời cũng tính toán lại vị trí của object theo camera mới này. Toàn bộ quá trình này gọi là view space transformation. Có hai loại view space là left-hand (LH) và right-hand (RH).
4. **Backface culling**. Một đa giác có hai mặt và ta định nghĩa một mặt là frontface còn mặt kia là backface. Direct3D sẽ bỏ đi backface khi render (không nhìn thấy) và việc này được gọi là backface culling.
5. **Lighting**. Ánh sáng là một object đặc biệt cho phép thể hiện độ sáng tối của game gần với thế giới thực.
6. **Clipping**. Ta cần cull (bỏ đi khi render trên view space) các phần nằm trong frustum. Việc này được gọi là clipping và có ba trường hợp:
   
   - Object hoàn toàn nằm trong frustum.
   - Object hoàn toàn nằm ngoài frustum.
   - Object nằm trong một phần và nằm ngoài một phần. Khi đó ta chỉ render phần nằm trong.

7. **Projection** (phép chiếu). Vùng nhìn thấy là một không gian 3D. Việc thể hiện không gian 3D lên màn hình 2D được gọi là projection (chiếu). Có nhiều cách chiếu nhưng ta quan tâm phép chiếu tâm (perspective projection). Lúc này vật càng xa thì càng nhỏ, càng gần thì càng lớn. Tỉ số aspect (aspect ratio) thường dùng là rộng/cao.
8. **Viewport transform**. Đôi khi ta không render trên cả window mà chỉ một phần của nó. Ví dụ như một cảnh trong Megaman rất lớn, khi di chuyển ta dời vị trí đi thì cũng dời không gian được render. Việc đưa từ tọa độ projection lên một vùng hình chữ nhật trên màn gọi là viewport.
9. **Rasterization**. Sau khi tất cả vertices đã được chiếu lên màn, ta có một danh sách tam giác. Rasterization sẽ tính toán màu sắc của mỗi pixel và vẽ từng tam giác cho tới khi render xong.

Vertex buffer và Index buffer
=============================

Trong DirectX 11 thì hai buffer này được tạo y hệt nhau bằng hàm:

.. code-block:: cpp

   HRESULT CreateBuffer(
   [in]            const D3D11_BUFFER_DESC      *pDesc,
   [in, optional]  const D3D11_SUBRESOURCE_DATA *pInitialData,
   [out, optional] ID3D11Buffer                 **ppBuffer
   );

Lighting
========

Có ba loại ánh sáng:

1. Amibient light (ánh sáng xung quanh).
2. Diffuse light (khuyếch tán).
3. Specular light (đặc thù).

Đối với specular light cần nhiều tính toán nên thường sẽ bị off.

Materials
=========

Màu của object khi hiển thị trên window thực chất là màu đã được phản chiếu từ ánh sáng. Để biểu diễn ta dùng ``D3DMATERIAL``.

Vertex Normals
==============

Normal ở đây có nghĩa là pháp tuyến. Trong hình học :math:`Oxyz` thì mỗi mặt phẳng xác định khi biết một điểm thuộc nó và một vector pháp tuyến của nó. Tương tự, ở đây mỗi đỉnh của mỗi object trong game sẽ có một normal.

Trong quá trình biến đổi độ dài của normal sẽ thay đổi nên cần thường xuyên kiểm tra và chuẩn hóa lại độ dài thành :math:`1`.

Light source
============

Nguồn sáng gồm ba loại là: point light, direction light và spot light.

Texture Coordinates
===================

Tọa độ của texture được thể hiện bằng cặp :math:`(u, v)`. Ta gọi đó là texel.

Với mỗi tam giác trên không gian 3D ta muốn định nghĩa tam giác tương ứng trên texture mà map với tam giác 3D đó.
