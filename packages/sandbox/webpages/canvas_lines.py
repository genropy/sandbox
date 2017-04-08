# -*- coding: UTF-8 -*-


class GnrCustomWebPage(object):
    def main(self,root,**kwargs):
        canvas_pane = root.contentPane(datapath='main.shared')
        root.sharedObject('main.shared', shared_id='servo',autoLoad=True,autoSave=True,expire=20)
        canvas_pane.canvas(width="600", height="600", id='mycanvas', datapath='main.shared')
        canvas_pane.dataController("""
            console.log(point);
            var x = point[0];
            var y = point[1];
            var r = Math.floor(255*point[2]);
            var g = Math.floor(255*point[3]);
            var b = Math.floor(255*point[4]);
            
            var d = 7.5;
            var canvas = document.getElementById('mycanvas');
            var context = canvas.getContext('2d');
            if (x==-1 && y==-1){
                context.clearRect(0, 0, canvas.width, canvas.height);
            }
            else{
            context.beginPath();
            console.log(x/4-d/2);
            console.log(y/4-d/2);
            
            context.arc(x/4-d/2, canvas.height-y/4-d/2, d, 0, 2 * Math.PI, false);
            var fillStyle = 'rgb('+r+','+g+','+b+')';
            console.log(fillStyle);
            context.fillStyle = fillStyle;
            context.fill();
            }
        """, point='^.point')
         