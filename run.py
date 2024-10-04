from app import app

if __name__ == '__main__':
    print("Routes enregistrées:")
    for rule in app.url_map.iter_rules():
        print(f"{rule.endpoint}: {rule.rule}")
    app.run(debug=True)