import csv
import json
import os
from io import TextIOWrapper


class FileService:
    def __init__(self, CONFIG):
        self.CONFIG = CONFIG

    @staticmethod
    def fullPath(path: str) -> str:
        return os.path.abspath(path)
    
    def checkIfFileExists(self, filename: str):
        return (filename in os.listdir(self.CONFIG["inputFolder"]))

    @staticmethod
    def createIfEmpty(path: str, foldername: str):
        if foldername not in os.listdir(path):
            os.mkdir(os.path.join(path, foldername))

    def getFile(self, filename: str) -> TextIOWrapper:
        return open(self.CONFIG["inputFolder"] + filename, mode="r", encoding="utf-8")

    @staticmethod
    def getFileAsString(path: str) -> str:
        with open(path, mode="r", encoding="utf-8") as f:
            return f.read()
        
    def readJSON(self, filename, encoding:str="utf-8") -> list[dict] | dict:
        with open(self.CONFIG["inputPath"] + filename, encoding=encoding) as f:
            return json.load(f)

    @staticmethod
    def getAllFilePaths(path: str) -> list[str]:
        return list(map(lambda x: os.path.join(path, x), os.listdir(path)))

    def getAllFileNamesRecursive(self, path: str) -> list[str]:
        folders = list(filter(lambda x: os.path.isdir(x), self.getAllFilePaths(path)))
        files = list(filter(lambda x: os.path.isfile(x), self.getAllFilePaths(path)))

        if folders:
            for folder in folders:
                files.extend(self.getAllFileNamesRecursive(folder))

        return files

    def writeCSV(self, filename: str, obj: list[dict]) -> None:
        self.createIfEmpty(self.CONFIG["outputPath"], "csv")
        with open(
            os.path.join(self.CONFIG["outputPath"], "csv", filename),
            mode="w",
            encoding="utf-8",
        ) as f:
            csv.writer(f, lineterminator="\n").writerow(list(obj[0].keys()))
            csv.writer(f, lineterminator="\n").writerows(list(map(lambda x: list(x.values()), obj)))

    def writeJSON(self, filename: str, obj) -> None:
        # self.createIfEmpty(self.CONFIG["outputPath"], "json")
        with open(
            # os.path.join(self.CONFIG["outputPath"], "json", filename),
            os.path.join(self.CONFIG["outputPath"], filename),
            mode="w",
            encoding="utf-8",
        ) as f:
            json.dump(obj, f, indent=4, ensure_ascii=False)

    def continuedWriteFile(self, filename: str, lines: list[str]) -> None:
        self.createIfEmpty(self.CONFIG["outputPath"], "txt")
        with open(
            os.path.join(self.CONFIG["outputPath"], "txt", filename),
            mode="a",
            encoding="utf-8",
        ) as f:
            f.writelines(lines)
