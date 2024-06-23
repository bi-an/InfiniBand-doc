CC = gcc
# `struct addrinfo' is not a part of standard C, but belongs to gnu.
# https://stackoverflow.com/questions/33076175/why-is-struct-addrinfo-defined-only-if-use-xopen2k-is-defined
CFLAGS = -Wall -Wextra -g -ggdb -pedantic -std=gnu99 -I /usr/include/infiniband
# LDFLAGS = -libverbs -lrdmacm -lc
LDFLAGS = -libverbs

all: RDMA_RC_example

RDMA_RC_example: RDMA_RC_example.c
	$(CC) $(CFLAGS) -o RDMA_RC_example RDMA_RC_example.c $(LDFLAGS)

# client: client.c
# 	$(CC) $(CFLAGS) -o client client.c $(LDFLAGS)

clean:
	rm -f RDMA_RC_example
