#!/usr/bin/env bash
set -euo pipefail
vivado -mode batch -source ../zynq_ps/vivado_build.tcl
