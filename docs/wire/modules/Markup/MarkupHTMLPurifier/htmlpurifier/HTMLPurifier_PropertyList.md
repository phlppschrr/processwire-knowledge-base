# HTMLPurifier_PropertyList

Source: `wire/modules/Markup/MarkupHTMLPurifier/htmlpurifier/HTMLPurifier.standalone.php`

Generic property list implementation

## get()

Recursively retrieves the value for a key
@param string $name
@throws HTMLPurifier_Exception

## set()

Sets the value of a key, for this plist
@param string $name
@param mixed $value

## has()

Returns true if a given key exists
@param string $name
@return bool

## reset()

Resets a value to the value of it's parent, usually the default. If
no value is specified, the entire plist is reset.
@param string $name

## squash()

Squashes this property list and all of its property lists into a single
array, and returns the array. This value is cached by default.
@param bool $force If true, ignores the cache and regenerates the array.
@return array

## getParent()

Returns the parent plist.
@return HTMLPurifier_PropertyList

## setParent()

Sets the parent plist.
@param HTMLPurifier_PropertyList $plist Parent plist
