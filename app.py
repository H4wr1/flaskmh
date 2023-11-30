from flask import Flask, json, request

app = Flask(__name__)

# Example memory storage
studio_data = []

# Load content of animations.json into studio_data
try:
    with open('animations.json', 'r') as file:
        data = json.load(file)
        studio_data = data.get("animations", [])
except FileNotFoundError:
    print("File not found. Using an empty list for studio_data.")

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

@app.route('/studios/<int:id>', methods=['PUT'])
def update_studio(id):
    new_studio = request.args.get('studio')

    # Check if the studio with the given ID exists
    studio_to_update = next((studio for studio in studio_data if studio["ID"] == id), None)

    if studio_to_update:
        # Update the 'Studio' value
        studio_to_update["Studio"] = new_studio
        return {"message": f"Studio with ID {id} updated successfully", "data": studio_to_update}
    else:
        return {"error": f"Studio with ID {id} not found"}, 404