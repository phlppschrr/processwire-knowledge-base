# Pagefiles::rename()

Source: `wire/core/Pagefiles.php`

Queue a rename of a Pagefile

This only queues a rename. Rename actually occurs when page is saved.
Note this differs from the behavior of `Pagefile::rename()`.


@param Pagefile $item

@param string $name

@return Pagefiles

@see Pagefile::rename()
