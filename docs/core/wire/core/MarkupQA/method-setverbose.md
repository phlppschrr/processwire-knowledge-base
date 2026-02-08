# MarkupQA::setVerbose()

Source: `wire/core/MarkupQA.php`

Get or set a setting

@param string $key Setting name to get or set, or omit to get all settings

@param string|array|int|null $value Setting value to set, or omit when getting setting

@return string|array|int|null|$this Returns value of $key

public function setting($key = null, $value = null) {
if($key === null) return $this->settings; // return all
if($value === null) return isset($this->settings[$key]) ? $this->settings[$key] : null; // return one
if($key === 'ignorePaths') return $this->ignorePaths($value); // set specific
$this->settings[$key] = $value; // set
return $value;
}
