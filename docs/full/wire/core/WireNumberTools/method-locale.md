# WireNumberTools::locale()

Source: `wire/core/WireNumberTools.php`

Get a number formatting property from current locale

In multi-language environments, this method’s return values are affected by the
current language locale.

@param string $key Property to get or omit to get all properties. Properties include:
 - `decimal_point`: Decimal point character
 - `thousands_sep`: Thousands separator
 - `currency_symbol`: Local currency symbol (i.e. $)
 - `int_curr_symbol`: International currency symbol (i.e. USD)
 - `mon_decimal_point`: Monetary decimal point character
 - `mon_thousands_sep`: Monetary thousands separator
 - `positive_sign`: Sign for positive values
 - `negative_sign`: Sign for negative values
 - `clear`: Clear any cached values for current language/locale.
 - See <https://www.php.net/manual/en/function.localeconv.php> for more.

@return array|string|int|null
