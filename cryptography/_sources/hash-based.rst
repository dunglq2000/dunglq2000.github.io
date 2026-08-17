Hash-based cryptography
=======================


Цель работы
-----------


Целью работы является исследование криптографической схемы "подпись MSS на основе W-OTS", которая описана.

Для достижения поставленной цели необходимо решить следующие задачи:

1. Выполнить описание примитивов и базовых принципов работы криптосистемы.
2. Выполнить формальное и словесное описание алгоритмов криптосистемы:

   - для схемы асимметричного шифрования: алгоритм выбора и инициализации системных параметров, алгоритм генерации ключевой пары, алгоритм шифрования, алгоритм расшифрования;
   - для схемы подписи: алгоритм выбора и инициализации системных параметров, алгоритм генерации ключевой пары, алгоритм формирования подписи, алгоритм проверки подписи.
   - для схемы выработки общего секретного ключа: алгоритм выбора и инициализации системных параметров, алгоритм выработки передаваемых по открытому каналу значений, алгоритм вычисления общего ключа на основе полученных по открытому каналу значений.

3. Выполнить формальное и словесное описание необходимых дополнительных алгоритмов, например, алгоритма декодирования для криптосистемы Classic McEliece или алгоритм поиска обратного элемента в кольце многочленов для NTRU.
4. Привести обоснование стойкости криптосистемы. Представить описание вычислительно сложных задач, к решению которых сводится криптостойкость системы.
5. Выделить преимущества и недостатки рассматриваемой криптосистемы.
6. Подобрать, исходя из заданных вариантом, значения полного набора системных параметров. Обосновать выбор.
7. Выполнить следующие практические задания:

   1. Выполнить реализацию криптосистемы с набором значений системных параметров, сформированным при выполнении п.6.
   2. Продемонстрировать корректность работы программной реализации. Представить в отчете скриншоты как правильной работы алгоритмов при корректном наборе значений системных параметров, так и неправильной при некорректных.
   3. Провести серию экспериментов  определить среднее время выполнения алгоритмов и объем используемой памяти.

8. Ответить на дополнительный вопрос или выполнить дополнительное задание варианта (при наличии).

Описание примитивов и базовых принципов работы криптосистемы
------------------------------------------------------------


One-time signature (OTS)
~~~~~~~~~~~~~~~~~~~~~~~~


Первая схема подписи на основе хэша была опубликована в 1979 году Лэмпортом. Идея автора заключалась в выборочном раскрытии прообраза в виде выходных значений односторонней функции :math:`f`, в зависимости от количества битов подписываемого сообщения.

Чтобы подписать сообщение длиной :math:`n` бит, необходимо сгенерировать :math:`n` пар случайных значений :math:`(s_{i, 0}, s_{i, 1})`, чтобы получить последовательность :math:`(s_{1,0}, s_{1, 1}, \ldots, s_{n, 0}, s_{n, 1})`. Эта последовательность будет использоваться в качестве секретного ключа.

Открытый ключ генерируется путём применения :math:`f` к каждому элементу закрытого ключа, чтобы получить последовательность :math:`(p_{1, 0}, p_{1, 1}, \ldots, p_{n, 0}, p_{n, 1})`, где :math:`p_{i, j} = f(s_{i, j})`,
:math:`1 \leqslant i \leqslant n`, :math:`0 \leqslant j \leqslant 1`.

Чтобы подписать сообщение :math:`M` длиной :math:`n` бит, мы представим его в виде последовательности бит :math:`(m_1, m_2, \ldots, m_n)`. После генерации пары закрытого и открытого ключей, :math:`M` можно подписать, выборочно раскрывая части закрытого ключа. Для :math:`i`-го бита :math:`M` мы раскрываем :math:`s_{i, 0}`, если :math:`m_i = 0`, и :math:`s_{i, 1}`, если :math:`m_i = 1`. Подпись представляет собой последовательность :math:`(\sigma_1, \sigma_2, \ldots, \sigma_n)`, где :math:`\sigma_i = s_{i, m_i}` для всех :math:`1 \leqslant i \leqslant n`.

Для проверки подписи мы используем открытый ключ. Нам нужно применить :math:`f` к подписи, :math:`(f(\sigma_1), f(\sigma_2), \ldots, f(\sigma_n))`, и сравнить :math:`f(\sigma_i) \stackrel{?}{=} p_{i, m_i}` для всех :math:`1 \leqslant i \leqslant n`.

Merkle signature scheme (MSS)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


В 1982 года Меркл описал структуру, позволяющую связать несколько подписей с одним открытым ключом. Мы называем это деревом Меркла или хеш-деревом, а результат - схемой цифровой подписи Меркла (Merkle signature scheme, MSS).

Для создания дерева Меркла подписывающая сторона создаёт :math:`N` пар одноразовых ключей, где :math:`N` - степень числа :math:`2`. С помощью хеш-функции :math:`F` все :math:`N` открытых ключей «сжимаются» в один ключ путём построения двоичного дерева, начиная с листовых узлов.

Процесс построения двоичного дерева выглядит следующим образом:

- для каждого открытого ключа :math:`pk_i` подписывающая сторона создаёт листовой узел :math:`h_i = F(pk_i)`;
- затем значение родительского узла получается путём вычисления :math:`F` конкатенации двух дочерних узлов. Предположим, что родительский узел имеет два дочерних узла: :math:`h_i` и :math:`h_{i+1}`, тогда значение родительского узла равно :math:`F(h_i \Vert h_{i+1})`. Продолжим, пока не будет найден корень дерева, который и будет многоразовым открытым ключом.

Подписывающая сторона создаёт подпись MSS, выбирая ранее неиспользованный конечный узел и создавая подпись с использованием базовой схемы OTS. Пример дерева Меркла представлен на рисунке :ref:`fig:merkle-tree`.

.. figure:: PQC/merkle-tree-01.svg
   :align: center
   :name: fig:merkle-tree

   Дерева Меркла с :math:`N=8` листовыми узлами


Чтобы доказать, что пара ключей, используемая для подписи, является частью дерева Меркла с долгосрочным открытым ключом в качестве корневого узла, подписывающая сторона объединяет путь аутентификации с подписью, содержащий индекс используемого конечного узла и кратчайший список узлов, позволяющий проверяющей стороне вычислить корневой узел дерева.

Пример пути аутентификации показан на рисунке :ref:`fig:merkle-auth-path`. Предположим,
что подписывающая сторона использует открытый ключ :math:`pk_1` для генерации подписи, тогда путь включает индекс :math:`1`. Чтобы позволить проверяющей стороне вычислить корень дерева, подписывающая сторона должна также отправить :math:`h_0`, :math:`h_9` и :math:`h_{13}`. Таким образом, подписывающая сторона публикует :math:`(sig, pk_1, 1, h_0, h_9, h_{13})`. Проверяющая сторона может вычислить :math:`h_1 = F(pk_1)`, :math:`h_8 = F(h_0 \Vert h_1)`, :math:`h_{12} = F(h_0 \Vert h_9)` и, наконец, :math:`h_{14} = F(h_{12} \Vert h_{13})`. Поскольку многоразовый открытый ключ
известен заранее, проверяющая сторона сравнивает с ним :math:`h_{14}`.

