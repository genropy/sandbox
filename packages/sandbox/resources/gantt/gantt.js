dojo.declare("gnr.widgets.GanntPane", gnr.widgets.gnrwdg, {

    createcreateContent:function(sourceNode, kw, children){
        sourceNode._("div",{innerHTML:"ciao"})
    }

});


//view_modes=view_modes or 
//
//var gantt = new Gantt("#gantt", tasks, {
//header_height: header_height,
//column_width: column_width,
//step: step,
//view_modes: view_modes.split(','),
//bar_height: bar_height,
//bar_corner_radius: bar_corner_radius,
//arrow_curve: arrow_curve,
//padding: padding,
//view_mode: view_mode,   
//date_format: date_format,
//custom_popup_html: custom_popup_html
//});""", gantt_id=gantt_id, tasks=tasks, **opt_kwargs