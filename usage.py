from dash import Dash, callback, html, Input, Output
import dash_drag_grid
import dash_mantine_components as dmc
from dash_iconify import DashIconify

app = Dash(__name__)

toolBox = [
    dash_drag_grid.DashboardItemResponsive(
        children=[html.Div('Test 1'), dmc.Space(h=5), dmc.Text("This is a longer example lorem ipsum text to fill the content of the dif more")],
        id='test1',
        h=5,
        w=5,
        x=0,
        y=0,
        inToolbox=False,
        defaultName="Test Component 1"
    ),
    dash_drag_grid.DashboardItemResponsive(
        children=[html.Div('Test 2'), dmc.Space(h=5), dmc.Text("This is a longer example lorem ipsum text to fill the content of the dif more")],
        id='test2',
        h=5,
        w=5,
        x=0,
        y=0,
        inToolbox=False,
        defaultName="Default name for Test 2"
    ),
    dash_drag_grid.DashboardItemResponsive(
        children=[html.Div('Test 3'), dmc.Space(h=5), dmc.Text("This is a longer example lorem ipsum text to fill the content of the dif more")],
        id='test3',
        h=5,
        w=5,
        x=0,
        y=0,
        inToolbox=True
    ),
    dash_drag_grid.DashboardItemResponsive(
        children=[html.Div('Test 4'), dmc.Space(h=5), dmc.Text("This is a longer example lorem ipsum text to fill the content of the dif more")],
        id='test4',
        h=5,
        w=5,
        x=0,
        y=0,
        inToolbox=False
    ),
    dash_drag_grid.DashboardItemResponsive(
        children=[html.Div('Test 5'), dmc.Space(h=5), dmc.Text("This is a longer example lorem ipsum text to fill the content of the dif more")],
        id='test5',
        h=5,
        w=5,
        x=0,
        y=0,
        inToolbox=False
    ),
    dash_drag_grid.DashboardItemResponsive(
        children=[html.Div('Test 6'), dmc.Space(h=5), dmc.Text("This is a longer example lorem ipsum text to fill the content of the dif more")],
        id='test6',
        h=3,
        w=2,
        x=0,
        y=0,
        inToolbox=False,
        toolboxContent=[DashIconify(icon="ion:logo-github", width=30), html.Div('icon test')]
    ),
]

toolBoxItems = [
    dash_drag_grid.ToolboxItem(
        id='test1',
        inToolbox=False
    ),
    dash_drag_grid.ToolboxItem(
        id='test2',
        inToolbox=False
    ),
    dash_drag_grid.ToolboxItem(
        id='test3',
        inToolbox=True
    ),
    dash_drag_grid.ToolboxItem(
        id='test4',
        inToolbox=False
    ),
    dash_drag_grid.ToolboxItem(
        id='test5',
        inToolbox=False,
        children=[html.Div('test 5')]
    ),
    dash_drag_grid.ToolboxItem(
        id='test6',
        inToolbox=False,
        children=[DashIconify(icon="ion:logo-github", width=30), html.Div('icon test')]
    ),
]

app.layout = dmc.Container(
    [dash_drag_grid.ToolBox2(title="Detached Toolbox", items=toolBoxItems, linkedId='test'), dash_drag_grid.ToolBoxGrid2(toolBox, id='test', deleteOnRemove=True)],
    fluid=True,
    style={'backgroundColor': 'grey'}
)

if __name__ == '__main__':
    app.run_server(debug=True)
