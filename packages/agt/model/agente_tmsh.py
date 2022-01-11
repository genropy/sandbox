try:
    from gnrpkg.tmsh.timesheet import TimeSheetTable
except Exception:
    TimeSheetTable = object

class Table(TimeSheetTable):

    def tmsh_appuntamento(self):
        return dict(tbl='agt.appuntamento')

    def tmsh_indisponibilita(self):
        return dict(tbl='agt.indisponibilita')
