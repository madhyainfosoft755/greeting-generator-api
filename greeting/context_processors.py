# myapp/context_processors.py

def breadcrumb_context(request):
    breadcrumb_items = []
    if request.path == '/':
        breadcrumb_items.append({'name': 'Home', 'url': '/', 'active': True})
    else:
        # Example for dynamic paths, adapt to your routing structure
        paths = request.path.strip('/').split('/')
        current_url = '/'
        for i, path in enumerate(paths):
            current_url += path + '/'
            is_last = (i == len(paths) - 1)
            breadcrumb_items.append({
                'name': path.replace('-', ' ').title(),  # Human-readable name
                'url': current_url,
                'active': is_last
            })
    return {'breadcrumb_items': breadcrumb_items}
