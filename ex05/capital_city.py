def get_capital(state):
    states = {
        "Oregon": "OR",
        "Alabama": "AL",
        "New Jersey": "NJ",
        "Colorado": "CO"
    }
    capital_cities = {
        "OR": "Salem",
        "AL": "Montgomery",
        "NJ": "Trenton",
        "CO": "Denver"
    }
    
    state = state.strip("'")
    
    state_code = states.get(state)
    if state_code:
        capital = capital_cities.get(state_code)
        if capital:
            return capital
        else:
            return "Unknown capital"
    else:
        return "Unknown state"

if __name__ == "__main__":
    state = raw_input("Enter a state: ")  # Alterado para raw_input() para Python 2
    capital = get_capital(state)
    print(capital)