.. figure:: PQC/merkle-tree-02.svg
   :align: center
   :name: fig:merkle-auth-path

   Путь аутентификации для листового узла :math:`h_1`


Winternitz one-time signature (W-OTS)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


Одноразовая подпись Винтерица (Winternitz one-time signature, W-OTS) была предложена в 1979 году Винтерицем и независимо от Лэмпорта. Она предназначена для уменьшения размера ключа и подписи по сравнению с оригинальной схемой Лэмпорта, за счёт увеличения времени генерации ключа и подписания.

W-OTS использует параметр :math:`w`, называемый параметром Винтерица, который определяет количество бит, обрабатываемых одновременно. Вместо того, чтобы подписывать каждый бит сообщения отдельно, как в схеме Лэмпорта, W-OTS группирует биты сообщения в блоки по :math:`w` бит и подписывает каждый блок с помощью цепочки хеш-функций.

Обозначение :math:`f^t(x) = \underbrace{f(f(\ldots(x)))}_{t \ \text{раз}}`. Обычно используется следующее соглашение: :math:`f^0(x) = x`.

Закрытый ключ W-OTS представляет собой список псевдослучайно сгенерированных значений. Соответствующие значения открытого ключа :math:`pk_i` получаются путём итерации :math:`f` для каждого значения закрытого ключа :math:`s_i` :math:`w-1` раз, то есть :math:`pk_i = f^{w-1}(s_i)`.

Параметр Винтерница обычно является степенью числа 2, то есть :math:`w = 2^t`.

Чтобы создать подпись, подписывающая сторона раскрывает промежуточные значения:

- предположим, что биты сообщения :math:`t` в десятичной форме представляют собой целое число :math:`u`, тогда подписывающая сторона раскрывает :math:`f^u(s_i)` как подписи;
- проверяющая сторона проверяет, вычисляя :math:`f`, добавляя :math:`w - 1 - u` раз, чтобы получить :math:`f^{w - 1 - u}(f^u(s_i)) = f^{w - 1}(s_i)`.

В описанной выше схеме есть изъян: если злоумышленник знает значение подписи :math:`f^u(s_i)`, он может легко вычислить :math:`f^{u+1}(s_i) = f(f^u(s_i))`, тем самым сгенерировав новую действительную подпись. Для решения этой проблемы мы используем контрольную сумму. При изменении подписи контрольная сумма становится недействительной.

Формальное и словесное описание алгоритмов криптосистемы
--------------------------------------------------------


Алгоритм подписи OTS Лэмпорта
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


Сначала мы устанавливаем процедуры для OTS Лэмпорта.

Общие параметры OTS включают в себя:

- :math:`N` - количество бит каждого подписываемого сообщения;
- :math:`F` - односторонняя функция :math:`\{ 0, 1 \}^k \to \{ 0, 1 \}^k` с фиксированным целевым числом :math:`k`.

Таким образом, :math:`k` - это количество бит каждого элемента секретного ключа :math:`s_{i, j}`, а также открытого ключа :math:`p_{i, j}`, где :math:`1 \leqslant i \leqslant N` и :math:`0 \leqslant j \leqslant 1`.

Обозначение :math:`\overset{\$}{\gets} \{ 0, 1 \}` представляет собой случайный выбор битовой строки длиной :math:`k`.

.. rubric:: :math:`\mathsf{Lambort.KeyGen}()` - генерация пары ключа OTS Лэмпорта
   :name: alg:ots-keygen


**Input** :math:`N, k, F`

**Output:** :math:`(sk, pk)`, где :math:`sk` - секретный ключ, :math:`pk` - открытый ключ

1. For :math:`i \gets 1` to :math:`N`

   1. For :math:`j \gets 0` to :math:`1`

      - :math:`s_{i, j} \overset{\$}{\gets} \{ 0, 1 \}^k`
      - :math:`p_{i, j} \gets F(s_{i, j})`

2. :math:`sk \gets (s_{1, 0}, s_{1, 1}, \ldots, s_{N, 0}, s_{N, 1})`
3. :math:`pk \gets (p_{1, 0}, p_{1, 1}, \ldots, p_{N, 0}, p_{N, 1})`
4. Return :math:`(sk, pk)`


.. rubric:: :math:`\mathsf{Lambort.Sign(M, sk)}` - создание подписи OTS Лэмпорта
   :name: alg:ots-sign


**Input:** сообщение :math:`M`, :math:`sk = (s_{1, 0}, s_{1, 1}, \ldots, s_{N, 0}, s_{N, 1})`, :math:`F`

**Output:** :math:`\sigma` - подпись :math:`M = (m_1, m_2, \ldots, m_N)`, где :math:`m_i \in \{ 0, 1 \}`

1. For :math:`i \gets 1` to :math:`N`
   - :math:`\sigma_i \gets s_{i, m_i}`

2. :math:`\sigma \gets (\sigma_1, \sigma_2, \ldots, \sigma_N)`
3. Return :math:`\sigma`


.. rubric:: :math:`\mathsf{Lambort.Verify(M, \sigma, pk)}` - проверка подписи OTS Лэмпорта
   :name: alg:ots-verify


**Input:** сообщение :math:`M`, подпись :math:`\sigma = (\sigma_1, \sigma_2,  \ldots, \sigma_N)`, :math:`pk = (p_{1, 0}, p_{1, 1}, \ldots, p_{N, 0}, p_{N, 1})`, :math:`F`

**Output:** true или false

1. :math:`M = (m_1, m_2, \ldots, m_N)`, где :math:`m_i \in \{ 0, 1 \}`
2. For :math:`i \gets 1` to :math:`N`

   1. If :math:`F(\sigma_i) \neq p_{i, m_i}`

      Return false
3. Return true


.. _sec:alg:wots:

Алгоритм подписи W-OTS
~~~~~~~~~~~~~~~~~~~~~~


Для схемы цифровой подписи W-OTS с параметром Винтерница :math:`w` нам понадобятся следующие дополнительные параметры:

- :math:`l_1 = \left\lceil \dfrac{N}{\log_2 w} \right\rceil` - максимальное количество фрагментов, которое может содержать сообщение. Например, если сообщение содержит 128 бит и :math:`w = 16 = 2^4`, мы можем разделить сообщение на 32 фрагмента по 4 бита в каждом;
- :math:`l_2 = \left\lfloor \dfrac{\log_2(l_1 (w - 1))}{\log_2 w} \right\rfloor + 1` - максимальная длина контрольной суммы.

Таким образом, параметры W-OTS включают в себя:

- :math:`l = l_1 + l_2` - количество элементов подписи;
- :math:`F` - односторонняя функция от :math:`\{ 0, 1 \}^k \to \{ 0, 1 \}^k`, где :math:`k` - фиксированное целое число;
- :math:`w` - параметр Винтерница.

