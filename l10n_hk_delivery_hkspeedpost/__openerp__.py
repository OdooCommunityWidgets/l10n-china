# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: Luke Branch <odoocommunitywidgets@gmail.com>
#    Copyright © 2015 Odoo Community Widgets
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
    'category': 'Localization',
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
        # Country rates ordered by ISO two digit codes
        # Line numbers in comments based on delivery grid pdf from HK SpeedPost
        'rates/delivery_rates_base.xml',  # base for adding delivery product and carrier
        'rates/delivery_rates_af.xml',    #01
        'rates/delivery_rates_al.xml',    #02
#        'rates/delivery_rates_dz.xml',    #03
        'rates/delivery_rates_ad.xml',    #04
#        'rates/delivery_rates_ao.xml',    #05
#        'rates/delivery_rates_ai.xml',    #06
#        'rates/delivery_rates_ag.xml',    #07
#        'rates/delivery_rates_ar.xml',    #08
#        'rates/delivery_rates_am.xml',    #09
#        'rates/delivery_rates_aw.xml',    #10
#        'rates/delivery_rates_au.xml',    #11
#        'rates/delivery_rates_at.xml',    #12
#        'rates/delivery_rates_az.xml',    #13
#        'rates/delivery_rates_bs.xml',    #14
#        'rates/delivery_rates_bh.xml',    #15
#        'rates/delivery_rates_bd.xml',    #16
#        'rates/delivery_rates_bb.xml',    #17
#        'rates/delivery_rates_by.xml',    #18
#        'rates/delivery_rates_be.xml',    #19
#        'rates/delivery_rates_bz.xml',    #20
#        'rates/delivery_rates_bj.xml',    #21
#        'rates/delivery_rates_bm.xml',    #22
#        'rates/delivery_rates_bt.xml',    #23
#        'rates/delivery_rates_bo.xml',    #24
#        'rates/delivery_rates_ba.xml',    #25
#        'rates/delivery_rates_bw.xml',    #26
#        'rates/delivery_rates_br.xml',    #27
#        'rates/delivery_rates_bn.xml',    #28
#        'rates/delivery_rates_bg.xml',    #29
#        'rates/delivery_rates_bf.xml',    #30
#        'rates/delivery_rates_bi.xml',    #31
#        'rates/delivery_rates_kh.xml',    #32
#        'rates/delivery_rates_cm.xml',    #33
        'rates/delivery_rates_ca.xml',    #34
#        'rates/delivery_rates_cv.xml',    #35
#        'rates/delivery_rates_fm.xml',    #36
#        'rates/delivery_rates_pw.xml',    #37
#        'rates/delivery_rates_ky.xml',    #38
#        'rates/delivery_rates_cf.xml',    #39
#        'rates/delivery_rates_td.xml',    #40
#        'rates/delivery_rates_cl.xml',    #41
#        'rates/delivery_rates_cn.xml',    #42
#        'rates/delivery_rates_co.xml',    #43
#        'rates/delivery_rates_cd.xml',    #44
#        'rates/delivery_rates_cg.xml',    #45
#        'rates/delivery_rates_cr.xml',    #46
#        'rates/delivery_rates_ci.xml',    #47
#        'rates/delivery_rates_hr.xml',    #48
#        'rates/delivery_rates_cu.xml',    #49
#        'rates/delivery_rates_cy.xml',    #50
#        'rates/delivery_rates_cz.xml',    #51
#        'rates/delivery_rates_dk.xml',    #52
#        'rates/delivery_rates_dj.xml',    #53
#        'rates/delivery_rates_dm.xml',    #54
#        'rates/delivery_rates_do.xml',    #55
#        'rates/delivery_rates_tp.xml',    #56
#        'rates/delivery_rates_ec.xml',    #57
#        'rates/delivery_rates_eg.xml',    #58
#        'rates/delivery_rates_sv.xml',    #59
#        'rates/delivery_rates_gq.xml',    #60
#        'rates/delivery_rates_er.xml',    #61
#        'rates/delivery_rates_ee.xml',    #62
#        'rates/delivery_rates_et.xml',    #63
#        'rates/delivery_rates_fo.xml',    #64
#        'rates/delivery_rates_fj.xml',    #65
#        'rates/delivery_rates_fi.xml',    #66
        'rates/delivery_rates_fr.xml',    #67
