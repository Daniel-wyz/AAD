import uuid, base64
from io import BytesIO
import matplotlib.pyplot as plt
import seaborn as sns


def is_ajax(request):
    return request.META.get("HTTP_X_REQUESTED_WITH") == "XMLHttpRequest"


def generate_code():
    code = str(uuid.uuid4()).replace("-", "").upper()[:12]
    return code


def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format="png")
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode("utf-8")
    buffer.close()
    return graph


def get_chart(chart_type, data, x_key, y_key, **kwargs):
    plt.switch_backend("AGG")
    fig = plt.figure(figsize=(10, 4))

    # d = data.groupby(key, as_index=False)["total_price"].agg("sum")

    if chart_type == "Bar Chart":
        print("bar chart")
        sns.barplot(x=x_key, y=y_key, data=data)
    elif chart_type == "Pie Chart":
        print("pie chart")
        plt.pie(data=data, x=x_key, labels=data[x_key].values)
    elif chart_type == "Line Chart":
        print("line chart")
        sns.lineplot(x=x_key, y=y_key, data=data)
        # plt.plot(
        #     data[x_key], data[y_key], color="green", marker="o", linestyle="dashed"
        # )
    else:
        print("ups... failed to identify the chart type")
    plt.tight_layout()
    chart = get_graph()
    return chart
