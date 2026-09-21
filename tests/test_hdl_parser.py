import tempfile
import textwrap
import unittest
from pathlib import Path

from hdl_parser import parse_project


class HDLParserTest(unittest.TestCase):
    def test_parse_hierarchy_and_behavioral_blocks(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            (root / "defs.svh").write_text("`define WIDTH 8\n", encoding="utf-8")
            (root / "child.sv").write_text(
                textwrap.dedent(
                    """
                    module child(input logic clk, output logic y);
                      logic r;
                      always_ff @(posedge clk) begin
                        r <= ~r;
                      end
                      assign y = r;
                    endmodule
                    """
                ),
                encoding="utf-8",
            )
            (root / "top.sv").write_text(
                textwrap.dedent(
                    """
                    `include "defs.svh"
                    module top(input logic clk, output logic y);
                      child u_child(.clk(clk), .y(y));
                    endmodule
                    """
                ),
                encoding="utf-8",
            )

            ir = parse_project(str(root))

            self.assertIn("top", ir["modules"])
            self.assertIn("child", ir["modules"])
            self.assertIn("defs.svh", ir["includes"])
            self.assertIn("WIDTH", ir["defines"])
            self.assertIn("child", ir["module_hierarchy"].get("top", []))
            self.assertTrue(ir["modules"]["child"]["always_blocks"])


if __name__ == "__main__":
    unittest.main()
