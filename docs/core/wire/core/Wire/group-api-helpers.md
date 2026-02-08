# Wire: api-helpers

Source: `wire/core/Wire.php`

Shortcuts to ProcessWire API variables. Access without any arguments returns the API variable. Some support arguments as shortcuts to methods in the API variable.

@method WireCache|string|array|PageArray|null cache($name = '', $expire = null, $func = null) Access the $cache API variable as a function.

@method Config|mixed config($key = '', $value = null) Access the $config API variable as a function.

@method WireDatabasePDO database() Access the $database API variable as a function.

@method WireDateTime|string|int datetime($format = '', $value = '') Access the $datetime API variable as a function.

@method Field|Fields|null fields($name = '') Access the $fields API variable as a function.

@method WireFileTools files() Access the $files API variable as a function.

@method WireInput|WireInputData|WireInputDataCookie|array|string|int|null input($type = '', $key = '', $sanitizer = '') Access the $input API variable as a function.

@method WireInputDataCookie|string|int|array|null inputCookie($key = '', $sanitizer = '') Access the $input->cookie() API variable as a function.

@method WireInputData|string|int|array|null inputGet($key = '', $sanitizer = '') Access the $input->get() API variable as a function.

@method WireInputData|string|int|array|null inputPost($key = '', $sanitizer = '') Access the $input->post() API variable as a function.

@method Languages|Language|NullPage|null languages($name = '') Access the $languages API variable as a function.

@method Modules|Module|ConfigurableModule|null modules($name = '') Access the $modules API variable as a function.

@method Page|Mixed page($key = '', $value = null) Access the $page API variable as a function.

@method Pages|PageArray|Page|NullPage pages($selector = '') Access the $pages API variable as a function.

@method Permissions|Permission|PageArray|null|NullPage permissions($selector = '') Access the $permissions API variable as a function.

@method Roles|Role|PageArray|null|NullPage roles($selector = '') Access the $roles API variable as a function.

@method Sanitizer|string|int|array|null|mixed sanitizer($name = '', $value = '') Access the $sanitizer API variable as a function.

@method Session|mixed session($key = '', $value = null) Access the $session API variable as a function.

@method Templates|Template|null templates($name = '') Access the $templates API variable as a function.

@method User|mixed user($key = '', $value = null) Access the $user API variable as a function.

@method Users|PageArray|User|mixed users($selector = '') Access the $users API variable as a function.
