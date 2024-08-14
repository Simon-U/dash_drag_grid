# AUTO GENERATED FILE - DO NOT EDIT

#' @export
toolBox2 <- function(id=NULL, breakpoints=NULL, component=NULL, items=NULL, layouts=NULL, linkedId=NULL, style=NULL, title=NULL) {
    
    props <- list(id=id, breakpoints=breakpoints, component=component, items=items, layouts=layouts, linkedId=linkedId, style=style, title=title)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'ToolBox2',
        namespace = 'dash_drag_grid',
        propNames = c('id', 'breakpoints', 'component', 'items', 'layouts', 'linkedId', 'style', 'title'),
        package = 'dashDragGrid'
        )

    structure(component, class = c('dash_component', 'list'))
}
