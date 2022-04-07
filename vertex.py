class Vertex:
    def __init__(self, key):
        self.key = key
        self.points_to = {}
    

    def get_key(self):
        return self.key

    def add_point(self, key, weight):
        return self.points_to.update({
            key:weight
        })

    def get_points(self) -> dict:
        return self.points_to

    def is_an_existing_point(self, vertex_key: str) -> bool:
        return vertex_key in self.points_to.keys()
    
    def get_weigth_point(self, vertex_key: str) -> int:
        return self.points_to[vertex_key]