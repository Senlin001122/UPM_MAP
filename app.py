from flask import Flask, jsonify, request, render_template
from routing_algorithm import dijkstra, reconstruct_path

app = Flask(__name__)

# Define the graphs for different time slots
graphs = {
    '9-11': {
        'Faculty of Computer Science': {'UPM Library': 2, 'Faculty of Engineering': 3,'IOI Mall':10, 'UPM Hospital':12},
        'MRT UPM': {'PETRONAS': 6, 'MIX':5, 'Tropical Villa':8, 'Beryl\'s Chocolate':8},
        'PETRONAS': {'Tropical Villa': 10, 'Beryl\'s Chocolate': 2, 'RHB Bank':8},
        'UPM Library': {'MRT UPM': 2},
        'MIX': {'Tropical Villa': 3},
        'Faculty of Engineering': {'Shell': 6,'Serdang Bus Station':10},
        'Shell': {'univ 360':3, 'Beryl\'s Chocolate':1},
        'Beryl\'s Chocolate': {'PETRONAS': 2, 'RHB Bank': 8,'Shell':2, 'univ 360':4},
        'RHB Bank': {'South City': 6, 'Astetica':8},
        'South City': {'East Lake': 3},
        'Serdang Bus Station': {'Astetica': 2},
        'univ 360': {'Serdang Bus Station': 10},
        'UPM Hospital': {'IOI Resort': 5},
        'IOI Mall': {'IOI Resort': 3},
        'Tropical Villa':{},
        'IOI Resort':{},
        'East Lake':{},
        'Astetica':{}
    },

    '11-14': {
        'Faculty of Computer Science': {'UPM Library': 3, 'Faculty of Engineering': 4,'IOI Mall':13, 'UPM Hospital':12},
        'MRT UPM': {'PETRONAS': 7, 'MIX':5, 'Tropical Villa':8, 'Beryl\'s Chocolate':7},
        'PETRONAS': {'Tropical Villa': 14, 'Beryl\'s Chocolate': 2, 'RHB Bank':12},
        'UPM Library': {'MRT UPM': 2},
        'MIX': {'Tropical Villa': 4},
        'Faculty of Engineering': {'Shell': 7,'Serdang Bus Station':11},
        'Shell': {'univ 360':4, 'Beryl\'s Chocolate':2},
        'Beryl\'s Chocolate': {'PETRONAS': 2, 'RHB Bank': 11,'Shell':2, 'univ 360':3},
        'RHB Bank': {'South City': 13, 'Astetica':12},
        'South City': {'East Lake': 5},
        'Serdang Bus Station': {'Astetica': 1},
        'univ 360': {'Serdang Bus Station': 12},
        'UPM Hospital': {'IOI Resort': 4},
        'IOI Mall': {'IOI Resort': 3},
        'Tropical Villa':{},
        'IOI Resort':{},
        'East Lake':{},
        'Astetica':{}
    },

    '14-18': {
        'Faculty of Computer Science': {'UPM Library': 2, 'Faculty of Engineering': 3,'IOI Mall':15, 'UPM Hospital':14},
        'MRT UPM': {'PETRONAS': 7, 'MIX':12, 'Tropical Villa':13, 'Beryl\'s Chocolate':8},
        'PETRONAS': {'Tropical Villa': 15, 'Beryl\'s Chocolate': 2, 'RHB Bank':12},
        'UPM Library': {'MRT UPM': 2},
        'MIX': {'Tropical Villa': 5},
        'Faculty of Engineering': {'Shell': 6,'Serdang Bus Station':18},
        'Shell': {'univ 360':3, 'Beryl\'s Chocolate':2},
        'Beryl\'s Chocolate': {'PETRONAS': 2, 'RHB Bank': 13,'Shell':2, 'univ 360':4},
        'RHB Bank': {'South City': 15, 'Astetica':14},
        'South City': {'East Lake': 5},
        'Serdang Bus Station': {'Astetica': 1},
        'univ 360': {'Serdang Bus Station': 15},
        'UPM Hospital': {'IOI Resort': 3},
        'IOI Mall': {'IOI Resort': 3},
        'Tropical Villa':{},
        'IOI Resort':{},
        'East Lake':{},
        'Astetica':{}
    },
}


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        time_slot = request.form['time_slot']
        destination = request.form['destination']
        start = 'Faculty of Computer Science'
        graph = graphs[time_slot]
        distances, previous_nodes = dijkstra(graph, start)
        path = reconstruct_path(start, destination, previous_nodes)
        time = distances[destination]  # Assuming 1 unit distance = 1 minute
        return render_template('index.html', time_slot=time_slot, from_start=start, to_destination=destination, path=path, time=time)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)











