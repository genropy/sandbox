# -*- coding: utf-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.web.gnrwebstruct import struct_method
from gnr.core.gnrdecorator import public_method,extract_kwargs

class Gantt(BaseComponent):
    js_requires='gantt/lib/frappe-gantt.min,gantt/gantt'
    css_requires='gantt/lib/frappe-gantt'

    @struct_method
    def gnt_ganttPane(self, parent, gantt_id=None, tasks=None, **kwargs):
        parent.child("ganttpane", gantt_id=gantt_id, tasks=tasks, **kwargs)
    #    pane = parent.contentPane(**kwargs)
    #    pane.svg(id=gantt_id)
    #    pane.dataController("""view_modes=viem
#
#
    #                            var gantt = new Gantt("#gantt", tasks, {
    #                            header_height: header_height,
    #                            column_width: column_width,
    #                            step: step,
    #                            view_modes: view_modes.split(','),
    #                            bar_height: bar_height,
    #                            bar_corner_radius: bar_corner_radius,
    #                            arrow_curve: arrow_curve,
    #                            padding: padding,
    #                            view_mode: view_mode,   
    #                            date_format: date_format,
    #                            custom_popup_html: custom_popup_html
    #                            });""", gantt_id=gantt_id, tasks=tasks, **opt_kwargs)