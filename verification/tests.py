"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""

TESTS = {
    "Basics": [
        {
            "input": [(2, 2), (2, 8), (8, 8), (5, 5), (8, 2)],
            "answer": 23.31370849898476,
            "show": 23.31,
            "explanation": ((2, 2), (2, 8), (8, 8), (5, 5), (8, 2)), },
        {
            "input": [(2, 2), (8, 8), (9, 9), (4, 4), (6, 6)],
            "answer": 12.727922061357857,
            "show": 12.73,
            "explanation": ((2, 2), (4, 4), (6, 6), (8, 8), (9, 9)), }

    ],
    "Edge": [
        {
            "input": [(5, 9), (1, 1), (9, 9), (1, 9), (9, 1)],
            "answer": 25.414213562373096,
            "show": 25.41,
            "explanation": ((1, 1), (9, 1), (9, 9), (5, 9), (1, 9)), },
        {
            "input": [(1, 2), (1, 5), (1, 3), (1, 1), (1, 4)],
            "answer": 5.414213562373095,
            "show": 5.41,
            "explanation": ((1, 1), (1, 2), (1, 3), (1, 4), (1, 5)), },
        {
            "input": [(5, 1), (3, 1), (9, 1), (1, 1), (7, 1)],
            "answer": 9.414213562373096,
            "show": 9.41,
            "explanation": ((1, 1), (3, 1), (5, 1), (7, 1), (9, 1)), }
    ],
    "Extra": [
        {
            "input": [(2, 4), (2, 6), (4, 6), (2, 1), (7, 9)],
            "answer": 13.478708664619074,
            "show": 13.48,
            "explanation": ((2, 1), (2, 4), (2, 6), (4, 6), (7, 9)), },
        {
            "input": [(3, 8), (5, 1), (6, 2), (9, 9), (7, 7)],
            "answer": 20.1729697588291,
            "show": 20.17,
            "explanation": ((5, 1), (6, 2), (3, 8), (7, 7), (9, 9)), },
        {
            "input": [(7, 4), (8, 5), (2, 6), (4, 1), (2, 1)],
            "answer": 15.975684757290388,
            "show": 15.98,
            "explanation": ((2, 1), (4, 1), (7, 4), (8, 5), (2, 6)), },
        {
            "input": [(4, 9), (3, 2), (1, 6), (5, 5), (6, 5)],
            "answer": 16.925879193046843,
            "show": 16.93,
            "explanation": ((3, 2), (5, 5), (6, 5), (4, 9), (1, 6)), },
        {
            "input": [(5, 4), (3, 1), (5, 2), (1, 4), (2, 2)],
            "answer": 12.009455142990335,
            "show": 12.01,
            "explanation": ((1, 4), (2, 2), (3, 1), (5, 2), (5, 4)), },
        {
            "input": [(5, 1), (9, 5), (9, 8), (5, 5), (8, 2)],
            "answer": 19.423574833929543,
            "show": 19.42,
            "explanation": ((5, 1), (8, 2), (9, 5), (9, 8), (5, 5)), },
        {
            "input": [(9, 2), (4, 2), (2, 1), (1, 9), (7, 2)],
            "answer": 20.10228176773423,
            "show": 20.1,
            "explanation": ((2, 1), (4, 2), (7, 2), (9, 2), (1, 9)), },
        {
            "input": [(8, 9), (5, 9), (2, 4), (9, 4), (1, 1)],
            "answer": 18.506462630979563,
            "show": 18.51,
            "explanation": ((1, 1), (2, 4), (5, 9), (8, 9), (9, 4)), },
        {
            "input": [(8, 9), (8, 6), (9, 3), (6, 7), (6, 3)],
            "answer": 17.93497669491373,
            "show": 17.93,
            "explanation": ((6, 3), (9, 3), (8, 6), (6, 7), (8, 9)), },
        {
            "input": [(8, 1), (5, 9), (2, 5), (9, 3), (3, 4)],
            "answer": 20.861384090800865,
            "show": 20.86,
            "explanation": ((3, 4), (2, 5), (5, 9), (9, 3), (8, 1)), },
        {
            "input": [(3, 8), (5, 1), (8, 8), (9, 1), (4, 6)],
            "answer": 22.87829125795763,
            "show": 22.88,
            "explanation": ((5, 1), (9, 1), (8, 8), (4, 6), (3, 8)), },
        {
            "input": [(5, 3), (4, 6), (7, 7), (7, 2), (9, 7)],
            "answer": 17.840733187117067,
            "show": 17.84,
            "explanation": ((7, 2), (5, 3), (4, 6), (7, 7), (9, 7)), },
        {
            "input": [(9, 2), (2, 5), (3, 1), (7, 8), (4, 8)],
            "answer": 20.215489881586787,
            "show": 20.22,
            "explanation": ((3, 1), (2, 5), (4, 8), (7, 8), (9, 2)), },

    ]
}
