# DatabaseQuerySelectFulltext::matchArrayValue()

Source: `wire/core/DatabaseQuerySelectFulltext.php`

Match when given $value is an array

Note: PageFinder uses its own array-to-value conversion, so this case applies only to other usages outside PageFinder,
such as FieldtypeMulti::getLoadQueryWhere()

@param array $value

@since 3.0.141

@throws WireException
