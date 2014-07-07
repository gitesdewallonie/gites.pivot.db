# encoding: utf-8
"""
gites.pivot.db

Created by mpeeters
Licensed under the GPL license, see LICENCE.txt for more details.
Copyright by Affinitic sprl
"""

from zope.configuration import xmlconfig


def parseZCML(package, file='configure.zcml'):
    context = xmlconfig._getContext()
    xmlconfig.include(context, file, package)
    context.execute_actions()
