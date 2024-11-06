## Version 1.2.0
_Release date: 6 November 2024_

**Updated**
* BREAKING CHANGE: The navigation slot in the NavigationDrawerLayout and the NavigationRailLayout now have the same name. This means that if you change the layout of your Form, the components in the navigation slot will stay there. For existing apps, components that were in a navigation slot will need to be dragged from the orphaned components panel back into the correct slot.
* The SidesheetContent component is now pre-populated with a Heading and IconButton
* The RadioGroupPanel component is now pre-populated with three RadioButtons
* When using the NavigationDrawerLayout that has collapsed to mobile view, you can now double click on the hamburger menu button in the designer to open the navigation drawer
* Some components had `background` properties that are now renamed to `background_color`
* In the designer, the NavigationDrawerLayout won't collapse to modal view until the screen is smaller
* When Text and Heading components have no `text`, their component names actually look like placeholders
* The `label` of a TextArea can now be edited from the Object Palette or by double clicking the component

**Fixed**
* FileLoader now has a `files` property that works as expected
* DataGrids now work as expected - they automatically populated with a RepeatingPanel
* Fixed and issue where DropdownMenu items were being duplicated with the `form_show` event was fired
* Fixed an issue where you couldn't make changes to DropdownMenu items once the component was rendered
* Material Icons no longer flash as text before being rendered as icons
* Fixed an issue where Data Binding writeback wasn't working for TextBoxes and TextAreas
* Setting the `align` property of ButtonMenus to `full` now works
* The `align` property of Links now works
* Fixed an issue where the ButtonMenu menu was behind popup menus
* The `display_text_color` property of TextBoxes and TextAreas now works
* Links in built-in Anvil modals are now properly styled
