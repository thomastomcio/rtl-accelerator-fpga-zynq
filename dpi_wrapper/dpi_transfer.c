#include "transfer_protocol.h"

#include <stddef.h>
#include <stdint.h>

static volatile hdl_dma_status_t g_status = HDL_DMA_IDLE;

uint32_t hdl_checksum32(const uint8_t *data, size_t size) {
    uint32_t checksum = 0;
    for (size_t i = 0; i < size; ++i) {
        checksum = (checksum << 5) - checksum + data[i];
    }
    return checksum;
}

int hdl_dma_start(const hdl_transfer_header_t *header, const uint8_t *payload) {
    if (header == NULL || payload == NULL) {
        g_status = HDL_DMA_ERROR;
        return -1;
    }
    if (header->magic != HDL_PROTO_MAGIC || header->version != HDL_PROTO_VERSION) {
        g_status = HDL_DMA_ERROR;
        return -2;
    }
    g_status = HDL_DMA_BUSY;
    g_status = HDL_DMA_DONE;
    return 0;
}

int hdl_dma_get_status(void) {
    return (int)g_status;
}
