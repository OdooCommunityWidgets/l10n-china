# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: Luke Branch <odoocommunitywidgets@gmail.com>
#    Copyright 2015 Odoo Community Widgets
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': '10n-HK Delivery Carrier Hong Kong SpeedPost',
    'version': '8.0.0.2.0',
    'author': "Luke Branch,Odoo Community Association (OCA)",
    'maintainer': 'Luke Branch',
    'category': 'Localization,Inventory',
    'depends': [
        'base',
        'delivery'        
    ],
    'description': """
Delivery Carrier 10n-HK Hong Kong SpeedPost
===========================================
Description
-----------
* Adds Hong Kong SpeedPost Delivery rates grid for shipments originating in Hong Kong for delivery worldwide using local public rates found in the SpeedPost Rate Plan (http://www.hongkongpost.hk/filemanager/common/forms/pos15a_posting_guide.pdf).

Contributors
------------
* Luke BRANCH <odoocommunitywidgets@gmail.com>
----
    """,
    'website': 'https://github.com/odoocommunitywidgets',
    'data': [
        'rates/delivery_rates_base.xml',
        'rates/delivery_rates_af.xml',
        'rates/delivery_rates_al.xml',
        'rates/delivery_rates_dz.xml',
        'rates/delivery_rates_ad.xml',
        'rates/delivery_rates_ao.xml',
        'rates/delivery_rates_ai.xml',
        'rates/delivery_rates_ag.xml',
        'rates/delivery_rates_ar.xml',
        'rates/delivery_rates_am.xml',
        'rates/delivery_rates_aw.xml',
        'rates/delivery_rates_au.xml',
    ],
    'tests': [],
    'installable': False,
    'auto_install': False,
    'license': 'AGPL-3',
    'application': False,
}