.. rubric:: :math:`\mathsf{WOTS.KeyGen}()` - генерация пары ключа W-OTS
   :name: alg:wots-keygen


**Input:** :math:`l, k, w, F`

**Output:** :math:`(sk, pk)`, где :math:`sk` - секретный ключ, :math:`pk` - открытый ключ

1. For :math:`i \gets 1` to :math:`l`

   - :math:`s_i \overset{\$}{\gets} \{ 0, 1 \}^k`
   - :math:`pk_i \gets f^{w-1}(s_i)`

2. :math:`sk \gets (s_1, s_2, \ldots, s_l)`
3. :math:`pk \gets (pk_1, pk_2, \ldots, pk_l)`
4. Return :math:`(sk, pk)`


.. rubric:: :math:`\mathsf{WOTS.Sign}(M, sk)` - создание подписи W-OTS
   :name: alg:wots-sign


**Input:** сообщение :math:`M`, :math:`sk = (s_1, s_2, \ldots, s_l)`, :math:`w`, :math:`l_1`, :math:`l_2`, :math:`F`

**Output:** :math:`\sigma` - подпись

1. :math:`M = (m_1, m_2, \ldots, m_{l_1})`, где :math:`m_i \in \{ 0, 1, \ldots, w - 1 \}`
2. For :math:`i \gets 1` to :math:`l_1`

   1. :math:`\sigma_i \gets F^{m_i}(s_i)`

3. :math:`c \gets \sum\limits_{i=1}^{l_1} (w - 1 - m_i)`
4. :math:`c = (c_1, c_2, \ldots, c_{l_2})`, где :math:`c_i \in \{ 0, 1, \ldots, w - 1\}`
5. For :math:`i \gets 1` to :math:`l_2`

   1. :math:`\sigma_{l_1 + i} \gets F^{c_i}(s_{l_1 + i})`

6. :math:`\sigma \gets (\sigma_1, \sigma_2, \ldots, \sigma_l)`
7. Return :math:`\sigma`


.. rubric:: :math:`\mathsf{WOTS.Verify}(M, \sigma, pk)` - проверка подписи W-OTS
   :name: alg:wots-verify


**Input:** сообщение :math:`M`, подпись :math:`\sigma = (\sigma_1, \sigma_2, \ldots, \sigma_l)`, :math:`pk = (pk_1, pk_2, \ldots, pk_l)`, :math:`w`, :math:`l_1`, :math:`l_2`, :math:`F`

**Output:** true или false

1. :math:`M = (m_1, m_2, \ldots, m_{l_1})`, где :math:`m_i \in \{ 0, 1, \ldots, w - 1 \}`
2. For :math:`i \gets 1` to :math:`l_1`

   1. If :math:`F^{w - 1 - m_i}(\sigma_i) \neq pk_i`

      1. Return false

3. :math:`c \gets \sum\limits_{i=1}^{l_1} (w - 1 - m_i)`
4. :math:`c = (c_1, c_2, \ldots, c_{l_2})`, где :math:`c_i \in \{ 0, 1, \ldots, w - 1\}`
5. For :math:`i \gets 1` to :math:`l_2`

   1. If :math:`F^{w - 1 - c_i}(\sigma_{l_1 + i}) \neq pk_{l_1 + i}`

      Return false

6. Return true


.. rubric:: :math:`\mathsf{WOTS.RecoverPK}(M, \sigma)` - восстановление открытого ключа W-OTS из подписи
   :name: alg:wots-recover-pk


**Input:** сообщение :math:`M`, подпись :math:`\sigma = (\sigma_1, \sigma_2, \ldots, \sigma_l)`, :math:`w`, :math:`l_1`, :math:`l_2`, :math:`F`

**Output:** :math:`pk` - открытый ключ

1. :math:`M = (m_1, m_2, \ldots, m_{l_1})`, где :math:`m_i \in \{ 0, 1, \ldots, w - 1 \}`
2. For :math:`i \gets 1` to :math:`l_1`

   1. :math:`pk_i \gets F^{w - 1 - m_i}(\sigma_i)`

3. :math:`c \gets \sum\limits_{i=1}^{l_1} (w - 1 - m_i)`
4. :math:`c = (c_1, c_2, \ldots, c_{l_2})`, где :math:`c_i \in \{ 0, 1, \ldots, w - 1\}`
5. For :math:`i \gets 1` to :math:`l_2`

   1. :math:`pk_{l_1 + i} \gets F^{w - 1 - c_i}(\sigma_{l_1 + i})`

6. :math:`pk \gets (pk_1, pk_2, \ldots, pk_l)`
7. Return :math:`pk`


.. rubric:: :math:`\mathsf{WOTS.RecoverPK}(sk)` - восстановление открытого ключа W-OTS из секретного ключа
   :name: alg:wots-recover-pk-from-sk


**Input:** :math:`sk = (s_1, s_2, \ldots, s_l)`, :math:`w`, :math:`l`, :math:`F`

**Output:** :math:`pk` - открытый ключ

1. For :math:`i \gets 1` to :math:`l`

   1. :math:`pk_i \gets F^{w - 1}(s_i)`

2. :math:`pk \gets (pk_1, pk_2, \ldots, pk_l)`
3. Return :math:`pk`


Алгоритм построения дерева Меркла
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


Для построения дерева Меркла нам понадобятся следующие параметры:

- :math:`n = 2^h` - количество листовых узлов, где :math:`h` - высота дерева;
- :math:`H` - хэш-функция от :math:`\{ 0, 1 \}^k \times \{ 0, 1 \}^k \to \{ 0, 1 \}^k`, где :math:`k` - фиксированное целое число.

Сначала мы генерируем :math:`p` пар одноразовых ключей OTS в виде :math:`(sk_i, pk_i)`, где :math:`i \in \{ 0, 1, \ldots, 2^{h-1} \}`. Затем мы используем их для построения двоичного дерева высотой :math:`h`.

Листовые узлы - это открытые ключи :math:`pk_i`. Дерево Меркла строится снизу вверх, листовые узлы имеют высоту 0. Каждый родительский узел строится путем вычисления хеш-значения :math:`H` от его дочерних узлов. Другими словами, если обозначение :math:`\mathsf{node}_{i, j}` является :math:`j`-м узлом на высоте :math:`i`, то узел :math:`\mathsf{node}_{i+1, j}` вычисляется по формуле

.. math::

   \mathsf{node}_{i+1, j} = H(\mathsf{node}_{i, 2j}, \mathsf{node}_{i, 2j+1}),


где :math:`0 \leqslant j < 2^{h - i - 1}` и :math:`0 \leqslant i < h`.

Алгоритм построения дерева Меркла представлен в алгоритме :ref:`alg:merkle-tree`.

.. rubric:: :math:`\mathsf{MerkleTree.Build}(\text{leaf}_0, \text{leaf}_1, \ldots, \text{leaf}_{2^{h-1} - 1})` - построение дерева Меркла
   :name: alg:merkle-tree


**Input:** :math:`h, H`

