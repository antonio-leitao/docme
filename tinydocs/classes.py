from numpydoc.docscrape import FunctionDoc, ClassDoc
from dataclasses import dataclass

@dataclass
class Routine:
    id: str
    name: str
    signature: str
    warnings: list
    summary: str
    parameters: list
    returns: list
    references: list
    examples: list


@dataclass
class ClassObj:
    id: str
    name: str
    signature: str
    warnings: list
    summary: str
    parameters: list
    returns: list
    references: list
    attributes: list
    methods: list[Routine]
    examples: list


@dataclass
class Module:
    id: str
    name: str
    doc: str
    classes: list[ClassDoc]
    routines: list[FunctionDoc]


@dataclass
class Package:
    modules: list[Module] | None
    data: dict