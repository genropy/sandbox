# -*- coding: UTF-8 -*-
            
class GnrCustomWebPage(object):
    
    def main(self,root,**kwargs):
        self.small(root, cols=1, width='300px')
        self.small(root, cols=2, width='500px')
        self.small(root, cols=4, width='700px')
        self.large(root)

        
    def small(self,pane, cols=None, width=None):
        box=pane.div(datapath='small',width=width,
                      margin='20px',border='1px solid gray',
                     shadow='3px 3px 6px #888')
        fb=box.div(margin='10px').formbuilder(cols=cols,
                                              width='100%',
                                              fld_width='100%',
                                              lbl_font_size='11px',
                                              lbl_font_weight='bold'
                                             )
        
        fb.input('^.name',lbl='Name')
        fb.input('^.surname',lbl='Surname')
        fb.input('^.address',lbl='Address')
        fb.input('^.state',lbl='State',width='70px',lbl_color='red')
        
    def large(self,pane):
        box=pane.div(datapath='large',width='600px',
                      margin='20px',border='1px solid gray',
                       shadow='3px 3px 6px #888')
        fb=box.div(margin='20px').formbuilder(cols=2,
                                              width='100%',
                                              fld_width='100%')
       
        fb.input('^.name',lbl='Name')
        fb.input('^.surname',lbl='Surname')
        fb.input('^.address',lbl='Address',colspan=2)
        fb.input('^.zip',lbl='Zip')
        fb.input('^.state',lbl='State',width='70px')
        fb.textArea('^.notes',lbl='Notes',colspan=2, height='100px')
        fb.input('^.phone',lbl='Phone')
        fb.img('^.image',lbl='Image', rowspan=8, height='170px',
                         background='white', border='1px solid #efefef')
        fb.input('^.fax',lbl='Fax')
        fb.input('^.mobile',lbl='Mobile')
        fb.input('^.email',lbl='Email')
        fb.input('^.skype',lbl='Skype')
        fb.input('^.aim',lbl='Aim',width='100%')
        fb.input('^.twitter',lbl='Twitter')
        fb.input('^.jabber',lbl='Jabber')
        fb.input('^.www',lbl='WWW',colspan=2)
        fb.button('Submit',action='alert(data.toXml())',data='=large')
        
        
       

