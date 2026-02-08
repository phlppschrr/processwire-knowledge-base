# $moduleConfig->getInputfields(): InputfieldWrapper

Source: `wire/core/ModuleConfig.php`

Return an InputfieldWrapper of Inputfields necessary to configure this module

Values will be populated to the Inputfields automatically. However, you may also retrieve
any of the values from $this->[property]; as needed.

Descending classes should call this method at the top of their getInputfields() method.

Use this method only if defining Inputfield objects programatically. If definining via
an array then you should not implement this method.

## Return value

InputfieldWrapper
