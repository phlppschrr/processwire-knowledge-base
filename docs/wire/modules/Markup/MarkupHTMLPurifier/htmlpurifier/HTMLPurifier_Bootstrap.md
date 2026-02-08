# HTMLPurifier_Bootstrap

Source: `wire/modules/Markup/MarkupHTMLPurifier/htmlpurifier/HTMLPurifier.standalone.php`

Bootstrap class that contains meta-functionality for HTML Purifier such as
the autoload function.

@note
     This class may be used without any other files from HTML Purifier.

## getPath()

Returns the path for a specific class.
@param string $class Class path to get
@return string

## registerAutoload()

"Pre-registers" our autoloader on the SPL stack.
