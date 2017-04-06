# -*- coding: UTF-8 -*-


class GnrCustomWebPage(object):
    def main(self,root,**kwargs):
        root.sharedObject('main.shared', shared_id='servo',autoLoad=True,autoSave=True,expire=20)
        bc = root.borderContainer(datapath = 'main.shared')
        form_pane = bc.contentPane(region='left', width='50%')

        canvas_pane = bc.contentPane(region='center')
        fb = form_pane.formbuilder(cols=2 )
        fb.textBox(lbl='Client ID', value='^page_id', colspan=2)
        for i in range(6):
            fb.horizontalSlider(lbl='Servo %i'%i,value='^.s_%i'%i,width='400px',
                minimum=1, maximum=100, intermediateChanges=True)
            fb.numberTextBox(value='^.s_%i'%i,places=0, readOnly=True)
            #fb.dataController("""
            #    genro.wsk.setInClientData(page_id,'position.s_%i',position);"""%i,
            #    page_id='=page_id', position='^position.s_%i'%i, _if='position')
        canvas_pane.canvas(width="400", height="400", id='mycanvas')
        canvas_pane.dataController("""
            console.log(point);
            var x = point[0];
            var y = point[1];
            var d = 7.5;
            var canvas = document.getElementById('mycanvas');
            var context = canvas.getContext('2d');
            context.beginPath();
            console.log(x/4-d/2);
            console.log(y/4-d/2);
            
            context.arc(x/4-d/2, canvas.height-y/4-d/2, d, 0, 2 * Math.PI, false);
            context.fillStyle = 'yellow';
            context.fill();
        """, point='^.point')
         