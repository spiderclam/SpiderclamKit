# SpiderclamKit

Just a blender addon for myself.

## Installation

Download zip. Install zip. Idk, you'll figure it out.

## Usage

This addon is currently only a pie menu in pose mode, which is toggled by pressing the `o` key. 

## Operations

I'll try my best to document the included operations. It's easy now, since I barely have any.

### Limit Distance bone constraint

Some operations that help with the bone constraint "Limit Distance".

#### SetDistanceBySelected

Allows you to quickly get and set the distance of selected bones on the active bone's limit distance constraint.

##### Usage:

Select all the bones in the chain of which you want the sum of their lengths to be set as the distance on the last selected bone and run the operation.

##### Notes:

- The last selected bone's length is not included in the sum
- The last selected bone must have a Limit Distance constraint set up

## Naming

I have no clue about naming conventions, since every addon seems to do its own thing.

So I made my own and documented the parts I care about.

### `bl_idname`

> sc.{abbreviation}\_{operation_name_in_snake_case}

Where sc stands for spiderclam

For example the `limit_distance_constraint` submodule of the `constraint_operations` module would have the abbreviation `co_ldc`.

Inside of that submodule is an operation class named `SetDistanceBySelected`.

So the full id would be:

`sc.co_ldc_set_distance_by_selected`

## LICENSE

MIT