#        'rates/delivery_rates_gf.xml',    #68
#        'rates/delivery_rates_pf.xml',    #69
#        'rates/delivery_rates_ga.xml',    #70
#        'rates/delivery_rates_gm.xml',    #71
#        'rates/delivery_rates_ps.xml',    #72
#        'rates/delivery_rates_ge.xml',    #73
#        'rates/delivery_rates_de.xml',    #74
#        'rates/delivery_rates_gh.xml',    #75
#        'rates/delivery_rates_gi.xml',    #76
#        'rates/delivery_rates_gr.xml',    #77
#        'rates/delivery_rates_gl.xml',    #78
#        'rates/delivery_rates_gd.xml',    #79
#        'rates/delivery_rates_gp.xml',    #80
#        'rates/delivery_rates_gu.xml',    #81
#        'rates/delivery_rates_gt.xml',    #82
#        'rates/delivery_rates_gn.xml',    #83
#        'rates/delivery_rates_gw.xml',    #84
#        'rates/delivery_rates_gy.xml',    #85
#        'rates/delivery_rates_ht.xml',    #86
#        'rates/delivery_rates_hn.xml',    #87
#        'rates/delivery_rates_hu.xml',    #88
#        'rates/delivery_rates_is.xml',    #89
#        'rates/delivery_rates_in.xml',    #90
#        'rates/delivery_rates_id.xml',    #91
#        'rates/delivery_rates_ir.xml',    #92
#        'rates/delivery_rates_iq.xml',    #93
#        'rates/delivery_rates_ie.xml',    #94
#        'rates/delivery_rates_il.xml',    #95
#        'rates/delivery_rates_it.xml',    #96
#        'rates/delivery_rates_jm.xml',    #97
        'rates/delivery_rates_jp.xml',    #98
