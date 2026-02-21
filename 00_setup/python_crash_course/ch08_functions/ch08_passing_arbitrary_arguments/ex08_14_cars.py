#8.14

def make_car(manufacturer,model,**optional_features):
    optional_features["manufacturer"] = manufacturer
    optional_features["model"] = model
    return optional_features


car = make_car('subaru','outback',color='blue',to_package=True)

print(car)