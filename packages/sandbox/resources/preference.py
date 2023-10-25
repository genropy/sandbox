
class AppPref(object):
    def prefpane_sandbox(self,parent,**kwargs):
        tc = parent.tabContainer(margin='2px',**kwargs)
        self.mixinComponent('pwa:PWAPreferencePane')
        self.pwaPreferencePane(tc)