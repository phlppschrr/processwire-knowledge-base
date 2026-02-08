# PagesLoader::findShortcut()

Source: `wire/core/PagesLoader.php`

Helper for find() method to attempt to shortcut the find when possible

@param string|array|Selectors $selector

@param array $options

@param array $loadOptions

@return bool|Page|PageArray Returns boolean false when no shortcut available
