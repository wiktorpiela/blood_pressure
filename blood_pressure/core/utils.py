import seaborn as sns
import matplotlib.pyplot as plt
import base64
from io import BytesIO

def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format="png")
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode("utf-8")
    buffer.close()
    return graph

def get_plot(timestamp, sys, dia, hr):
    plt.switch_backend("AGG")
    plt.figure(figsize=(10,4))
    plt.plot(timestamp, sys, label="górne")
    plt.plot(timestamp, dia, label="dolne")
    plt.plot(timestamp, hr, label="puls")
    plt.xticks([])
    plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.15), ncol=3)
    plt.rcParams.update({'font.size': 18})
    graph = get_graph()
    return graph