'''
Pegue o time com maior/menor quantidade de gols e maior/menor quantidade de derrotas.
'''
times = [
    {"time": "A", "gols": 1, 'derrotas':4},
    {"time": "B", "gols": 4, 'derrotas': 11},
    {"time": "C", "gols": 31, 'derrotas': 13},
    {"time": "D", "gols": 50, 'derrotas': 5}
]

print("Menor quantidade de gols: " +str (times[0:1]))
print("Maior quantidade de gols: " +str (times[3::1]))
print("Menor quantidade de derrotas: " +str (times[0:1]))
print("Maior quantidade de derrotas: " +str (times[2::2]))