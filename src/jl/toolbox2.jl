# AUTO GENERATED FILE - DO NOT EDIT

export toolbox2

"""
    toolbox2(;kwargs...)

A ToolBox2 component.

Keyword arguments:
- `id` (String; optional)
- `breakpoints` (Dict; optional)
- `items` (Array; required)
- `layouts` (Dict; optional)
- `linkedId` (String; optional)
- `style` (Dict; optional)
- `title` (String; optional)
"""
function toolbox2(; kwargs...)
        available_props = Symbol[:id, :breakpoints, :items, :layouts, :linkedId, :style, :title]
        wild_props = Symbol[]
        return Component("toolbox2", "ToolBox2", "dash_drag_grid", available_props, wild_props; kwargs...)
end

