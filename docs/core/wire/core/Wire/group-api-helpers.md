# Wire: api-helpers

Source: `wire/core/Wire.php`

Shortcuts to ProcessWire API variables. Access without any arguments returns the API variable. Some support arguments as shortcuts to methods in the API variable.

- cache($name = '', $expire = null, $func = null): WireCache|string|array|PageArray|null Access the $cache API variable as a function.

- config($key = '', $value = null): Config|mixed Access the $config API variable as a function.

- database(): WireDatabasePDO Access the $database API variable as a function.

- datetime($format = '', $value = ''): WireDateTime|string|int Access the $datetime API variable as a function.

- fields($name = ''): Field|Fields|null Access the $fields API variable as a function.

- files(): WireFileTools Access the $files API variable as a function.

- input($type = '', $key = '', $sanitizer = ''): WireInput|WireInputData|WireInputDataCookie|array|string|int|null Access the $input API variable as a function.

- inputCookie($key = '', $sanitizer = ''): WireInputDataCookie|string|int|array|null Access the $input->cookie() API variable as a function.

- inputGet($key = '', $sanitizer = ''): WireInputData|string|int|array|null Access the $input->get() API variable as a function.

- inputPost($key = '', $sanitizer = ''): WireInputData|string|int|array|null Access the $input->post() API variable as a function.

- languages($name = ''): Languages|Language|NullPage|null Access the $languages API variable as a function.

- modules($name = ''): Modules|Module|ConfigurableModule|null Access the $modules API variable as a function.

- page($key = '', $value = null): Page|Mixed Access the $page API variable as a function.

- pages($selector = ''): Pages|PageArray|Page|NullPage Access the $pages API variable as a function.

- permissions($selector = ''): Permissions|Permission|PageArray|null|NullPage Access the $permissions API variable as a function.

- roles($selector = ''): Roles|Role|PageArray|null|NullPage Access the $roles API variable as a function.

- sanitizer($name = '', $value = ''): Sanitizer|string|int|array|null|mixed Access the $sanitizer API variable as a function.

- session($key = '', $value = null): Session|mixed Access the $session API variable as a function.

- templates($name = ''): Templates|Template|null Access the $templates API variable as a function.

- user($key = '', $value = null): User|mixed Access the $user API variable as a function.

- users($selector = ''): Users|PageArray|User|mixed Access the $users API variable as a function.
