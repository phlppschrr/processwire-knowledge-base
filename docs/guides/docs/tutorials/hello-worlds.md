# Unknown

Source: https://processwire.com/docs/tutorials/hello-worlds/

In this tutorial you will learn how to create and work with templates, fields, pages, and how to output dynamic data via your templates. 

This tutorial plays on the 'hello world' phrase and lists information about planets in the solar system, starting with Earth. To keep it simple, we'll assume that the basic site profile is installed, as that's what comes with ProcessWire (so there's no need to uninstall anything). But we won't start using any of it's files at this stage. Instead, we'll start out by creating our own files.

After completing this tutorial you will have learned how to create and work with templates, fields, pages, and how to output dynamic data via your templates.

### Step 1 – Create a template file

Create a new file called: /site/templates/planet.php, and copy+paste the following HTML into that file:

```
<html>
  <head>
    <title>Earth</title>
  </head>
  <body>
    <h1>Earth</h1>
    <h2>Type: Happy planet, Age: Millions of years</h2>
    <p>Earth (or the Earth) is the third planet from the Sun,
    and the densest and fifth-largest of the eight planets
    in the Solar System. It is also the largest of the Solar
    System's four terrestrial planets. It is sometimes
    referred to as the World, the Blue Planet, or by its
    Latin name, Terra.</p>
  </body>
</html>
```

The above is just a plain HTML file with nothing specific to ProcessWire. We will use this as the starting point for our template, and we'll go back and modify it later.

---

## Create a Template and a Page

### Step 2 – Add a template to ProcessWire

- Login to ProcessWire admin and go to Setup > Templates. This page shows a list of templates currently in the system.
- Click the Add New Template button. On the next screen that appears, you'll see it found your "planet" template file.
- Check the box next to the planet template and click *Add Template*. You may ignore any other options that appear on this screen.

### Step 3 – Creating a page using your template

Your planet template is now in the system and ready to use, but it's not being used by any pages. So lets create a page that uses the planet template.

- In the ProcessWire admin, click Pages in the top navigation. This is a site map of your page structure. We want to create a new page under the homepage, so click the new link that appears to the right of the home page.
- The next screen has 3 inputs: title, name and template. Enter "Earth" for the title, and the name should populate automatically. For the template, select planet. Then click Save.
- Now you have created a new page using the template that you added. You are now in the page edit screen and you should see your title field populated with "Earth". Click the View link that appears on this page edit screen. You should see the output of the HTML from step 1. Click the back button in your browser to return to the edit screen.

---

## Setting up Custom Fields

### Step 4 – Creating a new field

Now you know how to create a template and a page using that template. You could create more pages using the same template if you wanted to. But that wouldn't be particularly useful – this template file is just a static HTML file.

Lets make it dynamic by creating some fields and adding them to it. We are going to create 3 fields to represent the pieces of data that currently appear in our static template. These include the planet's type, age in years, and a brief summary. We will call these fields: `planet_type`, `planet_age` and `planet_summary`.

- In ProcessWire admin, click Setup > Fields. This screen shows a list of fields currently in the system, most of which are general purpose fields for the basic profile. For the purposes of this tutorial, we are going to ignore those and create our own.
- Click the *Add New Field* button. On the next screen, enter `planet_type` for the Name, select "Text" as the Type, and enter "Planet Type" for the Label. Then click the *Save Field* button. Now that your field is saved, you are on the Field Edit screen. At this point, your field is created and ready to be added to your planet template.
- *Optional but recommended:* While editing your field, click the details tab where you'll see a select box for Text Formatters. Select "HTML Entity Encoder" – this ensures that characters like `<`, `>` and `&` will be converted to HTML entities and not confused as HTML tags. While not required, it's a good practice for text fields like this. After you've done that, click the *Save Field* button.

### Step 5 – Creating more new fields

In step 4 we created the planet_type field. Now we want to create the `planet_age` and `planet_summary` fields. So in this step, you'll want to do the same thing for the remaining two fields:

- Create the `planet_age` field exactly like you created the planet_type field, but enter "Planet age in years" for the label.
- Create the `planet_summary` field exactly like you created the `planet_type` field, but chose "Textarea" as the Type and enter "Planet summary" for the label.

*Note that a "textarea" field is just like a "text" field, except that it can contain multiple lines of text.*

### Step 6 – Adding new fields to your template

Now that you've created 3 new fields, you need to add them to your planet template.

- In ProcessWire admin, click Setup > Templates > planet. You are now editing your planet template.
- In the Fields select box, choose `planet_type`, then `planet_age`, then `planet_summary`. You will see each added to the list. Cick the *Save Template* button.

### Step 7 – Editing a page using your template

Now that you have new fields added to your template, go back and edit the Earth page you created earlier and populate the new fields that are on it.

- In ProcessWire admin, click Pages at the top, then click the Earth page, and click the edit button that appears to the right of it.
- You are now editing the Earth page you created earlier. You should see the new fields you added, waiting for text.
- Enter "Terrestrial planet" for Planet Type
- Enter "4.54 billion" for Planet Age in Years
- Paste in the text below for Planet Summary and then click Save.

> Earth (or the Earth) is the third planet from the Sun, and the densest and fifth-largest of the eight planets in the Solar System. It is also the largest of the Solar System's four terrestrial planets. It is sometimes referred to as the World, the Blue Planet, or by its Latin name, Terra.

---

## The Template File

### Step 8 – Outputting dynamic data in your template file

While still in the page editor from step 7, click the "View" link to see your page. Note that it still says "Happy planet" for type (rather than "Terrestrial planet") and "Millions of years" rather than "4.54 billion years". That's because the page is still being rendered with just the static data in it. We need to update the template file so that it recognizes the fields we added and outputs the values of those fields.

Edit /site/templates/planet.php and replace the static text in there with tags like this, replacing `field_name` with the name of the field:

```
<?php echo $page->field_name; ?>
```

If supported by your server, you may also use this shorter format which some people find easier to look at and faster to enter:

```
<?=$page->field_name?>
```

Here is the /site/templates/planet.php file updated to output the content of the page using tags like the above:

```
<html>
  <head>
    <title><?php echo $page->title; ?></title>
  </head>
  <body>
    <h1><?php echo $page->title; ?></h1>
    <h2>
        Type: <?php echo $page->planet_type; ?>,
        Age: <?php echo $page->planet_age; ?> years
    </h2>
    <p><?php echo $page->planet_summary; ?></p>
  </body>
</html>
```

After making these changes, save your planet.php template file. Now view your Earth page again. You should see it properly outputting all of the content you entered on the page, including "Terrestrial planet" for Type and "4.54 billion years" for age. Any changes you make from this point forward should be reflected in the output.

---

## More Pages

### Step 9 – Creating more pages, reusing your template

For this last step, we'll create another page (for Jupiter) using the same template just to demonstrate how a template may be reused.

- In ProcessWire Admin, click Pages and then click the new link to the right of the home page.
- Enter "Jupiter" as the Title and select "planet" for the Template. Click Save.
- Now that you are editing the Jupiter page, enter "Gas giant" for Type, enter "4.5 billion" for Age in Years, and copy+paste the following for Planet Summary:

> Jupiter is the fifth planet from the Sun and the largest planet within the Solar System.[13] It is a gas giant with mass one-thousandth that of the Sun but is two and a half times the mass of all the other planets in our Solar System combined. Jupiter is classified as a gas giant along with Saturn, Uranus and Neptune. Together, these four planets are sometimes referred to as the Jovian or outer planets.

- Click the Publish button and then View the page. You should now see your planet template being used to output the information for Jupiter rather than Earth.

---

## Conclusion

In this tutorial, we covered the basics of how to develop in ProcessWire, including the following:

- Creating templates and their associated template files
- Creating basic text fields and adding them to templates
- Creating and editing pages that use your templates
- Outputting the values of fields in template files

- [Tutorials](/docs/tutorials/)
- [A Beginner’s Guide To ProcessWire](https://www.smashingmagazine.com/2016/07/the-aesthetic-of-non-opinionated-content-management-a-beginners-guide-to-processwire/)
- [How to install and setup ProcessWire CMS](https://webdesign.tutsplus.com/tutorials/how-to-install-and-setup-processwire-cms--cms-25509)
- [Hello Worlds](/docs/tutorials/hello-worlds/)
- [How to Create an AJAX Driven Theme for ProcessWire](https://webdesign.tutsplus.com/tutorials/how-to-create-an-ajax-driven-theme-for-processwire--cms-26579)
- [A Beginner’s Introduction to Writing Modules in ProcessWire](https://webdesign.tutsplus.com/tutorials/a-beginners-introduction-to-writing-modules-in-processwire--cms-26862)
- [Extending the ProcessWire Admin Using Custom Modules](https://webdesign.tutsplus.com/tutorials/extending-the-processwire-admin-using-custom-modules--cms-26863)
- [How to Develop a Processwire Theme](https://webdesign.tutsplus.com/tutorials/how-to-develop-a-processwire-theme--cms-25692)
- [Default site profile](/docs/tutorials/default-site-profile/)
- [How to structure your template files](/docs/tutorials/how-to-structure-your-template-files/)
- [Using custom page types in ProcessWire](/docs/tutorials/using-custom-page-types-in-processwire/)
- [More tutorials](https://www.pwtuts.com)

- [Docs](/docs/)
- [API reference](/api/ref/)
- [Getting started](/docs/start/)
- [Front-end](/docs/front-end/)
- [Tutorials](/docs/tutorials/)
- [Selectors](/docs/selectors/)
- [Modules & hooks](/docs/modules/)
- [Fields, types, input](/docs/fields/)
- [Access control](/docs/user-access/)
- [Security](/docs/security/)
- [Multi-language](/docs/multi-language-support/)
- [More topics](/docs/more/)
