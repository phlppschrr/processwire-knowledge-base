# HTMLPurifier_Printer_ConfigForm

Source: `wire/modules/Markup/MarkupHTMLPurifier/htmlpurifier/standalone/HTMLPurifier/Printer/ConfigForm.php`

@todo Rewrite to use Interchange objects

## setTextareaDimensions()

Sets default column and row size for textareas in sub-printers
@param $cols Integer columns of textarea, null to use default
@param $rows Integer rows of textarea, null to use default

## getCSS()

Retrieves styling, in case it is not accessible by webserver

## getJavaScript()

Retrieves JavaScript, in case it is not accessible by webserver

## render()

Returns HTML output for a configuration form
@param HTMLPurifier_Config|array $config Configuration object of current form state, or an array
       where [0] has an HTML namespace and [1] is being rendered.
@param array|bool $allowed Optional namespace(s) and directives to restrict form to.
@param bool $render_controls
@return string

## renderNamespace()

Renders a single namespace
@param $ns String namespace name
@param array $directives array of directives to values
@return string
