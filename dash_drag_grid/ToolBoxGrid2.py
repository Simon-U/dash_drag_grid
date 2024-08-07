# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class ToolBoxGrid2(Component):
    """A ToolBoxGrid2 component.


Keyword arguments:

- children (list of a list of or a singular dash component, string or numbers | a list of or a singular dash component, string or number; optional):
    Children is a list of the items (dash Components and/or
    DashboardItem) to diplay on the layout. By default all the items
    can be dragged and resized.

- id (string; optional):
    (string) The ID used to identify this component in Dash callbacks.
    The id is also used to automatically save the layout on client
    side.

- autoSize (boolean; default True):
    (bool) Other props defined by react-grid-layout If True, the
    container height swells and contracts to fit contents.

- breakpoints (dict; optional):
    ({breakpoint: number}) The breakpoints for the responsive layout.
    For each screen size (breakpoint) we can define a different
    layout. (see also 'layouts' and 'gridCols' arguments) Default
    value is {lg: 1200, md: 996, sm: 768, xs: 480, xxs: 0}.

- className (string; default ''):
    (string) class passed to the react-grid-layout component.

- clearSavedLayout (boolean; default False):
    (bool) If set to True, the position of elements saved on client
    side will be cleared on the next page load.

- compactType (a value equal to: 'vertical', 'horizontal'; default 'vertical'):
    Compaction type.

- containerPadding (list of numbers | dict; default [10, 10]):
    Padding inside the container [x, y] in px.

- currentBreakpoint (string; default 'lg'):
    current breakpoint.

- defaultInToolbox (boolean; default False):
    This value sets if children, which do not have inToolbox defined,
    should be in the Toolbox by default.

- deleteOnRemove (boolean; optional):
    When an item is removed from the grid, delete it's underlying
    element rather than just hiding it.

- draggableCancel (string; default ''):
    (string) A CSS selector for tags that will not be draggable. or
    example: draggableCancel:'.MyNonDraggableAreaClassName' If you
    forget the leading . it will not work.

- draggableHandle (string; default ''):
    A CSS selector for tags that will act as the draggable handle. For
    example: draggableHandle:'.MyDragHandleClassName' If you forget
    the leading . it will not work.

- enableToolbox (boolean; default True):
    When set to False no toolbox will be rendered.

- gridCols (dict; optional):
    ({breakpoint: number}) the number of columns in the grid layout.
    Default value is {lg: 12, md: 10, sm: 6, xs: 4, xxs: 2}.

- height (number; optional):
    (number) height of a row (in px). Default value is 30.

- isBounded (boolean; default False):
    Are items resizable.

- isDraggable (boolean; default True):
    Are items draggable.

- isDroppable (boolean; default True):
    If True, droppable elements (with `draggable={True}` attribute)
    can be dropped on the grid. It triggers \"onDrop\" callback with
    position and event object as parameters. It can be useful for
    dropping an element in a specific position  NOTE: In case of using
    Firefox you should add `onDragStart={e =>
    e.dataTransfer.setData('text/plain', '')}` attribute along with
    `draggable={True}` otherwise this feature will work incorrect.
    onDragStart attribute is required for Firefox for a dragging
    initialization  @see
    https://bugzilla.mozilla.org/show_bug.cgi?id=568313.

- isResizable (boolean; default True):
    Are items resizable.

- layouts (dict; optional):
    Layout is a list(python)/vector(R) of dictionnary(Python)/list(R)
    with the format: {x: number, y: number, w: number, h: number} The
    index into the layout must match the id used on each item
    component with DashboardItem. If you choose to use custom keys,
    you can specify that key in the layout array objects like so: {i:
    string, x: number, y: number, w: number, h: number} The ID used to
    identify this component in Dash callbacks. The id is also used to
    automatically save the layout on client side.

- margin (list of numbers | dict; default [10, 10]):
    Margin between items [x, y] in px.

- ncols (dict; optional):
    ({breakpoint: number}) the default number of columns by item.
    Default value is {lg: 6, md: 5, sm: 3, xs: 4, xxs: 2}.

- nrows (number; optional):
    (number) the default number of row by item. Default value is 8.

- onDropHeight (number; default 5):
    Set the default height of items that are dropped from the toolbox
    into the grid. default is 5.

- onDropWidth (number; default 4):
    Set the default height of items that are dropped from the toolbox
    into the grid. default is 4.

- preventCollision (boolean; default False):
    If True, grid items won't change position when being dragged over.

- resizeHandles (list of a value equal to: 's', 'w', 'e', 'n', 'sw', 'nw', 'se', 'ne's; default ['se']):
    Defines which resize handles should be rendered Allows for any
    combination of: 's' - South handle (bottom-center) 'w' - West
    handle (left-center) 'e' - East handle (right-center) 'n' - North
    handle (top-center) 'sw' - Southwest handle (bottom-left) 'nw' -
    Northwest handle (top-left) 'se' - Southeast handle (bottom-right)
    'ne' - Northeast handle (top-right).

- save (boolean; default True):
    (bool) If True, then the layout is automatically saved on client
    browser. Default value is True.

- style (dict; optional):
    (dict) css style passed to the react-grid-layout component.

- toolbox (dict; default { lg: [], md: [], sm: [] }):
    The toolbox layout.

- toolboxTitle (string; optional):
    (string) The title above the toolbox.

- transformScale (number; default 1):
    If parent DOM node of ResponsiveReactGridLayout or ReactGridLayout
    has \"transform: scale(n)\" css property, we should set scale
    coefficient to avoid render artefacts while dragging.

- useCSSTransforms (boolean; default True):
    Uses CSS3 translate() instead of position top/left. This makes
    about 6x faster paint performance.

- verticalCompact (boolean; default True):
    If True, the layout will compact vertically."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_drag_grid'
    _type = 'ToolBoxGrid2'
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, layouts=Component.UNDEFINED, breakpoints=Component.UNDEFINED, gridCols=Component.UNDEFINED, toolboxTitle=Component.UNDEFINED, toolboxComponent=Component.UNDEFINED, save=Component.UNDEFINED, clearSavedLayout=Component.UNDEFINED, ncols=Component.UNDEFINED, nrows=Component.UNDEFINED, height=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, autoSize=Component.UNDEFINED, draggableCancel=Component.UNDEFINED, draggableHandle=Component.UNDEFINED, verticalCompact=Component.UNDEFINED, compactType=Component.UNDEFINED, margin=Component.UNDEFINED, containerPadding=Component.UNDEFINED, isDraggable=Component.UNDEFINED, isResizable=Component.UNDEFINED, isBounded=Component.UNDEFINED, useCSSTransforms=Component.UNDEFINED, transformScale=Component.UNDEFINED, preventCollision=Component.UNDEFINED, isDroppable=Component.UNDEFINED, resizeHandles=Component.UNDEFINED, toolbox=Component.UNDEFINED, currentBreakpoint=Component.UNDEFINED, onDropHeight=Component.UNDEFINED, onDropWidth=Component.UNDEFINED, defaultInToolbox=Component.UNDEFINED, enableToolbox=Component.UNDEFINED, deleteOnRemove=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'autoSize', 'breakpoints', 'className', 'clearSavedLayout', 'compactType', 'containerPadding', 'currentBreakpoint', 'defaultInToolbox', 'deleteOnRemove', 'draggableCancel', 'draggableHandle', 'enableToolbox', 'gridCols', 'height', 'isBounded', 'isDraggable', 'isDroppable', 'isResizable', 'layouts', 'margin', 'ncols', 'nrows', 'onDropHeight', 'onDropWidth', 'preventCollision', 'resizeHandles', 'save', 'style', 'toolbox', 'toolboxTitle', 'transformScale', 'useCSSTransforms', 'verticalCompact']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'autoSize', 'breakpoints', 'className', 'clearSavedLayout', 'compactType', 'containerPadding', 'currentBreakpoint', 'defaultInToolbox', 'deleteOnRemove', 'draggableCancel', 'draggableHandle', 'enableToolbox', 'gridCols', 'height', 'isBounded', 'isDraggable', 'isDroppable', 'isResizable', 'layouts', 'margin', 'ncols', 'nrows', 'onDropHeight', 'onDropWidth', 'preventCollision', 'resizeHandles', 'save', 'style', 'toolbox', 'toolboxTitle', 'transformScale', 'useCSSTransforms', 'verticalCompact']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(ToolBoxGrid2, self).__init__(children=children, **args)
