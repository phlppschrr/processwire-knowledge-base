# CMS Repeater fields (aka Matrix fields) using FieldtypeRepeater in ProcessWire

Source: https://processwire.com/docs/fields/repeaters/

## Summary

The repeater fieldtype enables you to create a group of fields and make it repeatable in any quantity on your page. This opens many new possibilities with how you might manage and structure data.

## Key Points

- feet_high
- num_floors
- year_built

## Sections


## Repeatable Fields / Matrix Fields

The repeater fieldtype enables you to create a group of fields and make it repeatable in any quantity on your page. This opens many new possibilities with how you might manage and structure data.

Repeatable fields are also referred to as matrix fields in some other platforms. We refer to them as repeatable fields or repeaters, but they are all the same thing. Below is a video that demonstratates how to create and use a repeater field. I suggest viewing the video full screen to see the higher resolution version.

While this is an old video, it still does a good job of demonstrating the basics of repeaters.


### When to use repeaters

Repeaters are ideal for managing simple-to-complex groups of information in smaller known or unknown quantities. Things like rate tables, locations, product variations, staff directories, photo galleries with meta data, and so on might be a good fit with repeaters. The sky is the limit.

Choose repeaters when they will represent a good long term, and short-term, solution to a problem. If you know the quantity of repeated items will stay at a reasonable size on the given pages despite time and scale, repeaters are a good solution to consider.


### When not to use repeaters

Repeaters aren't infinitely scalable in quantity, so avoid repeaters for quantities of items that you think may need to be infinitely scalable. When you edit a repeater field in your page, you edit all items at once. As a result, you probably don't want to use a repeater if you expect hundreds of items, as that may slow your editing experience. It's better to use pages without repeaters when dealing with huge quantities of items.

You also don't want to use repeaters for items of content that you want to have their own URL. Individual repeater items don't have individual URLs, so repeaters are better for items that you will be showing as a group on one page. However, there's nothing preventing you from attaching repeater items to URL segments or GET variables (for example), but consider whether you would be better off just using regular pages.


## How to use repeaters


### How to create a repeatable field

The repeaters fieldtype is not installed by default. To install, login to your ProcessWire admin and click to Modules. Locate the Fieldtype section and click the Install button for the Repeater fieldtype.

Next create the individual fields that will live in your repeater. Create these fields like you would any other, from Setup > Fields > Add New Field. Lets say that I wanted to create fields to hold data for skyscrapers. I might plan to re-use the built-in title field for my building name, and then create these 3 new fields:

- feet_high
- num_floors
- year_built

Once you've created the fields you want to use with your repeater, you can go on to create the actual repeater field. Click Setup > Fields > Add New Field, and choose "Repeater" as the field type. Continuing the example above, I might name my field "buildings". Click Save and the repeater field will be created.

Now you want to add the title, feet_high, num_floors and year_built fields to your repeater. Click the details tab while editing your repeater field. Select those fields to add them. Drag them to the order you want. Then click Save.

After saving, you may want to customize the title field so that it has a label of "Building Name" rather than "Title". While still in the details tab, click the name "title" in your list of fields. It will pop open a modal window enabling you to change the context of the title field when used in this buildings repeater field. Change the label to "Building Name" and click Save. Now click Save again in the field editor.

Next you want to add your buildings repeater field to a template. Go to Setup > Templates and click an existing template to edit. In my case, I'm editing my "home" template. In the field selection box, select the field "buildings" (or whatever you named your repeater field) to add it to the template. Then click Save.

Now you can edit or create any pages using that template and they will have the repeater field available. All you need to do to add a repeater is click "add new", populate your content and Save your page.


### Outputting repeatable fields

The individual items contained in a repeater field are technically pages in ProcessWire. The value of a repeater field is a PageArray. As a result, you may interact with them exactly like you would any other group of pages in ProcessWire. You might iterate through and output the group of items like this (using the fictional buildings repeater, created in the previous section):

```
foreach($page->buildings as $building) {
    echo "<h2>{$building->title}</h2><p>";
    echo "Height: {$building->feet_high} feet, ";
    echo "Floors: {$building->num_floors}, ";
    echo "Year built: {$building->year_built} </p>";
}
```

That's all there is to it. Everything that you know about outputting any other pages in ProcessWire applies to outputting repeaters.


### Testing for an empty value

Like with any other PageArray, you can tell how many items there are by using count():

```
if(count($page->buildings)) {
    echo "<p>There are " . count($page->buildings) . " buildings.</p>";
} else {
    echo "<p>There are no buildings.</p>";
}
```


### Finding pages by repeater value (using selectors)

Use selector subfields to locate pages by a value in a repeater field. Subfields are those that are split with a period, like "field.subfield". This is best demonstrated by examples, again continuing with our buildings field, we will locate pages that have a buildings repeater field by properties of the individual buildings within that repeater field:

```php
// find all pages that have at least one building with a height > 500 feet
$buildings = $pages->find("buildings.height>500");

// find all pages that have a building made in 1940 with at least 20 floors
$buildings = $pages->find("buildings.year_built=1940, buildings.num_floors>=20");

// find all pages using the basic-page template with at least 1 building
$buildings = $pages->find("template=basic-page, buildings.count>0")
```


### Using the API to add or remove repeater items

Unlike other pages in ProcessWire, new repeater items must be created by ProcessWire rather than you. As a result, a helper method is provided called getNew(). You may call getNew() on any repeater field to get a new item. The item that it returns is ready to populate and has already been added to the repeater. Once populated, you simply save the page that the repeater field is on.

```
$building = $page->buildings->getNew();
$building->title = 'One Atlantic Center';
$building->feet_high = 880;
$building->num_floors = 50;
$building->year_built = 1997;
$building->save();
$page->buildings->add($building);
$page->save();
```

Remove a repeater item in exactly the same way you remove an item from any other PageArray:

```
$building = $page->buildings->first(); // or whatever item you want to remove
$page->buildings->remove($building);
$page->save();
```


### Implementing templates for repeater fields

While not commonly done, you can actually implement template files for your repeater fields, if you want to.

If you want to implement a template file for your repeater, you create a file in your /site/templates/ named "repeater_[field name].php", i.e. in the case of the buildings field, it would be "repeater_buildings.php". That template file will receive a $page variable that is represents one 'buildings' record. So you could do something like this:

/site/templates/repeater_buildings.php

```
echo "<h2>{$page->building_name}</h2>"; 
echo "<p>{$page->floors} floors, {$page->height} feet</p>";
```

The template used by your page with a 'buildings' field could then do this:

/site/template/basic-page.php

```
foreach($page->buildings as $building) {
    echo $building->render();
}
```


### See also

Repeater Matrix
