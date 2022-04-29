def setup_views(container):
    app = container.app()

    app.add_url_rule('/api/prediction', methods=['GET'], view_func=container.get_prediction.as_view())

