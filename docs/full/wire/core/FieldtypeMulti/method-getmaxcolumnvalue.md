# FieldtypeMulti::getMaxColumnValue()

Source: `wire/core/FieldtypeMulti.php`

Get max value of column for given Page and Field or boolean false (or specified $noValue) if no rows present

@param Page $page

@param Field $field

@param string $column

@param int|bool $noValue Return this value if there are no rows to count from (default=false)

@return int|bool|mixed

@throws WireException

@since 3.0.154
