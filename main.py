# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line
def greet(name, greeting_template= 'Hello, <name>!'):
    greeting = greeting_template.replace('<name>', name)
    return greeting

print(greet('Doc'))
print(greet('Bob', 'Whats up, <name>!'))

def force(mass, body='earth'):
    body_dict = {
        'sun': round(274, 1),
        'jupiter': round(24.92, 1),
        'neptune': round(11.15, 1),
        'saturn': round(10.44, 1),
        'earth': round(9.798, 1),
        'uranus': round(8.87, 1),
        'venus': round(8.87, 1),
        'mars': round(3.71, 1),
        'mercury': round(3.7, 1),
        'moon': round(1.62, 1),
        'pluto': round(0.58, 1)
        }
    force = mass * body_dict[body]
    return force

print(force(100))

def pull(m1, m2, d):
    G = (6.674 * (10 **-11))
    pull = G * ((m1*m2)/(d**2))
    return pull

print(pull(800, 1500, 3))

