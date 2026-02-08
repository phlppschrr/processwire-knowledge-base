# DatabaseQuery::copyTo()

Source: `wire/core/DatabaseQuery.php`

Copy queries from this DatabaseQuery to another DatabaseQuery

If you want to copy bind values you should also call copyBindValuesTo($query) afterwards.

@param DatabaseQuery $query Query to copy data to

@param array $methods Optionally specify the names of methods to copy, otherwise all are copied

@return int Total items copied

@since 3.0.157
