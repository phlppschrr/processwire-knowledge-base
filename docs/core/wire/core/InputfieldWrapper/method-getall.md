# InputfieldWrapper::getAll()

Source: `wire/core/InputfieldWrapper.php`

Get all Inputfields below this recursively in a flat InputfieldWrapper (children, and their children, etc.)

Note that all InputfieldWrapper instances are removed as a result (except for the containing InputfieldWrapper).


@param array $options Options to modify behavior (3.0.169+)
 - `withWrappers` (bool): Also include InputfieldWrapper objects? (default=false) 3.0.169+

@return InputfieldsArray
