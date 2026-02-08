# $module->className($options = null): string

Source: `wire/core/Module.php`

Return this object’s class name

If your Module descends from Wire, or any of it's derivatives (as would usually be the case),
then you don't need to implement this method as it's already present.

## Arguments

- array|bool|null $options Optionally an option or boolean for 'namespace' option: - `lowercase` (bool): Specify true to make it return hyphenated lowercase version of class name - `namespace` (bool): Specify false to omit namespace from returned class name. Default=true. - Note: when lowercase=true option is specified, the namespace=false option is required.

## Return value

string

## See also

- [Wire::className()](../Wire/method-classname.md)
