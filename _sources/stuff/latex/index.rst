Trải nghiệm người dùng với LaTeX
********************************

Mình rất thích sử dụng LaTeX để soạn thảo tài liệu. Ví dụ 
như notebook này sử dụng MathJax để hiển thị các công thức 
toán học giống LaTeX. Theo định nghĩa của `wikipedia <https://en.wikipedia.org/wiki/LaTeX>`_ 
và `The LaTeX project <https://www.latex-project.org/>`_ 
thì LaTeX là hệ thống soạn thảo văn bản (typesetting system).

Bài viết này không nhằm hướng dẫn sử dụng LaTeX mà là trải 
nghiệm và cách xử lý vấn đề của bản thân khi sử dụng LaTeX.

Vấn đề mình gặp khi dùng LaTeX trên Overleaf
============================================

Khi sử dụng LaTeX gặp phải một số vấn đề khá khó chịu. Ban đầu 
mình dùng Overleaf là một trình soạn thảo LaTeX dạng web. Điểm 
lợi của web là project được lưu trên server của Overleaf nên 
không tốn bộ nhớ. Thêm nữa, Overleaf hỗ trợ việc colab, tức là 
mình có thể soạn thảo với nhiều người khác cùng lúc, cũng có thể 
comment cho nhau. Tuy nhiên mình gặp một vấn đề khá thú vị khi 
soạn thảo văn bản đa ngôn ngữ, cụ thể là một tài liệu có tiếng 
Việt, tiếng Anh và tiếng Nga.

Tiếng Anh là ngôn ngữ chuẩn của LaTeX. Chúng ta không cần tùy 
chỉnh chỉnh gì, sử dụng trình biên dịch mặc định ``pdflatex`` 
là được. Đối với danh mục tài liệu tham khảo (bibliography) 
thì chúng ta cũng sử dụng trình biên dịch mặc định ``bibtex``. 
Đây cũng là cấu trúc trích dẫn phổ biến, thường được các tạp 
chí đính kèm vào thông tin về nghiên cứu khoa học.

Tiếng Nga được hỗ trợ chính thức trong hai package: ``babel`` 
hoặc ``polyglossia``. Tiếng Nga có thể biên dịch với ``pdflatex``, 
nhưng cũng có thể sử dụng các trình biên dịch hiện đại là ``xelatex`` 
và ``lualatex``. Đối với bibliography thì chúng ta cũng có thể sử dụng:

- BibTex đi với ``pdflatex``;
- BibLatex đi với ``xelatex`` hoặc ``lualatex``.

Vấn đề xảy ra khi mình viết tiếng Việt. Trong package ``babel`` 
cũng có hỗ trợ tiếng Việt, nhưng mình rất hay gặp lỗi font khi 
dùng chung hai ngôn ngữ: tiếng Việt và tiếng Nga. Tiếng Việt ở 
link `babel-vietnamese <https://ctan.org/pkg/babel-vietnamese>`_ 
đã ngừng cập nhật từ năm 2015. Thực tế thì vẫn có nhiều project 
được viết bởi package này (hoặc sử dụng file ``vietnamese.ldf``) 
nhưng trong trường hợp của mình thì sẽ bị xung đột với tiếng Nga.

Trong lúc tình cờ mình đã tìm được cách xử lý. Mình sử dụng trình 
biên dịch ``xelatex`` và package ``fontspec`` là đã có thể viết 
thoải mái cả ba ngôn ngữ.

Ơ kìa cuộc sống bạn đùa tôi à? Khi sử dụng ``xelatex`` thì một 
vấn đề siêu to khổng lồ khác xuất hiện là thời gian biên dịch. 
Khi dịch từ file ``.tex`` ra ``.pdf`` thì việc sử dụng ``pdflatex`` 
nhanh hơn rất nhiều so với ``xelatex``. Khác biệt thời gian sẽ 
tăng lên đáng kể khi số trang của tài liệu tăng lên và biên dịch 
thêm bibliography.

Nếu chúng ta muốn biên dịch một file ``main.tex`` với ``pdflatex`` 
thì dùng lệnh

.. code-block:: bash

    pdflatex main.tex

