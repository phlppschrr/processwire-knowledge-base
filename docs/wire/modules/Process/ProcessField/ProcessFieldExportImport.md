# ProcessFieldExportImport

Source: `wire/modules/Process/ProcessField/ProcessFieldExportImport.php`

Handles import/export for ProcessField

ProcessWire 3.x, Copyright 2017 by Ryan Cramer
https://processwire.com

## other

@method InputfieldForm buildExport()

@method InputfieldForm buildImport()

@method InputfieldForm buildInputDataForm()

@method void processImport()

## getExportData()

Return export data for all given $exportFields

@param array $exportFields field names

@return array

## ___buildExport()

Execute export

@return InputfieldForm

## ___buildInputDataForm()

Build Textarea input form to pass JSON data into

@return InputfieldForm

## ___buildImport()

Execute import

@return InputfieldForm

@throws WireException if given invalid import data

## ___processImport()

Commit changed field data