**Output:** дерево Меркла с корневым узлом :math:`\mathsf{node}_{h, 0}`

1. For :math:`j \gets 0` to :math:`2^{h-1} - 1`

   1. :math:`\mathsf{node}_{0, j} \gets \text{leaf}_j`

2. For :math:`i \gets 0` to :math:`h - 1`

   1. For :math:`j \gets 0` to :math:`2^{h - i - 1} - 1`

      1. :math:`\mathsf{node}_{i+1, j} \gets H(\mathsf{node}_{i, 2j}, \mathsf{node}_{i, 2j+1})`

3. Return :math:`\mathsf{node}_{i, j}` для всех :math:`0 \leqslant i \leqslant h` и :math:`0 \leqslant j < 2^{h - i}`


Алгоритм криптосистемы подписи MSS на основе W-OTS
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


.. rubric:: :math:`\mathsf{MSS.KeyGen}()` - генерация ключа MSS на основе W-OTS
   :name: alg:mss-keygen


**Input:** :math:`h` -- высота дерева

**Output:** :math:`SK = (sk_0, \ldots, sk_{2^h-1})` - секретные ключи, :math:`PK` - открытый ключ

1. For :math:`i \gets 0` to :math:`2^{h} - 1`

   1. :math:`(sk_i, pk_i) \gets \mathsf{WOTS.KeyGen}()`

2. :math:`\mathsf{node}_{i, j} \gets \mathsf{MerkleTree.Build}(pk_0, pk_1, \ldots, pk_{2^{h} - 1})`
3. :math:`PK \gets \mathsf{node}_{h, 0}`
4. :math:`SK \gets (sk_0, sk_1, \ldots, sk_{2^h - 1})`
5. Return :math:`SK, PK`


.. rubric:: :math:`\mathsf{MSS.Sign}(M, idx, SK)` - создание подписи MSS на основе W-OTS
   :name: alg:mss-sign


**Input:** сообщение :math:`M`, :math:`SK = (sk_0, \ldots, sk_{2^h-1})` - секретные ключи

**Output:** :math:`\sigma` - подпись

1. If :math:`idx \geqslant 2^h - 1`

   1. Return error

2. :math:`\sigma_{wots} \gets \mathsf{WOTS.Sign}(M, sk_{idx})`
3. For :math:`j \gets 0` to :math:`2^h - 1`

   1. :math:`pk_j \gets WOTS.RecoverPK(sk_j)`

4. :math:`\mathsf{node}_{i, j} \gets \mathsf{MerkleTree.Build}(pk_0, pk_1, \ldots, pk_{2^{h} - 1})`
5. :math:`j \gets idx`
6. For :math:`i \gets 0` to :math:`h - 1`

   1. If :math:`j` четно: :math:`\text{auth}_i \gets \mathsf{node}_{i, j + 1}`
   2. Else: :math:`\text{auth}_i \gets \mathsf{node}_{i, j - 1}`
   3. :math:`j \gets \lfloor j / 2 \rfloor`

7. :math:`\sigma \gets (idx, pk_{idx}, \sigma_{wots}, \text{auth}_0, \text{auth}_1, \ldots, \text{auth}_{h-1})`
8. Return :math:`\sigma`


.. rubric:: :math:`\mathsf{MSS.Verify}(M, \sigma, PK)` - проверка подписи MSS на основе W-OTS
   :name: alg:mss-verify


**Input:** сообщение :math:`M`, подпись :math:`\sigma = (idx, pk_{idx}, \sigma_{wots}, \text{auth}_0, \text{auth}_1, \ldots, \text{auth}_{h-1})`, :math:`PK` - открытый ключ

**Output:** true или false

1. :math:`\sigma \gets (idx, pk_{idx}, \sigma_{ots}, \text{auth}_0, \text{auth}_1, \ldots, \text{auth}_{h-1})`
2. If{:math:`\mathsf{WOTS.Verify}(M, \sigma_{ots}, pk_{idx})` = false}

   1. Return false

3. :math:`\mathsf{node}_0 \gets pk_{idx}`
4. :math:`j \gets idx`
5. For :math:`i \gets 0` to :math:`h - 1`

   1. If :math:`j` четно: :math:`\mathsf{node}_{i+1} \gets H(\mathsf{node}_i, \text{auth}_i)`
   2. Else: :math:`\mathsf{node}_{i+1} \gets H(\text{auth}_i, \mathsf{node}_i)`
   3. :math:`j \gets \lfloor j / 2 \rfloor`

6. If :math:`\mathsf{node}_h \neq PK`

   1. Return false

7. Return true


Формальное и словесное описание необходимых дополнительных алгоритмов
---------------------------------------------------------------------


Обоснование стойкости криптосистемы
-----------------------------------


Схема MSS на основе W-OTS использует криптографические хеш-функции для генерации ключей и подписи сообщений, что делает её устойчивой к атакам с пересчётом секретного ключа. Кроме того, использование W-OTS позволяет подписывать несколько сообщений, избегая повторения ключей. Это помогает избежать уязвимостей, возникающих при многократном использовании одного и того же ключа (например, оракулы).

Здесь используется хеш-функция SHA256. Это безопасная хеш-функция, определённая в стандарте США.

Преимущества и недостатки рассматриваемой криптосистемы
-------------------------------------------------------


Преимущества схемы подписи MSS на основе W-OTS включают в себя:

- она позволяет подписывать несколько сообщений одним и тем же открытым ключом, являющимся корнем дерева Меркла;
- простота реализации: многие библиотеки в языках программирования уже поддерживают криптографические хеш-функции, и написание программ для деревьев Меркла несложно;
- значение секретного ключа, которое необходимо сгенерировать, меньше, чем для OTS Лампорта, поскольку мы разбиваем сообщение на сегменты по :math:`t` бит; чем больше :math:`t`, тем меньше требуется :math:`s_i`.

Недостатки вышеописанной схемы:

1. Каждый секретный ключ W-OTS :math:`sk_i` состоит из :math:`l` компонентов, как описано в разделе :ref:`sec:alg:wots`. Каждый компонент имеет длину 256 бит, что соответствует длине результата хэширования, поэтому общая длина каждого секретного ключа составляет :math:`256 l / 8 = 32 l` байт.
2. Каждый секретный ключ :math:`sk_i` сопровождается открытым ключом :math:`pk_i` той же длины. Мы можем либо вычислить :math:`pk_i` и сохранить его для многократного использования, либо использовать алгоритм :ref:`alg:wots-recover-pk-from-sk` для его восстановления. Первый вариант требует больше памяти, а второй - больше вычислений.
3. Если дерево Меркла содержит :math:`n` листовых узлов, то для хранения всех листьев дерева потребуется всего :math:`32 l n` байт. Причина хранения всех секретных ключей заключается в том, чтобы выбрать ключ, который не использовался при подписании новых сообщений. Обычно :math:`n` - это степень двойки для оптимизации построения дерева Меркла, но это потребует большого объёма памяти.
4. Общий открытый ключ (корень дерева Меркла) будет подписывать :math:`n` различных сообщений, соответствующих :math:`n` конечным узлам. Число :math:`n` должно быть достаточно большим для обеспечения практичности, поскольку в других классических алгоритмах (Эль-Гамаля, ECC) каждый открытый ключ позволяет подписывать множество различных сообщений.