Nếu chúng ta muốn biên dịch file ``main.tex`` là tài liệu LaTeX 
chính và thêm bibliography là file ``reference.bib`` nữa thì sẽ 
dùng bốn lệnh/

.. code-block:: bash

    pdflatex main.tex
    bibtex reference.bib
    pdflatex main.tex
    pdflatex main.tex

Có nhiều lý do để biên dịch lại hai lần sau khi dùng BibTex như để 
cập nhật các tham chiếu cho mục lục (nội dung, hình ảnh, bảng). Bây 
giờ nếu mình đổi ``pdflatex`` thành ``xelatex`` và ``bibtex`` thành 
``biber`` (cho BibLatex) thì rõ ràng thời gian biên dịch dài hơn ba 
lần ứng với ba lần đổi ``pdflatex`` thành ``xelatex``.

Và câu chuyện éo le khi Overleaf bản free không cho phép thời gian 
dịch đi quá một ngưỡng nào đó. Khi viết khóa luận tốt nghiệp cử nhân, 
mình chỉ viết 51 trang là yêu cầu tối thiểu về số trang nhưng vẫn bị 
quá thời gian dịch.

Từ đó nếu chỉ viết tài liệu ngắn hoặc cần colab với đồng chí mình 
mới dùng Overleaf. Sau đây mình sẽ hướng dẫn cách sử dụng Visual 
Studio Code (VSCode) để soạn thảo LaTeX. Nhiều người sẽ quen với 
hai phần mềm thông dụng là TeXstudio và Texmaker hơn và mình công 
nhận có một số khía cạnh hai phần mềm này tốt hơn VSCode. Ngược 
lại, VSCode cũng có một số khía cạnh tốt hơn Overleaf và hai phần 
mềm trên. Những điểm sáng này cực kì thuận tiện cho mình nên mình 
lựa chọn VSCode cho các project LaTex.

Sử dụng VSCode trên Windows hoặc WLS2
=====================================

Bước 1u. VSCode và Latex Workshop
---------------------------------

Chúng ta tải VSCode trên Windows và cài đặt extension *Latex Workshop* 
của James Yu.

Nếu muốn sử dụng WSL2 thì ta cần cài đặt extension *WSL* để mở thư 
mục trong WLS bằng VSCode, sau đó cài extension *Latex Workshop* ở 
trên cho WSL.

Bước 1v. TeX Live/MiKTeX
------------------------

TeX Live và MiKTeX là hai bộ biên dịch LaTeX, nghĩa là chúng sẽ dịch 
một hoặc nhiều file có đuôi ``.tex`` thành file PDF. Trên Windows 
chúng ta có thể dùng cả hai còn trên WSL2 (Linux) thì chúng ta dùng TeX Live.

Sau khi cài đặt TeX Live hoặc MiKTeX thì chúng ta đã sẵn sàng sử dụng LaTeX để soạn thảo.

Soạn thảo LaTeX trên WSL
------------------------

Mở Powershell và thực hiện các lệnh sau

.. code-block:: bash

    cd
    mkdir project
    cd project
    touch main.tex
    code .

Dòng lệnh kế cuối tạo một file ``main.tex`` trong thư mục ``project``. 
Dòng lệnh cuối để mở thư mục bằng VSCode. Nếu thực hiện đúng thì cửa 
sổ VSCode sẽ mở ra như hình sau. Khi đã cài đặt extension *Latex Workshop* 
thì ở cột bên tay trái sẽ có công cụ **TEX**.

.. figure:: 01-open-project.png

Mở file ``main.tex`` và chép đoạn này vào.

.. code-block:: tex

    \documentclass{article}

    \begin{document}
    Xin chào, tôi đến từ Việt Nam.
    \end{document}

Để biên dịch, chúng ta bấm vào nút tam giác màu xanh lá cỏ ở góc 
trên phải (Build LaTeX project).

.. figure:: 02-build-latex.png

Kết quả sẽ ra lỗi vì không nhận diện được các kí tự Unicode.

Bây giờ, bấm vào công cụ **TEX** ở cột bên trái, chọn build 
bằng ``Recipe: latexmk (lualatex)`` (lựa chọn thứ 3), hoặc 
``Recipe: latexmk (xelatex)`` (lựa chọn thứ 4).

