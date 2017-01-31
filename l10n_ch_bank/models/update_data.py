import xlrd
from xlrd import open_workbook

try:
    from cStringIO import StringIO
except:
    from StringIO import StringIO

import os
import time
import unicodecsv as csv
import base64


HEADER_ODOO = [
    ('id', 'id'),
    ('code', 11),
    ('bank_postaccount', 21),
    ('bank_clearing_new', 3),
    ('bank_headquarter', 5),
    ('street', 13),
    ('bank_group', 0),
    ('city', 16),
    ('zip', 15),
    ('clearing', 1),
    ('bank_areacode', 19),
    ('bank_bcart', 6),
    ('fax', 18),
    ('bank_eurosic', 10),
    ('bank_sicnr', 5),
    ('bic', 22),
    ('bic bank_branchid', 2),
    ('bank_sic', 8),
    ('phone', 17),
    ('active', 'true_value'),
    ('bank_lang', 10),
    ('bank_postaladdress', 14),
    ('name', 12),
    ('country', 'null_value'),
    ('bank_valid_from', 'null_value'),
]

sixt_file = xlrd.open_workbook('../data/bcbankenstamm_e.xls')
sixt_sheet = sixt_file.sheet_by_name('BC Bank Master Data')

encoding = 'utf-8'
quoting = csv.QUOTE_MINIMAL
separator = ';'
output = StringIO()
csv_writer = csv.writer(output,
                        encoding=encoding,
                        quoting=quoting,
                        delimiter=separator)
# Get headers
header = [x[0] for x in HEADER_ODOO]
for row_idx in range(sixt_sheet.nrows):  # Loop on all records
    row = []

    sixt_row = sixt_sheet.row(row_idx)
    if row_idx != 0:
        for header in HEADER_ODOO:
            if header[1] == 'id':
                row.append('l10n_ch.bank_' + sixt_row[1].value + '_' + sixt_row[2].value)
            elif header[1] == 'null_value':
                row.append('')
            elif header[1] == 'true_value':
                row.append('True')
            elif header[0] == 'bank_postaccount':
                row.append(sixt_row[header[1]].value.replace("*", ''))
            else:
                row.append(sixt_row[header[1]].value)
    csv_writer.writerow(row)

# filename
timestr = time.strftime("%Y%m%d-%H%M%S")
filename = 'banks' + timestr + '.csv'

# write to file
with open(filename, 'w') as out:
    out.write(output.getvalue())
    out.close()

sixt_file.unload_sheet('BC Bank Master Data')
