from zebra import Zebra
from simple_zpl2 import NetworkPrinter, ZPLDocument, Code128_Barcode

prn = NetworkPrinter('10.243.243.100','5964')
# Each label is built with a ZPLDocument object
zdoc = ZPLDocument()
zdoc.add_comment(77777)
# zdoc.add_zpl_raw('^BY3')  # example of custom command; this ^BY command allows to˓→change barcode width (default is 2, range is 1-10)
zdoc.add_field_origin(20, 20)
code128_data = 'TEST BARCODE'
bc = Code128_Barcode(code128_data, 'N', 30, 'Y')
zdoc.add_barcode(bc)


print(zdoc.zpl_text)
print(prn)
