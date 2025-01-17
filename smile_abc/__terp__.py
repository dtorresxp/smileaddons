# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution    
#    Copyright (C) 2010 Smile (<http://www.smile.fr>). All Rights Reserved
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    "name" : "Smile ABC",
    "version" : "1.0",
    "author" : "Smile",
    "website": 'http://www.smile.fr',
    "category" : "Smile ABC",
    "description": "Smile ABC",
    "depends" : [],
    "init_xml" : [],
    "update_xml": [
        'smile_abc_view.xml',
        'security/smile_abc_security.xml',
        'security/ir.model.access.csv',
    ],
    "demo_xml" : [],
    "installable": True,
    "active": False,
    "certificate": '',
}
