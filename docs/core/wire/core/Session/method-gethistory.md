# Session::getHistory()

Source: `wire/core/Session.php`

Get the session history (if enabled)

Applicable only if `$config->sessionHistory > 0`.

~~~~~
$history = $session->getHistory();
print_r($history);
// outputs the following:
array(
  0  => array(
		'url' => 'http://domain.com/path/to/page/', // URL
		'page' => 1234, // page ID
		'time' => 234993498, // unix timestamp
  ),
  1 => array(
     // ...
  ),
  2 => array(
     // ...
  ),
  ...
);
~~~~~


@return array Array of arrays containing history entries.
