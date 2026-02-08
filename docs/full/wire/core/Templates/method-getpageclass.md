# $templates->getPageClass(Template $template, $withNamespace = true): string

Source: `wire/core/Templates.php`

Get class name to use for pages using given Template

Note that value can be different from the `$template->pageClass` property, since it is determined at runtime.
If it is different, then it is at least a class that extends the one defined by pageClass.

## Arguments

- `$template` `Template`
- `$withNamespace` (optional) `bool` Include namespace? (default=true)

## Return value

string Returned class name includes namespace

## Since

3.0.152
