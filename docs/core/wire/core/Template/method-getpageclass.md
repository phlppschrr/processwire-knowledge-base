# Template::getPageClass()

Source: `wire/core/Template.php`

Get class name to use for Page objects using this template

Note that value can be different from the `$template->pageClass` property, since it is determined at runtime.
If it is different, then it is at least a class that extends the one defined by the pageClass property.


@param bool $withNamespace Returned class includes namespace? (default=true)

@return string Returned page class includes namespace

@since 3.0.152
