# -*- coding: utf-8 -*-
from affinitic.db.mapper import MappedClassBase
from gites.pivot.db import DeclarativeBase, session


class PivotMappedClassBase(DeclarativeBase, MappedClassBase):
    __abstract__ = True

    @classmethod
    def _session(self):
        return session()
