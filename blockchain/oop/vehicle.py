class Vehicle:
    def __init__(self, raftaar=100):
        self.top_speed = raftaar
        self.warnings = []

    def __repr__(self):
        return 'Meri gaddi ko {} warnings mile hai'.format(len(self.warnings))


    def add_warning(self, warning):
        self.warnings.append(warning)

    def show_warnings(self):
        for x in self.warnings:
            print(x)

    def drive(self):
        print('Gaadi ki raftaar hai : {}'.format(self.top_speed))