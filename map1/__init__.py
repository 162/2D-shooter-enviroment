map_size = [1080, 720]

# walls color
clr = '#888888'

# walls and columns positions
map_walls = []
map_walls.append(((540, 10), 1080, 20, clr))
map_walls.append(((540, 710), 1080, 20, clr))
map_walls.append(((1070, 360), 20, 720, clr))
map_walls.append(((10, 360), 20, 720, clr))

map_columns = [((150, 150), 30, clr),
               ((930, 150), 30, clr),
               ((930, 570), 30, clr),
               ((150, 570), 30, clr),
               ((200, 200), 20, clr),
               ((880, 200), 20, clr),
               ((880, 520), 20, clr),
               ((200, 520), 20, clr)]

default_parameters = {'max_velocity': 1.2,
                      'turn_speed': 0.05,
                      'max_health': 100,
                      'max_armor': 100,
                      'spawn_point': (100, 100),
                      'starting_angle': 0,
                      'starter_weapon_pack': None,
                      'starter_ammo_pack': None,
                      'color': '#555599',
                      'radius': 12}

# Agents generating (without decision functions)
map_agents = [('KeyboardAgent', default_parameters.copy()),
              ('EmptyAgent', default_parameters.copy()),
              ('PerceptronAgent', default_parameters.copy())]


map_agents[1][1]['color'] = '#559955'
map_agents[1][1]['spawn_point'] = (1000, 100)

map_agents[2][1]['color'] = '#995555'
map_agents[2][1]['spawn_point'] = (550, 600)

# Bonuses spawn points with timeouts
map_bonuses = [[(180, 180, 250), (900, 180, 250), (180, 540, 250), (900, 540, 250)],  # bullet packs
               [],  # shells packs
               [],  # rockets packs
               [],  # medkits
               []]  # armor vests
