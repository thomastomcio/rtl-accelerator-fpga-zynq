#ifndef HDL_TRANSFER_PROTOCOL_H
#define HDL_TRANSFER_PROTOCOL_H

#include <stdint.h>

#define HDL_PROTO_MAGIC 0x48444C49u
#define HDL_PROTO_VERSION 0x0001u
#define HDL_DESIGN_NAME_MAX 64u
#define HDL_MAX_CHUNK_SIZE 4096u

typedef struct {
    uint32_t magic;
    uint16_t version;
    uint16_t flags;
    char design_name[HDL_DESIGN_NAME_MAX];
    uint32_t module_count;
    uint32_t ir_size_bytes;
    uint32_t chunk_size;
    uint32_t checksum;
} hdl_transfer_header_t;

typedef enum {
    HDL_DMA_IDLE = 0,
    HDL_DMA_BUSY = 1,
    HDL_DMA_DONE = 2,
    HDL_DMA_ERROR = 3
} hdl_dma_status_t;

#endif
