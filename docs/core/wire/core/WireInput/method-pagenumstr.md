# WireInput::pageNumStr()

Source: `wire/core/WireInput.php`

Return the string that represents the page number URL segment

Returns blank when page number is 1, since page 1 is assumed when no pagination number present in URL.

This is the string that gets appended to the URL and typically looks like `page123`,
but can be changed by modifying the `$config->pageNumUrlPrefix` setting, or specifying
language-specific page number settings in the LanguageSupportPageNames module.


@param int $pageNum Optionally specify page number to use (default=0, which means use current page number)

@return string

@since 3.0.106
