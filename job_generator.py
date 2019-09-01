import random

verbs = []
nouns = []
last_job = ['init', 'init']
highlighted_verbs = []
highlighted_nouns = []
use_highlighted = False

def generate_new_job():
    if verbs == [] or nouns == []:
        print('There are no jobs!')
    elif use_highlighted == True:
        verb = random.choice(highlighted_verbs)
        noun = random.choice(highlighted_nouns)
        print("%s the %s!" % (verb, noun))
        last_job[0] = verb
        last_job[1] = noun
    else:
        verb = random.choice(verbs)
        noun = random.choice(nouns)
        print("%s the %s!" % (verb, noun))
        last_job[0] = verb
        last_job[1] = noun

def add_new_job():
    verb = input("New verb: ").capitalize()
    noun = input("New noun: ")
    print("Your new job: %s the %s." % (verb, noun))
    verbs.append(verb)
    nouns.append(noun)

def save_lists():
    filepath = input("Filepath: ")
    file = open(filepath, "w")
    file.write("nouns = %s\nverbs = %s\nhighlighted_nouns = %s\nhighlighted_verbs = %s" % (nouns, verbs, highlighted_nouns, highlighted_verbs))
    file.close()

def load_lists():
    try:
        filepath = input("Filepath: ")
        file = open(filepath)
        lists = file.read()
        exec(lists, globals(), globals())
        file.close()
    except:
        print("The file is corrupt.")

def list_jobs():
    for i in range(len(verbs)):
        verb = verbs[i]
        noun = nouns[i]
        print("%s the %s" % (verb, noun))
    print('Highlighted verbs:')
    for j in highlighted_verbs:
        print(j)
    print('Highlighted nouns:')
    for k in highlighted_nouns:
        print(k)

def edit_job():
    for i in range(len(verbs)):
        verb = verbs[i]
        noun = nouns[i]
        print("%s the %s" % (verb, noun))
        to_edit = input("Edit?: ").lower()
        if to_edit not in ["", "n", "no"]:
            part_of_speech = input("Edit noun, verb, or both?" ).lower()
            new_noun = noun
            new_verb = verb
            if part_of_speech in ["n", "noun", "b", "both"]:
                new_noun = input("Replace noun: ").lower()
            if part_of_speech in ["v", "verb", "b", "both"]:
                new_verb = input("Replace verb: ").capitalize()
            verbs[i] = new_verb
            nouns[i] = new_noun

def delete_job():
    for i in range(len(verbs)):
        verb = verbs[i]
        noun = nouns[i]
        print("%s the %s" % (verb, noun))
        to_edit = input("Delete?: ").lower()
        if to_edit in ["y", "yes"]:
            del verbs[i]
            del nouns[i]
            print("Deleted: %s the %s" % (verb, noun))

def highlight_job():
    if last_job[0] not in highlighted_verbs:
        highlighted_verbs.append(last_job[0])
    else:
        print('%s is already highlighted!' % last_job[0])
    if last_job[1] not in highlighted_nouns:
        highlighted_nouns.append(last_job[1]) 
    else:
        print('%s is already highlighted!' % last_job[1])
    print("Highlighted last job: %s the %s" % (last_job[0], last_job[1]))

def remove_highlight():
    to_delete = input("Highlight to remove: ")
    if to_delete.capitalize() in highlighted_verbs:
        del highlighted_verbs[highlighted_verbs.index(to_delete.capitalize())]
        print("Removed from highlighted verbs")
    if to_delete in highlighted_nouns:
        del highlighted_nouns[highlighted_nouns.index(to_delete)]
        print("Removed from highlighted nouns")

def toggle_mode():
    global use_highlighted
    use_highlighted = not use_highlighted
    print("Toggled mode to %s" % ('highlighted' if use_highlighted else 'standard'))

def get_help():
    print("""
Hello! Welcome to the job generator, where you can find silly things to do!
Available commands:
    add -- Creates a new job.
    delete -- Deletes an existing job.
    edit -- Edits an existing job.
    generate -- Shows a mixed-up job.
    help -- Shows this message.
    highlight -- Highlight a job for use in use_highlighted mode
    mode -- toggles mode between highlighted only and standards
    job -- Aliased to generate
    list -- Lists existing jobs.
    load -- Loads jobs from a pre-saved file.
    n[ew] -- Aliased to add.
    unhighlight -- Demote a verb/noun to unhighlighted status.
    save -- Saves jobs to a file.
    quit -- Quits the program.
    
    If you just press enter/return, it is aliased to generate.
Have fun!

Disclaimer: The creators of this program are not responsible for any actions taken on account of this program.
""")

def loop():
    get_help()
    while True:
        command = input("> ")
        if command in ["", "generate", "job"]:
            generate_new_job()
        elif command in ["n", "new","add"]:
            add_new_job()
        elif command == "save":
            save_lists()
        elif command == "load":
            load_lists()
        elif command == "list":
            list_jobs()
        elif command == "edit":
            edit_job()
        elif command == "delete":
            delete_job()
        elif command == "help":
            get_help()
        elif command in ["highlight", "h"]:
            highlight_job()
        elif command == "unhighlight":
            remove_highlight()
        elif command == "mode":
            toggle_mode()
        elif command == "quit":
            break

loop()