Подбор значений полного набора системных параметров
---------------------------------------------------


Значения системных параметров: :math:`n = 32`, :math:`w = 8`.

Практические задания
--------------------


Реализация криптосистемы с заданным набором значений системных параметров
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


Код реализации криптосистемы представлен в приложении :ref:`appendix:mss-bin`.

Код реализации криптосистемы на основе троичного дерева (ДОПОЛНИТЕЛЬНОЕ ЗАДАНИЕ) представлен в приложении :ref:`appendix:mss-ter`.

Демонстрация корректности работы программной реализации
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


Для демонстрации корректности программной реализации была проведена серия экспериментов с использованием pytest.

Результаты тестирования дерева Меркла (и двоичное, и троичное) показаны на рисунке :ref:`fig:test-merkle-tree`, где каждый тест строит дерево Меркла и проверяет узлы в нём вручную. Тестовая программа представлена в приложении :ref:`sec:test_merkle_tree`.

.. figure:: PQC/test_merkle_tree.png
   :align: center
   :name: fig:test-merkle-tree

   Проверка корректности работы дерева Меркла


Результаты тестирования корректности схемы MSS на основе W-OTS (и двоичное, и троичное дерева Меркла) показаны на рисунке :ref:`fig:test-mss-wots`, где каждый тест строит дерево Меркла и проверяет узлы в нём вручную. Тестовая программа представлена в приложении :ref:`sec:test_mss_wots`.

.. figure:: PQC/test_mss_wots.png
   :align: center
   :name: fig:test-mss-wots

   Проверка корректности схемы MSS на основе W-OTS


Серия экспериментов
~~~~~~~~~~~~~~~~~~~


В серии экспериментов изучалось среднее время, необходимое для подписания 32 сообщений с использованием одного и того же дерева Меркла. На рисунке :ref:`fig:test-timing` показано сравнение среднего времени (в микросекундах) при использовании двоичного и троичного деревьев.

Двоичное дерево имеет :math:`2^5 = 32` листовых узла, а троичное дерево - :math:`3^4 = 81` листовой узел. Высота бинарного дерева равна 6, а троичного - 5.

.. figure:: PQC/test_timing.png
   :align: center
   :name: fig:test-timing

   Сравнение среднего времени подписания между двоичным и троичным деревом


Дополнительное задание
----------------------


Реализация дополнительного задания
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


Код реализации схемы подписи на основе троичного дерева, вместо бинарного, представлен в приложении :ref:`appendix:mss-ter`.

Результаты проверки корректности программной реализации уже показан на рисунках :ref:`fig:test-merkle-tree` и :ref:`fig:test-mss-wots`.

Серия экспериментов для сравнения среднего времени подписания уже показана на рисунке :ref:`fig:test-timing`.

Функциональное сравнение схем подписи
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


Сравнение длины пути аутентификации
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Для бинарного дерева количество листовых узлов обычно равно степени 2 для оптимизации построения дерева. Аналогично, для троичного дерева количество листовых узлов равно степени 3. Каждый лист представляет собой пару ключей W-OTS и не зависит от того, является ли дерево Меркла бинарным или троичным.

Далее мы проанализируем общий случай :math:`n` листьев. Тогда высота двоичного дерева с :math:`n` листьями равна :math:`h_2 = \lceil \log_2 n \rceil + 1`, а высота троичного дерева с :math:`n` листьями равна :math:`h_3 = \lceil \log_3 n \rceil + 1`. При построении пути аутентификации каждый уровень двоичного дерева будет содержать один элемент, включенный в путь. Аналогично, каждый уровень троичного дерева будет содержать два элемента, включенных в путь. Таким образом, путь аутентификации двоичного дерева содержит :math:`h_2 - 1` узлов, а троичного дерева - :math:`2 (h_3 - 1)` узлов (не считая корневого уровня).

Поскольку :math:`2 (h_3 - 1) > h_2 - 1` при :math:`n \geqslant 4`, длина пути аутентификации для троичного дерева всегда больше, чем для бинарного. С ростом :math:`n` разница становится более существенной.

Сравнение объём подписи
^^^^^^^^^^^^^^^^^^^^^^^


Легко видеть, что каждый листовой узел имеет фиксированную длину (в байтах), поэтому при использовании хеш-функции SHA-256 общая длина всех закрытых и открытых ключей составляет :math:`32n + 32n = 64n` байт, где :math:`n` - количество листовых узлов. Следовательно, независимо от того, является ли дерево двоичным или троичным, объём памяти, используемой для хранения листовых узлов (пар ключей W-OTS), одинаков.

Разница заключается в объёме памяти и времени, необходимом для построения дерева Меркла. Поскольку :math:`\log_2 n > \log_3 n`, построение двоичного дерева Меркла займёт больше времени (больше слоёв). Это означает, что потребуется больше памяти, поскольку для вычисления верхнего слоя требуются все узлы нижнего слоя.

Сравнение среднего времени подписания
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


На рисунке :ref:`fig:test-timing` видно, что среднее время подписания троичного дерева значительно выше, чем у бинарного, несмотря на меньшую высоту троичного дерева и одинаковое количество требуемых конечных узлов для подписания. Это связано с тем, что, как было показано выше, путь аутентификации троичного дерева длиннее, поэтому генерация подписи занимает больше времени.

Однако следует добавить, что измерение производится в микросекундах, поэтому при данных параметрах мы не увидим существенной разницы. При очень большом количестве конечных узлов разница будет ещё более очевидной.

Заключение
----------


На основе выполнения лабораторной работы я сделали следующие выводы:

1. Я построил схему подписи пост-количества, используя двоичное дерево Меркла на основе W-OTS. Тестирование программы со случайными значениями в каждом запуске гарантирует её корректность. Кроме того, я оценил безопасность схемы, а также проанализировал её преимущества и недостатки.
2. Я реализовал схему на основе троичного дерева Меркла и сравнил её со схемой на основе бинарного дерева. Показано, что троичное дерево увеличивает длину пути аутентификации при :math:`n \geqslant 4`, поэтому использование троичного дерева непрактически.

.. _appendix:mss-bin:

Реализация криптосистемы
------------------------


.. code-block:: python
   :caption: merkle_tree.py

   from utils import hash_function
   from typing import List
   from wots import WOTS

   class MerkleTree:
       def __init__(self):
           self.nodes = None
           self.height = None

       def tree_build(self, leaves: List[bytes]) -> None:

           return None

       def get_size(self) -> int:
           return 0

   if __name__ == "__main__":
       ...