#        'rates/delivery_rates_jo.xml',    #99
#        'rates/delivery_rates_kz.xml',    #100
#        'rates/delivery_rates_ke.xml',    #101
#        'rates/delivery_rates_ki.xml',    #102
#        'rates/delivery_rates_kp.xml',    #103
#        'rates/delivery_rates_kr.xml',    #104
#        'rates/delivery_rates_kw.xml',    #105
#        'rates/delivery_rates_kg.xml',    #106
#        'rates/delivery_rates_la.xml',    #107
#        'rates/delivery_rates_lv.xml',    #108
#        'rates/delivery_rates_lb.xml',    #109
#        'rates/delivery_rates_ls.xml',    #110
#        'rates/delivery_rates_lr.xml',    #111
#        'rates/delivery_rates_ly.xml',    #112
#        'rates/delivery_rates_li.xml',    #113
#        'rates/delivery_rates_lt.xml',    #114
#        'rates/delivery_rates_lu.xml',    #115
#        'rates/delivery_rates_mo.xml',    #116
#        'rates/delivery_rates_mk.xml',    #117
#        'rates/delivery_rates_mg.xml',    #118
#        'rates/delivery_rates_mw.xml',    #119
#        'rates/delivery_rates_my.xml',    #120
#        'rates/delivery_rates_mv.xml',    #121
#        'rates/delivery_rates_ml.xml',    #122
#        'rates/delivery_rates_mt.xml',    #123
#        'rates/delivery_rates_mp.xml',    #124
#        'rates/delivery_rates_mh.xml',    #125
#        'rates/delivery_rates_mq.xml',    #126
#        'rates/delivery_rates_mr.xml',    #127
#        'rates/delivery_rates_mu.xml',    #128
#        'rates/delivery_rates_mx.xml',    #129
#        'rates/delivery_rates_md.xml',    #130
#        'rates/delivery_rates_mc.xml',    #131
#        'rates/delivery_rates_mn.xml',    #132
#        'rates/delivery_rates_me.xml',    #133
#        'rates/delivery_rates_ms.xml',    #134
#        'rates/delivery_rates_ma.xml',    #135
#        'rates/delivery_rates_mz.xml',    #136
#        'rates/delivery_rates_mm.xml',    #137
#        'rates/delivery_rates_na.xml',    #138
#        'rates/delivery_rates_nr.xml',    #139
#        'rates/delivery_rates_np.xml',    #140
#        'rates/delivery_rates_nl.xml',    #141
#        'rates/delivery_rates_an.xml',    #142
#        'rates/delivery_rates_nc.xml',    #143
#        'rates/delivery_rates_nz.xml',    #144
#        'rates/delivery_rates_ck.xml',    #145
#        'rates/delivery_rates_ni.xml',    #146
#        'rates/delivery_rates_ne.xml',    #147
#        'rates/delivery_rates_ng.xml',    #148
#        'rates/delivery_rates_nf.xml',    #149
#        'rates/delivery_rates_no.xml',    #150
#        'rates/delivery_rates_om.xml',    #151
#        'rates/delivery_rates_pk.xml',    #152
#        'rates/delivery_rates_pa.xml',    #153
#        'rates/delivery_rates_pg.xml',    #154
#        'rates/delivery_rates_py.xml',    #155
#        'rates/delivery_rates_pe.xml',    #156
#        'rates/delivery_rates_ph.xml',    #157
#        'rates/delivery_rates_pl.xml',    #158
#        'rates/delivery_rates_pt.xml',    #159
#        'rates/delivery_rates_pr.xml',    #160
#        'rates/delivery_rates_qa.xml',    #161
#        'rates/delivery_rates_re.xml',    #162
#        'rates/delivery_rates_ro.xml',    #163
#        'rates/delivery_rates_ru.xml',    #164
#        'rates/delivery_rates_rw.xml',    #165
#        'rates/delivery_rates_ws.xml',    #166
#        'rates/delivery_rates_sm.xml',    #167
#        'rates/delivery_rates_st.xml',    #168
#        'rates/delivery_rates_sa.xml',    #169
#        'rates/delivery_rates_sn.xml',    #170
#        'rates/delivery_rates_rs.xml',    #171
#        'rates/delivery_rates_sc.xml',    #172
#        'rates/delivery_rates_sl.xml',    #173
#        'rates/delivery_rates_sg.xml',    #174
#        'rates/delivery_rates_sk.xml',    #175
#        'rates/delivery_rates_si.xml',    #176
#        'rates/delivery_rates_sb.xml',    #177
#        'rates/delivery_rates_za.xml',    #178
#        'rates/delivery_rates_es.xml',    #179
#        'rates/delivery_rates_lk.xml',    #180
#        'rates/delivery_rates_kn.xml',    #181
#        'rates/delivery_rates_lc.xml',    #182
#        'rates/delivery_rates_vc.xml',    #183
#        'rates/delivery_rates_sd.xml',    #184
#        'rates/delivery_rates_sr.xml',    #185
#        'rates/delivery_rates_sz.xml',    #186
#        'rates/delivery_rates_se.xml',    #187
#        'rates/delivery_rates_ch.xml',    #188
#        'rates/delivery_rates_sy.xml',    #189
#        'rates/delivery_rates_tw.xml',    #190
#        'rates/delivery_rates_tj.xml',    #191
#        'rates/delivery_rates_tz.xml',    #192
#        'rates/delivery_rates_th.xml',    #193
#        'rates/delivery_rates_tg.xml',    #194
#        'rates/delivery_rates_to.xml',    #195
#        'rates/delivery_rates_vg.xml',    #196
#        'rates/delivery_rates_tt.xml',    #197
#        'rates/delivery_rates_tn.xml',    #198
#        'rates/delivery_rates_tr.xml',    #199
#        'rates/delivery_rates_tm.xml',    #200
#        'rates/delivery_rates_tc.xml',    #201
#        'rates/delivery_rates_tv.xml',    #202
#        'rates/delivery_rates_ug.xml',    #203
#        'rates/delivery_rates_ua.xml',    #204
#        'rates/delivery_rates_ae.xml',    #205
        'rates/delivery_rates_gb.xml',    #206
        'rates/delivery_rates_us.xml',    #207
#        'rates/delivery_rates_uy.xml',    #208
#        'rates/delivery_rates_uz.xml',    #209
#        'rates/delivery_rates_vu.xml',    #210
#        'rates/delivery_rates_ve.xml',    #211
#        'rates/delivery_rates_vn.xml',    #212
#        'rates/delivery_rates_vi.xml',    #213
#        'rates/delivery_rates_ws.xml',    #214
#        'rates/delivery_rates_ye.xml',    #215
#        'rates/delivery_rates_zm.xml',    #216
#        'rates/delivery_rates_zw.xml',    #217
    ],
    'tests': [],
    'installable': True,
    'auto_install': False,
    'license': 'AGPL-3',
    'application': False,
}
