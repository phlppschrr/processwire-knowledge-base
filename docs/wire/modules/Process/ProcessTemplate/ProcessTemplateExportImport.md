# ProcessTemplateExportImport

Source: `wire/modules/Process/ProcessTemplate/ProcessTemplateExportImport.php`


## other

@method string buildExport()

@method InputfieldForm buildInputDataForm()

@method string buildImport()

@method void processImport()

## getExportData()

Return export data for all given $exportTemplates

@param array $exportTemplates template names

@return array

## ___buildExport()

Execute export

@return InputfieldForm

## ___buildInputDataForm()

Build Textarea input form to past JSON data into

@return InputfieldForm

## ___buildImport()

Execute import

@return string

@throws WireException if given invalid import data

## ___processImport()

Commit changed field data

## saveItem()

@param Template $item

@param array $changes
