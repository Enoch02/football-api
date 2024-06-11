from flask import Flask

def list_endpoints(app: Flask) -> list[str]:
    output = []
    
    for rule in app.url_map.iter_rules():
        methods = ','.join(rule.methods)
        line = f"{rule.endpoint}: {rule.rule} [{methods}]"
        output.append(line)

    return output