.. figure:: 03-build-lualatex.png

    Build với LuaLaTeX

Lúc này ô cửa sổ lỗi không hiện ra nữa. Để xem review PDF giống 
Overleaf ở nửa màn hình bên phải ta bấm vào nút có hình kính lúp 
kế bên nút tam giác xanh lá cỏ.

.. figure:: 04-view-pdf.png

Như vậy ta có thể xem kết quả biên dịch song song với code.

.. figure:: 05-tex-pdf.png

Ở những lần sau khi viết thêm nội dung chúng ta có thể sử dụng tổ 
hợp phím Ctrl+S để lưu và dịch lại. Tuy nhiên lần này sẽ bị lỗi. 
Lý do là Ctrl+S sẽ sử dụng phương án build đầu tiên xuất hiện trong 
danh sách trong công cụ **TEX**. Lúc nãy chúng ta build được tiếng 
Việt là nhờ LuaLaTex ở lựa chọn thứ 3 hoặc XeLaTeX ở lựa chọn thứ 4. 
Lúc này chúng ta phải đổi XeLaTex hoặc LuaLaTeX lên đầu.

Để thiết lập lại thứ tự ưu tiên của *Latex Workshop* chúng ta sẽ 
chỉnh sửa JSON của project. Nhấn tổ hợp phím Ctrl+Shift+P, nhập vào 
``Open Workspace Settings (JSON)`` để mở file ``settings.json``. 
File này được lưu ở thư mục code ``.vscode`` ở thư mục hiện tại.

Nếu chúng ta nhập vào ``"latex-workshop.latex.tools"`` thì chúng ta 
sẽ thấy cài đặt gốc của *Latex Workshop*. Ở đây XeLaTex được build 
bằng lệnh ``latexmk`` với option  ``-xelatex``. Tương tự, LuaLaTex 
cũng được build bằng lệnh ``latexmk`` với option ``-lualatex``. 
Dưới đây là cài đặt gốc của *Latex Workshop*.

.. admonition:: "latex-workshop.latex.tools" mặc định
    :class: dropdown

    .. code-block:: json

        {
            "latex-workshop.latex.tools": [
                {
                    "name": "latexmk",
                    "command": "latexmk",
                    "args": [
                        "-synctex=1",
                        "-interaction=nonstopmode",
                        "-file-line-error",
                        "-pdf",
                        "-outdir=%OUTDIR%",
                        "%DOC%"
                    ],
                    "env": {}
                },
                {
                    "name": "lualatexmk",
                    "command": "latexmk",
                    "args": [
                        "-synctex=1",
                        "-interaction=nonstopmode",
                        "-file-line-error",
                        "-lualatex",
                        "-outdir=%OUTDIR%",
                        "%DOC%"
                    ],
                    "env": {}
                },
                {
                    "name": "xelatexmk",
                    "command": "latexmk",
                    "args": [
                        "-synctex=1",
                        "-interaction=nonstopmode",
                        "-file-line-error",
                        "-xelatex",
                        "-outdir=%OUTDIR%",
                        "%DOC%"
                    ],
                    "env": {}
                },
                {
                    "name": "latexmk_rconly",
                    "command": "latexmk",
                    "args": [
                        "%DOC%"
                    ],
                    "env": {}
                },
                {
                    "name": "pdflatex",
                    "command": "pdflatex",
                    "args": [
                        "-synctex=1",
                        "-interaction=nonstopmode",
                        "-file-line-error",
                        "%DOC%"
                    ],
                    "env": {}
                },
                {
                    "name": "bibtex",
                    "command": "bibtex",
                    "args": [
                        "%DOCFILE%"
                    ],
                    "env": {}
                },
                {
                    "name": "rnw2tex",
                    "command": "Rscript",
                    "args": [
                        "-e",
                        "knitr::opts_knit$set(concordance = TRUE); knitr::knit('%DOCFILE_EXT%')"
                    ],
                    "env": {}
                },
                {
                    "name": "jnw2tex",
                    "command": "julia",
                    "args": [
                        "-e",
                        "using Weave; weave(\"%DOC_EXT%\", doctype=\"tex\")"
                    ],
                    "env": {}
                },
                {
                    "name": "jnw2texminted",
                    "command": "julia",
                    "args": [
                        "-e",
                        "using Weave; weave(\"%DOC_EXT%\", doctype=\"texminted\")"
                    ],
                    "env": {}
                },
                {
                    "name": "pnw2tex",
                    "command": "pweave",
                    "args": [
                        "-f",
                        "tex",
                        "%DOC_EXT%"
                    ],
                    "env": {}
                },
                {
                    "name": "pnw2texminted",
                    "command": "pweave",
                    "args": [
                        "-f",
                        "texminted",
                        "%DOC_EXT%"
                    ],
                    "env": {}
                },
                {
                    "name": "tectonic",
                    "command": "tectonic",
                    "args": [
                        "--synctex",
                        "--keep-logs",
                        "--print",
                        "%DOC%.tex"
                    ],
                    "env": {}
                }
            ]
        }

