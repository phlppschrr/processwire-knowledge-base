# $moduleConfig->__construct()

Source: `wire/core/ModuleConfig.php`

Use the construct method if you are defining your module config fields as an array

Example for method body:

  array(
    'name' => 'fullname'
    'type' => 'text',
    'label' => 'Full Name',
    'value' => '',
  ),
  array(
    'name' => 'email',
    'type' => 'email',
    'label' => 'Email Address',
    'placeholder' => 'you@company.com',
    'value' => '',
  ),
));

## Example

```php
$this->add(array(
```

## Usage

~~~~~
// basic usage
$result = $moduleConfig->__construct();
~~~~~
