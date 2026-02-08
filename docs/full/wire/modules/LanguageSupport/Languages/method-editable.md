# Languages::editable()

Source: `wire/modules/LanguageSupport/Languages.php`

Does current user have edit access for page fields in given language?

@param Language|int|string $language Language id, name or object, or string "none" to refer to non-multi-language fields

@return bool True if editable, false if not
