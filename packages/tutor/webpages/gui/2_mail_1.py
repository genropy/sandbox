# -*- coding: UTF-8 -*-
from gnr.core.gnrdecorator import public_method

class GnrCustomWebPage(object):
    def main(self,root,**kwargs):
        box = root.div(datapath='mailclient')
        fb = box.formbuilder(border_spacing='3px',cols=1,datapath='.data')
        fb.textbox(value='^.to_address',lbl='To',width='40em')
        fb.textbox(value='^.subject',lbl='Subject',width='40em')
        fb.simpleTextArea(value='^.body',lbl='Body',width='40em',
                    height='80px')
        fb.button('Send',fire='mailclient.send')
        box.dataRpc('.result',self.sendEmail,data='=.data',_fired='^.send')
        box.pre('^.result')

    @public_method
    def sendEmail(self,command=None,data=None):
        try:
            mailserver = self.site.getService('mail')
            mailserver.sendmail_template(data)     
            return "Successfully sent email"
        except Exception:
            return "Error: unable to send email"