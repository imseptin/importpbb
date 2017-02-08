# -*- coding: utf-8 -*-
"""
/***************************************************************************
 importbidang
                                 A QGIS plugin
 Plugin digunakan untuk memasukkan data bidang dari temporary shp ke database bidang
                             -------------------
        begin                : 2017-02-07
        copyright            : (C) 2017 by Septin Mulatsih Rezki
        email                : septinmulatsihrezki@gmail.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load importbidang class from file importbidang.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .import_bidang import importbidang
    return importbidang(iface)
