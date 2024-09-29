##############################################################################
# Author: SINAPSYS GLOBAL SA || MASTERCORE SAS
# Copyleft: 2022-Present.
# License LGPL-3.0 or later (http: //www.gnu.org/licenses/lgpl.html).
#
#
###############################################################################
from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    disable_islr = fields.Boolean("No sujeto a ISLR")
