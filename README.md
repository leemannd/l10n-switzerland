Odoo/OpenERP Swiss Localization
===============================

This repository provides official swiss localization provided by OCA.

It extends Odoo/OpenERP to add needed functionnalites to use Odoo/OpenERP in Switzerland.


l10n_ch_bank
------------

Provides the list of swiss banks offices with all relative data as clearing, city etc


l10n_ch_zip
-----------

Provides the list of swiss postal city and ZIP for auto-completion


l10n_ch_payment_slip
--------------------

Adds ESR/BVR report on invoice. Everey ESR/BVR element position can be configured by company.
Multiple payment tems on invoice are supported

It will also allow you to do the import of V11 bank statement files and do an automatical reconciliation


l10n_ch_base_bank
-----------------

Adds the support of postal account and bank postal account norm.
The partner banks form allows you to input swiss bank account and postal account in a correct manner.


l10n_ch_dta
-----------

Provides support of DTA payment file protocol to generate electronic payment file.
This feature will be depreacted around the end of 2014.


l10n_ch_sepa
------------

Provide support of SEPA/PAIN electronic payment file.
Only credit transfert file are supported


l10n_ch_scan_bvr
----------------

Allows you to scan the ESR/BVR reference and automatically create the proper supplier invoices
