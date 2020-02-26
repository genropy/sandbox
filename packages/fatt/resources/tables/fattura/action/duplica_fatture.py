from gnr.web.batch.btcaction import BaseResourceAction

caption = 'Duplica fatture'
description = 'Duplica fatture'

class Main(BaseResourceAction):
    batch_prefix = 'DUPF' # DUPlica Fatture
    batch_title = 'Duplica fatture'
    batch_cancellable = True
    batch_immediate = True
    batch_delay = 0.5

    def do(self):

        fatture_pkeys = self.get_selection_pkeys()

        for fattura_pkey in self.btc.thermo_wrapper(fatture_pkeys, 'fatture', message='Fattura', maximum=len(fatture_pkeys)):
            self.tblobj.duplica(fattura_id=fattura_pkey)
        # self.db.commit()
