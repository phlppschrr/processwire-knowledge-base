# Using date range fields in ProcessWire

Source: https://processwire.com/blog/posts/date-range-fields/

## Sections


## Using date range fields in ProcessWire

24 November 2023 by Ryan Cramer [ 0 Comments](/blog/posts/date-range-fields/#comments)

This week we'll take a detailed look at the newest addition to the ProFields set of modules: the Date Range Fieldtype and Inputfield.

Date Range fields enable input, storage and querying of two dates ("date from" and "date to"). This is useful for anything that requires a starting and ending date. A single-date selection mode is also available. This module can be used for fields in ProcessWire, FormBuilder, or any other Inputfield-based form.

Above: example of a date range input with Sundays disabled for starting date ranges.


### About date range fields

Over the years, I've come across so many situations where I needed two date fields for "from" and "to", "start" and "stop", "begin" and "end", and so on. I always setup two separate "datetime" fields for that purpose. But that solution isn't always ideal because it requires two separate fields. And those two fields are completely independent of one another, without any context to each other when it comes to configuration and input requirements. On the input side, it isn't ideal for the user to use two separate fields (with their own date pickers). Nor is it ideal for what consumes the selected dates, as there is no ability to impose rules or validate them against each other… short of manually adding a hook to form processing.

This module solves those issues and limitations by integrating the "from" and "to" dates into a single field. It uses a single input widget enabling the user to select these dates directly from a calendar. This enables range specific input requirements and limitations that make it easier on both the user entering the dates *and* the user that ultimately uses them.

I recently came across a travel site that used what I thought was the ideal solution for selecting dates at booking time. It enabled you to select two dates for the purpose of making a hotel reservation, and it made it so simple and bulletproof that I had to investigate further. This module is based around the same solution found there. The front-end JS input portion is based around a version of the excellent [Hotel Datepicker](https://github.com/benitolopez/hotel-datepicker) library that we have modified and customized to make it more less hotel-specific and more general purpose. We've also updated it to support a single-date selection mode, among other tweaks.

Date range fields are exceptionally "findable" in ProcessWire selectors. Not only can you find pages by starting and ending dates, but you can find by partial dates, years, number of nights, number of days, whether a date is in the past, current or future, and whether a date range has a specific date. The API section of this page covers this and more in detail.


## Configuring date range fields

This field comes with numerous configuration options, particularly when it comes to configuration of the Inputfield. These settings are all described on the screen where you configure them. If you are configuring a ProcessWire field, you'll have both field and input configuration screens. If configuring a field in FormBuilder, you'll have just the input configuration screen.


### Inputfield configuration

These settings are available on the "Input" tab when editing a Date Range field (or the "Details" tab when editing a Date Range field in FormBuilder). At the top of the configuration is an example preview of the datepicker. This datepicker is live-updated as you make changes to your configuration, enabling you to see the effect that each setting has immediately.

One setting I'd like to point your attention to above is the "Minimum selectable date". If no date is selected here then the current date is assumed. If your need calls for selection of dates in the past, please be sure to specify a date here. If the field already has a value for some date in the past, then that becomes the minimum selectable date automatically at runtime.


### Fieldtype configuration

The Fieldtype configuration settings are visible on the "Details" tab when editing a Date Range field. The screenshot below shows the settings available. Note that this configuration is only used when editing a ProcessWire field, as the Fieldtype is not used when editing a field in FormBuilder or other Inputfield form.


### Single day selection mode

If you only need to collect one date, but would still like to use the date picker provided by this module, it can be configured for single day selection mode. In this mode, the user just selects a single day and this completes the selection (no end date option is needed or provided in this mode).

When single day selection mode is active, note that the module stores the same date for both `date_from` and `date_to`. Since you don't need both, we recommend just using the `date_from` in your queries or code. But if modifying the value from the API, you'll want to update both the `date_from` and `date_to` so that they remain the same.


## Date Range API

Getting the value of a date range field is as simple as accessing `$page->date_range`, where date_range is the name of your field. When output or cast as a string, it returns the selected date range in the format `YYYY-MM-DD - YYYY-MM-DD`. For example `2024-04-08 - 2024-05-04`. If you configured the field to use a different date format, then it will use that format instead when the page’s output formatting state is on.


### Getting date ranges

The value of a date range field on a page is an object of type `DateRangeValue`, which can also behave as a string. If treated as a string, it will simply output the selected range. In the example below, our date range field is named "date_range":

```
// outputs: 2024-01-02 - 2024-01-08
echo $page->date_range;
```

Because the date_range is an object, you can also access any of the date range properties off of it:

```
echo $page->date_range->date_from; // 2024-01-02
echo $page->date_range->date_to; // 2024-01-08
echo $page->date_range->nights; // 6
echo $page->date_range->days; // 7
```

We can also access a few boolean properties to identify where the range is relative to the current date:

```
if($page->date_range->current) {
  // today is Jan 1-8 in 2024
} else {
  // we are not currently in this date range
}

if($page->date_range->future) {
  // this range is in the future
} else {
  // this range is in the past or current
}

if($page->date_range->past) {
  // this range is in the past
} else {
  // this range is in the future or current
}
```

Whether getting, setting or querying date ranges, Note that the `date_from` can also be referred to as `dateFrom` or just `from`. Likewise, the `date_to` property can also be referred to as `dateTo` or just `to`. For example:

```
echo $page->date_range->from; // 2024-01-02
echo $page->date_range->to; // 2024-01-08
```

When you get a date range from a formatted page the object type becomes `DateRangePageFieldValue` and this value is essentially the same as the `DateRangeValue` except that its dates and ranges are formatted according to your comfiguration in the field settings (Details tab).


### Setting and saving date ranges

There are just two properties that you can set on a date range: `date_from` and `date_to`. The other properties such as nights and days are calculated automatically at runtime from the dates.

When setting dates, I recommend using the `YYYY-MM-DD` (ISO-8601) date format. However, this module will work with any format recognized by PHP’s strtotime function. For instance, the string `today` would refer to today's date. But in our examples below, we'll stick with using the `YYYY-MM-DD` format.

```
// turn off output formatting if needed
$page->of(false);

// set date_from and date_to
$page->date_range->date_from = '2024-04-08';
$page->date_range->date_to = '2024-05-04';

// same as above but just using shorter syntax
$page->date_range->from = '2024-04-08';
$page->date_range->to = '2024-05-04';

// set both date_from and date_to in one call as string
$page->date_range = '2024-04-08 - 2024-05-04';

// set both date_from and date_to in one call as array
$page->date_range = [ '2024-04-08', '2024-05-04' ];

// save the date range field after setting it to the page
$page->save('date_range');
```


### Querying date range fields from selectors

When it comes to querying date range fields from database matching selectors, there are many options. You can query the dates individually, perform partial text matching on then, match by year or year+month, match by number of days or nights, and match by whether the range is current, future or past.

When querying dates, I recommend using the `YYYY-MM-DD` (ISO-8601) date format. However, this module will work with any format recognized by PHP’s strtotime function.


### Querying date_from or date_to

```php
// find pages with date from greater than April 8, 2024
$pages->find('date_range.from>2024-04-08');

// find pages with date ranges between April 8 and May 4, 2024
$pages->find('date_range.from>=2024-04-08, date_range.to<=2024-05-04');

// find pages with any date_from in 2024
$pages->find('date_range.from=2024');

// find pages with date_from in 2023 and date_to in 2024
$pages->find('date_range.from=2023, date_range.to=2024');

// find pages with any date_from in December, 2023
$pages->find('date_range.from=2023-12');
```


### Finding pages by partial ranges

```php
// find pages with date ranges fully in December 2023
$pages->find('date_range=2023-12');

// find pages whether either date_from OR date_to in in 2024
$pages->find('date_range%=2024');

// find pages whether either date_from OR date_to is 2024-01-15
$pages->find('date_range%=2024-01-15');
```


### Finding pages by dates in range

```php
// find pages where Christmas is in the selected range
$pages->find('date_range.has=2024-12-25');

// find pages that don't have St. Patricks day in selected range
$pages->find('date_range.has!=2024-03-17');
```


### Finding by nights and days

```php
// find pages with ranges having fewer than 4 nights
$pages->find('date_range.nights<4');

// find pages with ranges between 5 and 8 days
$pages->find('date_range.days>=5, date_range.days<=10');
```


### Finding by current, past or future ranges

```php
// find pages that have ranges within the current date
$pages->find('date_range.current=1');

// find pages that have ranges fully in the past
$pages->find('date_range.past=1');

// find pages that have ranges fully in the future
$pages->find('date_range.future=1');
```

As you can see, there are a lot of different ways that you can query a date range field. A good way to test out different selectors and queries is by using Pages > Find (with ListerPro) in the ProcessWire admin, or by using Tracy Debugger's console. If you have any questions about how to use the Date Range field or its API, please don't hesitate to ask!


### Using a hook for dynamic settings at runtime

There are several settings in date range fields that can in many cases be more powerful to set dynamically at runtime, rather than predefined in configuration. For instance, settings like start and end dates set today likely won't be useful a year from now. In addition, disabled dates might be based on whether a property is already booked or not, which is not something you would know at the time you are creating your date range field. For this reason, all of the date range input settings can be modified by a hook named `InputfieldDateRange::getSettings`. Below is an example of using this hook to modify several settings at runtime:

```
$wire->addHookBefore('InputfieldDateRange::getSettings', function($e) {
  $f = $e->object; /** @var InputfieldDateRange $f */

  // skip if this isn't the field we want to modify
  if($f->name != 'date_range') return;

  // set max selectable date to be 1 year from today
  $f->endDate = wireDate('Y-m-d', '+1 year');

  // set min selectable date to be whatever date is the next Monday
  $f->startDate = wireDate('Y-m-d', 'Next Monday');

  // set Christmas and New Years Day to be disabled
  $f->disabledDates = [ '2023-12-25', '2024-01-01' ];

  // disable Sundays but only when month is January
  if(date('M') == 'Jan') $f->disabledDaysOfWeek = [ 'Sunday' ];
});
```

This hook could go in your /site/ready.php file. Or if this was a ProcessWire field only edited in the admin, you could put it in /site/templates/admin.php.


### Translating for other languages

All text and labels for the date selection calendar can be translated by pointing ProcessWire's translation tool to this file: /site/modules/FieldtypeDateRange/InputfieldDateRangeLabels.php. If you create a translation for the module, consider sharing it in the ProFields board. Like with any other module, labels can also be modified dynamically at runtime using the [wireLangReplacements](../api-full/wire/core/FunctionsAPI/index.md) function.


## Download

This module is currently available in the [ProFields](/talk/store/product/10-profields/) set of modules, and available for download to ProFields subscribers in the ProFields support board [download thread](/talk/topic/6413-profields-downloads-updated-15-september-2023/) (login required). The initial release version is a beta version, and the stable version will be posted by or before January 1, 2024.
