InfiniBand Code Examples
========================

Installation
------------

To build and run the InfiniBand code, you must have the InfiniBand Hardware
and Utilities installed.

```
TODO
```

Also, you need to have the C++ basic packages installed.

```
TODO
```

Build the code examples
-----------------------


Tips for Debugging
-----------------------

1. Check the number of ports in an IB device

    Use the `ibstat` or `ibv_devinfo` commands.

2. Check InfiniBand devices

    ```bash
    # List the IB devices
    $ lspci | grep -i infiniband
    # See the details of the specified IB device
    $ lspci -s <IB device> -vvv
    ```