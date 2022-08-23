import dash
from dash import html, Output, Input, State, dcc
import joblib

app = dash.Dash(__name__)
main_div = html.Div(id="main-div",
                    children=html.Button("Enter", className="enter-button", id="enter-button"))
lock_div = html.Div(id="lock-div", className="lock-body",
                    children=html.Div([html.Img(src="assets/lock2.png"),
                                       html.Div(className="flex-col",
                                       children=[
                                           dcc.Input(id="username-input",
                                                     placeholder="Pleas enter username"),
                                           html.Button(id="username-button", children="OPEN", className="username-button")]),
                                       dcc.ConfirmDialog(id="message", message="You are not authorized to open the safe", displayed=False)]),
                    style={"display": "none"})

money_div = html.Div(id="money-div", className="money-body",
                     children=html.Div(
                         "You Stole The Money!", className="success"),
                     style={"display": "none"})

app.layout = html.Div(id="body",
                      className="main-body",
                      children=[main_div, lock_div, money_div])


@ app.callback(Output("main-div", "style"),
               Output("lock-div", "style"),
               Output("money-div", "style"),
               Output("message", "displayed"),
               Input("enter-button",
                     "n_clicks"), Input("username-button", "n_clicks"),
               State("username-input", "value"), prevent_initial_call=True)
def new_page(n_clicks1, n_clicks2, username):
    print(dash.callback_context.triggered)
    if dash.callback_context.triggered[0]["prop_id"].startswith("enter-button"):
        return {"display": "none"}, {}, dash.no_update, dash.no_update
    elif dash.callback_context.triggered[0]["prop_id"].startswith("username-button"):
        authorized_users = joblib.load("lst.zlib")
        if username in authorized_users:
            return {"display": "none"}, {"display": "none"}, {}, dash.no_update
        else:
            return dash.no_update, dash.no_update, dash.no_update, True
    return dash.no_update, dash.no_update, dash.no_update, dash.no_update


app.run_server(debug=True)
