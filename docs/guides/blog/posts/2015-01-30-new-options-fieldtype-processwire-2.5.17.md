# New Options Fieldtype (ProcessWire 2.5.17)

Source: https://processwire.com/blog/posts/new-options-fieldtype-processwire-2.5.17/

## Sections


## New Options Fieldtype (ProcessWire 2.5.17)

30 January 2015 by Ryan Cramer [ 8 Comments](/blog/posts/new-options-fieldtype-processwire-2.5.17/#comments)


### Selectable Options in ProcessWire

Many people new to ProcessWire initially think that we don't have any kind of selectable options fields. But then they discover the Page Fieldtype, and then realize that not only do we have selectable options, we've got them on steroids!

Despite that, the fact remains that this is one area where ProcessWire is completely unique (relative to other CMSs out there), and thus it may take awhile before people "get" it. I've always worried that someone evaluating PW might overlook this, and move-on before they really understand the power of what PW offers in this area.

Then there's also the aspect that pages are sometimes overkill for all selectable-option needs. Granted, there's no harm in it, and I'd rather be over-prepared than under-prepared. But using pages for selectable options does require a certain level of understanding and planning, and perhaps a little more time, than people always have.

Given these factors, something that's been on my `@todo` for a long time has been to create a new fieldtype that provides selectable options, outside of using pages. But I didn't want to skimp on building it the right way, and building it the right way takes time. It means storing references to options rather than the options themselves, in a database normalized way, while still making it possible to query the text of those options from selectors.


### Introducing FieldtypeOptions

This week I'm glad to introduce the new [FieldtypeOptions](https://processwire.com/api/modules/select-options-fieldtype/) module, which provides a neat alternative to pages for selectable options in ProcessWire. Here are a few highlights:

- **Provides selectable options in a normalized, scalable way.** If you edit or rename an existing option, the change is reflected in all existing selections. If an option is deleted, all usages and references are likewise deleted.
- **Supports input from any module that extends InputfieldSelect, including single and multi-value inputs.** This includes numerous core and 3rd party Inputfield modules. In the core, this includes Select, Select Multiple, Checkboxes, Radios, and AsmSelect.
- **Options are exceptionally easy to define.** If you want to create a Options field with 200 selectable countries, just copy and paste a list of countries from a page like [this](https://openconcept.ca/blog/mgifford/text-list-all-countries-world) (titles only) or [this](https://gist.github.com/marijn/396531#file-countries-txt) (values and titles), and paste them into the field. Save, and you are done.
- **Options are multi-language.** If you have LanguageSupport installed (with LanguageSupportFields), your options definition gets a tab for each language.
- **Options are sortable per-page**, when supported by the Inputfield (like AsmSelect).
- **Supports pre-selected options** when combined with "required" status.
- Each option contains a "title", but can also optionally have an independent "value" that goes with it.
- Accessed from the API in the same way as pages.
- Unlike pages, the same API code can apply to either single or multi-value selections. To put it simply, `$page->countries->first()->title` and `$page->countries->title` product the same result. Meaning, properties of the first item can be accessed directly from array value.
- All option deletions are confirmed.
- Options can be managed from the admin, but also from the API (as you would expect in PW).

If this sounds interesting to you, please see the [new documentation page for the Options Fieldtype](https://processwire.com/api/modules/select-options-fieldtype/). Since this is brand new, and only on the dev branch (PW 2.5.17+) please consider it beta… use it for sites in development, but not yet for live or production sites. Please let me know how it works for you.
