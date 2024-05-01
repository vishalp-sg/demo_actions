# -*- coding: utf-8 -*-
import werkzeug
from werkzeug.exceptions import NotFound, Forbidden

from odoo import http
from odoo.http import request
from odoo.addons.portal.controllers.mail import _check_special_access, PortalChatter
from odoo.tools import plaintext2html, html2plaintext


class SlidesPortalChatter(PortalChatter):

    @http.route(['/mail/chatter_post'], type='json', methods=['POST'], auth='public', website=True)
    def portal_chatter_post(self, res_model, res_id, message, **kw):
        result = super(SlidesPortalChatter, self).portal_chatter_post(res_model, res_id, message, **kw)
        if result and res_model == 'slide.channel':
            rating_value = kw.get('rating_value', False)
            slide_channel = request.env[res_model].sudo().browse(int(res_id))
            if rating_value and slide_channel and request.env.user.partner_id.id == int(kw.get('pid')):
                # apply karma gain rule only once
                request.env.user.add_karma(slide_channel.karma_gen_channel_rank)
            result.update({
                'default_rating_value': rating_value,
                'rating_avg': slide_channel.rating_avg,
                'rating_count': slide_channel.rating_count,
                'force_submit_url': result.get('default_message_id') and '/slides/mail/update_comment',
            })

            lead_vals = {
                'name': message,
                'message_id': result.get('default_message_id'),
                'feedback_ratings': float(rating_value),
                'model': res_model,
                'res_id': res_id
            }
            if request.env.user.has_group('base.group_public'):
                lead_vals.update({
                    'partner_id': False,
                    'email_from': False,
                    'phone': False,
                    'user_id': False
                })
            else:
                lead_vals.update({
                    'partner_id': request.env.user.partner_id.id,
                    'email_from': request.env.user.partner_id.email,
                    'phone': request.env.user.partner_id.phone,
                    'user_id': request.env.user.sudo().id
                })
            request.env['crm.lead'].sudo().create(lead_vals)
        return result