.. code-block:: python
   :caption: mss_wots.py

   import math
   from typing import List, Tuple

   from utils import hash_function
   from wots import WOTS
   from merkle_ternary_tree import MerkleTernaryTree

   class MSS_WOTS:
       def __init__(self, n: int = 32):
           self.n = n
           self.height = None
           self.wots = WOTS()
           keys = [self.wots.generate_key() for _ in range(self.n)]
           self.private_keys: List[List[bytes]] = []
           self.public_keys_hash: List[bytes] = []

           for key in keys:
               private_key, public_key = key
               self.private_keys.append(private_key)
               self.public_keys_hash.append(hash_function(b"".join(public_key)))

           self.pubkey = None
           self.used_keys: List[int] = []

       def sign(
               self, message: bytes, leaf_index: int
               ) -> Tuple[int, List[bytes], bytes, List[bytes]]:
           return None

       def verify(
               self, message: bytes,
               signature: Tuple[int, List[bytes], bytes, List[bytes]]
               ) -> bool:
           return True

   if __name__ == "__main__":
       ...


.. code-block:: python
   :caption: test_timing.py

   from mss_binary_wots import MSS_BIN_WOTS
   from mss_ternary_wots import MSS_TER_WOTS
   import secrets
   import time
   from typing import List

   if __name__ == "__main__":
       mss_bin_wots = MSS_BIN_WOTS(n=32)
       signing_bin_time: List[float] = []
       for i in range(32):

           message = secrets.token_bytes(16)

           start: float = time.time()

           signature = mss_bin_wots.sign(message, i)
           end: float = time.time()
           signing_bin_time.append(end - start)

       average_bin_time = 10**6 * (sum(signing_bin_time) / 32)
       print(f"Testing on 32 signing keys of Merkle binary tree")
       print(f"Average signing time: {average_bin_time:.4f} microseconds")

       mss_ter_wots = MSS_TER_WOTS(n=81)
       signing_ter_time: List[float] = []
       for i in range(32):

           message = secrets.token_bytes(16)

           start: float = time.time()

           signature = mss_ter_wots.sign(message, i)
           end: float = time.time()
           signing_ter_time.append(end - start)

       average_ter_time = 10**6 * (sum(signing_ter_time) / 32)
       print(f"Testing on 32 signing keys of Merkle ternary tree")
       print(f"Average signing time: {average_ter_time:.4f} microseconds")


Дополнительные функции
~~~~~~~~~~~~~~~~~~~~~~


.. code-block:: python
   :caption: utils.py

   import hashlib

   def hash_function(data: bytes) -> bytes:
       return hashlib.sha256(data).digest()

   def chain_function(start_value: bytes, steps: int, hash_func: callable) -> bytes:
       current_value = start_value
       for _ in range(steps):
           current_value = hash_func(current_value)
       return current_value

   def bytes_to_base_w(digest: bytes, w: int, l1: int, l2: int) -> list[int]:

       digest_int = int.from_bytes(digest, 'big')
       a = []

       for _ in range(l1):
           a.append(digest_int % w)
           digest_int //= w
       a.reverse()

       checksum = sum(w - 1 - val for val in a)

       b = []

       for _ in range(l2):
           b.append(checksum % w)
           checksum //= w
       b.reverse()

       return a + b


Код для W-OTS
~~~~~~~~~~~~~


.. code-block:: python
   :caption: wots.py

   from utils import hash_function, chain_function, bytes_to_base_w
   import secrets
   from typing import List, Tuple
   import math

   class WOTS:
       def __init__(self, N: int = 32, W: int = 8):
           self.N = N
           self.W = W
           self.L1 = math.ceil(N / math.log2(W))
           self.L2 = math.floor(math.log2(self.L1 * (W - 1) / math.log2(W))) + 1
           self.L = self.L1 + self.L2

       def generate_key(self) -> Tuple[List[bytes], List[bytes]]:

           private_keys: List[bytes] = [secrets.token_bytes(self.N) for _ in range(self.L)]
           public_keys: List[bytes] = [chain_function(seed, self.W - 1, hash_function)
                                       for seed in private_keys]

           return private_keys, public_keys

       def sign(self, message: bytes, private_key: List[bytes]) -> List[bytes]:
           digest: bytes = hash_function(message)
           base_w_digits = bytes_to_base_w(digest, self.W, self.L1, self.L2)

           signature = []
           for i in range(self.L):

               steps = base_w_digits[i]
               sig_element = chain_function(private_key[i], steps, hash_function)
               signature.append(sig_element)

           return signature

       def verify(self, message: bytes, signature: List[bytes], public_key: List[bytes]) -> bool:
           digest = hash_function(message)
           base_w_digits = bytes_to_base_w(digest, self.W, self.L1, self.L2)
           for i in range(self.L):
               steps = self.W - 1 - base_w_digits[i]
               if chain_function(signature[i], steps, hash_function) != public_key[i]:
                   return False
           return True

       def get_pubkey_from_signature(self, message: bytes, signature: List[bytes]) -> List[bytes]:
           digest = hash_function(message)
           base_w_digits = bytes_to_base_w(digest, self.W, self.L1, self.L2)

           public_key = []
           for i in range(self.L):
               steps = base_w_digits[i]
               remaining_steps = self.W - 1 - steps
               pub_element = chain_function(signature[i], remaining_steps, hash_function)
               public_key.append(pub_element)

           return public_key

       def get_pubkey_from_privkey(self, private_key: List[bytes]) -> List[bytes]:
           public_key = [chain_function(seed, self.W - 1, hash_function) for seed in private_key]
           return public_key

   if __name__ == "__main__":
       wots = WOTS()
       priv_key, pub_key = wots.generate_key()
       message = secrets.token_bytes(16)
       signature = wots.sign(message, priv_key)
       reconstructed_pub_key = wots.get_pubkey_from_signature(message, signature)
       assert reconstructed_pub_key == pub_key, "Signature verification failed!"
       assert wots.verify(message, signature, pub_key)


Код для дерева Меркла
~~~~~~~~~~~~~~~~~~~~~


.. code-block:: python
   :caption: merkle_binary_tree.py

   from utils import hash_function
   from typing import List
   from wots import WOTS
   from merkle_tree import MerkleTree

   class MerkleBinaryTree(MerkleTree):
       def __init__(self):
           self.nodes = None
           self.height = None

       def tree_build(self, leaves: List[bytes]) -> None:

           self.nodes: List[List[bytes]] = [leaves[:]]
           level_size = len(leaves)

           while level_size > 1:
               new_level = []

               for i in range(0, level_size, 2):
                   left = self.nodes[-1][len(self.nodes[-1]) - level_size + i]
                   right = self.nodes[-1][len(self.nodes[-1]) - level_size + i + 1]

                   new_node = MerkleBinaryTree.H(left, right)
                   new_level.append(new_node)

               self.nodes.append(new_level)
               level_size = len(new_level)

           self.nodes.reverse()
           self.height = len(self.nodes)

       def get_size(self) -> int:
           S: int = 0
           for i in range(len(self.nodes[-1])):
               S += len(self.nodes[-1][i])
           return S

       @staticmethod
       def H(message_1: bytes, message_2: bytes) -> bytes:
           return hash_function(message_1 + message_2)

   if __name__ == "__main__":
       wots = WOTS()
       keys = [wots.generate_key() for _ in range(32)]
       private_keys: List[List[bytes]] = []
       public_keys_hash: List[bytes] = []

       for i, key in enumerate(keys):
           private_key, public_key = key
           private_keys.append(private_key)
           public_keys_hash.append(hash_function(b"".join(public_key)))

       merkle_tree = MerkleBinaryTree()
       merkle_tree.tree_build(public_keys_hash)

       h = len(merkle_tree.nodes)
       for i in range(h - 1):
           for j in range(len(merkle_tree.nodes[i])):
               assert merkle_tree.nodes[i][j] == \
                   hash_function(merkle_tree.nodes[i+1][2*j] + merkle_tree.nodes[i+1][2*j+1])


