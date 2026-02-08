# Selectors::___getCustomVariableValue()

Source: `wire/core/Selectors.php`

Get the value for a custom [var] to populate in a selector (also works in PageFinder)

This can be useful for cases where the variable would be stored somewhere in
a configuration, like a Lister selector or Page reference field selector, where PHP
variables typically wouldn't be available.

If hooking this method, /site/ready.php is recommended.

@param string $name

@return null|string

@since 3.0.255