Cá nhân mình thấy khá ... không thích kiểu này nên mình sẽ 
thay đổi thành ``lualatex`` và ``xelatex``, thêm nữa mình 
sẽ thêm ``biber`` vào để dùng cho BibLatex. Cuối cùng mình 
xóa râu ria đi. File ``settings.json`` của mình bây giờ gồm 
``lualatex``, ``xelatex``, ``pdflatex`` chuẩn, ``bibtex`` 
chuẩn, và ``biber`` cho BibLatex.

.. code-block:: json

    {
        "latex-workshop.latex.tools": [
            {
                "name": "lualatex",
                "command": "lualatex",
                "args": [
                    "-synctex=1",
                    "-interaction=nonstopmode",
                    "-file-line-error",
                    "-outdir=%OUTDIR%",
                    "%DOC%"
                ],
                "env": {}
            },
            {
                "name": "xelatex",
                "command": "xelatex",
                "args": [
                    "-synctex=1",
                    "-interaction=nonstopmode",
                    "-file-line-error",
                    "-outdir=%OUTDIR%",
                    "%DOC%"
                ],
                "env": {}
            },
            {
                "name": "pdflatex",
                "command": "pdflatex",
                "args": [
                    "-synctex=1",
                    "-interaction=nonstopmode",
                    "-file-line-error",
                    "%DOC%"
                ],
                "env": {}
            },
            {
                "name": "bibtex",
                "command": "bibtex",
                "args": [
                    "%DOCFILE%"
                ],
                "env": {}
            },
            {
                "name": "biber",
                "command": "biber",
                "args": [
                    "%DOCFILE%"
                ],
                "env": {}
            },
        ]
    }

Tuy nhiên đây chỉ là các tools để build. Chúng ta có thể 
kết hợp nhiều tools lại và build, gọi là **recipes**. Sau 
dấu đóng ngoặc vuông, thêm dấu phẩy, xuống dòng và gõ 
``"latex-workshop.latex.recipes"`` chúng ta sẽ được thêm 
một đoạn JSON nữa. Tương tự, lần này mình sẽ sửa

- ``lualatexmk`` thành ``lualatex`` ứng với tools ``lualatex`` trong phần **tools**
- ``xelatexmk`` thành ``xelatex`` ứng với tools ``xelatex`` trong phần **tools**
- tạo một recipe mới giống chuỗi ``pdflatex -> bibtex -> pdflatex * 2`` để build với XeLaTeX/LuaLaTeX + BibLatex.

Cuối cùng mình sắp xếp lại để ``xelatex`` lên đầu, và recipe 
chuỗi sẽ đi ngay sau recipe đơn. Bản full khá dài nên mình để 
ở `đây <https://gist.github.com/dunglq2000/e41fd0c6a89987abf6d879d885f1d1a9>`_.

Khi đó ở bên trái phần công cụ **TEX** đã xuất hiện các commands là các recipes ta đã định nghĩa.

.. figure:: 07-recipes.png

[TODO] Vẽ hình với TikZ
=======================

Vẽ hình trên TikZ trên một file riêng, compile ra PDF rồi include vào tài liệu chính.

[TODO] Cấu hình lại các lệnh có sẵn theo tiếng Việt
===================================================

Sử dụng một số package phổ biến để tùy chỉnh lại các command 
có sẵn đang ở tiếng Anh (như ``contentsname``, ``chaptername``, 
``sectionname``, ...).