Код для реализации подписи MSS на основе W-OTS
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


.. code-block:: python
   :caption: mss_binary_wots.py

   import math
   from typing import List, Tuple, Union

   from utils import hash_function
   from wots import WOTS
   from mss_wots import MSS_WOTS
   from merkle_binary_tree import MerkleBinaryTree

   class MSS_BIN_WOTS(MSS_WOTS):
       def __init__(self, n: int = 32):
           super().__init__(n=n)

           self.height = math.ceil(math.log2(n)) + 1

           tree = MerkleBinaryTree()
           tree.tree_build(self.public_keys_hash)

           self.pubkey = tree.nodes[0][0]

       def sign(
               self, message: bytes, leaf_index: int,
               ) -> Union[None, Tuple[int, List[bytes], bytes, List[bytes]]]:

           private_key = self.private_keys[leaf_index]
           if leaf_index > self.n - 1 or leaf_index in self.used_keys:
               raise ValueError("Private key index is invalid")

           signature_wots = self.wots.sign(message, private_key)
           public_keys: List[List[bytes]] = [
               self.wots.get_pubkey_from_privkey(privkey)
                   for privkey in self.private_keys]
           public_keys_hash: List[bytes] = [
               hash_function(b"".join(pubkey)) for pubkey in public_keys]
           merkle_tree = MerkleBinaryTree()
           merkle_tree.tree_build(public_keys_hash)

           auth: List[bytes] = []
           self.used_keys.append(leaf_index)
           index = leaf_index
           for i in range(self.height - 1):
               if index % 2 == 0:
                   auth.append(merkle_tree.nodes[self.height - 1 - i][index + 1])
               else:
                   auth.append(merkle_tree.nodes[self.height - 1 - i][index - 1])
               index //= 2

           signature: Tuple[int, List[bytes], bytes, List[bytes]] = (
               leaf_index, public_keys[leaf_index], signature_wots, auth
               )

           return signature

       def verify(
               self, message: bytes,
               signature: Union[None, Tuple[int, List[bytes], bytes, List[bytes]]],
               ) -> bool:
           if signature is None: return False
           leaf_index, public_keys, signature_wots, auth = signature
           if not self.wots.verify(message, signature_wots, public_keys):
               return False
           nodes: List[bytes] = [hash_function(b"".join(public_keys))]
           index = leaf_index
           for i in range(self.height - 1):
               if index % 2 == 0:
                   nodes.append(MerkleBinaryTree.H(nodes[-1], auth[i]))
               else:
                   nodes.append(MerkleBinaryTree.H(auth[i], nodes[-1]))
               index //= 2
           if nodes[-1] != self.pubkey:
               return False
           return True

   if __name__ == "__main__":
       import secrets
       mss_wots = MSS_BIN_WOTS()

       message = secrets.token_bytes(16)

       signature_1 = mss_wots.sign(message, 2)
       assert mss_wots.verify(message, signature_1)

       signature_2 = mss_wots.sign(message, 2)
       print(mss_wots.verify(message, signature_2))


.. _appendix:mss-ter:

Реализация криптосистемы на основе троичного дерева
---------------------------------------------------


Код для троичного дерева Меркла
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


.. code-block:: python
   :caption: merkle_ternary_tree.py

   from utils import hash_function
   from typing import List
   from wots import WOTS
   from merkle_tree import MerkleTree

   class MerkleTernaryTree(MerkleTree):
       def __init__(self):
           self.nodes = None
           self.height = None

       def tree_build(self, leaves: List[bytes]) -> None:

           self.nodes: List[List[bytes]] = [leaves[:]]
           level_size = len(leaves)

           while level_size > 1:
               new_level = []

               for i in range(0, level_size, 3):
                   first = self.nodes[-1][len(self.nodes[-1]) - level_size + i]
                   second = self.nodes[-1][len(self.nodes[-1]) - level_size + i + 1]
                   third = self.nodes[-1][len(self.nodes[-1]) - level_size + i + 2]

                   new_node = MerkleTernaryTree.H(first, second, third)
                   new_level.append(new_node)

               self.nodes.append(new_level)
               level_size = len(new_level)

           self.nodes.reverse()
           self.height = len(self.nodes)

       def get_size(self) -> int:
           S = 0
           for i in range(len(self.nodes[-1])):
               S += len(self.nodes[-1][i])
           return S

       @staticmethod
       def H(message_1: bytes, message_2: bytes, message_3: bytes) -> bytes:
           return hash_function(message_1 + message_2 + message_3)

   if __name__ == "__main__":
       wots = WOTS()
       keys = [wots.generate_key() for _ in range(81)]
       private_keys: List[List[bytes]] = []
       public_keys_hash: List[bytes] = []

       for i, key in enumerate(keys):
           private_key, public_key = key
           private_keys.append(private_key)
           public_keys_hash.append(hash_function(b"".join(public_key)))

       merkle_tree = MerkleTernaryTree()
       merkle_tree.tree_build(public_keys_hash)
       h = len(merkle_tree.nodes)
       for i in range(h - 1):
           for j in range(len(merkle_tree.nodes[i])):
               assert merkle_tree.nodes[i][j] == hash_function(merkle_tree.nodes[i+1][3*j] + merkle_tree.nodes[i+1][3*j+1] + merkle_tree.nodes[i+1][3*j+2])


Код для реализации подписи MSS на основе W-OTS
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


