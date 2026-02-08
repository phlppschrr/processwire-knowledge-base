# $template->getPageClass($withNamespace = true): string

Source: `wire/core/Template.php`

Get class name to use for Page objects using this template

Note that value can be different from the `$template->pageClass` property, since it is determined at runtime.
If it is different, then it is at least a class that extends the one defined by the pageClass property.

## Usage

~~~~~
// basic usage
$string = $template->getPageClass();

// usage with all arguments
$string = $template->getPageClass($withNamespace = true);
~~~~~

## Arguments

- `$withNamespace` (optional) `bool` Returned class includes namespace? (default=true)

## Return value

- `string` Returned page class includes namespace

## Since

3.0.152
