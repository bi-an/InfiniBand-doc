Glossary in InfiniBand
======================

.. * `CQ` - Complete Queue 完成队列
.. * `WQ` - Work Queue 工作队列
.. * `WR` - Work Request 工作请求
.. * `QP` - Queue Pairs 队列对（Send-Receive）
.. * `SQ` - Send Queue 发送队列
.. * `RQ` - Receive Queue 接收队列
.. * `PD` - Protection Domain 保护域，将QP和MR结合在一起
.. * `MR` - Memory Region 内存区域。一块经注册过的且本地网卡可以读写的内存区域。包含R_Key和L_Key。
.. * `SGE` - Scatter/Gather Elements 分散/聚集元素。
.. * `R_Key` - Remote Key
.. * `L_Key` - Local Key
.. * `CA` - (Host) Channel Adapter, an inifiniband network interface card.
.. * `NIC` - Network Interface Card 网卡。
.. * `LID` - Local Identifier.
.. * `CM` - Connection Manager.

.. csv-table::
    :header: "Term", "Description"
    :widths: 10,70
    :class: tight-table

    "Access Layer", "Low level operating system infrastructure (plumbing) used
    for accessing the interconnect fabric (VPI™, InfiniBand®, Ethernet, FCoE).
    It includes all basic transport services needed to support upper level
    network protocols, middleware, and management agents."
