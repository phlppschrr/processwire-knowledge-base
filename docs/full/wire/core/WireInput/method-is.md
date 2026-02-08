# WireInput::is()

Source: `wire/core/WireInput.php`

Is the current request of the specified type?

This is a more readable/shorter alias of `$input->requestMethod('type')` for syntax convenience.
Internally, it determines the request type without accessing any input data, so it is efficient.

~~~~~
// The following are equivalent:
$isPost = $input->is('post');
$isPost = $input->requestMethod('post');
~~~~~

@param string $method Specify one of: post, get, head, put, delete, options, patch (not case sensitive)

@return bool

@since 3.0.145
