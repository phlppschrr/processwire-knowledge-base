# Pages::___renameReady()

Source: `wire/core/Pages.php`

Hook called when a page is about to be renamed i.e. had its name field change)

The previous name can be accessed at `$page->namePrevious`.
The new name can be accessed at `$page->name`.

This hook is only called when a page's name changes. It is not called when
a page is moved unless the name was changed at the same time.

**Multi-language note:**
Also note this hook may be called if a page's multi-language name changes.
In those cases the language-specific name is stored in "name123" while the
previous value is stored in "-name123" (where 123 is the language ID).


@param Page $page The $page that was renamed

@since 3.0.235
