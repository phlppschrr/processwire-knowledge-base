# Pages::___saveReady()

Source: `wire/core/Pages.php`

Hook called just before a page is saved

May be preferable to a before `Pages::save` hook because you know for sure a save will
be executed immediately after this is called. Whereas you don't necessarily know
that when the before `Pages::save` is called, as an error may prevent it.


@param Page $page The page about to be saved

@return array Optional extra data to add to pages save query, which the hook can populate.

@see Pages::savePageOrFieldReady(), Pages::saveFieldReady()
