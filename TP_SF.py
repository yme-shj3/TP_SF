import ply.lex as lex


reserved = {
    'actor': 'ACTOR',
    'as': 'AS',
    'usecase': 'USECASE',
    'package': 'PACKAGE',
    'includes': 'INCLUDES',
    'extends': 'EXTENDS',
    '@startuml': 'START_UML',  
    '@enduml': 'END_UML',      
}


tokens = [
    'COLON',
    'RIGHT_ARROW_1',
    'RIGHT_ARROW_2',
    'LBRACE',
    'RBRACE',
    'INHERIT',
    'EOL',
    'STRING',
    'STEREO',
    'ACTOR_TEXT',
    'USE_CASE_TEXT',
    'ID',
] + list(reserved.values())


t_COLON = r'\:'
t_RIGHT_ARROW_1 = '->|-->'
t_RIGHT_ARROW_2 = '.>|..>'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_INHERIT = r'<\|--'
t_EOL = r'\n'
t_STRING = '"[A-Za-z0-9_]*"'
t_STEREO = '<<[A-Za-z_]*>>'
t_ACTOR_TEXT = ':[a-zA-Z_]*:'
t_USE_CASE_TEXT = r'\([a-zA-Z ]+\)'
  


t_ignore = " \t"


def t_ID(t):
    '@?[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')  
    return t


def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)


lexer = lex.lex()


lexer.input("""
@startuml System
 actor :User:
 usecase (Define travel)
 usecase (Set VIP options)
 usecase (Authentication)
  :User: --> (Define travel)
  :User: --> (Set VIP options)
  (Define travel) --> (Authentication) : includes
  (Set VIP options) --> (Define travel) : extends
 package Administration {
 actor :Admin:
      :User: <|-- :Admin:
 usecase (Remove travel)
      :Admin: --> (Remove travel)
      (Remove travel) --> (Authentication) : includes
  }
 @enduml
""")


while token := lexer.token():
    print(token)


