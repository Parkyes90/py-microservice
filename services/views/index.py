from flakon import JsonBlueprint


index = JsonBlueprint("index", __name__)


@index.route("/")
def index_view():
    """Index View"""
    return {}
