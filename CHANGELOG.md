## Version 1.2.1
_Release date: 15 November 2024_

**Updates**
* When in the designer, the placeholder text for the Link looks more like placeholder text
  
**Fixes**
* The Dropdown border is now rounded on the dropdown menu 
* Fixed an issue with the Dropdown where when the items are a list of tuples, the selected_value is the entire tuple
* Fixed an issue where the label text for Dropdowns was appearing beind the outline
* Add writeback support for various components (Checkbox, DropdownMenu, RadioGroupPanel, Switch)
* Placeholder text reappears when a component is removed from a Link
* Added close button to Notifications and Confirms
* Added click event parameters to all click events. Add the keys argument to ButtomMenus, IconButtons and ToggleIconButtons
* Added slider change_end event

## Version 1.2.0
_Release date: 6 November 2024_

**Breaking Changes**
* The navigation slot in the NavigationDrawerLayout and the NavigationRailLayout now have the same name. This means that if you change the layout of your Form, the components in the navigation slot will stay there. For existing apps, components that were in a navigation slot will need to be dragged from the [orphaned components panel](https://anvil.works/docs/ui/layouts#orphaned-components) back into the correct slot.

**Updates**
* The SidesheetContent component is now pre-populated with a Heading and IconButton.
* The RadioGroupPanel component is now pre-populated with three RadioButtons.
* When using the NavigationDrawerLayout that has collapsed to mobile view, you can now double click on the hamburger menu button in the designer to open the navigation drawer.
* Some components had `background` properties that are now renamed to `background_color`.
* In the designer, the NavigationDrawerLayout won't collapse to modal view until the screen is smaller.
* When Text and Heading components have no `text`, their component names actually look like placeholders.
* The `label` of a TextArea can now be edited from the Object Palette or by double clicking the component.

**Fixes**
* FileLoader now has a `files` property that works as expected.
* DataGrids now work as expected - they're automatically populated with a RepeatingPanel.
* Fixed an issue where DropdownMenu items were being duplicated when the `show` event was fired.
* Fixed an issue where you couldn't make changes to DropdownMenu items once the component was rendered.
* Material Icons no longer flash as text before being rendered as icons.
* Fixed an issue where Data Binding writeback wasn't working for TextBoxes and TextAreas.
* Setting the `align` property of ButtonMenus to `full` now works.
* The `align` property of Links now works.
* Fixed an issue where the ButtonMenu menu rendered behind popup menus.
* The `display_text_color` property of TextBoxes and TextAreas now works.
* Links in built-in Anvil modals are now properly styled.
