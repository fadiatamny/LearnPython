
import pandas as pd
import os.path as path


class MatrixException(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message: str = message

    def __str__(self) -> str:
        return f'{self.message}'


class Matrix:
    def __init__(self, fileName: str):
        if not path.isfile(fileName):
            raise MatrixException('File does not exist.')
        if not fileName.endswith('.json'):
            raise MatrixException('Incorrect file format.')

        self.data = pd.read_json(fileName)

    def __find(self, propertyname: str):
        if not propertyname in self.data.columns:
            raise MatrixException('Property doesnt exist in the data.')
        if not pd.api.types.is_numeric_dtype(self.data[propertyname]):
            raise MatrixException('DATA MISMATCH - property is not a number')

        return self.data[propertyname]

    def average(self, propertyname: str) -> float:
        res = self.__find(propertyname)
        return res.mean()

    def max(self, propertyname: str) -> int:
        res = self.__find(propertyname)
        return res.max()

    def min(self, propertyname: str) -> int:
        res = self.__find(propertyname)
        return res.min()

    def total(self, propertyname: str) -> int:
        res = self.__find(propertyname)
        return res.sum()
