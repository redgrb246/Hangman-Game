
def hang_man_guy(guesses,total_attemts):
    stages = ["""
              
        ------
        |    |
        |
        |
        |
        |
        |
    ------------
    """, """
        ------
        |    |
        |    O
        |
        |
        |
        |
    ------------
    """, """
        ------
        |    |
        |    O
        |    |
        |    |
        |
        |
    ------------
    """, """
        ------
        |    |
        |    O
        |    |
        |    |
        |   /
        |
    ------------
    """, """
        ------
        |    |
        |    O
        |    |
        |    |
        |   / \.
        |
    ------------
    """, """
        ------
        |    |
        |    O
        |  --|
        |    |
        |   / \.
        |
    ------------
    """, """
        ------
        |    |
        |    O
        |  --|--
        |    |
        |   / \.
        |
    ------------
               
              """  
    ]
    return stages[total_attemts-guesses]