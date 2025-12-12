
def add_entry(d, key, value):  
    d[key] = value

def search_entry(d, key): 
    return d.get(key, None)

def display_entries(d):
    for k, v in d.items():
        print(f"{k}: {v}")

db = {} # this is empty Dictionary
add_entry(db, "Muneer", "03") # we are adding entries to the dictionary
add_entry(db, "Hussain", "04")
print("Search Hussain ->", search_entry(db, "Hussain")) # we are searching a key value
print("All entries:")
display_entries(db)
