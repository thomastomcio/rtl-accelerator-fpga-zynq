#include "axi_registers.h"

#include <stdint.h>

static inline void mmio_write(uint32_t addr, uint32_t value) {
    *(volatile uint32_t *)addr = value;
}

static inline uint32_t mmio_read(uint32_t addr) {
    return *(volatile uint32_t *)addr;
}

void accel_start_dma(uint32_t token) {
    mmio_write(AXI_CTRL_BASE + AXI_REG_DMA_START, token);
}

uint32_t accel_get_dma_status(void) {
    return mmio_read(AXI_CTRL_BASE + AXI_REG_DMA_STATUS);
}

uint32_t accel_read_signal(void) {
    return mmio_read(AXI_CTRL_BASE + AXI_REG_SIGNAL_READ);
}
