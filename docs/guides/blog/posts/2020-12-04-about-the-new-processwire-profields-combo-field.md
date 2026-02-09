# About the new ProcessWire ProFields Combo Field

Source: https://processwire.com/blog/posts/about-the-new-processwire-profields-combo-field/

## Sections


## About the new ProcessWire ProFields Combo Field

4 December 2020 by Ryan Cramer [ 13 Comments](/blog/posts/about-the-new-processwire-profields-combo-field/#comments)

This week we’ll take a brief look at a powerful new ProFields module for ProcessWire that’s just around the corner—the Combo field.

In last week's forum post about [ProcessWire 3.0.169](https://processwire.com/talk/topic/24706-pw-30169-%E2%80%93-core-updates/), I briefly mentioned the new ProFields Combo field that's in development and coming soon (likely this month). Like many of the ProFields, it includes 2 parts: “FieldtypeCombo” and “InputfieldCombo”. Unlike other ProFields, the Inputfield part can be used independently of the Fieldtype. Meaning it can be used in FormBuilder forms or any other ProcessWire form.

While the Combo field does have some crossover with other ProFields, it’s also something very different that I think will fill a common need. I’m particularly excited about it because I think it really rounds out the ProFields set of modules nicely, and it’s the one ProFields module that I anticipate using the most out of all of them.


### One field, any number of combinations

The word “Combo” in this case refers to “Combination”. A Combo field lets you have a combination of different fields within it. But unlike other ProFields modules, or other solutions in ProcessWire, the fields in your Combo don’t use other ProcessWire fields, and it doesn’t use other ProcessWire pages. So a single Combo field can have as many other fields in it as you want, but it’s still just 1 field in ProcessWire, and it consumes no more resources that 1 field in ProcessWire, making it especially efficient.


### A simple Combo example

If you are still wondering just what a Combo field is and how it works, I think the best way to explore that is with a simple example. Let’s say that we want to have a field named `mailing_address` that contains the combination of fields necessary to hold each of the following pieces of information independently:

- first name
- last name
- street address
- city
- state or province
- zip or postal code
- country

The above would be comprised of a combination of text, select, and/or Page reference fields/inputs. Without the Combo field, we would need to create fields in ProcessWire for each of those aspects of a mailing address, and then add them to a template (perhaps also in a Fieldset). This is fine of course, no problem. But the goal of ProFields is to reduce the quantity of fields necessary to accomplish a particular task, so we prefer fewer fields when possible. The Combo field really takes that goal to the next level.

Here’s how our new `mailing_address` field looks in the Page editor:


### Familiar and straightforward API

As you might guess, in our template file, we can simply refer to any of the fields as properties of the `mailing_address` field, like this (using `first_name` as an example):

```
echo $page->mailing_address->first_name;
```

If you want to search for "Frank" in the `mailing_address.first_name` field across all pages, you can do so like this:

```php
$results = $pages->find("mailing_address.first_name=Frank");
```

Or if you want to search for the word "Frank" in all `mailing_address` fields, you can do so like this:

```php
$results = $pages->find("mailing_address~=Frank");
```

Basically, if you’ve used ProcessWire for anything else, then you already know how to use a Combo field from the coding side. But the Combo field makes it particularly straightforward and without compromise.


### Easy to create and manage

Defining a Combo field is really simple. Below are a couple screenshots of how it looks in the field editor (Setup > Fields > mailing_address):

The selectable type options that you see in the screenshot above are Inputfield modules. The above are just what happens to be installed on a core installation without any 3rd party modules (other than the Combo field), but you can install other types to use with Combo fields too.


### Fast and efficient storage

When it comes to storage in the database, the Combo field is also unique. It stores data in individual DB columns like the ProFields Table field, but also keeps a combined index, making it possible to perform text matching searches on all data in a Combo field at once. This makes it fast and efficient for searches, whether a granular search on a single property, or a wide search on all properties.

I’m aiming to have the Combo field ready for release in the ProFields support/upgrades board by the end of the year, which is this month. I should have more information about the Combo field in the next couple of weeks as well. But if you have any questions, feel free to ask anytime. Thanks for reading, have a great weekend, and enjoy the latest [ProcessWire Weekly](https://weekly.pw)!
