# -*- coding: UTF-8 -*-


class GnrCustomWebPage(object):

    def main(self,root,**kwargs):
        bc = root.borderContainer(datapath = 'main.shared')
        form_pane = bc.contentPane(region='left', width='50%')
        root.sharedObject('main.shared', shared_id='servo',autoLoad=True,autoSave=True,expire=20)

        steps_pane = bc.contentPane(region='center', datapath='main.record')
        fb = form_pane.formbuilder(cols=4 )
        #fb.textBox(lbl='Client ID', value='^page_id', colspan=2)

        fb.data('.recording', False)
        fb.dataFormula('.label', "recording?'Stop':'Record'", recording='^.recording')
        fb.dataFormula('.recording', "recording?false:true", recording='=.recording', _fired='^.toggle',
            _userChanges=True
        )
        
        fb.button(label='^.label', action='FIRE .toggle')
        fb.button(label='Snap', action='FIRE .snap')
        fb.button(label='Clear', action='FIRE .clear')
        fb.button(label='Play', action='FIRE .play')

        for i in range(6):
            fb.horizontalSlider(lbl='Servo %i'%i,value='^.s_%i'%i,width='400px',
                minimum=1, maximum=100, intermediateChanges=True, colspan=3)
            fb.numberTextBox(value='^.s_%i'%i,places=0, readOnly=True)
        
#        frame = steps_pane.bagGrid(storepath='.store',
#                        title='Passi',
#                        datapath='.steps',
#                        struct=self.refstruct,
#                        addrow=False,delrow=False,
#                        height='300px')
#
#
#
#    def steps_struct(self,struct):
#        r = struct.view().rows()
#        for i in range(6):
#            r.cell('s_%i'%i,name='Servo %i'%i)
#    