MEMORY
{
  ps7_ram (rwx) : ORIGIN = 0x00000000, LENGTH = 256K
}

SECTIONS
{
  .text : { *(.text*) } > ps7_ram
  .rodata : { *(.rodata*) } > ps7_ram
  .data : { *(.data*) } > ps7_ram
  .bss : { *(.bss*) *(COMMON) } > ps7_ram
}
