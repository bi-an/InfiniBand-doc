3.2 传输模式
----------------

建立 QP 时，您可以选择多种不同的传输模式。下表显示了每种模式下可用的操作。此 API 不支持 RD。

.. csv-table::
    :header: 操作, UD, UC, RC, RD
    :class: tight-class

    发送（带立即数）, +, +, +, +
    接收, +, +, +, +
    RDMA 写（带立即数）, , +, +, +
    RDMA 读, , , +, +
    原子：Fetch and Add / Cmp and Swap, , , +, +
    最大消息大小, MTU, 1 GB, 1 GB, 1 GB
