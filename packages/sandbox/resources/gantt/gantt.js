dojo.declare("gnr.widgets.GanttPane", gnr.widgets.gnrwdg, {
    createContent:function(sourceNode, kw, children){
        let opt_kw = objectExtract(kw,'opt_*',null,true);
        let gantt_id = objectPop(kw,'gantt_id');
        let tasks = objectPop(kw,'tasks');
        let pane =  sourceNode._('contentPane',kw);
        let gnrwdg = sourceNode.gnrwdg;
        gnrwdg.gantt_id = gantt_id;
        gnrwdg.opt_kw = opt_kw;
        pane._('div',{id:gantt_id})
        sourceNode.attr.tasks = tasks;
        for(let k in opt_kw){
            sourceNode.attr[k] = opt_kw[k];
        }
        setTimeout(function(){
            gnrwdg.build();
        },1);
        
        return pane;
    },
    gnrwdg_getTasks:function(){
        return this.sourceNode.getRelativeData(this.sourceNode.attr.tasks) || new gnr.GnrBag();
    },

    gnrwdg_setTasks:function(tasks,kw){
        if(kw.reason=='drag_event'){
            return;
        }
        this.gannt.setup_tasks(this.convertedTasks());
        this.gannt.render();
    },


    gnrwdg_setOptions:function(opt,kw,trigger_reason){
        objectUpdate(this.gannt.options,this.convertedOptions());
        this.gannt.render();
    },

    gnrwdg_convertedTasks:function(){
        let tasks = this.getTasks();
        let result = [];
        for(let t of tasks.values()){
            result.push(t.asDict());
        }
        return result;
    },
   

    gnrwdg_convertedOptions:function(){
        let result = this.sourceNode.evaluateOnNode(this.opt_kw);
        if(result.view_modes && typeof(result.view_modes)=='string'){
            result.view_modes = result.view_modes.split(',');
        }
        return objectExtract(result,'opt_*');
    },

    gnrwdg_catch_opt:function(){
        this.setOptions();
    },
    gnrwdg_on_date_change(task, start, end){
        let tasks = this.getTasks();
        let taskNode = tasks.getNodeByValue('id',task.id);
        let v = taskNode.getValue()
        v.setItem('start',start,null,{doTrigger:'drag_event'});
        v.setItem('end',end,null,{doTrigger:'drag_event'});
    },

    gnrwdg_on_progress_change(task, progress){
        let tasks = this.getTasks();
        let taskNode = tasks.getNodeByValue('id',task.id);
        let v = taskNode.getValue()
        v.setItem('progress',progress,null,{doTrigger:'drag_event'});
    },

    gnrwdg_build:function(){
        let opt = this.convertedOptions();
        var that = this;
        opt.on_click = function (task) {
            console.log('on_click',task);
        };
        opt.on_date_change = function(task, start, end) {
            that.on_date_change(task, start, end);
        };
        opt.on_progress_change = function(task, progress) {
            that.on_progress_change(task, progress);
        };
        opt.on_view_change = function(mode) {
            console.log('on_view_change',mode);
        };
        this.gannt = new Gantt(`#${this.gantt_id}`,this.convertedTasks(),opt);
    },

});