# $markupQA->setVerbose($verbose): string|array|int|null|$this

Source: `wire/core/MarkupQA.php`

Get or set a setting




public function setting($key = null, $value = null) {
if($key === null) return $this->settings; // return all
if($value === null) return isset($this->settings[$key]) ? $this->settings[$key] : null; // return one
if($key === 'ignorePaths') return $this->ignorePaths($value); // set specific
$this->settings[$key] = $value; // set
return $value;
}

## Arguments

- `$key` `string` Setting name to get or set, or omit to get all settings
- `$value` `string|array|int|null` Setting value to set, or omit when getting setting

## Return value

string|array|int|null|$this Returns value of $key
