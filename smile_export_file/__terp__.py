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
    "name" : "Export File",
    "version" : "1.0",
    "author" : "Smile",
    "website": 'http://www.smile.fr',
    "category" : "Tools",
    "description": """Export data in flat file

Principle

* Define a file template
* Choose storage methods
    * create an attachment
    * upload in FTP server
    * send by email

Suggestions & Feedback to: corentin.pouhet-brunerie@smile.fr
""",
    "depends" : ['smile_export'],
    "init_xml" : [],
    "update_xml": [
        'export_file_view.xml',
        'export_view.xml',
        'security/ir.model.access.csv',
    ],
    "demo_xml" : [],
    "installable": True,
    "active": False,
}
