import pickle
import os

# set up all available models
traits = {
    "gram-positive": 'Gram-positive',
    "spore-forming": 'Spore-forming',
    "aerobic": 'Aerobic',
    "anaerobic": 'Anaerobic',
    "thermophile": 'Thermophilic',
    "halophile": 'Halophilic',
    'motile': 'Motile',
    "flagellated": 'Flagellated',
    "glucose-util": 'Glucose-utilizing',
    "glucose-ferment": 'Glucose-fermenting',
}

MODELPATH = os.path.dirname(__file__)+"/models/"
# go through all remaining traits
for trait in traits:
    label = traits[trait]

    # load model
    dump = pickle.load(open(MODELPATH+trait + "_data.p", "rb"))
    clf = dump.get('model')
    categories = dump.get("categories")

    dump = {
        "categories": categories,
        "model": clf,
    }
    pickle.dump(dump, open(MODELPATH+'M_'+trait + ".p", "wb"))