# $fieldtype->getDatabaseSchema(Field $field): array

Source: `wire/core/Fieldtype.php`

Get the database schema for this field

- Should return an array like in the example below, indexed by field name with type details as the value
  (as it would be in an SQL statement).

- Indexes are passed through with a `keys` array. Note that `pages_id` as a field and primary key may be
  retrieved by starting with the parent schema return from the built-in getDatabaseSchema() method.

- At minimum, each Fieldtype must add a `data` field as well as an index for it.

- If you want a PHP `NULL` value to become a NULL in the database, your column definition must specify:
  `DEFAULT NULL`.

~~~~~~
array(
 'data' => 'mediumtext NOT NULL',
 'keys' => array(
   'primary' => 'PRIMARY KEY (`pages_id`)',
   'FULLTEXT KEY data (data)',
 ),
 'xtra' => array(
   // optional extras, MySQL defaults will be used if omitted
   'append' =>
     'ENGINE={$this->config->dbEngine} ' .
     'DEFAULT CHARSET={$this->config->dbCharset}'

   // true (default) if this schema provides all storage for this fieldtype.
   // false if other storage is involved with this fieldtype, beyond this schema
   // (like repeaters, PageTable, etc.)
   'all' => true,
 )
);
~~~~~~

## Arguments

- Field $field In case it's needed for the schema, but typically isn't.

## Return value

array