.. code-block:: python
   :caption: mss_ternary_wots.py

   import math
   from typing import List, Tuple

   from utils import hash_function
   from wots import WOTS
   from mss_wots import MSS_WOTS
   from merkle_ternary_tree import MerkleTernaryTree

   class MSS_TER_WOTS(MSS_WOTS):
       def __init__(self, n: int = 27):

           super().__init__(n=n)
           self.height = math.ceil(math.log(n, 3)) + 1

           tree = MerkleTernaryTree()
           tree.tree_build(self.public_keys_hash)

           self.pubkey = tree.nodes[0][0]

       def sign(
               self, message: bytes, leaf_index: int
               ) -> Tuple[int, List[bytes], bytes, List[bytes]]:
           private_key = self.private_keys[leaf_index]
           if leaf_index > self.n - 1 or leaf_index in self.used_keys:
               raise ValueError("Private key index is invalid")

           signature_wots = self.wots.sign(message, private_key)
           public_keys: List[List[bytes]] = [
               self.wots.get_pubkey_from_privkey(privkey) for privkey in self.private_keys
               ]
           public_keys_hash: List[bytes] = [
               hash_function(b"".join(pubkey)) for pubkey in public_keys
               ]
           merkle_tree = MerkleTernaryTree()
           merkle_tree.tree_build(public_keys_hash)

           auth: List[bytes] = []
           self.used_keys.append(leaf_index)
           index = leaf_index
           for i in range(self.height - 1):
               if index % 3 == 0:
                   auth.append(merkle_tree.nodes[self.height - 1 - i][index + 1])
                   auth.append(merkle_tree.nodes[self.height - 1 - i][index + 2])
               elif index % 3 == 1:
                   auth.append(merkle_tree.nodes[self.height - 1 - i][index - 1])
                   auth.append(merkle_tree.nodes[self.height - 1 - i][index + 1])
               else:
                   auth.append(merkle_tree.nodes[self.height - 1 - i][index - 2])
                   auth.append(merkle_tree.nodes[self.height - 1 - i][index - 1])
               index //= 3

           signature: Tuple[int, List[bytes], bytes, List[bytes]] = (
               leaf_index, public_keys[leaf_index], signature_wots, auth
               )

           return signature

       def verify(
               self, message: bytes,
               signature: Tuple[int, List[bytes], bytes, List[bytes]]
               ) -> bool:
           leaf_index, public_keys, signature_wots, auth = signature
           if not self.wots.verify(message, signature_wots, public_keys):
               return False
           nodes: List[bytes] = [hash_function(b"".join(public_keys))]
           index = leaf_index
           for i in range(self.height - 1):
               if index % 3 == 0:
                   nodes.append(MerkleTernaryTree.H(nodes[-1], auth[2*i], auth[2*i+1]))
               elif index % 3 == 1:
                   nodes.append(MerkleTernaryTree.H(auth[2*i], nodes[-1], auth[2*i+1]))
               else:
                   nodes.append(MerkleTernaryTree.H(auth[2*i], auth[2*i+1], nodes[-1]))
               index //= 3
           if nodes[-1] != self.pubkey:
               return False
           return True

   if __name__ == "__main__":
       import secrets
       mss_wots = MSS_TER_WOTS(n=27)
       message = secrets.token_bytes(16)
       signature = mss_wots.sign(message, 2)
       assert mss_wots.verify(message, signature)

       signature_2 = mss_wots.sign(message, 2)
       print(mss_wots.verify(message, signature_2))


.. _appendix:testing:

Тестирование корректности программной реализации
------------------------------------------------


.. _sec:test_merkle_tree:

Код для тестирования дерева Меркла
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


.. code-block:: python
   :caption: test_merkle_tree.py

   from typing import List
   from utils import hash_function
   from wots import WOTS
   from merkle_binary_tree import MerkleBinaryTree
   from merkle_ternary_tree import MerkleTernaryTree
   from mss_binary_wots import MSS_BIN_WOTS

   def test_merkle_binary_tree():
       wots = WOTS()
       keys = [wots.generate_key() for _ in range(32)]
       private_keys: List[List[bytes]] = []
       public_keys_hash: List[bytes] = []

       for i, key in enumerate(keys):
           private_key, public_key = key
           private_keys.append(private_key)
           public_keys_hash.append(hash_function(b"".join(public_key)))

       merkle_tree = MerkleBinaryTree()
       merkle_tree.tree_build(public_keys_hash)

       h = len(merkle_tree.nodes)
       for i in range(h - 1):
           for j in range(len(merkle_tree.nodes[i])):
               assert merkle_tree.nodes[i][j] == \
                   hash_function(merkle_tree.nodes[i+1][2*j] + merkle_tree.nodes[i+1][2*j+1])
       assert merkle_tree.get_size() == 32 * 32

   def test_merkle_ternary_tree():
       wots = WOTS()
       keys = [wots.generate_key() for _ in range(81)]
       private_keys: List[List[bytes]] = []
       public_keys_hash: List[bytes] = []

       for i, key in enumerate(keys):
           private_key, public_key = key
           private_keys.append(private_key)
           public_keys_hash.append(hash_function(b"".join(public_key)))

       merkle_tree = MerkleTernaryTree()
       merkle_tree.tree_build(public_keys_hash)
       h = len(merkle_tree.nodes)
       for i in range(h - 1):
           for j in range(len(merkle_tree.nodes[i])):
               assert merkle_tree.nodes[i][j] == hash_function(merkle_tree.nodes[i+1][3*j] + merkle_tree.nodes[i+1][3*j+1] + merkle_tree.nodes[i+1][3*j+2])
       assert merkle_tree.get_size() == 81 * 32


.. _sec:test_mss_wots:

Код для тестирования дерева Меркла
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


.. code-block:: python
   :caption: test_mss_wots.py

   from mss_binary_wots import MSS_BIN_WOTS
   from mss_ternary_wots import MSS_TER_WOTS
   import random

   def test_mss_bin_wots_1():
       import secrets
       mss_wots = MSS_BIN_WOTS()

       message = secrets.token_bytes(16)

       signature = mss_wots.sign(message, 0)
       assert mss_wots.verify(message, signature)

   def test_mss_bin_wots_2():
       import secrets
       mss_wots = MSS_BIN_WOTS()

       message = secrets.token_bytes(16)

       signature = mss_wots.sign(message, 1)
       assert mss_wots.verify(message, signature)

   def test_mss_bin_wots_3():
       import secrets
       mss_wots = MSS_BIN_WOTS()

       message = secrets.token_bytes(16)

       signature = mss_wots.sign(message, 2)
       assert mss_wots.verify(message, signature)

   def test_mss_bin_wots_4():
       import secrets
       mss_wots = MSS_BIN_WOTS()

       message = secrets.token_bytes(16)

       signature = mss_wots.sign(message, random.randrange(0, 32))
       assert mss_wots.verify(message, signature)

   def test_mss_ter_wots_1():
       import secrets
       mss_wots = MSS_TER_WOTS()

       message = secrets.token_bytes(16)

       signature = mss_wots.sign(message, 0)
       assert mss_wots.verify(message, signature)

   def test_mss_ter_wots_2():
       import secrets
       mss_wots = MSS_TER_WOTS()

       message = secrets.token_bytes(16)

       signature = mss_wots.sign(message, 1)
       assert mss_wots.verify(message, signature)

   def test_mss_ter_wots_3():
       import secrets
       mss_wots = MSS_TER_WOTS()

       message = secrets.token_bytes(16)

       signature = mss_wots.sign(message, 2)
       assert mss_wots.verify(message, signature)

   def test_mss_ter_wots_4():
       import secrets
       mss_wots = MSS_TER_WOTS()

       message = secrets.token_bytes(16)

       signature = mss_wots.sign(message, random.randrange(0, 32))
       assert mss_wots.verify(message, signature)
