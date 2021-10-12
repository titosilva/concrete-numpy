"""Module to hold the result of compilation."""

from pathlib import Path
from typing import List, Optional, Union

from zamalang import CompilerEngine

from .debugging import draw_graph, get_printable_graph
from .operator_graph import OPGraph


class FHECircuit:
    """Class which is the result of compilation."""

    opgraph: OPGraph
    engine: CompilerEngine

    def __init__(self, opgraph: OPGraph, engine: CompilerEngine):
        self.opgraph = opgraph
        self.engine = engine

    def __str__(self):
        return get_printable_graph(self.opgraph, show_data_types=True)

    def draw(
        self,
        show: bool = False,
        vertical: bool = True,
        save_to: Optional[Path] = None,
    ) -> str:
        """Draw operation graph of the circuit and optionally save/show the drawing.

        Args:
            show (bool): if set to True, the drawing will be shown using matplotlib
            vertical (bool): if set to True, the orientation will be vertical
            save_to (Optional[Path]): if specified, the drawn graph will be saved to this path;
                otherwise it will be saved to a temporary file

        Returns:
            str: path of the file where the drawn graph is saved

        """

        return draw_graph(self.opgraph, show, vertical, save_to)

    def run(self, *args: List[Union[int, List[int]]]) -> int:
        """Encrypt, evaluate, and decrypt the inputs on the circuit.

        Args:
            *args (List[Union[int, List[int]]]): inputs to the circuit

        Returns:
            int: homomorphic evaluation result

        """

        return self.engine.run(*args)