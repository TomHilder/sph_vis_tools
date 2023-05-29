# read.py
# Written by Thomas Hilder

"""
Contains TODO: add contents
"""

# import Python libraries
from pathlib import Path
from typing import Tuple

# import packages
import numpy as np
import sarracen as sc


class PhantomDumpCollection:
    """
    Class for collecting Phantom dump files and converting to simple gridded data with
    Sarracen, and storing in Numpy array files.
    """

    # initialise attributes
    _files = None

    # create object
    def __init__(self, path: str, dump_label: str) -> None:
        """
        Create PhantomDumpCollection object.

        Parameters
        ----------
        path : str
            Path to location where Phantom dump files are located.
        dump_label : str
            String contained in the name of each dump file.
        """

        # load files
        self._files = self.get_files(path, dump_label)

        # print message for user
        print("Phantom Dumps loaded successfully.")

    def make_grids(
        self,
        quantities: list[str],
        xlim: Tuple[float, float],
        ylim: Tuple[float, float],
        zlim: Tuple[float, float],
    ) -> None:
        """
        Convert Phantom Dump files into Numpy arrays of gridded data, by interpolating
        over user specified bounds with Sarracen.

        Parameters
        ----------
        quantities : list[str]
            List containing quantities from Phantom dump to be included, e.g. "rho"
        xlim : Tuple[float,float]
            Upper and lower limits along the x-axis for data to be included
        ylim : Tuple[float,float]
            Upper and lower limits along the y-axis for data to be included
        zlim : Tuple[float,float]
            Upper and lower limits along the z-axis for data to be included
        """
        pass

    # convert desired data to arrays using Sarracen
    @staticmethod
    def convert_to_arr(
        file: str,
        quantities: list[str],
        xlim: Tuple[float, float],
        ylim: Tuple[float, float],
        zlim: Tuple[float, float],
    ) -> np.ndarray[float]:
        # loop over quantities

        # read quantity into numpy array with Sarracen
        # concatenate arrays

        # return array
        pass

    # collect files in path using Path objects
    @staticmethod
    def get_files(path: str, label: str) -> list[str]:
        return list(Path(path).glob(f"*{label}*"))

    @property
    def files(self) -> list:
        return self._files

    @files.setter
    def files(self, files: list[str]) -> None:
        # TODO: add some logic here
        self._files = files
