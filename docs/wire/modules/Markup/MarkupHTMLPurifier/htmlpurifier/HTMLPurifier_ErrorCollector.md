# HTMLPurifier_ErrorCollector

Source: `wire/modules/Markup/MarkupHTMLPurifier/htmlpurifier/HTMLPurifier.standalone.php`

Error collection class that enables HTML Purifier to report HTML
problems back to the user

## send()

Sends an error message to the collector for later use
@param int $severity Error severity, PHP error style (don't use E_USER_)
@param string $msg Error message text

## getRaw()

Retrieves raw error data for custom formatter to use

## getHTMLFormatted()

Default HTML formatting implementation for error messages
@param HTMLPurifier_Config $config Configuration, vital for HTML output nature
@param array $errors Errors array to display; used for recursion.
@return string
