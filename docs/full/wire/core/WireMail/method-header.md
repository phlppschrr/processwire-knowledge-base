# WireMail::header()

Source: `wire/core/WireMail.php`

Set any email header

- Multiple calls will append existing headers.
- To remove an existing header, specify NULL as the value.


@param string|array $key Header name

@param string $value Header value or specify null to unset

@return $this
