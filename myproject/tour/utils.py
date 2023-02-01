import plotly.graph_objects as go

def get_plot(df, title: str, legends: list[str], ylabel: str):
    fig = go.Figure()
    for data, legend in zip(df.columns, legends):
        fig.add_trace(go.Scatter(
            x=df.index, 
            y=df[data], 
            name=legend
            ))
    fig.update_layout(title=title,
                      xaxis_title="Data", 
                      yaxis_title=ylabel)
    fig.update_layout(height=600)
    fig.update_xaxes(tickformat="%Y-%m-%d")
    graph_html = fig.to_html(full_html=False)
    return graph_html
