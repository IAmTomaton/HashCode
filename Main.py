class Intersection:

    def __init__(self, id):
        self.id = id

    def __str__(self):
        return 'inter: id: {0}'.format(self.id)


class Street:

    def __init__(self, id, first_int, second_int, name, transit_time):
        self.id = id
        self.first_int = first_int
        self.second_int = second_int
        self.name = name
        self.transit_time = transit_time

    def __str__(self):
        return 'street: id: {0} fth_inter: {1} scn_inter: {2} name: {3} tran_time: {4}'\
            .format(self.id, self.first_int, self.second_int, self.name, self.transit_time)


class Car:

    def __init__(self, id, streets):
        self.id = id
        self.streets = streets

    def __str__(self):
        return 'car: id: {0} streets: '\
            .format(self.id, self.streets)



class Parser:

    @staticmethod
    def parse_input(input):
        lines = input.split('\n')
        first_numbers = lines[0].split(' ')

        simulation_time = int(first_numbers[0])
        intersection_count = int(first_numbers[1])
        street_count = int(first_numbers[2])
        car_count = int(first_numbers[3])
        score = int(first_numbers[4])

        intersections = [Intersection(i) for i in range(intersection_count)]

        streets = []
        for i in range(street_count):
            street_line = lines[i + 1].split(' ')
            first_int = int(street_line[0])
            second_int = int(street_line[1])
            street_name = street_line[2]
            transit_time = int(street_line[3])
            street = Street(i, first_int, second_int, street_name, transit_time)
            streets.append(street)

        cars = []
        for i in range(car_count):
            car_streets = lines[i + street_count + 1].split(' ')[1:]
            car = Car(i, car_streets)
            cars.append(car)

        return simulation_time, score, intersections, streets, cars


def main():
    with open('input.txt') as file:
        text = file.read()
    simulation_time, score, intersections, streets, cars = Parser.parse_input(text)
    print('3')
    print('1')
    print('2')
    print('rue-d-athenes 2')
    print('rue-d-amsterdam 1')
    print('0')
    print('1')
    print('rue-de-londres 2')
    print('2')
    print('1')
    print('rue-de-moscou 1')


if __name__ == '__main__':
    main()
