class Flight:
    '''A flight with a particular passenger aircraft.'''

    def __init__(self, number, aircraft) -> None:

        if not number[:2].isalpha():
            raise ValueError(f"No airline code in '{number}'")

        if not number[:2].isupper():
            raise ValueError(f"No airline code in '{number}'")

        if not number[2:].isdigit() and int(number[2:]) <= 9999:
            raise ValueError(f"No air3line code in '{number}'")

        self._number = number
        self._aircraft = aircraft

    def number(self):
        return self._number
    
    def aircraft_model(self):
        return self._aircraft.model()

class aircraft:

    def __init__(self, registration, model, num_rows, num_seats_per_row) -> None:
        self._registration = registration
        self._model = model
        self._num_rows = num_rows
        self._num_seats_per_row = num_seats_per_row

    def registration (self):
        return self._registration

    def model (self):
        return self._model

    def seating_plan(self):
        return (range(1, self._num_rows +1), 
            "ABCDEFGHIJK"[:self._num_seats_per_row])
    

