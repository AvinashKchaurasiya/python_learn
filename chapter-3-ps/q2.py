letter = '''Hello <|name|> you are selected on, Date <|Date|>'''
name = letter.replace("<|name|>", "Avinash Chaurasiya").replace("<|Date|>", "20-Aug-2025")
print(name)