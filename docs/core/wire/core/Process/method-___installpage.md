# Process::___installPage()

Source: `wire/core/Process.php`

Install a dedicated page for this Process module and assign it this Process

To be called by Process module's ___install() method.


@param string $name Desired name of page, or omit (or blank) to use module name

@param Page|string|int|null Parent for the page, with one of the following:
	- name of parent, relative to admin root, i.e. "setup"
	- Page object of parent
	- path to parent
	- parent ID
	- Or omit and admin root is assumed

@param string $title Omit or blank to pull title from module information

@param string|Template Template to use for page (omit to assume 'admin')

@param array $extras Any extra properties to assign (like status)

@return Page Returns the page that was created

@throws WireException if page can't be created
