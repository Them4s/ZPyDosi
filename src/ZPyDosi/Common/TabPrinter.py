from ..Common.utils_general import *
from ..Prints.PrintnSave import *
import numpy as np
class TabPrinter:
    """
    Utility class for building and formatting tabular text output.

    This class incrementally collects column-based data associated with a
    predefined set of keys and produces a formatted, aligned text table.
    Column widths are automatically adjusted based on content and header
    lengths.
    """
    def __init__(self, l_key, sep_size=1):
        """
        Initialize a tabular printer with predefined column keys.

        Parameters
        ----------
        l_key : list of str
            Ordered list of column names defining the table structure.
        sep_size : int, optional
            Number of spaces added as padding between columns.
        """
        self.l_key = l_key
        self.d_key2data = {}
        self.sep_size = sep_size
        for key in self.l_key:
            self.d_key2data[key] = []
            
    def add(self,key,val):
        """
        Add a value to a specified column.

        The value is appended to the column corresponding to ``key``.
        Other columns are padded as needed to maintain row alignment.

        Parameters
        ----------
        key : str
            Column key to which the value should be added.
        val : object
            Value to insert into the table. It is converted to a string
            before storage.
        """
        if key not in self.d_key2data:
            print("Error - TabPrinter - add - key not found:",key," not in "+" ".join(self.d_key2data.keys()))
            exit()
        for other_key in self.d_key2data.keys():
            if len(self.d_key2data[key]) > len(self.d_key2data[other_key]):
                self.d_key2data[other_key] += [""]
        self.d_key2data[key] += [str(val)]
        
        
    def get_text(self):
        """
        Generate the formatted tabular text output.

        The method aligns all columns based on the maximum width of their
        headers and values, and returns the resulting table as a single
        string suitable for printing or logging.

        Returns
        -------
        str
            Formatted table represented as a multi-line string.
        """
        maxi = max(map(lambda key_l:len(key_l[1]), self.d_key2data.items()))
        for key in self.d_key2data.keys():
            if len(self.d_key2data[key]) < maxi:
                self.d_key2data[key] += [""]
        l_size = lmap(lambda key: self.sep_size+max(len(key),max(map(lambda s:len(s), self.d_key2data[key]))), self.l_key)
        out = "".join(lmap(lambda i: aff(self.l_key[i], l_size[i]), range(len(self.l_key))))
        for il in range(len(self.d_key2data[self.l_key[0]])):
            out += "\n"
            out += "".join(lmap(lambda i: aff(self.d_key2data[self.l_key[i]][il], l_size[i]), range(len(self.l_key))))
        return out