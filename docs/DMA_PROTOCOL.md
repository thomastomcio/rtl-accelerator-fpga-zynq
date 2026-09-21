# DMA Protocol

`dpi_wrapper/transfer_protocol.h` defines the packet format.

Header fields:
- magic/version
- design name
- module count
- IR payload size
- chunk size
- checksum

Payload is zlib-compressed IR bytes created by `dpi_wrapper/this.py`.
