8.2 发送、接收、RDMA 读取、RDMA 写入的代码
---------------------------------------------

示例代码
^^^^^^^^^^^^^^^

   .. container:: toggle

       .. container:: header

           .. container:: btn btn-info

               RDMA_RC_example.c (show/hide)

       .. literalinclude:: ../../../code/8_ibv_examples/01_RMDA_RC/RDMA_RC_example.c
               :language: cpp
               :linenos:
               :lineno-start: 1
               :lines: 1-

运行演示
^^^^^^^^^^^

#. 启动服务端

   .. code-block:: shell

       ./RDMA_RC_example

#. 启动客户端

   .. code-block:: shell

       ./RDMA_RC_example localhost

#. 运行结果

   服务端输出示例

   .. container:: toggle

       .. container:: header

           .. container:: btn btn-info

               server output (show/hide)

       .. literalinclude:: ../../../code/8_ibv_examples/01_RMDA_RC/result_example/server.out

   客户端输出示例

   .. container:: toggle

       .. container:: header

           .. container:: btn btn-info

               client output (show/hide)

       .. literalinclude:: ../../../code/8_ibv_examples/01_RMDA_RC/result_example/client.out
