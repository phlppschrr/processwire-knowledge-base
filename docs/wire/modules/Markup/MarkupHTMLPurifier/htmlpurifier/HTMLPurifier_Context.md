# HTMLPurifier_Context

Source: `wire/modules/Markup/MarkupHTMLPurifier/htmlpurifier/HTMLPurifier.standalone.php`

Registry object that contains information about the current context.
@warning Is a bit buggy when variables are set to null: it thinks
         they don't exist! So use false instead, please.
@note Since the variables Context deals with may not be objects,
      references are very important here! Do not remove!

## get()

Retrieves a variable reference from the context.
@param string $name String name
@param bool $ignore_error Boolean whether or not to ignore error
@return mixed

## destroy()

Destroys a variable in the context.
@param string $name String name

## exists()

Checks whether or not the variable exists.
@param string $name String name
@return bool

## loadArray()

Loads a series of variables from an associative array
@param array $context_array Assoc array of variables to load
