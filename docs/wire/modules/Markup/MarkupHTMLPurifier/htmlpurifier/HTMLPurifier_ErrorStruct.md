# HTMLPurifier_ErrorStruct

Source: `wire/modules/Markup/MarkupHTMLPurifier/htmlpurifier/HTMLPurifier.standalone.php`

Records errors for particular segments of an HTML document such as tokens,
attributes or CSS properties. They can contain error structs (which apply
to components of what they represent), but their main purpose is to hold
errors applying to whatever struct is being used.

## addError()

@param int $severity
@param string $message
