from movies import *


@app.before_first_request
def create_table():
    db.create_all()


@app.route('/movies', methods=['GET'])
def get_movies():
    return jsonify({'Movies': get_all_movies()})


@app.route('/movies/<int:id>', methods=['GET'])
def get_movie_by_id(id):
    return_value = get_movie(id)
    return jsonify(return_value)


@app.route('/movies', methods=['POST'])
def add_movies():
    request_data = request.get_json()
    id = add_movie(request_data["title"], request_data['year'], request_data['genre'])
    response = Response(f"Movie Added with id {id}", 201, mimetype='application/json')
    return response


@app.route('/movies/', methods=['PUT'])
def update_movies():
    request_data = request.get_json()
    update_movie(request_data['id'], request_data['title'], request_data['year'], request_data['genre'])
    response = Response("movie Updated", status=200, mimetype='application/json')
    return response


@app.route('/movies/<int:id>', methods=['DELETE'])
def remove_movies(id):
    delete_movie(id)
    response = Response("Movie Deleted", status=200, mimetype='application/json')
    return response


if __name__ == "__main__":
    db.init_app(app)

    app.run(host='localhost', port=3000, debug=True)
