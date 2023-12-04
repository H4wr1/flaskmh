from flask import Flask, json, request

app = Flask(__name__)

with open('animations.json') as json_file:
    data = json.load(json_file)
    animations = data['animations']

@app.route("/")
def hello():
    return '<h1>Hello World!</h1>'

@app.route('/titles', methods=['GET'])
def get_original_titles():
    try:
        with open('animations.json', 'r') as file:
            result = []
            #data = json.load(file)
            for animation in data["animations"]:
                result.append(animation['Original title'])
 
        return result
    except FileNotFoundError:
        return {"error": "File not found"}, 404

@app.route('/ids/<int:animation_id>', methods=['GET'])
def get_animation_by_id(animation_id):
        try:
            with open('animations.json', 'r') as file:
                #data = json.load(file)
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
            #data = json.load(file)
            result = []

            for ani in data["animations"]:
                if keyword in ani["Keywords"]:
                    result.append(ani['Original title'])
            return result

    except FileNotFoundError:
        return {"error": "File not found"}, 404



@app.route('/studios/<int:animation_id>', methods=['PUT', 'GET'])
def update_studio(animation_id):
    new_studio = request.args.get('studio')
    animation = next((a for a in animations if a['ID'] == animation_id), None)

    if animation:
        animation['Studio'] = new_studio
        return {'message': f'Zmienione studio dla ID: {animation_id}','updated_data': animation}, 200
    else:
        return {'error': f'Nie znaleziono ID: {animation_id}'}, 404