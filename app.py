from flask import Flask, json

app = Flask(__name__)


@app.route("/")
def hello():
    return '<h1>Hello World!</h1>'


@app.route('/titles', methods=['GET'])
def get_original_titles():
    try:
        with open('animations.json', 'r') as file:
            result = []

            data = json.load(file)
            for animation in data["animations"]:
                result.append(animation['Original title'])
            # original_titles = [item['Original title'] for item in data]

        return result
    except FileNotFoundError:
        return {"error": "File not found"}, 404





@app.route('/ids/<int:animation_id>', methods=['GET'])
def get_animation_by_id(animation_id):
        try:
            with open('animations.json', 'r') as file:
                data = json.load(file)
                animation = None
                for ani in data['animations']:
                    if ani["ID"] == animation_id:
                        animation = ani
                        break

            if animation:
                return animation
            else:
                return {"error": f"Animacji z id {animation_id} nie ma"}, 404

        except FileNotFoundError:
            return {"error": "File not found"}, 404

@app.route('/titles/<keyword>', methods=['GET'])
def get_titles_by_keyword(keyword):
    try:
        with open('animations.json', 'r') as file:
            data = json.load(file)
            result = []

            for ani in data["animations"]:
                if keyword in ani["Keywords"]:
                    result.append(ani['Original title'])

            return result

    except FileNotFoundError:
        return {"error": "File not found"}, 404