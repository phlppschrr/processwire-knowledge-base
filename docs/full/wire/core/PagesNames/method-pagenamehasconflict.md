# PagesNames::pageNameHasConflict()

Source: `wire/core/PagesNames.php`

Does given page have a name that has a conflict/collision?

In multi-language environment this applies to default language only.


@param Page $page Page to check

@return string|bool Returns string with conflict reason or boolean false if no conflict

@throws WireException If given invalid $options argument

@since 3.0.127
