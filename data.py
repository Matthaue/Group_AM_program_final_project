import json
import numpy as np

class ScenicData:
    def __init__(self, filepath):
        self.filepath = filepath
        self.spot_names = []
        self.spot_map = {}
        self.dist_matrix = None
        self.time_matrix = None
        self.price_matrix = None
        self.transport_type = 'taxi'  # or 'taxi'
        self._load_data()

    def _load_data(self):
        """
        Loads data from the specified JSON file and prepares matrices for algorithms.
        """
        with open(self.filepath, 'r', encoding='utf-8') as f:
            all_data = json.load(f)

        # Prepare distinct spot names
        spots = set()
        for start, ends in all_data.items():
            spots.add(start)
            for end in ends.keys():
                spots.add(end)
        self.spot_names = sorted(list(spots))
        self.spot_map = {name: idx for idx, name in enumerate(self.spot_names)}
        n = len(self.spot_names)

        # Initialize matrices
        self.dist_matrix = np.full((n, n), np.inf)
        self.time_matrix = np.full((n, n), np.inf)
        self.price_matrix = np.full((n, n), np.inf)

        # Fill matrices
        for start, ends in all_data.items():
            for end, data in ends.items():
                i = self.spot_map[start]
                j = self.spot_map[end]
                # Default: public transport
                pt = data.get('public_transport', {})
                taxi = data.get('taxi', {})
                self.dist_matrix[i, j] = pt.get('distance_km', np.inf)
                self.time_matrix[i, j] = pt.get('time_min', np.inf)
                self.price_matrix[i, j] = taxi.get('price_yuan', np.inf)

    def get_matrix(self, mode='distance'):
        """Returns the specified matrix: 'distance', 'time', or 'price'"""
        if mode == 'distance':
            return self.dist_matrix.copy()
        elif mode == 'time':
            return self.time_matrix.copy()
        elif mode == 'price':
            return self.price_matrix.copy()
        else:
            raise ValueError("Mode must be 'distance', 'time', or 'price'.")

    def get_spot_names(self):
        """Returns ordered scenic spot names."""
        return self.spot_names.copy()

    def get_spot_index(self, name):
        """Returns the index for a spot name."""
        return self.spot_map.get(name)

    def get_route_info(self, start, end):
        """Returns information between two spots."""
        with open(self.filepath, 'r', encoding='utf-8') as f:
            all_data = json.load(f)
        info = all_data.get(start, {}).get(end, None)
        return info

    @staticmethod
    def matrix_to_dict(matrix, spot_names):
        """Convert matrix to a dict for visualization or debugging."""
        result = {}
        for i, start in enumerate(spot_names):
            result[start] = {}
            for j, end in enumerate(spot_names):
                result[start][end] = matrix[i, j]
        return result